# Node-Specific Knowledge System

This package adds the flat-path node system, detection and injection utilities, and wrapper addendum.

## Integrate

1. Merge `nodes/` and `tools/` into the repository root.
2. Append `prompt_injection/inject_templates/universal_wrapper.node_injection.addendum.md` to your existing universal wrapper **after** the "Registry Validation" section.
3. Merge `governance_registry.additions.yaml` under the root `governance_registry.yaml` at the top-level key `node_knowledge_system`.
4. Optional: add more nodes under `nodes/` using `_framework/node_template` as a scaffold.

## Validate

- Required files per node: `knowledge_base.yaml`, `supplement_prompt.md`, `constraints.yaml`.
- Run `python tools/node_detector.py` sanity tests.
- Run `python tools/knowledge_injector.py` sample build.
