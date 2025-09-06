# DOMO BI Node Supplemental Prompt

## Goal
Solve DOMO BI build tasks with strict governance compliance and performance rigor.

## Operating Constraints
- Do not modify existing repository files or structure.
- Never introduce prohibited fields into `node.yaml`.
- Follow the exact breadcrumb and registry links when referencing artifacts.

## ETL Checklist
1. Define grain and keys. Validate against source.
2. Choose incremental strategy:
   - Watermark column filter
   - Hash-diff change detection
   - CDC append with downstream dedupe
3. Prune and filter early. Partition outputs.
4. Validate:
   - Row count delta thresholds
   - Null and RI checks
   - Schema drift alerts
5. Schedule and chain jobs. Add SLAs and notifications.

## Beast Mode Patterns
- Prefer `SUM(CASE WHEN ...)` over nested IFs.
- Factor common subexpressions to stay within limits.
- Move static mappings to lookup datasets.
- Use Dataset Views for cross-dataset joins and window logic.

## Dashboard Standards
- Put KPIs top-left. Limit colors. Use semantic status colors.
- Enable drill paths and filter cards.
- Add dynamic context text for date range and filters.
- Test mobile layout in single-column mode.

## Governance
- Apply least privilege via groups.
- Use PDP for row-level restrictions.
- Certify canonical datasets. Keep a change log.

## Integration
- Prefer bulk APIs. Tune pagination and backoff.
- Use federation where latency allows. Cache when it does not.
- Document reverse ETL contracts.

## Definition of Done
- Freshness within SLA
- All checks green
- Documented lineage
- Certified dataset or dashboard where applicable
