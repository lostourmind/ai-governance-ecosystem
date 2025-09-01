# Cross-Platform AI Exchange Protocols v1.0

```yaml
document_version: v1.0.0
governance_source: https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml
enforcement_policy: HALT_ON_ASSUMPTION
last_updated: 2025-08-31T12:00:00-04:00
test_failure_integration: SeaWorld_photo_restoration_lessons_learned
```

## 🔄 **Multi-Platform Workflow Architecture**

### **Standard Exchange Pattern**
```
[AI Tool A] → [Registry Validation] → [Capability Check] → [Quarantine Verification] → [Handoff Context] → [AI Tool B] → [Execution/Delegation]
```

### **Governance Checkpoints (MANDATORY)**
1. **Registry Validation**: Every AI interaction begins with governance validation
2. **Quarantine Check**: Verify task is not deprecated based on test failures
3. **Capability Declaration**: Each platform declares boundaries and limitations
4. **Authority Confirmation**: Establish what the receiving AI can/cannot do
5. **Delegation Protocol**: Hand off to appropriate tools when capability gaps exist

## 🎯 **Platform Coordination Matrix**

### **Task Routing Logic (Based on Test Results)**
```yaml
task_routing:
  analysis_and_documentation:
    primary: Claude
    secondary: Copilot
    delegation_trigger: execution_required
    quarantine_check: verify_no_image_restoration
  
  repository_operations:
    primary: Copilot
    secondary: user_direct
    delegation_trigger: complex_analysis_required
    quarantine_check: verify_no_deprecated_tasks
  
  file_generation:
    primary: ChatGPT
    secondary: Copilot
    delegation_trigger: complex_logic_required
    quarantine_check: verify_no_execution_validation_needed
  
  code_execution:
    primary: user_environment
    ai_support: code_generation_and_guidance_only
    delegation_trigger: NEVER_DELEGATE_EXECUTION_TO_AI
    quarantine_enforcement: immediate_halt_on_ai_execution_request
  
  image_processing:
    primary: external_specialized_tools
    ai_support: guidance_and_tool_selection_only
    delegation_trigger: immediate_for_any_image_modification
    quarantine_enforcement: immediate_halt_on_ai_image_processing
```

### **Handoff Context Standard (COMPLETE TEMPLATE)**
```yaml
# [COPY THIS TEMPLATE FOR ALL CROSS-PLATFORM HANDOFFS]

handoff_context:
  session_metadata:
    session_id: "[task_YYYYMMDD_HHmm_NNN]"
    source_tool: "[CURRENT_PLATFORM]"
    target_tool: "[RECEIVING_PLATFORM]"
    handoff_timestamp: "[ISO_8601]"
    governance_validated: true
    quarantine_checked: true
  
  governance_context:
    registry_source: "https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml"
    quarantine_source: "/quarantine/deprecated_tasks.yaml"
    layer_path: "[SPECIFIC_REGISTRY_PATH]"
    lifecycle_phase: "[CURRENT_PHASE]"
    rollback_anchor: "[SPECIFIC_REFERENCE]"
    constraints_active: "[LIST_OF_CONSTRAINTS]"
  
  task_specification:
    objective: "[EXPLICIT_GOAL]"
    scope_boundaries: "[WHAT_IS_INCLUDED]"
    exclusions: "[WHAT_IS_EXCLUDED_INCLUDING_QUARANTINED]"
    success_criteria: "[MEASURABLE_OUTCOMES]"
    failure_conditions: "[HALT_TRIGGERS]"
  
  capability_requirements:
    execution_required: "[true|false]"
    file_modification_required: "[true|false]"
    image_processing_required: "[true|false]"
    analysis_depth_required: "[lightweight|moderate|complex]"
    authority_level_needed: "[read|analyze|recommend|delegate]"
  
  platform_constraints:
    prohibited_actions: "[QUARANTINED_TASKS_LIST]"
    delegation_triggers: "[CAPABILITY_GAP_CONDITIONS]"
    escalation_conditions: "[WHEN_TO_HALT_AND_REQUEST_CLARIFICATION]"
```

## 🛡️ **Test Failure Integration**

### **Lessons Learned from SeaWorld Photo Test**
```yaml
documented_failures:
  Claude:
    failure: "generated_python_code_without_execution_capability"
    lesson: "must_delegate_execution_to_user_environment"
    enforcement: "halt_on_execution_requests"
  
  Copilot:
    failure: "created_new_image_instead_of_remastering"
    lesson: "image_tasks_must_be_delegated_to_external_tools"
    enforcement: "quarantine_all_ai_image_processing"
  
  ChatGPT:
    failure: "stalled_under_load_lost_context_fidelity"
    lesson: "limit_to_lightweight_operations_only"
    enforcement: "delegate_heavy_computation_immediately"

governance_improvements:
  - registry_validation_mandatory_first_step
  - capability_boundaries_explicitly_declared
  - task_quarantine_prevents_deprecated_actions
  - delegation_protocols_prevent_capability_overreach
```
