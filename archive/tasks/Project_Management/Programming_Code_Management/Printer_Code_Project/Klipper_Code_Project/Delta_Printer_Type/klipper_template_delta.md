version: v1.0.0  
last_updated: 2025-08-30T19:35:00-04:00  
inherits: klipper_base_template.md  
printer_type: Delta  
objective: Restart-safe macro governance for Delta architecture  
source_declared: FLSUN_S1_Pro_Functions_Governance_Revised.rtf  

constraints:
  - Must enforce lifecycle tagging
  - Must preserve printer state across macro execution
  - Must mutation-log rollback logic
  - Must halt on assumption or syntax drift
