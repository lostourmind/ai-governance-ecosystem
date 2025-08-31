# Repository Access

RepositoryAccessManager fetches the governance registry and node knowledge via raw GitHub URLs with caching.

## Cache
- Location: `.governance_cache/`
- Timeout: 1 hour

## Fallbacks
- Use cache if available.
- Minimal governance structure if both live fetch and cache fail.
