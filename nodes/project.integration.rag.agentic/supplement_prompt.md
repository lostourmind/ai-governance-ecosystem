# Supplement Prompt: Project Integration RAG Agentic

## Objectives
- Enforce schema constraints and governance anchors.
- Operate RAG retrieval with precision and measurable quality.
- Orchestrate agent tools safely with deterministic handoffs.

## RAG Retrieval Protocol
1. Define the task and required evidence.
2. Choose retrieval mode:
   - Dense: embedding similarity on vector DB.
   - Sparse: keyword/BM25 for exact terms.
   - Hybrid: merge + deduplicate + normalize scores.
3. Chunking:
   - Aim for semantic units.
   - Overlap small where context breaks.
   - Keep token budgets explicit.
4. Ranking:
   - Heuristic pre-filter then cross-encoder rerank if budget allows.
   - Penalize duplicates and low-information chunks.
5. Grounding:
   - Attach citations and identifiers.
   - Track recall@k and MRR per task.

## Agentic Orchestration
- Single-agent first. Escalate to multi-agent only for parallelizable or specialized steps.
- Shared memory:
  - Short-term: conversation buffer with TTL.
  - Long-term: distilled summaries in vector store + key-value facts.
- Planning:
  - Decompose into steps. Tag each step with inputs, tools, and exit criteria.
- Robustness:
  - Retries with backoff on transient faults.
  - Guardrails on tool outputs.
  - Safe fallbacks on missing data.

## Web Handoff Patterns
- HTTP POST for task payloads. Include correlation IDs.
- Webhooks for async completion. Verify signatures.
- OAuth2 or signed tokens for auth. Scope minimally.
- Rate limit client and server. Observe budgets.
- Version endpoints. Keep backward compatibility windows.

## Manual Integration
- Human-in-the-loop gates for high risk changes.
- Approval chains with audit trails.
- Templates for handoff documents and escalation notes.

## API Integration
- Prefer REST for stability and GraphQL where clients need flexibility.
- Stream tokens or partials when latency matters.
- Maintain SDKs with typed models and test fixtures.
- Versioning plan: Semantic versioning, deprecation notices, migration guides.

## Quality Metrics
- Retrieval: recall@k, nDCG, MRR.
- Generation: factuality score with adversarial checks.
- Agent: task success rate, mean steps, tool error rate.
