#!/usr/bin/env python3
import sys, json, yaml, pathlib, hashlib, datetime

def load_yaml(p):
    with open(p, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def handoff(node_dir: pathlib.Path, repo_root: pathlib.Path, include_raw=True, updates=None, extra=""):
    node_yaml = node_dir / "node.yaml"
    node = load_yaml(node_yaml) if node_yaml.exists() else {}
    breadcrumbs = load_yaml(repo_root / "nodes" / "_framework" / "breadcrumbs.yaml")

    art_lines = []
    for a in node.get("breadcrumbs", {}).get("artifacts", []):
        art_lines.append(f"- {a['path']}")

    raw_node = node.get("breadcrumbs", {}).get("node_yaml_raw", "")
    web_node = node.get("breadcrumbs", {}).get("node_yaml_web", "")

    reg = node.get("breadcrumbs", {}).get("registry", {})
    reg_line = f"{reg.get('path','N/A')} (sha256: {reg.get('checksum_sha256','N/A')})"

    updates = updates or {}

    md = []
    md.append(f"# Handoff for {node.get('node_id', node_dir.name)}")
    md.append("")
    md.append("## Intent")
    md.append("Update existing node information and attach artifacts for API/tool integration.")
    md.append("")
    md.append("## Inputs")
    md.append(f"- node_id: {node.get('node_id', node_dir.name)}")
    md.append(f"- extra_context: {extra}")
    md.append("")
    md.append("## Registry")
    md.append(f"- path: {reg.get('path','N/A')}")
    if include_raw:
        md.append(f"- raw: {reg.get('raw_url','N/A')}")
        md.append(f"- web: {reg.get('web_url','N/A')}")
    md.append(f"- checksum: {reg.get('checksum_sha256','N/A')}")
    md.append("")
    md.append("## Node Manifest")
    if include_raw:
        md.append(f"- node.yaml (raw): {raw_node}")
        md.append(f"- node.yaml (web): {web_node}")
    md.append("")
    md.append("## Artifacts")
    md.extend(art_lines or ["- none"])
    md.append("")
    md.append("## Patches")
    md.append("```json")
    md.append(json.dumps({"update_fields": updates}, indent=2))
    md.append("```")
    return "\n".join(md)

def main():
    repo_root = pathlib.Path(__file__).resolve().parent.parent
    req = json.loads(sys.stdin.read() or "{}")
    node_id = req.get("node_id")
    include_raw = req.get("include_raw_git_links", True)
    updates = req.get("update_fields")
    extra = req.get("extra_context","")
    if not node_id:
        print("# Error: node_id required")
        return
    node_dir = repo_root / "nodes" / node_id if not node_id.startswith("nodes/") else repo_root / node_id
    print(handoff(node_dir, repo_root, include_raw, updates, extra))

if __name__ == "__main__":
    main()
