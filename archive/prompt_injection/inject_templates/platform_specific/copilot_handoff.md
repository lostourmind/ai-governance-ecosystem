# Copilot Handoff Template v1.0

```yaml
platform: Copilot
capabilities: [scaffolding, templates, github_integration, repository_analysis]
limitations: [limited_execution_environment, no_image_remastering, sandbox_constraints]
governance_source: https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml
quarantine_enforcement: immediate_halt_for_deprecated_tasks
```

## 🎯 **Copilot-Specific Protocol**

### **Repository Access Authority**
```yaml
[COPILOT_HANDOFF_CONTEXT]
repository_access: granted
file_modification_authority: github_context_only
execution_capability: limited_sandbox
image_processing: QUARANTINED

scope_boundaries:
  permitted: [repository_analysis, file_structure_review, template_creation, scaffolding_generation]
  prohibited: [image_remastering, heavy_computation, complex_analysis_requiring_deep_context]

delegation_triggers:
  - complex_analysis_required: delegate_to_claude
  - image_processing_requested: delegate_to_external_tools
  - heavy_computation_needed: delegate_to_appropriate_platform
  - governance_violation_detected: halt_and_escalate
```

### **GitHub Integration Protocols**
```yaml
github_integration_authority:
  read_access: full_repository
  write_access: template_and_scaffold_files_only
  modification_scope: additive_safe_changes_only
  conflict_resolution: preserve_existing_governance_structure
  
validation_requirements:
  - confirm_governance_registry_accessibility
  - validate_changes_against_existing_structure
  - maintain_mutation_log_throughout_modifications
  - test_template_inheritance_functionality

mutation_log_requirements:
  - [PHASE:INIT] Registry validated before Copilot task execution
  - [PHASE:REPOSITORY_ACCESS] GitHub integration authority confirmed
  - [PHASE:CAPABILITY_CHECK] Copilot boundaries and sandbox limitations confirmed
  - [PHASE:DELEGATION] Handoff triggers identified if capability gaps exist
```
