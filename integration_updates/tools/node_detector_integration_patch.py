#!/usr/bin/env python3
"""Automated integrator for node detector to attach platform hints.
Run from repo root:
  python integration_updates/tools/node_detector_integration_patch.py
"""
from pathlib import Path
import re

TARGET = Path("nodes/node_detector.py")
BACKUP = Path("nodes/node_detector.py.bak")

INJECT_IMPORT = "from automation_tools.tools.tool_selector import EmpiricalToolSelector, TaskCharacteristics\n"
INJECT_FIELD  = "        self.tool_selector = EmpiricalToolSelector()\n"
INJECT_METHOD = '''
    def detect_nodes_with_platform_recommendation(self, user_input: str):
        nodes = self.detect_nodes(user_input)
        task = TaskCharacteristics(domain="general", output_type="analysis")
        rec = self.tool_selector.recommend_platform(task)
        return nodes, {"primary": rec.primary_platform, "fallbacks": rec.fallback_options, "confidence": rec.confidence_score}
'''

def main():
    if not TARGET.exists():
        print("node_detector.py not found; aborting.")
        return
    src = TARGET.read_text(encoding="utf-8")
    BACKUP.write_text(src, encoding="utf-8")

    # inject import at top if missing
    if "EmpiricalToolSelector" not in src:
        src = INJECT_IMPORT + src

    # ensure __init__ has tool_selector assignment
    if "self.tool_selector = EmpiricalToolSelector()" not in src:
        src = re.sub(r"(def __init__\(.*?\):\n\s*super\(\).__init__\(.*?\)\n)", r"\1" + INJECT_FIELD, src, count=1, flags=re.S)

    # add helper method if not present
    if "detect_nodes_with_platform_recommendation" not in src:
        src += "\n" + INJECT_METHOD + "\n"

    TARGET.write_text(src, encoding="utf-8")
    print("Integration completed. Backup at:", BACKUP)

if __name__ == "__main__":
    main()
