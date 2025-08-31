# FLSun S1 Pro — Klipper Governance Package (Live Baseline)

Package: `FLSun_S1_Pro_Governance_Package_20250824_223203`  
Date: 20250824_223203

This is the canonical, clean baseline snapshot. It mirrors your current, working printer and macro set.

## Contents
- `configs/` — live `printer.cfg`, `macros.cfg`, `oldstock.cfg`
- `docs/` — Governance guide, flowcharts, changelog
- `prompts/` — Agent prompt & safety rules for future chats/agents
- `tools/` — validation checklist
- `versions/manifest.json` — file hashes for integrity

## Inventory (auto-extracted)
- GCODE Macros (75): CALIBRATE_MOTOR, CALIBRATE_MOTOR_DATA, CANCEL, CANCEL_PRINT, CLEAN_CALIBRATE_MOTOR, CLEAN_FILAMENT, END_PRINT, END_PRINT_GOV, FIRST_LAYER_STABLE_RELEASE, GOV_CANARY_ADAPTIVE_PREP, GOV_ECHO, GOV_FILAMENT_UI, GOV_FLS_ARM, GOV_FLS_STATE, GOV_FUI_START, GOV_FUI_STOP, GOV_HYDRATE_NOW, GOV_MESH_FLAGS_READ, GOV_MESH_SAVE_AND_COMMIT, GOV_MESH_SAVE_CURRENT, GOV_PROBE_FLAGS_READ, GOV_PROBE_OFFSET_APPLY_SUGGEST, GOV_PROBE_OFFSET_SUGGEST, GOV_PROBE_READBACK_VERBOSE, GOV_PROBE_RECORD_RESULT, GOV_PROBE_TOUCH_CENTER_CAPTURE, GOV_PROBE_VALIDATE, GOV_PURGE_PRIME, GOV_SET_MESH_PROFILE_CODE, GOV_Z_OFFSET_APPLY, GOV_Z_OFFSET_COMMIT, LOAD_FILAMENT, M106, M600, MEASURING_RESONANCES, PAUSE, PAUSE_AFTER_D, PID_BED, PID_HOTEND, PRE_RESUME, PRE_RESUME_INTERRUPTED, PRINT_CANCEL, PRINT_END, PRINT_LAUNCHER, PROBE_STATE_GOV, RESTORE_E_CURRENT, RESUME, RESUME_INTERRUPTED, SAVE_POWER_LOSS_PARAMS, SET_GCODE_OFFSET, SHUTDOWN, START_PRINT, START_PRINT_RESUME, START_PRINT_SEQUENCE_GOV, STOP_PRINT, TIMELAPSE, TMC, UNLOAD_FILAMENT, ZDOWN, ZUP, _RESUME_PRE_EXTRUDE, bed_level_1, bed_level_2, box_led_off, box_led_on, drying_box_1, drying_box_off, laser_off, laser_on, relay_off, relay_on, save_time, screen_led_off, screen_led_on, set_fan
- Delayed GCodes (10): GOV_DELTA_RISK_NOTE, GOV_FLS_WATCH, GOV_FUI_LOOP, GOV_MOTORS_OFF_WHEN_COOL, GOV_STARTUP_HYDRATE, LOAD_FUNCTION_SWITCH_DELAY, LOAD_GCODE_OFFSETS, PAUSE_AT_D, heatsink, setfan
- Filament Sensors (5): filament_switch_sensor filament_sensor, filament_motion_sensor my_sensor, filament_switch_sensor filament_sensor, filament_motion_sensor my_sensor, filament_switch_sensor power_loss
- Heater/Fan/Sensor blocks (7) entries

## Golden Rules (short)
1) Do NOT place double-curly expressions inside RESPOND MSG. Precompute with {% set %} and concatenate using ~, or use plain literals.
2) Keep Jinja control blocks on their own lines. Avoid inline if/endif on one line.
3) Never change factory pins or pullups without hardware confirmation.
4) Gate extrusions by temperature; guard delta moves with reach clamps and safe Z.
5) Use unique macro names; avoid redefining factory M-codes unless required.
