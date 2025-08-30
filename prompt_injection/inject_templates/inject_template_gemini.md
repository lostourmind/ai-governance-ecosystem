version: v1.0.0  
last_updated: 2025-08-30T15:34:00-04:00  
platform: Gemini  
objective: [INSERT OBJECTIVE]  
source_declared: [INSERT SOURCE URL OR FILE PATH]  

constraints:
  - Must halt execution if source is inaccessible or unreadable
  - Must not fabricate validation or fallback logic
  - Must request clarification if scope or constraints are unclear
  - Must include lifecycle tags: [PHASE:INIT], [PHASE:VALIDATED], [PHASE:ROLLBACK]
  - Must mutation-log any deviation from declared source
  - Must preserve state or context relevant to the task
  - Must include rollback logic and audit-grade logging

execution_policy: HALT_ON_ASSUMPTION  
phase: INIT
