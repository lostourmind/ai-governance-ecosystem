Drop-in package for repo root.

Install:
1) On your target git branch.
2) Remove current files except .git/.github/.gitignore.
3) Unzip contents here.
4) git add -A && git commit -m "Replace with validated drop-in" && git push

Canonical files:
- detection_patterns.yaml (root, replaces nodes/_framework/detection_patterns.yaml)
- breadcrumbs.yaml, schema_validation.yaml, governance_registry.yaml
- injection_templates/, nodes_flat/, _validation_reports/
