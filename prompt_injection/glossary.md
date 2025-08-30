# Governance Glossary

restart-safe:
  - Printer macros: preserves execution state across power loss or emergency stop
  - AI workflows: maintains clause discipline and source fidelity across session resets
  - Governance scaffolds: supports rollback, mutation logging, and revalidation without drift

mutation-log:
  - Structured record of platform behavior, breaches, and lifecycle transitions

SOURCE_DECLARED:
  - Explicit reference to the authoritative source file or repo
  - Must be honored before execution

HALT_ON_ASSUMPTION:
  - Execution policy tag that forces platform to stop and request clarification if scope or constraints are unclear
