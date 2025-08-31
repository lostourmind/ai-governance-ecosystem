
# Implementation Check

Run these checks before any workflow:
1. Load and parse `governance_registry.yaml`.
2. Verify required sections exist.
3. Confirm quarantine registry present at `quarantine/deprecated_tasks.yaml`.
4. Ensure platform-specific handoff templates exist under `inject_templates/platform_specific/` within the `prompt_injection/` root if present, else at repo root.
