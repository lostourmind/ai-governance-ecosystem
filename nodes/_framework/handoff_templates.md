# Node Creation Handoff Templates

## Standard Node Creation Template

Use this exact template structure in all node creation handoffs:

### Complete node.yaml Template
```yaml
# COPY THIS STRUCTURE EXACTLY - Replace only the indicated placeholders
node_id: {NODE_DOMAIN_PATH}
title: "Project {CATEGORY} {DOMAIN}"
breadcrumbs:
  node_dir: "nodes/{NODE_DOMAIN_PATH}"
  node_yaml_raw: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/{NODE_DOMAIN_PATH}/node.yaml"
  node_yaml_web: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/{NODE_DOMAIN_PATH}/node.yaml"
  artifacts:
  - path: "nodes/{NODE_DOMAIN_PATH}/README.md"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/{NODE_DOMAIN_PATH}/README.md"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/{NODE_DOMAIN_PATH}/README.md"
  - path: "nodes/{NODE_DOMAIN_PATH}/constraints.yaml"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/{NODE_DOMAIN_PATH}/constraints.yaml"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/{NODE_DOMAIN_PATH}/constraints.yaml"
  - path: "nodes/{NODE_DOMAIN_PATH}/knowledge_base.yaml"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/{NODE_DOMAIN_PATH}/knowledge_base.yaml"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/{NODE_DOMAIN_PATH}/knowledge_base.yaml"
  - path: "nodes/{NODE_DOMAIN_PATH}/supplement_prompt.md"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/nodes/{NODE_DOMAIN_PATH}/supplement_prompt.md"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/nodes/{NODE_DOMAIN_PATH}/supplement_prompt.md"
  registry:
    path: "governance_registry.yaml"
    raw_url: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml"
    web_url: "https://github.com/lostourmind/ai-governance-ecosystem/blob/main/governance_registry.yaml"
    checksum_sha256: "a7e44727a187cd3d65fcdac70d460cb82f3d0db1f6755a977fbba9eaa84988c6"
governance:
  registry_path: "governance_registry.yaml"
  registry_checksum_sha256: "a7e44727a187cd3d65fcdac70d460cb82f3d0db1f6755a977fbba9eaa84988c6"
updated_at: "2025-09-02T00:00:00Z"