# Validation Checklist
- [ ] Klipper boots clean (no TemplateSyntaxError / parse errors)
- [ ] Slicer handoff → PRINT_LAUNCHER → mesh+purge executes
- [ ] First-layer throttle releases to 100% at gate height + audit OK
- [ ] PAUSE and runout park away from part; RESUME restores cleanly
- [ ] FUI does not spam (STOP/HARD_RESET verified)
- [ ] Dryer macros present (if used) and no SET_FAN_SPEED errors
