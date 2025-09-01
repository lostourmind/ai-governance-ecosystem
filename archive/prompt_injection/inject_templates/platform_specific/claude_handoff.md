# Claude Handoff Template v1.0

```yaml
platform: Claude
capabilities: [analysis, code_generation, documentation, recommendations]
limitations: [no_execution, no_file_modification, no_image_processing]
governance_source: https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml
quarantine_enforcement: immediate_halt_for_deprecated_tasks
```

## 🎯 **Claude-Specific Protocol**

### **Mandatory Handoff Context**
```yaml
[CLAUDE_HANDOFF_CONTEXT]
task_classification: [analysis|code_generation|documentation|recommendation]
execution_required: false
file_modification_required: false
image_processing_required: false

scope_boundaries:
  permitted: [analyze_existing_content, generate_code_templates, create_documentation, provide_recommendations]
  prohibited: [execute_code, modify_files_directly, process_images, validate_execution_results]

delegation_triggers:
  - execution_required: delegate_to_user_environment
  - file_modification_needed: delegate_to_copilot_or_user
  - image_processing_requested: delegate_to_external_tools
  - validation_of_execution_needed: delegate_to_user_testing
```

### **Quality Gates for Claude**
```yaml
claude_quality_enforcement:
  code_generation:
    - include_comprehensive_comments
    - provide_usage_examples
    - specify_dependencies_explicitly
    - include_error_handling
    - note_execution_environment_requirements
  
  analysis_and_recommendations:
    - cite_specific_evidence_or_sources
    - provide_measurable_criteria
    - include_implementation_guidance
    - specify_validation_steps
    - identify_potential_risks_or_limitations

mutation_log_requirements:
  - [PHASE:INIT] Registry validated before Claude task execution
  - [PHASE:CAPABILITY_CHECK] Claude boundaries confirmed
  - [PHASE:QUARANTINE_CHECK] Deprecated tasks verified
  - [PHASE:DELEGATION] Handoff triggers identified if capability gaps exist
```
