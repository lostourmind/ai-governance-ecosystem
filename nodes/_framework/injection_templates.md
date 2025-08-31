# Knowledge Injection Templates

## Standard Injection Format
```yaml
[NODE_INJECTION_BLOCK]
node_path: "{detected_node_path}"
knowledge_source: "nodes/{node_path}/supplement_prompt.md"
injection_method: append_to_universal_wrapper
priority: high
```

## Multi-Node Injection
```yaml
[MULTI_NODE_INJECTION]
primary_node: "{most_specific_node}"
supporting_nodes:
  - "{broader_category_node}"
  - "{related_domain_node}"
injection_strategy: layer_from_general_to_specific
```

## Injection Placement Points
- After Registry Validation: Node context setting
- Before Task Execution: Constraint application
- During Handoff Assembly: Knowledge compilation
- Pre-Output Generation: Final validation criteria

## Template Variables
- {node_path}: Detected node path
- {knowledge_base}: Content from knowledge_base.yaml
- {constraints}: Content from constraints.yaml
- {supplement_prompt}: Content from supplement_prompt.md
