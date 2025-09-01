# Universal Wrapper v3.0 - Cross-Platform Task Injection

```yaml
version: v3.0.0
last_updated: 2025-08-31T12:00:00-04:00
governance_source: https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml
enforcement_policy: HALT_ON_ASSUMPTION
registry_validated: REQUIRED_FIRST_STEP
quarantine_registry: /quarantine/deprecated_tasks.yaml
```

## 🛡️ **MANDATORY FIRST STEP: REGISTRY VALIDATION**

**CRITICAL**: Before any task execution, the receiving AI MUST:

```yaml
[PHASE:INIT]
registry_validation_gateway:
  governance_source: https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml
  quarantine_source: /quarantine/deprecated_tasks.yaml
  validation_required: true
  halt_if_inaccessible: true
  
mandatory_sequence:
  1. fetch_governance_registry
  2. validate_enforcement_policy_active
  3. confirm_lifecycle_tags_available
  4. check_quarantine_registry_for_task_restrictions
  5. establish_rollback_anchor
  6. declare_platform_capabilities_explicitly
  
failure_protocol:
  registry_inaccessible: HALT_AND_REQUEST_CLARIFICATION
  constraints_unclear: HALT_AND_REQUEST_CLARIFICATION
  task_quarantined: HALT_AND_DELEGATE_TO_APPROVED_ALTERNATIVE
  capabilities_insufficient: HALT_AND_DELEGATE_TO_APPROPRIATE_PLATFORM
```

## 🔄 **CROSS-PLATFORM HANDOFF PROTOCOL**

### **Outbound Handoff Requirements (Source AI)**
```yaml
handoff_context_mandatory:
  session_metadata:
    session_id: "[task_YYYYMMDD_HHmm_NNN]"
    source_tool: "[copilot|claude|chatgpt|gemini|external]"
    target_tool: "[RECEIVING_PLATFORM]"
    handoff_timestamp: "[ISO_8601_FORMAT]"
    governance_registry_validated: true
  
  task_definition:
    objective: "[SPECIFIC_MEASURABLE_GOAL]"
    scope_boundaries: "[EXPLICIT_INCLUSIONS]"
    exclusions: "[EXPLICIT_EXCLUSIONS_INCLUDING_QUARANTINED_TASKS]"
    success_criteria: "[MEASURABLE_OUTCOMES]"
    failure_conditions: "[SPECIFIC_HALT_TRIGGERS]"
  
  governance_inheritance:
    registry_source: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml"
    layer_path: "[SPECIFIC_REGISTRY_PATH]"
    constraints_active: "[LIST_OF_ACTIVE_CONSTRAINTS]"
    quality_gates: "[ENFORCEMENT_REQUIREMENTS]"
    rollback_anchor: "[SPECIFIC_REFERENCE_POINT]"
    lifecycle_phase: "[CURRENT_PHASE]"
  
  capability_requirements:
    execution_required: "[true|false]"
    validation_required: "[true|false]"
    modification_authority: "[read_only|analyze|recommend|delegate]"
    prohibited_actions: "[QUARANTINED_TASKS_LIST]"
    platform_limitations_acknowledged: true
```

### **Inbound Validation Requirements (Receiving AI)**
```yaml
[PHASE:HANDOFF_VALIDATION]
mandatory_validation_sequence:
  1. registry_accessibility_verification
  2. quarantine_registry_check_for_task_restrictions
  3. handoff_context_completeness_validation
  4. capability_requirement_matching_against_platform_matrix
  5. authority_boundary_confirmation_and_enforcement
  6. rollback_anchor_establishment
  7. mutation_log_initialization_with_handoff_reference

validation_gates:
  all_required_fields_present: HALT_IF_MISSING
  task_not_quarantined: HALT_IF_DEPRECATED
  capability_requirements_achievable: HALT_IF_INSUFFICIENT
  scope_boundaries_clear_and_achievable: HALT_IF_AMBIGUOUS
  constraints_compatible_with_platform: HALT_IF_CONFLICTING
  authority_appropriate_for_platform: HALT_IF_OVERREACH
```

## 🚨 **CAPABILITY ENFORCEMENT MATRIX**

### **Platform Capability Boundaries (ENFORCED)**
```yaml
platform_enforcement:
  Claude:
    permitted_actions: [analyze, code_generation, documentation, recommendations]
    execution_capability: false
    image_tasks: QUARANTINED
    handoff_required_for: [execution, file_modification, image_processing]
    authority_limit: analysis_and_recommendations_only
  
  Copilot:
    permitted_actions: [scaffolding, templates, github_integration, repository_analysis]
    execution_capability: limited_sandbox_only
    image_tasks: QUARANTINED
    handoff_required_for: [complex_analysis, heavy_computation, image_processing]
    authority_limit: repository_context_and_scaffolding
  
  ChatGPT:
    permitted_actions: [lightweight_validation, quick_analysis, file_generation]
    execution_capability: false
    load_handling: poor_performance_documented
    image_tasks: QUARANTINED
    handoff_required_for: [heavy_computation, complex_analysis, execution]
    authority_limit: lightweight_operations_and_file_generation
  
  External_Tools:
    image_processing: [Nero_AI, ESRGAN, Real_ESRGAN, GFPGAN]
    execution_environments: [user_local, cloud_services]
    authority: full_capability_within_specialization
```

## ⚡ **QUARANTINE ENFORCEMENT PROTOCOLS**
```yaml
immediate_halt_triggers:
  - ai_image_restoration_request
  - ai_image_upscaling_request  
  - likeness_retention_task_ai
  - code_execution_request_without_user_environment
  - scope_drift_beyond_capability_boundaries
  - registry_validation_failure
  - handoff_context_incomplete

delegation_requirements:
  image_tasks: delegate_to_external_tools_immediately
  execution_tasks: delegate_to_user_environment_with_guidance
  capability_gaps: delegate_to_appropriate_platform_with_context
```

## 📝 **MUTATION LOGGING ENFORCEMENT**
```yaml
mandatory_mutation_log_entries:
  - [PHASE:INIT] Registry validated before task execution
  - [PHASE:CAPABILITY_CHECK] Platform boundaries confirmed
  - [PHASE:QUARANTINE_CHECK] Deprecated tasks verified against registry
  - [PHASE:VALIDATED] Task approved for platform capabilities
  - [PHASE:EXECUTION] Progress within scope and authority boundaries
  - [PHASE:CHECKPOINT] Validation points reached successfully
  - [PHASE:DELEGATION] Handoff required due to capability gap
  - [PHASE:QUARANTINE] Task halted due to deprecated status
  - [PHASE:ROLLBACK] State restored to established anchor
  - [PHASE:COMPLETION] Objective achieved within governance constraints
```
