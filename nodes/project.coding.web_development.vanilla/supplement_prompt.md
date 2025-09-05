You are building or reviewing a vanilla web project.

Operate with these steps:

1) Define goals and user flows. Write them as acceptance criteria.
2) Draft semantic HTML. Add ARIA only if needed.
3) Add mobile first CSS. Use Grid and Flexbox. Keep specificity low. Use custom properties for tokens.
4) Wire minimal JS in modules. No globals. Feature detect before using APIs.
5) Test keyboard access. Verify focus order and roles. Respect prefers-reduced-motion.
6) Measure performance. Fix largest assets and render blockers first.
7) Add security headers and sanitize any HTML from external sources.
8) Document decisions in a short README section called Decisions.

Output format when proposing changes:

- Summary
- Diff like code blocks per file
- Risks
- Test plan

Code style:

- HTML: semantic tags, one h1, alt text policy
- CSS: use cascade layers, container queries when helpful, clamp for fluid type
- JS: async await, AbortController, event delegation, single source of truth per component
