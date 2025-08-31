#!/usr/bin/env python3
"""
Knowledge Injection and Handoff Assembly Tool
Merges node-specific knowledge with base governance wrapper
"""

import yaml
import json
from pathlib import Path
from datetime import datetime

class KnowledgeInjector:
    def __init__(self, nodes_path="nodes", templates_path="prompt_injection/inject_templates"):
        self.nodes_path = Path(nodes_path)
        self.templates_path = Path(templates_path)

    def create_enhanced_handoff(self, detected_nodes, user_request, target_platform):
        base_wrapper = self._load_base_wrapper()
        enhanced_wrapper = self._inject_node_knowledge(base_wrapper, detected_nodes)
        handoff_context = self._assemble_handoff_context(
            enhanced_wrapper, user_request, target_platform, detected_nodes
        )
        return handoff_context

    def _load_base_wrapper(self):
        wrapper_path = self.templates_path / "universal_wrapper.md"
        if wrapper_path.exists():
            return wrapper_path.read_text(encoding='utf-8')
        # Fall back to addendum-only if base wrapper not present
        addendum = (self.templates_path / "universal_wrapper.node_injection.addendum.md").read_text(encoding='utf-8')
        return f"# Universal Wrapper (placeholder)\n\n{addendum}"

    def _inject_node_knowledge(self, base_wrapper, nodes):
        enhanced_wrapper = base_wrapper
        for node in nodes:
            node_path = self.nodes_path / node
            kb = self._load_yaml(node_path / "knowledge_base.yaml")
            constraints = self._load_yaml(node_path / "constraints.yaml")
            supplement = self._load_file(node_path / "supplement_prompt.md")

            enhanced_wrapper += f"\n\n## NODE-SPECIFIC KNOWLEDGE: {node}\n"
            enhanced_wrapper += supplement
            enhanced_wrapper += f"\n### Constraints from {node}:\n"
            enhanced_wrapper += self._format_constraints(constraints)
        return enhanced_wrapper

    def _assemble_handoff_context(self, enhanced_wrapper, user_request, target_platform, nodes):
        timestamp = datetime.now().isoformat()
        session_id = f"enhanced_handoff_{timestamp.replace(':','').split('.')[0]}"
        return {
            "handoff_metadata": {
                "session_id": session_id,
                "source_tool": "ChatGPT_Plus",
                "target_tool": target_platform,
                "handoff_timestamp": timestamp,
                "governance_registry": "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml",
                "nodes_applied": nodes,
            },
            "enhanced_wrapper": enhanced_wrapper,
            "user_request": user_request,
            "node_knowledge_applied": [
                {"node": n, "knowledge_source": f"nodes/{n}/"} for n in nodes
            ],
            "mutation_log": [
                f"[PHASE:NODE_DETECTION] Detected applicable nodes: {', '.join(nodes)}",
                "[PHASE:KNOWLEDGE_INJECTION] Domain-specific knowledge integrated",
                "[PHASE:HANDOFF_ASSEMBLY] Enhanced context package created",
            ],
        }

    def _load_yaml(self, p: Path):
        if p.exists():
            return yaml.safe_load(p.read_text(encoding='utf-8'))
        return {}

    def _load_file(self, p: Path):
        if p.exists():
            return p.read_text(encoding='utf-8')
        return ""

    def _format_constraints(self, constraints):
        if not constraints:
            return ""
        formatted = ""
        c = constraints.get('constraints', {})
        if isinstance(c, dict) and c.get('hard_limits'):
            formatted += "**Hard Limits:**\n"
            for limit in c['hard_limits']:
                formatted += f"- {limit['constraint']}: {limit['reason']}\n"
        deps = constraints.get('dependencies', {})
        if isinstance(deps, dict) and deps.get('required'):
            formatted += "\n**Required Dependencies:**\n"
            for dep in deps['required']:
                version = dep.get('version', '')
                version_str = f" ({version})" if version else ""
                formatted += f"- {dep['name']}{version_str}\n"
        return formatted

if __name__ == "__main__":
    injector = KnowledgeInjector()
    example_nodes = ["project.coding.klipper.corexy"]
    example_request = "Help configure CoreXY on Klipper with governance"
    out = injector.create_enhanced_handoff(example_nodes, example_request, target_platform="ChatGPT_Plus")
    print(json.dumps(out, indent=2))
