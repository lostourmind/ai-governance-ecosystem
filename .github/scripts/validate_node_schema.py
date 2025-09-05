#!/usr/bin/env python3
import hashlib, os, re, sys

NODE_PATH = "nodes/project.coding.web_development.vanilla/node.yaml"
REG_PATH  = "governance_registry.yaml"

PROHIBITED = {
    "schema_version","version","lifecycle_phase","inputs","outputs","runbook_hooks",
    "constraints_anchor","routing","id","description","assets","breadcrumb_links","navigation"
}

TEMPLATE_FIXED = """node_id: "project.coding.web_development.vanilla"
title: "Project Coding Web Development Vanilla"
breadcrumbs:
  node_dir: "nodes/project.coding.web_development.vanilla"
  node_yaml_raw: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/project.coding.web_development.vanilla/node.yaml"
  node_yaml_web: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/project.coding.web_development.vanilla/node.yaml"
  artifacts:
  - path: "nodes/project.coding.web_development.vanilla/README.md"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/project.coding.web_development.vanilla/README.md"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/project.coding.web_development.vanilla/README.md"
  - path: "nodes/project.coding.web_development.vanilla/constraints.yaml"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/project.coding.web_development.vanilla/constraints.yaml"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/project.coding.web_development.vanilla/constraints.yaml"
  - path: "nodes/project.coding.web_development.vanilla/knowledge_base.yaml"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/project.coding.web_development.vanilla/knowledge_base.yaml"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/project.coding.web_development.vanilla/knowledge_base.yaml"
  - path: "nodes/project.coding.web_development.vanilla/supplement_prompt.md"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/project.coding.web_development.vanilla/supplement_prompt.md"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/project.coding.web_development.vanilla/supplement_prompt.md"
  registry:
    path: "governance_registry.yaml"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/governance_registry.yaml"
    checksum_sha256: "{SHA}"
governance:
  registry_path: "governance_registry.yaml"
  registry_checksum_sha256: "{SHA}"
updated_at: "{TS}"
"""

def fail(msg):
    print(f"ERROR: {msg}")
    sys.exit(1)

# 1) Files exist
if not os.path.isfile(NODE_PATH):
    fail(f"Missing {NODE_PATH}")
if not os.path.isfile(REG_PATH):
    fail(f"Missing {REG_PATH}")

# 2) Compute registry sha256
h = hashlib.sha256()
with open(REG_PATH, "rb") as f:
    for chunk in iter(lambda: f.read(1<<16), b""):
        h.update(chunk)
sha = h.hexdigest()

# 3) Read node.yaml
with open(NODE_PATH, "r", encoding="utf-8") as f:
    node_text = f.read()

# 4) Prohibited fields check (simple substring scan, whole-word-ish)
for key in PROHIBITED:
    if re.search(rf'(^|\s){re.escape(key)}\s*:', node_text):
        fail(f"Prohibited field present: {key}")

# 5) Exact structure check except timestamp value
#    Extract updated_at line and replace it with a placeholder to compare
m = re.search(r'updated_at:\s*"([^"]+)"\s*$', node_text.strip(), re.M)
if not m:
    fail('Missing updated_at field')
ts = m.group(1)

# 6) Timestamp sanity (very light ISO 8601 Z)
if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', ts):
    fail('updated_at must be ISO8601 UTC ending with Z, e.g. 2025-09-05T00:00:00Z')

# 7) Check both checksum fields match the registry hash
if f'checksum_sha256: "{sha}"' not in node_text:
    fail("Breadcrumbs registry.checksum_sha256 does not match governance_registry.yaml")
if f'registry_checksum_sha256: "{sha}"' not in node_text:
    fail("governance.registry_checksum_sha256 does not match go
