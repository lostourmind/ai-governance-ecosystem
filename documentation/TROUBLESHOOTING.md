# Troubleshooting

## Symptoms and fixes
- **Duplicate nodes in output**: Ensure `node_prioritization.most_specific_wins: true` and that the dedup method is present.
- **Registry fetch failures**: Check network. Confirm `governance_cache` directory is writable. Fallback will activate automatically.
- **High token usage warnings**: Split handoffs or reduce injected content. See `TOKEN_MANAGEMENT.md`.
- **No logs on disk**: Confirm process has write access to `./logs`.
