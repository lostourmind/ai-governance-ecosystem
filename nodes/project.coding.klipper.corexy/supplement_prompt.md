# Klipper CoreXY Node Supplement

```yaml
node_context:
  path: "project.coding.klipper.corexy"
  inject_priority: high
  merge_strategy: append_to_universal_wrapper
```

## Node-Specific Context Injection

### Mandatory Constraints
- Homing must use safe Z behavior and verified endstop logic. Enforce soft-endstops on entry.
- Persistent state writes must be mutation-logged and restart-safe using SAVE_VARIABLE.

### Domain-Specific Knowledge
**Critical Success Factors:**
- Accurate shaper and PA calibration before speed trials.
- Verified belt symmetry and frame rigidity.

**Known Pitfalls:**
- Slicer overrides that fight firmware limits. Lock key limits in macros.
- Probe offset drift after hot-end changes. Require revalidation hooks.

### Validation Requirements
```yaml
node_validation:
  required_checks:
    - shaper_values_present
    - pressure_advance_validated
  quality_gates:
    - no_thermal_faults_in_stress_test
    - no_stepper_overtemp_events
  success_criteria:
    - dimensional_accuracy_within_spec
    - ringing_reduction_threshold_met
```

### Integration Guidance
**Compatible Approaches:**
- Mesh calibration pre-flight hydration with restart-safe flags.
- Audit overlays via RESPOND MSG for operator confirmations.

**Incompatible Patterns:**
- Unsafe direct G92 Z without verification. Use guarded probes.
- Live config editing during motion. Use queued changes post-print.

### Mutation Log Enhancement
```yaml
node_mutation_log:
  - [PHASE:NODE_CONTEXT] project.coding.klipper.corexy specific knowledge injected
  - [PHASE:CONSTRAINTS] Domain constraints applied
  - [PHASE:VALIDATION] Node validation criteria established
```
