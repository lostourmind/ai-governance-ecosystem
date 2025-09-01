#!/usr/bin/env python3
import sys, json, yaml
from pathlib import Path

def main():
    repo = Path(".")
    yaml_files = list(repo.rglob("*.yml")) + list(repo.rglob("*.yaml"))
    pss_locations = []
    deprecated_defs = []
    aliases = {}
    errors = []

    for yf in yaml_files:
        try:
            data = yaml.safe_load(yf.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(data, dict):
            if "platform_selection_system" in data:
                pss_locations.append(str(yf))
            if "deprecated_tasks" in data:
                deprecated_defs.append(str(yf))
            if "platform_name_aliases" in data and not aliases:
                aliases = data["platform_name_aliases"]

    # Rule: only one PSS definition, must be in governance_registry.yaml
    targets = [p for p in pss_locations if not p.endswith("governance_registry.yaml")]
    if len(pss_locations) == 0:
        errors.append("No platform_selection_system found.")
    elif len(pss_locations) > 1 or targets:
        errors.append(f"platform_selection_system defined in multiple files: {pss_locations}")

    # Rule: exactly one deprecated_tasks
    if len(deprecated_defs) == 0:
        errors.append("No deprecated_tasks block found.")
    elif len(deprecated_defs) > 1:
        # allow only governance_registry.yaml
        extras = [p for p in deprecated_defs if not p.endswith("governance_registry.yaml")]
        if extras:
            errors.append(f"deprecated_tasks duplicated in: {extras}")

    if errors:
        print("::error::" + " | ".join(errors))
        sys.exit(1)
    print("Governance consistency checks passed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
