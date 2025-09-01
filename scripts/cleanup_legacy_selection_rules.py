#!/usr/bin/env python3
# Remove legacy duplicated selection-rule files safely.
from pathlib import Path
LEGACY = [
  "governance_registry_platform_selection_additions.yaml",
  "rules/platform_selection_rules.yaml",
  "configuration/tool_selection_rules.yaml"
]
removed = []
for rel in LEGACY:
    p = Path(rel)
    if p.exists():
        p.unlink()
        removed.append(rel)
print("Removed:", removed)
