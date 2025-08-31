# SQL DOMO Node Supplement

```yaml
node_context:
  path: "project.coding.SQL.DOMO"
  inject_priority: high
  merge_strategy: append_to_universal_wrapper
```

## Node-Specific Context Injection

### Mandatory Constraints
- Enforce dataset grain and primary keys before joins.
- Apply RLS and masking where required by policy.

### Domain-Specific Knowledge
**Critical Success Factors:**
- Stable lineage with scheduled jobs and clear failure alerts.
- Efficient connectors with pushdown of filters and projections when possible.

**Known Pitfalls:**
- SELECT * in production causing schema drift breakage.
- Window functions without ORDER BY leading to nondeterministic results.

### Validation Requirements
```yaml
node_validation:
  required_checks:
    - dataset_grain_verified
    - rls_policies_applied
  quality_gates:
    - schema_drift_check_passed
    - null_duplicate_thresholds_met
  success_criteria:
    - freshness_within_sla
    - aggregates_match_reference
```

### Integration Guidance
**Compatible Approaches:**
- Incremental DataFlows with backfill windows.
- Parameterized queries for reuse.

**Incompatible Patterns:**
- Cross-tenant data joins. Instead use secured exports and curated staging.
- Unbounded cross joins. Use keys and filters.

### Mutation Log Enhancement
```yaml
node_mutation_log:
  - [PHASE:NODE_CONTEXT] project.coding.SQL.DOMO specific knowledge injected
  - [PHASE:CONSTRAINTS] Domain constraints applied
  - [PHASE:VALIDATION] Node validation criteria established
```
