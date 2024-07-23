import os
import json

def create_metadata(combo, output_metadata_dir, idx):
    metadata = {key: os.path.basename(value) for key, value in combo.items()}
    metadata_path = os.path.join(output_metadata_dir, f"metadata_{idx+1}.json")
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=4)
