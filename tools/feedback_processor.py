#!/usr/bin/env python3
"""
Feedback processor stub.
Appends feedback notes to node mutation logs for later curation.
"""
import sys, yaml
from pathlib import Path
from datetime import datetime

def append_feedback(node_path: str, note: str):
    kb_path = Path(f"nodes/{node_path}/knowledge_base.yaml")
    if not kb_path.exists():
        raise FileNotFoundError(f"Missing knowledge_base.yaml for {node_path}")
    data = yaml.safe_load(kb_path.read_text(encoding='utf-8'))
    ml = data.get('mutation_log', [])
    ml.append(f"[PHASE:FEEDBACK] {datetime.now().isoformat()} {note}")
    data['mutation_log'] = ml
    kb_path.write_text(yaml.dump(data, sort_keys=False), encoding='utf-8')
    print(f"Feedback appended to {kb_path}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python tools/feedback_processor.py project.coding.klipper.corexy 'note text'")
        sys.exit(1)
    append_feedback(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
