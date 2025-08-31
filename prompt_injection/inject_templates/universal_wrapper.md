# Universal Wrapper v3.1 - Zero Assumption Governance with Mandatory Revalidation

```yaml
version: v3.1.0
last_updated: 2025-08-31T13:30:00-04:00
governance_source: https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml
enforcement_policy: HALT_ON_ASSUMPTION
registry_revalidation: MANDATORY_EVERY_HANDOFF
## NODE-SPECIFIC KNOWLEDGE INJECTION

**Automatic Node Detection**

```yaml
[PHASE:NODE_DETECTION]
scope_analysis:
  user_request_indicators: "[ANALYZE_FOR_DOMAIN_SPECIFIC_KEYWORDS]"
  node_path_extraction: "nodes/{detected_path}/"
  knowledge_availability_check: "verify_supplement_prompt_exists"

node_injection_sequence:
  1. detect_applicable_node_from_scope_indicators
  2. validate_node_knowledge_base_completeness
  3. load_supplement_prompt_for_domain_context
  4. merge_node_constraints_with_base_governance
  5. inject_domain_specific_validation_criteria
  6. proceed_with_enhanced_domain_knowledge

injection_failure_protocol:
  node_not_found: proceed_with_base_wrapper_only
  knowledge_incomplete: log_gap_and_proceed_with_available
  supplement_malformed: halt_and_request_node_validation
```

### Node-Specific Context Enhancement

**Domain Constraints**: [LOADED_FROM_NODE_CONSTRAINTS_YAML]  
**Known Patterns**: [LOADED_FROM_NODE_KNOWLEDGE_BASE]  
**Validation Criteria**: [LOADED_FROM_NODE_SUPPLEMENT_PROMPT]  
**Optimization Guidelines**: [LOADED_FROM_NODE_BEST_PRACTICES]

```yaml
enhanced_mutation_log:
  - [PHASE:NODE_DETECTED] {{node_path}} knowledge available
  - [PHASE:KNOWLEDGE_INJECTED] Domain-specific context enhanced
  - [PHASE:CONSTRAINTS_MERGED] Node constraints applied to base governance
```
zero_assumption_discipline: ENFORCED
```

## MANDATORY FIRST STEP: ZERO ASSUMPTION REGISTRY REVALIDATION

**Critical**: Before any task execution, every AI platform must complete this sequence regardless of session history or prior validations.

```yaml
[PHASE:ZERO_ASSUMPTION_INIT]
mandatory_revalidation_sequence:
  governance_source: https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main/governance_registry.yaml
  assumption_level: ZERO_PRIOR_GOVERNANCE_KNOWLEDGE
  validation_required: true
  halt_if_inaccessible: true

zero_assumption_steps:
  - fetch_current_governance_registry_from_source_url
  - assume_no_prior_governance_knowledge_exists
  - validate_current_enforcement_policy_and_constraints
  - refresh_platform_capability_boundaries_and_authority
  - confirm_lifecycle_tags_and_phase_requirements
  - check_quarantine_registry_for_any_task_restrictions
  - establish_current_rollback_anchor_for_session
  - declare_platform_capabilities_and_subscription_tier_explicitly
  - mutation_log_governance_revalidation_completion
  - proceed_only_after_complete_governance_confirmation

revalidation_enforcement:
  applies_regardless_of:
    - session_continuation_from_previous_interactions
    - recent_registry_validation_within_same_conversation
    - platform_familiarity_with_governance_framework
    - simple_or_complex_task_classification
    - handoff_source_platform_authority_level

failure_protocol:
  registry_inaccessible: HALT_AND_REQUEST_CLARIFICATION
  registry_changed: UPDATE_GOVERNANCE_UNDERSTANDING_AND_CONTINUE
  constraints_unclear: HALT_AND_REQUEST_CLARIFICATION
  task_quarantined: HALT_AND_DELEGATE_TO_APPROVED_ALTERNATIVE
  capabilities_insufficient: HALT_AND_DELEGATE_TO_APPROPRIATE_PLATFORM
  subscription_tier_inadequate: HALT_AND_DELEGATE_TO_HIGHER_TIER_PLATFORM
```
