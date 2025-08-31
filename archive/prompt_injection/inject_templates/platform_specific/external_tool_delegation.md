# External Tool Delegation Template v1.0

```yaml
delegation_authority: user_execution_required
governance_source: https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml
enforcement_policy: HALT_ON_ASSUMPTION
quarantine_compliance: enforces_deprecated_task_delegation
```

## 🎯 **External Tool Handoff Protocol**

### **Approved External Tools**
```yaml
image_processing_tools:
  Nero_AI:
    capability: image_upscaling_and_enhancement
    validated: true
    cost_model: pay_to_play
    governance_status: approved_for_likeness_retention
    test_validation: "SeaWorld_photo_successful_upscale_2025_08_30"
  
  ESRGAN:
    capability: general_image_super_resolution
    validated: true
    cost_model: open_source
    governance_status: approved_for_restoration
  
  Real_ESRGAN:
    capability: real_world_image_restoration
    validated: true
    cost_model: open_source
    governance_status: approved_for_photo_enhancement
  
  GFPGAN:
    capability: face_restoration_specialized
    validated: true
    cost_model: open_source
    governance_status: approved_for_face_enhancement

execution_environments:
  user_local:
    authority: full_execution_capability
    validation: user_responsibility
    governance: maintain_audit_trail
  
  cloud_services:
    authority: platform_dependent
    validation: service_dependent
    governance: preserve_handoff_context
```

### **Delegation Context Requirements**
```yaml
external_tool_handoff:
  task_specification:
    - objective_clear_and_measurable
    - input_requirements_specified
    - output_format_defined
    - quality_criteria_established
  
  governance_preservation:
    - original_ai_conversation_context
    - rollback_anchor_to_ai_session
    - validation_criteria_for_results
    - integration_back_to_ai_workflow
  
  user_execution_guidance:
    - tool_selection_rationale
    - step_by_step_execution_guide
    - validation_checkpoints
    - result_integration_protocols

mutation_log_requirements:
  - [PHASE:DELEGATION] External tool handoff initiated
  - [PHASE:TOOL_SELECTION] Appropriate tool identified and validated
  - [PHASE:USER_EXECUTION] Execution delegated to user environment
  - [PHASE:VALIDATION] Results validation criteria established
```
