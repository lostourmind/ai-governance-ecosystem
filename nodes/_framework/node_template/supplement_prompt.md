# Node Supplement Prompt Template

```yaml
node_context:
  path: "[PROJECT.CATEGORY.SUBCATEGORY.SPECIFIC]"
  inject_priority: high
  merge_strategy: append_to_universal_wrapper
```

## Node-Specific Context Injection

### Mandatory Constraints
- [CONSTRAINT_1]: [DETAILED_EXPLANATION_AND_ENFORCEMENT]
- [CONSTRAINT_2]: [DETAILED_EXPLANATION_AND_ENFORCEMENT]

### Domain-Specific Knowledge
**Critical Success Factors:**
- [SUCCESS_FACTOR_1]: [IMPLEMENTATION_GUIDANCE]
- [SUCCESS_FACTOR_2]: [IMPLEMENTATION_GUIDANCE]

**Known Pitfalls:**
- [PITFALL_1]: [AVOIDANCE_STRATEGY]
- [PITFALL_2]: [AVOIDANCE_STRATEGY]

### Validation Requirements
```yaml
node_validation:
  required_checks:
    - [VALIDATION_CHECK_1]
    - [VALIDATION_CHECK_2]
  quality_gates:
    - [QUALITY_GATE_1]
    - [QUALITY_GATE_2]
  success_criteria:
    - [SUCCESS_CRITERION_1]
    - [SUCCESS_CRITERION_2]
```

### Integration Guidance
**Compatible Approaches:**
- [APPROACH_1]: [INTEGRATION_METHOD]
- [APPROACH_2]: [INTEGRATION_METHOD]

**Incompatible Patterns:**
- [PATTERN_1]: [REASON_AND_ALTERNATIVE]
- [PATTERN_2]: [REASON_AND_ALTERNATIVE]

### Mutation Log Enhancement
```yaml
node_mutation_log:
  - [PHASE:NODE_CONTEXT] [NODE_PATH] specific knowledge injected
  - [PHASE:CONSTRAINTS] Domain constraints applied
  - [PHASE:VALIDATION] Node validation criteria established
```
