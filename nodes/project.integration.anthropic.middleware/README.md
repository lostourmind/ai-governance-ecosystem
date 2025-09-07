# Project Integration Anthropic Middleware

Purpose: Provide a governance-compliant node for integrating Anthropic's Claude API into the AI Governance Ecosystem.

## Scope
- Handoff generation from Anthropic to framework nodes
- Schema validation automation for node creation
- Governance anchor verification and audit logging

## Contents
- `node.yaml` — canonical node descriptor (template-exact)
- `constraints.yaml` — operational restrictions mirrored from framework
- `knowledge_base.yaml` — domain knowledge for implementation
- `supplement_prompt.md` — supplemental runtime prompt

## Minimal Usage Flow
1. Validate `node.yaml` against `nodes/_framework/schema_validation.yaml`.
2. Load `constraints.yaml` to enforce write-scope and actions.
3. Use `knowledge_base.yaml` to drive middleware implementation tasks.
4. Apply `supplement_prompt.md` to standardize orchestration prompts.

## Security
- Store API keys in environment variables.
- Scope tokens per service.
- Log only non-sensitive metadata for audits.
