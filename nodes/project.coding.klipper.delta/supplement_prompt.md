# Klipper Delta Node Supplement

```yaml
node_context:
  path: "project.coding.klipper.delta"
  inject_priority: high
  merge_strategy: append_to_universal_wrapper
```

## Node-Specific Context Injection

### Mandatory Constraints
- Guard Z homing and probing at center with soft-endstops active.
- Treat `delta_radius` and `arm_length` as controlled parameters. Change only with re-measure + governance log.

### Domain-Specific Knowledge
**Critical Success Factors:**
- Accurate DELTA_CALIBRATE followed by mesh hydration.
- Verified probe repeatability and temperature stabilization.

**Known Pitfalls:**
- Editing endstop trim instead of addressing mechanical tilt.
- Probing with unheated nozzle causing offset drift.

### Validation Requirements
```yaml
node_validation:
  required_checks:
    - delta_calibrate_residuals_within_spec
    - probe_repeatability_pass
  quality_gates:
    - no_nozzle_contact_events
    - mesh_variance_threshold_met
  success_criteria:
    - first_layer_variance_within_spec
    - stable_z_at_perimeter
```

### Integration Guidance
**Compatible Approaches:**
- Lifecycle flags for factory vs field calibration.
- RESPOND overlays requiring confirm for calibration writes.

**Incompatible Patterns:**
- Live edits to geometry during motion.
- Bypassing probe health checks prior to mesh.

### Mutation Log Enhancement
```yaml
node_mutation_log:
  - [PHASE:NODE_CONTEXT] project.coding.klipper.delta specific knowledge injected
  - [PHASE:CONSTRAINTS] Domain constraints applied
  - [PHASE:VALIDATION] Node validation criteria established
```
