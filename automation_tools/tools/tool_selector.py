#!/usr/bin/env python3
import yaml, json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple

try:
    from .enhanced_logger import governance_logger
except Exception:
    class _Noop:
        def log_repository_access(self,*a,**k): pass
        def log_node_detection(self,*a,**k): pass
        def log_handoff_assembly(self,*a,**k): pass
        def log_governance_validation(self,*a,**k): pass
    governance_logger = _Noop()

@dataclass
class TaskCharacteristics:
    complexity: str = "moderate"
    domain: str = "general"
    output_type: str = "analysis"
    interaction_pattern: str = "single_query"
    runtime_requirements: str = "none"
    github_integration_needed: str = "none"
    long_context_required: bool = False
    specialized_processing: Optional[str] = None

@dataclass
class PlatformRecommendation:
    primary_platform: str
    confidence_score: float
    rationale: str
    fallback_options: List[str]
    empirical_basis: str
    selection_metadata: Dict

class EmpiricalToolSelector:
    def __init__(self, governance_registry_path: str = "governance_registry.yaml"):
        self.registry_path = Path(governance_registry_path)
        self.registry = self._load_yaml(self.registry_path)
        self.aliases: Dict[str,str] = self.registry.get("platform_name_aliases", {})
        self.pss = self.registry.get("platform_selection_system", {})
        self.capabilities = self.pss.get("empirically_validated_capabilities", {})
        self.performance_log = Path("logs/tool_selection_performance.json")
        self.performance_log.parent.mkdir(parents=True, exist_ok=True)

    def _load_yaml(self, path: Path) -> Dict:
        try:
            if path.exists():
                return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception as e:
            governance_logger.log_repository_access("governance_registry", False, e)
        return {}

    def _canonical(self, name: str) -> str:
        return self.aliases.get(name, name)

    def _check_quarantine(self, task: TaskCharacteristics) -> Optional[str]:
        dep = self.registry.get("deprecated_tasks", {})
        if task.domain in ["image_processing","video_processing"] or (task.specialized_processing in ["image_restoration","video_enhancement"]):
            if "image_restoration_ai" in dep:
                return "External_Tools.Nero_AI"
        return None

    def _capability_score(self, platform: str, task: TaskCharacteristics) -> Tuple[float, List[str]]:
        cfg = self.capabilities.get(platform) or self.capabilities.get(self._canonical(platform), {})
        if not cfg:
            return 0.0, ["platform_not_configured"]
        score = 0.0; why: List[str] = []
        for crit in cfg.get("optimal_tasks", []):
            if isinstance(crit, dict):
                for k, vals in crit.items():
                    field = {"interaction":"interaction_pattern","runtime":"runtime_requirements"}.get(k, k)
                    tv = getattr(task, field, None)
                    if tv in vals: score += 1.0; why.append(f"{k}_match")
        mult = {"high":1.2,"moderate":1.0,"low":0.8}.get(cfg.get("confidence_rating","moderate"),1.0)
        score *= mult
        if "limitations_documented" in cfg:
            lim = " ".join(cfg["limitations_documented"])
            if any(x in lim for x in ["limited_repository_analysis","conceptual_implementation_focus"]):
                score *= 0.85; why.append("limitations_penalty")
        return score, why

    def _historical(self, platform: str, task_type: str) -> float:
        if not self.performance_log.exists(): return 0.5
        try:
            data = json.loads(self.performance_log.read_text())
            plat = data.get(platform) or data.get(self._canonical(platform)) or {}
            rec = plat.get(task_type, {"successes":0,"total":0})
            return 0.5 if rec.get("total",0)==0 else rec["successes"]/rec["total"]
        except Exception:
            return 0.5

    def recommend_platform(self, task: TaskCharacteristics) -> PlatformRecommendation:
        q = self._check_quarantine(task)
        if q:
            return PlatformRecommendation(q, 0.99, "quarantine_enforcement", [], "registry_quarantine", {"task_characteristics": asdict(task)})
        scores: Dict[str, Dict] = {}
        for p in self.capabilities.keys():
            s, why = self._capability_score(p, task)
            h = self._historical(p, task.domain)
            scores[p] = {"score": s*0.7 + h*0.3, "why": why, "hist": h}
        if not scores:
            return PlatformRecommendation("ChatGPT_Plus", 0.6, "default", ["Claude_Sonnet_4_Pro","Copilot"], "no_rules", {"task_characteristics":asdict(task)})
        best = max(scores.items(), key=lambda kv: kv[1]["score"])
        ordered = [k for k,_ in sorted(scores.items(), key=lambda kv: kv[1]["score"], reverse=True)]
        fallbacks = [k for k in ordered if k != best[0]]
        return PlatformRecommendation(best[0], min(best[1]["score"]/3.0,0.99), f"capability_match: {', '.join(best[1]['why'][:3])}", fallbacks, "capability+history", {"task_characteristics":asdict(task),"capability_score":best[1]["score"],"historical":best[1]["hist"]})
