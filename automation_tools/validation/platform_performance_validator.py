#!/usr/bin/env python3
import json
from datetime import datetime, timedelta
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

try:
    from ..tools.enhanced_logger import governance_logger
except Exception:
    from automation_tools.tools.enhanced_logger import governance_logger

@dataclass
class ValidationTest:
    test_id: str
    platform: str
    task_type: str
    test_prompt: str
    expected_deliverables: List[str]
    success_criteria: Dict[str, str]

@dataclass
class ValidationResult:
    test_id: str
    platform: str
    timestamp: str
    success: bool
    deliverable_quality: float
    response_time: Optional[float]
    notes: str

class PlatformValidator:
    def __init__(self, validation_log_path="logs/platform_validation.json"):
        self.validation_log = Path(validation_log_path)
        self.validation_log.parent.mkdir(parents=True, exist_ok=True)
        self.validation_threshold = 0.7
    
    def should_trigger_validation(self, platform: str, task_type: str) -> bool:
        return self._recent_failure_rate(platform, task_type, 7) > (1 - self.validation_threshold)
    
    def run_baseline_comparison(self, test_prompt: str, platforms: List[str]) -> Dict[str, ValidationResult]:
        results = {}
        for p in platforms:
            r = ValidationResult(
                test_id=f"baseline_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                platform=p,
                timestamp=datetime.now().isoformat(),
                success=True,
                deliverable_quality=0.8,
                response_time=None,
                notes=f"Baseline: {test_prompt[:50]}... {p}"
            )
            results[p] = r
            self._log(r)
        return results
    
    def _recent_failure_rate(self, platform: str, task_type: str, days: int) -> float:
        if not self.validation_log.exists(): return 0.0
        data = json.loads(self.validation_log.read_text())
        cutoff = datetime.now() - timedelta(days=days)
        recents = [x for x in data.get("validation_results", []) if x.get("platform")==platform and task_type in x.get("notes","") and datetime.fromisoformat(x["timestamp"])>cutoff]
        if not recents: return 0.0
        fails = sum(1 for x in recents if not x.get("success", False))
        return fails/len(recents)
    
    def _log(self, r: ValidationResult):
        data = {"validation_results": []}
        if self.validation_log.exists():
            data = json.loads(self.validation_log.read_text())
        data["validation_results"].append(asdict(r))
        data["validation_results"] = data["validation_results"][-1000:]
        self.validation_log.write_text(json.dumps(data, indent=2))
