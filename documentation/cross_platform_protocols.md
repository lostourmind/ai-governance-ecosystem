
# Cross-Platform Protocols

This document outlines the handoff, validation, and rollback protocols across analysis and execution tools. All sessions must validate `governance_registry.yaml` before action and must respect documented authority boundaries.

## Subscription-aware routing and zero-assumption workflow

- Always revalidate governance registry on every handoff.
- Route governance design to Claude_Sonnet_4_Pro.
- Route repository file generation to ChatGPT_Plus.
- Route image tasks to Nero_AI_Image_Pro and video tasks to Nero_AI_Video_Pro.
- Avoid Copilot_Free for anything beyond basic browsing.
