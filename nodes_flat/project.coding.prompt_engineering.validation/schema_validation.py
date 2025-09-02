#!/usr/bin/env python3
import argparse
import os
import sys
import yaml

REQ_KB_KEYS = [
    "node_info.path",
    "node_info.description",
    "platform_constraints",
    "validation_criteria",
]
REQ_CONSTRAINT_KEYS = ["constraints", "dependencies"]
REQ_SUPP_SECTIONS = [
    "# node_context",
    "## Node-Specific Context Injection",
    "## Validation Requirements",
]

def load_yaml(p):
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def check_keys(data, dotted_keys):
    for dk in dotted_keys:
        cur = data
        for part in dk.split("."):
            if part not in cur:
                return False, dk
            cur = cur[part]
    return True, None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", required=True)
    args = ap.parse_args()

    root = os.path.abspath(args.repo_root)
    node = os.path.join(root, "nodes", "project.coding.prompt_engineering")

    kb = os.path.join(node, "knowledge_base.yaml")
    cs = os.path.join(node, "constraints.yaml")
    sp = os.path.join(node, "supplement_prompt.md")

    missing = [p for p in [kb, cs, sp] if not os.path.isfile(p)]
    if missing:
        print(f"ERROR: Missing required files: {missing}")
        sys.exit(1)

    kb_data = load_yaml(kb)
    ok, miss = check_keys(kb_data, REQ_KB_KEYS)
    if not ok:
        print(f"ERROR: knowledge_base.yaml missing key: {miss}")
        sys.exit(1)

    cs_data = load_yaml(cs)
    for k in REQ_CONSTRAINT_KEYS:
        if k not in cs_data:
            print(f"ERROR: constraints.yaml missing key: {k}")
            sys.exit(1)

    with open(sp, "r", encoding="utf-8") as f:
        txt = f.read()
    for sec in REQ_SUPP_SECTIONS:
        if sec not in txt:
            print(f"ERROR: supplement_prompt.md missing section: {sec}")
            sys.exit(1)

    print("OK: Schema validation passed.")

if __name__ == "__main__":
    main()
