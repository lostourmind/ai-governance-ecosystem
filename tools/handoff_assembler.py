#!/usr/bin/env python3
"""
Package builder that runs detection + injection and emits a JSON handoff file.
"""
import json, sys
from pathlib import Path
from node_detector import NodeDetector
from knowledge_injector import KnowledgeInjector
def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/handoff_assembler.py 'free form user request'")
        sys.exit(1)
    request = sys.argv[1]
    # Resolve repo root two levels up from this file (tools/..)
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str((repo_root / "tools").resolve()))
    detector = NodeDetector(framework_path=str(repo_root / "nodes/_framework"))
    injector = KnowledgeInjector(nodes_path=str(repo_root / "nodes"),
                                 templates_path=str(repo_root / "prompt_injection/inject_templates"))
    nodes = detector.detect_nodes(request)
    handoff = injector.create_enhanced_handoff(nodes, user_request=request, target_platform="ChatGPT_Plus")
    out_path = repo_root / "handoff_output.json"
    out_path.write_text(json.dumps(handoff, indent=2), encoding='utf-8')
    print(str(out_path))

if __name__ == "__main__":
    main()
