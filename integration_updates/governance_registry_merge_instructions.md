# Governance Registry Merge Instructions

1. Open `governance_registry.yaml` in repo root.
2. Merge the contents of `governance_enhancements/governance_registry_platform_selection_additions.yaml`
   under the root key (top-level). Preserve existing keys.
3. Verify the new top-level key exists:
   ```yaml
   platform_selection_system: { ... }
   ```
4. Commit changes:
   ```bash
   git add governance_registry.yaml
   git commit -m "feat(selection): merge empirically validated platform selection system"
   ```
