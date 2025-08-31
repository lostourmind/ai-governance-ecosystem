# Operational Deployment

## Scope
Deploy enhancements for node detection deduplication, token budget tracking, repository access resilience, and enhanced logging.

## Steps
1. Copy `tools/*.py` into your repository `tools/`.
2. Merge `governance/registry_overlays/operational_resilience.yaml` into `governance_registry.yaml`.
3. Optionally merge `config/detection_patterns_enhanced.yaml` into your detection patterns source.
4. Validate with your existing test flow.

## Smoke Test
```bash
python tools/repository_access_manager.py
python -c "from tools.node_detector import NodeDetector; print(NodeDetector().detect_nodes('NextJS app router with React'))"
python -c "from tools.knowledge_injector import KnowledgeInjector as KI; print(KI()._assemble_handoff_context('x','y','ChatGPT',['project.coding.web_development.react.nextjs'])['token_budget'])"
```

## Rollback
Remove the new tools and revert config merges. Registry overlay is additive only.
