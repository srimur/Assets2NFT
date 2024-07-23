import os
import json
from asset_collector import collect_assets
from image_composer import compose_images
from metadata_creator import create_metadata

def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

def generate_nft_assets(config):
    input_dir = config['input_dir']
    output_images_dir = config['output_images_dir']
    output_metadata_dir = config['output_metadata_dir']
    image_size = (config['image_size']['width'], config['image_size']['height'])
    
    asset_dict = collect_assets(input_dir)

    combinations = [{}]
    for key, paths in asset_dict.items():
        new_combinations = []
        for combo in combinations:
            for path in paths:
                new_combo = combo.copy()
                new_combo[key] = path
                new_combinations.append(new_combo)
        combinations = new_combinations

    for idx, combo in enumerate(combinations):
        image_paths = list(combo.values())
        composite_image = compose_images(image_paths, size=image_size)
        
        image_path = os.path.join(output_images_dir, f"nft_image_{idx+1}.png")
        composite_image.save(image_path)

        create_metadata(combo, output_metadata_dir, idx)

if __name__ == "__main__":
    config_path = "config.json"
    
    config = load_config(config_path)
    
    # Create output directories if they don't exist
    os.makedirs(config['output_images_dir'], exist_ok=True)
    os.makedirs(config['output_metadata_dir'], exist_ok=True)
    
    generate_nft_assets(config)
