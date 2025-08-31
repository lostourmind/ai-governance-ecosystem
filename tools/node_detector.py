#!/usr/bin/env python3
"""
Node Detector with deduplication, logging, and resilient config loading.
Drop-in replacement or reference implementation.
"""

from typing import List
from enhanced_logger import governance_logger
from repository_access_manager import RepositoryAccessManager

class NodeDetector:
    def __init__(self, framework_path=None):
        # Use repository access manager instead of direct file access
        self.access_manager = RepositoryAccessManager()
        self.detection_patterns = self._load_detection_patterns()
    
    def _get_basic_detection_patterns(self):
        # Minimal defaults if registry not available
        return {
            "node_prioritization": {"most_specific_wins": True},
            "patterns": {
                "project.coding.web_development.react.nextjs": ["nextjs", "react", "app router", "pages router"],
                "project.coding.SQL.DOMO": ["domo", "beast mode", "sql"],
            }
        }
    
    def _load_detection_patterns(self):
        """Load detection patterns with fallback strategies"""
        try:
            # Try to get from governance registry first
            registry = self.access_manager.get_governance_registry()
            if isinstance(registry, dict) and 'detection_patterns' in registry:
                governance_logger.log_repository_access("detection_patterns_from_registry", True)
                return registry['detection_patterns']
        except Exception as e:
            governance_logger.log_repository_access("detection_patterns_from_registry", False, e)
        
        # Fallback to basic patterns
        governance_logger.log_repository_access("detection_patterns_basic_defaults", True, fallback_used=True)
        return self._get_basic_detection_patterns()
    
    def _validate_nodes(self, nodes: List[str]) -> List[str]:
        # Basic validation: non-empty strings and known namespace shape
        valid = [n for n in nodes if isinstance(n, str) and n.count('.') >= 2]
        return valid
    
    def _deduplicate_detected_nodes(self, nodes: List[str]) -> List[str]:
        """Remove duplicate node detections and prioritize most specific"""
        if not nodes:
            return nodes
        
        # Remove exact duplicates while preserving order
        unique_nodes = list(dict.fromkeys(nodes))
        
        # Group by specificity (path depth)
        specificity_groups = {}
        for node in unique_nodes:
            depth = len(node.split('.'))
            specificity_groups.setdefault(depth, []).append(node)
        
        # Return most specific nodes, or all if same specificity
        most_specific = (self.detection_patterns.get('node_prioritization', {}) or {}).get('most_specific_wins', True)
        if most_specific:
            max_depth = max(specificity_groups.keys())
            return specificity_groups[max_depth]
        
        return unique_nodes

    def detect_nodes(self, user_input: str) -> List[str]:
        """Analyze user input and return applicable node paths"""
        detected_nodes = []
        
        # --- existing detection logic would go here ---
        # Simple heuristic matcher using patterns
        text = (user_input or "").lower()
        patterns = (self.detection_patterns or {}).get("patterns", {})
        for node, keywords in patterns.items():
            for kw in keywords:
                if kw.lower() in text:
                    detected_nodes.append(node)
                    break
        
        # Apply deduplication
        original_count = len(detected_nodes)
        detected_nodes = self._deduplicate_detected_nodes(detected_nodes)
        deduplication_applied = len(detected_nodes) != original_count
        
        # Log results
        governance_logger.log_node_detection(user_input, detected_nodes, deduplication_applied)
        
        return self._validate_nodes(detected_nodes)
