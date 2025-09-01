# automation_tools/tools/enhanced_node_detector.py
from typing import List, Tuple
try:
    from nodes.node_detector import NodeDetector
except Exception:
    class NodeDetector:
        def __init__(self, framework_path=None): pass
        def detect_nodes(self, user_input: str) -> List[str]: return []

try:
    from .tool_selector import EmpiricalToolSelector, TaskCharacteristics
except Exception:
    from automation_tools.tools.tool_selector import EmpiricalToolSelector, TaskCharacteristics

class EnhancedNodeDetector(NodeDetector):
    def __init__(self, framework_path=None):
        super().__init__(framework_path)
        self.tool_selector = EmpiricalToolSelector()
    def detect_nodes_with_platform_recommendation(self, user_input: str) -> Tuple[List[str], dict]:
        nodes = self.detect_nodes(user_input)
        task = self._analyze_task_characteristics(user_input, nodes)
        rec = self.tool_selector.recommend_platform(task)
        return nodes, {"primary": rec.primary_platform, "fallbacks": rec.fallback_options, "confidence": rec.confidence_score, "rationale": rec.rationale}
    def _analyze_task_characteristics(self, user_input: str, nodes: List[str]) -> TaskCharacteristics:
        level = "moderate"
        text = user_input.lower()
        if any(k in text for k in ["architect","govern","orchestrate","framework"]): level = "expert_level"
        elif any(k in text for k in ["optimize","integrate","coordinate","design"]): level = "complex"
        elif any(k in text for k in ["help","what is","how to","basic"]): level = "simple"
        domain = "general"
        output = "analysis"
        if any(k in text for k in ["code","script","function","class","implement"]): output = "code"
        elif any(k in text for k in ["file","template","config","generate","create"]): output = "files"
        elif any(k in text for k in ["guide","advice","recommend","suggest"]): output = "guidance"
        return TaskCharacteristics(complexity=level, domain=domain, output_type=output, interaction_pattern="iterative", long_context_required=len(user_input)>1200)
