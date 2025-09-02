# project.coding.prompt_engineering
Framework-aligned prompt engineering node.

## Validate
```bash
python nodes/project.coding.prompt_engineering/validation/schema_validation.py --repo-root .
python nodes/project.coding.prompt_engineering/validation/framework_compliance.py --repo-root .
```

## Detection Rules Update (in `nodes/_framework/detection_patterns.yaml`)
```yaml
prompt_engineering:
  patterns:
    - "prompt engineering"
    - "prompt design"
    - "ai prompting"
    - "prompt optimization"
    - "prompt templates"
    - "context injection"
  nodes:
    - project.coding.prompt_engineering
```

Regex for context analysis: `prompt (?P<technique>.+) for (?P<platform>.+)`
