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
    detector = NodeDetector()
    nodes = detector.detect_nodes(request)
    injector = KnowledgeInjector()
    handoff = injector.create_enhanced_handoff(nodes, user_request=request, target_platform="ChatGPT_Plus")
    Path("handoff_output.json").write_text(json.dumps(handoff, indent=2), encoding='utf-8')
    print("handoff_output.json written.")

if __name__ == "__main__":
    main()
