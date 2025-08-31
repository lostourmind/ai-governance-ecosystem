# React Next.js Node Supplement

```yaml
node_context:
  path: "project.coding.web_development.react.nextjs"
  inject_priority: high
  merge_strategy: append_to_universal_wrapper
```

## Node-Specific Context Injection

### Mandatory Constraints
- Secrets and tokens must remain server-side; never import env accessors into client components.
- Define per-route caching policy (SSR/SSG/ISR) and revalidation triggers.

### Domain-Specific Knowledge
**Critical Success Factors:**
- Clear server vs client component boundaries.
- Measured caching and routing strategy matched to traffic.

**Known Pitfalls:**
- Accidental client hydration of heavy components.
- Middleware doing CPU-bound work.

### Validation Requirements
```yaml
node_validation:
  required_checks:
    - no_secrets_in_client_bundle
    - caching_policies_defined
  quality_gates:
    - typecheck_lint_security_green
    - route_tests_pass
  success_criteria:
    - performance_budgets_met
    - error_boundaries_present
```

### Integration Guidance
**Compatible Approaches:**
- Edge runtime for simple public routes.
- Server Actions for secure data mutations.

**Incompatible Patterns:**
- Client-side secret access.
- Blocking work in middleware.

### Mutation Log Enhancement
```yaml
node_mutation_log:
  - [PHASE:NODE_CONTEXT] project.coding.web_development.react.nextjs specific knowledge injected
  - [PHASE:CONSTRAINTS] Domain constraints applied
  - [PHASE:VALIDATION] Node validation criteria established
```
