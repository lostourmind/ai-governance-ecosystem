version: v1.0.1  
last_updated: 2025-08-30T19:30:00-04:00  
scope: project.platform.*  
objective: Governance-grade prompt injection scaffold for multi-agent orchestration  
source_declared: https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/prompt_injection/inject_templates/universal_wrapper.md  

constraints:
  - Lifecycle tagging required
  - HALT_ON_ASSUMPTION enforced
  - Rollback logic must be mutation-logged
  - All platform wrappers must inherit this structure
  - Execution must halt if declared source is inaccessible or unverifiable
  - No fallback logic may be fabricated
  - Scope drift must be detected and halted
  - All deviations must be mutation-logged with rollback anchors

execution_policy: HALT_ON_ASSUMPTION  
phase: INIT  

governance_capsule:
  lifecycle_tags:
    - PHASE:INIT
    - PHASE:VALIDATED
    - PHASE:ROLLBACK
    - PHASE:SETPOINT
    - PHASE:QUARANTINE
  rollback_anchor: [INSERT FILE OR LOG PATH]
  context_registry: context_registry.yaml
  gate_controls:
    code_quality: enforced
    scope_drift: monitored
    progress_validation: required
  handoff_protocol:
    required_fields:
      - source_tool
      - target_tool
      - task_scope
      - rollback_anchor
      - lifecycle_phase
    validation_required: true
    context_registry: context_registry.yaml

validation_notes:
  - This wrapper is the root governance scaffold for all platform inject templates
  - All constraints are inherited unless explicitly overridden with justification
  - Source must be raw Git URL for universal compatibility
  - Wrapper is restart-safe and zero-maintenance across prompt cycles

mutation_log_reference:
  - [PHASE:VALIDATED] Wrapper scaffold confirmed
  - [PHASE:SETPOINT] Raw file enforcement locked
  - [PHASE:QUARANTINE] Historical ambiguity flushed
