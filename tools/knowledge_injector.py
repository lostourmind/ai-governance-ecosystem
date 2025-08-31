#!/usr/bin/env python3
"""
Knowledge Injector with token budget tracking.
Reference implementation for integration.
"""

from typing import Dict, Any
from enhanced_logger import governance_logger

class KnowledgeInjector:
    def __init__(self):
        pass

    # --- Token budget utilities ---
    def _calculate_token_estimate(self, text: str) -> int:
        """Rough token estimation for budget tracking. 1 token ≈ 4 characters."""
        if not text:
            return 0
        return max(1, len(text) // 4)

    def _get_optimization_suggestions(self, token_count: int):
        """Provide optimization suggestions based on token usage"""
        suggestions = []
        if token_count > 1000:
            suggestions.append("Consider splitting into multiple focused handoffs")
            suggestions.append("Review node-specific content for redundancy")
        elif token_count > 500:
            suggestions.append("Monitor for scope creep in future handoffs")
            suggestions.append("Consider more specific node targeting")
        else:
            suggestions.append("Token usage within efficient range")
        return suggestions

    def _create_token_budget(self, handoff_context: Dict[str, Any]) -> Dict[str, Any]:
        """Create token budget tracking for handoff package"""
        enhanced_wrapper_tokens = self._calculate_token_estimate(handoff_context.get('enhanced_wrapper', ''))
        user_request_tokens = self._calculate_token_estimate(handoff_context.get('user_request', ''))
        metadata_tokens = self._calculate_token_estimate(str(handoff_context.get('handoff_metadata', {})))
        
        total_estimated = enhanced_wrapper_tokens + user_request_tokens + metadata_tokens
        
        budget = {
            "estimated_tokens": total_estimated,
            "component_breakdown": {
                "enhanced_wrapper": enhanced_wrapper_tokens,
                "user_request": user_request_tokens,
                "metadata": metadata_tokens
            },
            "budget_warnings": {
                "high_usage": total_estimated > 500,
                "very_high_usage": total_estimated > 1000
            },
            "optimization_suggestions": self._get_optimization_suggestions(total_estimated)
        }
        return budget

    # --- Handoff assembly integrating token budget ---
    def _assemble_handoff_context(self, enhanced_wrapper: str, user_request: str, target_platform: str, nodes):
        """Create complete handoff context package with token budget"""
        handoff_context: Dict[str, Any] = {
            "enhanced_wrapper": enhanced_wrapper or "",
            "user_request": user_request or "",
            "handoff_metadata": {
                "target_platform": target_platform,
                "nodes_applied": nodes or []
            }
        }
        # Add token budget
        token_budget = self._create_token_budget(handoff_context)
        handoff_context["token_budget"] = token_budget
        
        # Log assembly
        governance_logger.log_handoff_assembly(nodes or [], token_budget, target_platform)
        return handoff_context
