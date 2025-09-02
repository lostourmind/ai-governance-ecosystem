# node_context
This node handles prompt engineering tasks. It delivers prompt templates, context plans, and optimization checklists. It must obey the governance registry and the standard injection template.

## Node-Specific Context Injection
Use these variables with the standard injection format:
- {node_path} → nodes/project.coding.prompt_engineering/
- {knowledge_base} → nodes/project.coding.prompt_engineering/knowledge_base.yaml
- {constraints} → nodes/project.coding.prompt_engineering/constraints.yaml
- {supplement_prompt} → nodes/project.coding.prompt_engineering/supplement_prompt.md

Injection placement points:
1) after_registry_validation
2) before_task_execution

When invoked by detection patterns matching prompt engineering intents, prioritize the most specific node. On mismatch, fall back to base wrapper only.

### Minimal Execution Outline
1. Read governance_registry.yaml and revalidate authority.
2. Confirm detection match and node path.
3. Load constraints.yaml. Enforce constraints.
4. Load knowledge_base.yaml. Bind platform constraints.
5. Inject this supplement at the placement points with listed variables.
6. Execute task-specific prompt operations.

## Validation Requirements
- Presence and readability of all three required files.
- Keys present:
  - knowledge_base.yaml: node_info.path, node_info.description, platform_constraints, validation_criteria
  - constraints.yaml: constraints, dependencies
  - supplement_prompt.md sections: node_context, Node-Specific Context Injection, Validation Requirements
- Detection mapping exists and points to `project.coding.prompt_engineering`.
