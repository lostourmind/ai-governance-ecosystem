#!/usr/bin/env python3
"""
Repository Access Manager
Provides resilient access to governance registry and node knowledge across platforms
"""

import requests
import yaml
from pathlib import Path
import json
from datetime import datetime, timedelta

class RepositoryAccessManager:
    def __init__(self, base_url="https://raw.githubusercontent.com/lostourmind/ai-governance-ecosystem/main"):
        self.base_url = base_url.rstrip('/')
        self.cache_dir = Path(".governance_cache")
        self.cache_dir.mkdir(exist_ok=True)
        self.cache_timeout = timedelta(hours=1)  # Cache for 1 hour
    
    def get_governance_registry(self, use_cache=True):
        """Get governance registry with fallback strategies"""
        cache_file = self.cache_dir / "governance_registry.yaml"
        
        # Try cache first if enabled and recent
        if use_cache and self._is_cache_valid(cache_file):
            return self._load_from_cache(cache_file)
        
        # Try primary URL
        try:
            registry_url = f"{self.base_url}/governance_registry.yaml"
            response = requests.get(registry_url, timeout=10)
            response.raise_for_status()
            
            registry_data = yaml.safe_load(response.text) or {}
            
            # Cache successful fetch
            self._save_to_cache(cache_file, registry_data)
            return registry_data
            
        except Exception as e:
            # Fallback to cache if available
            if cache_file.exists():
                print(f"Primary fetch failed: {e}. Using cached registry.")
                return self._load_from_cache(cache_file)
            
            # Final fallback: basic governance structure
            return self._get_minimal_governance_fallback()
    
    def get_node_knowledge(self, node_path, use_cache=True):
        """Get node-specific knowledge with fallback strategies"""
        cache_file = self.cache_dir / f"{node_path.replace('.', '_')}.json"
        
        # Try cache first
        if use_cache and self._is_cache_valid(cache_file):
            return self._load_from_cache(cache_file)
        
        # Try fetching node files
        try:
            node_data = {}
            
            # Fetch knowledge base
            kb_url = f"{self.base_url}/nodes/{node_path}/knowledge_base.yaml"
            kb_response = requests.get(kb_url, timeout=10)
            if kb_response.status_code == 200:
                node_data['knowledge_base'] = yaml.safe_load(kb_response.text)
            
            # Fetch supplement prompt
            sp_url = f"{self.base_url}/nodes/{node_path}/supplement_prompt.md"
            sp_response = requests.get(sp_url, timeout=10)
            if sp_response.status_code == 200:
                node_data['supplement_prompt'] = sp_response.text
            
            # Fetch constraints
            const_url = f"{self.base_url}/nodes/{node_path}/constraints.yaml"
            const_response = requests.get(const_url, timeout=10)
            if const_response.status_code == 200:
                node_data['constraints'] = yaml.safe_load(const_response.text)
            
            # Cache if we got anything
            if node_data:
                self._save_to_cache(cache_file, node_data)
            
            return node_data if node_data else None
            
        except Exception as e:
            # Fallback to cache
            if cache_file.exists():
                print(f"Node fetch failed: {e}. Using cached data.")
                return self._load_from_cache(cache_file)
            
            return None
    
    def _is_cache_valid(self, cache_file):
        """Check if cache file is recent enough"""
        if not cache_file.exists():
            return False
        
        file_age = datetime.now() - datetime.fromtimestamp(cache_file.stat().st_mtime)
        return file_age < self.cache_timeout
    
    def _load_from_cache(self, cache_file):
        """Load data from cache file"""
        if cache_file.suffix == '.yaml':
            with open(cache_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        else:
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
    
    def _save_to_cache(self, cache_file, data):
        """Save data to cache file"""
        if cache_file.suffix == '.yaml':
            with open(cache_file, 'w', encoding='utf-8') as f:
                yaml.safe_dump(data, f, sort_keys=False)
        else:
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
    
    def _get_minimal_governance_fallback(self):
        """Minimal governance structure for offline operation"""
        return {
            "version": "v1.0.1-fallback",
            "enforcement_policy": "HALT_ON_ASSUMPTION",
            "lifecycle_tags": ["PHASE:INIT", "PHASE:VALIDATED", "PHASE:ROLLBACK", "PHASE:SETPOINT", "PHASE:QUARANTINE"],
            "fallback_mode": True,
            "note": "Minimal governance structure - limited functionality"
        }

if __name__ == "__main__":
    ram = RepositoryAccessManager()
    
    # Test governance registry access
    registry = ram.get_governance_registry()
    print(f"Registry version: {registry.get('version', 'unknown')}")
    
    # Test node access
    node_data = ram.get_node_knowledge("project.coding.SQL.DOMO")
    print(f"Node data available: {bool(node_data)}")
