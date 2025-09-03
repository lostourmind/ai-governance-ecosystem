# Injection-Ready Operations Manual Context

## Goal
Produce a complete, accessible, and versioned operations manual section that meets the constraints and schema.

## Inputs
- **Task**: {{task}}
- **Source Evidence**: {{evidence}}
- **Constraints**: {{constraints}}
- **Output Schema**: {{schema}}

## Steps
1. Restate task in one sentence.
2. Identify prerequisites and assumptions. Mark unknowns as "UNKNOWN".
3. Draft procedure as numbered steps with expected results.
4. Add rollback path and validation checks.
5. Add references and version notes.
6. Validate against schema and accessibility constraints.
7. Emit only the final output per schema.

## Constraints
- Use active voice and numbered steps.
- Include alt text for images and diagrams.
- Include roles, inputs, outputs, risks, and rollback.
- No extra prose outside schema.

## Output
Return only the object that matches **Output Schema**.
