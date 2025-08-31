#!/usr/bin/env python3
"""
Node Detection and Scope Analysis Tool
Analyzes user input to identify applicable knowledge nodes
"""

import yaml
import re
from pathlib import Path

class NodeDetector:
    def __init__(self, framework_path="nodes/_framework"):
        self.framework_path = Path(framework_path)
        self.detection_patterns = self._load_detection_patterns()

    def _load_detection_patterns(self):
        patterns_file = self.framework_path / "detection_patterns.yaml"
        with open(patterns_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def detect_nodes(self, user_input):
        detected_nodes = []
        rules = self.detection_patterns.get('detection_rules', {})
        keywords = rules.get('keywords', {})
        # Keyword-based detection
        for _, config in keywords.items():
            for pattern in config.get('patterns', []):
                if re.search(pattern, user_input, re.IGNORECASE):
                    detected_nodes.extend(config.get('nodes', []))

        # TODO: Context-based extraction using named groups if needed

        # Prioritize most specific nodes
        node_prior = rules.get('node_prioritization', {})
        if node_prior.get('most_specific_wins', True):
            detected_nodes = self._prioritize_specific_nodes(detected_nodes)

        return self._validate_nodes(detected_nodes)

    def _prioritize_specific_nodes(self, nodes):
        if not nodes:
            return nodes
        max_depth = max(len(n.split('.')) for n in nodes)
        return [n for n in nodes if len(n.split('.')) == max_depth]

    def _validate_nodes(self, nodes):
        validated = []
        for node in nodes:
            node_path = Path(f"nodes/{node}")
            if (node_path.exists() and
                (node_path / "knowledge_base.yaml").exists() and
                (node_path / "supplement_prompt.md").exists() and
                (node_path / "constraints.yaml").exists()):
                validated.append(node)
        return validated

if __name__ == "__main__":
    detector = NodeDetector()
    samples = [
        "I need help with my Klipper CoreXY printer configuration",
        "Setting up SQL queries for DOMO analytics platform",
        "Building a React NextJS web application"
    ]
    for q in samples:
        try:
            nodes = detector.detect_nodes(q)
            print(f"Query: {q}\nDetected nodes: {nodes}\n")
        except FileNotFoundError:
            print("Framework files missing. Ensure nodes/_framework/detection_patterns.yaml exists.")
