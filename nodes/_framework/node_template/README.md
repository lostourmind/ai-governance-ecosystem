# Node Template Usage

Use this template to seed a new knowledge node under `nodes/<flat.path.name>/`.

Required files per node:
- `knowledge_base.yaml` — domain knowledge, failure patterns, optimization, validation gates.
- `supplement_prompt.md` — injection block, mandatory constraints, validation spec.
- `constraints.yaml` — hard/soft limits, dependencies, platform specifics.

Steps:
1. Copy this `node_template` into your new node folder.
2. Replace placeholders with concrete, domain-specific details.
3. Ensure `node_info.path` equals the node's flat path.
4. Add any `validated_configs/` examples and a `README.md` describing scope.
