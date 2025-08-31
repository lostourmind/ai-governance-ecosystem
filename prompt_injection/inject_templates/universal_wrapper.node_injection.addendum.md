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
