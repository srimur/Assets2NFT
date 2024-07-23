import os

def collect_assets(input_dir):
    asset_dict = {}
    for root, dirs, files in os.walk(input_dir):
        for name in dirs:
            asset_dict[name] = []
            dir_path = os.path.join(root, name)
            for file in os.listdir(dir_path):
                if file.endswith('.png'):
                    asset_dict[name].append(os.path.join(dir_path, file))
    return asset_dict
