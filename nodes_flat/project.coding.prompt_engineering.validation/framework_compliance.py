#!/usr/bin/env python3
import argparse
import os
import sys
import yaml

DETECTION_INSERT = {
    "prompt_engineering": {
        "patterns": [
            "prompt engineering",
            "prompt design",
            "ai prompting",
            "prompt optimization",
            "prompt templates",
            "context injection",
        ],
        "nodes": ["project.coding.prompt_engineering"],
    }
}

def load_yaml(p):
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def ensure_detection_mapping(dp_path):
    data = load_yaml(dp_path)
    pe = data.get("prompt_engineering")
    if not pe:
        return False, "detection_patterns.yaml lacks 'prompt_engineering' mapping"
    nodes = pe.get("nodes", [])
    if "project.coding.prompt_engineering" not in nodes:
        return False, "detection_patterns.yaml missing node entry for project.coding.prompt_engineering"
    patterns = set(pe.get("patterns", []))
    needed = set(DETECTION_INSERT["prompt_engineering"]["patterns"])
    missing = sorted(list(needed - patterns))
    if missing:
        return False, f"detection_patterns.yaml missing patterns: {missing}"
    return True, ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", required=True)
    args = ap.parse_args()

    root = os.path.abspath(args.repo_root)
    node = os.path.join(root, "nodes", "project.coding.prompt_engineering")

    # Node path correctness
    if not os.path.isdir(node):
        print("ERROR: Node directory not present or path incorrect.")
        sys.exit(1)

    # Required files present
    for rel in ["knowledge_base.yaml", "constraints.yaml", "supplement_prompt.md"]:
        if not os.path.isfile(os.path.join(node, rel)):
            print(f"ERROR: Missing required file: {rel}")
            sys.exit(1)

    # Framework files presence
    dp = os.path.join(root, "nodes", "_framework", "detection_patterns.yaml")
    sv = os.path.join(root, "nodes", "_framework", "schema_validation.yaml")
    inj = os.path.join(root, "nodes", "_framework", "injection_templates.md")
    reg = os.path.join(root, "governance_registry.yaml")

    missing = [p for p in [dp, sv, inj, reg] if not os.path.isfile(p)]
    if missing:
        print(f"ERROR: Framework access failure. Missing: {missing}")
        sys.exit(1)

    ok, msg = ensure_detection_mapping(dp)
    if not ok:
        print(f"ERROR: {msg}")
        sys.exit(1)

    print("OK: Framework compliance checks passed.")

if __name__ == "__main__":
    main()
