#!/usr/bin/env python3
import yaml
import os
from datetime import datetime

def update_breadcrumbs():
    """Auto-update breadcrumbs.yaml with current node list"""
    nodes = []
    for node_dir in os.listdir('nodes'):
        if os.path.isdir(f'nodes/{node_dir}') and not node_dir.startswith('_'):
            node_yaml_path = f'nodes/{node_dir}/node.yaml'
            if os.path.exists(node_yaml_path):
                with open(node_yaml_path, 'r') as f:
                    node_data = yaml.safe_load(f)
                    nodes.append({
                        'id': node_data.get('node_id'),
                        'path': f'nodes/{node_dir}/',
                        'status': 'operational'
                    })
    
    # Update breadcrumbs.yaml
    with open('nodes/_framework/breadcrumbs.yaml', 'r') as f:
        breadcrumbs = yaml.safe_load(f)
    
    breadcrumbs['active_nodes'] = nodes
    breadcrumbs['last_updated'] = datetime.utcnow().isoformat() + 'Z'
    
    with open('nodes/_framework/breadcrumbs.yaml', 'w') as f:
        yaml.dump(breadcrumbs, f, default_flow_style=False)

def update_detection_patterns():
    """Auto-generate detection patterns from node directories"""
    patterns = {}
    for node_dir in os.listdir('nodes'):
        if os.path.isdir(f'nodes/{node_dir}') and not node_dir.startswith('_'):
            # Extract keywords from node_id
            node_parts = node_dir.replace('.', ' ').split()
            patterns[node_dir] = node_parts
    
    # Update detection_patterns.yaml
    # Implementation here...