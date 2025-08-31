#!/usr/bin/env python3
"""
Enhanced Logging for AI Governance Ecosystem
Provides comprehensive logging for debugging and audit trails
"""

import logging
import json
from datetime import datetime
from pathlib import Path

class GovernanceLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
        # Setup main logger
        self.logger = logging.getLogger('governance')
        self.logger.setLevel(logging.INFO)
        
        # Avoid duplicate handlers if re-imported
        if not self.logger.handlers:
            self._setup_handlers()
    
    def _setup_handlers(self):
        """Setup logging handlers for file and console output"""
        
        # File handler for all logs
        log_file = self.log_dir / f"governance_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # Console handler for warnings and errors
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def log_node_detection(self, user_input, detected_nodes, deduplication_applied=False):
        """Log node detection results"""
        preview = user_input[:100] + "..." if isinstance(user_input, str) and len(user_input) > 100 else user_input
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": "node_detection",
            "user_input_preview": preview,
            "detected_nodes": detected_nodes,
            "deduplication_applied": deduplication_applied,
            "node_count": len(detected_nodes) if detected_nodes else 0
        }
        
        self.logger.info(f"Node Detection: {json.dumps(log_entry, indent=2)}")
    
    def log_repository_access(self, resource, success, error=None, fallback_used=False):
        """Log repository access attempts"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": "repository_access",
            "resource": resource,
            "success": bool(success),
            "fallback_used": bool(fallback_used),
            "error": str(error) if error else None
        }
        
        level = logging.INFO if success else logging.WARNING
        self.logger.log(level, f"Repository Access: {json.dumps(log_entry, indent=2)}")
    
    def log_handoff_assembly(self, nodes, token_budget, target_platform):
        """Log handoff package assembly"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": "handoff_assembly",
            "nodes_applied": nodes or [],
            "estimated_tokens": (token_budget or {}).get("estimated_tokens", 0),
            "target_platform": target_platform,
            "high_usage_warning": (token_budget or {}).get("budget_warnings", {}).get("high_usage", False)
        }
        
        level = logging.WARNING if log_entry["high_usage_warning"] else logging.INFO
        self.logger.log(level, f"Handoff Assembly: {json.dumps(log_entry, indent=2)}")
    
    def log_governance_validation(self, platform, success, registry_version=None, error=None):
        """Log governance validation results"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": "governance_validation", 
            "platform": platform,
            "success": bool(success),
            "registry_version": registry_version,
            "error": str(error) if error else None
        }
        
        level = logging.INFO if success else logging.ERROR
        self.logger.log(level, f"Governance Validation: {json.dumps(log_entry, indent=2)}")

# Global logger instance
governance_logger = GovernanceLogger()
