# Assets2NFT

## Overview

Assets2NFT combines various image assets and generates corresponding metadata json, so you can create cool NFTs with ease.


## Project Structure
```
nft_generator/
├── asset_collector.py
├── image_composer.py
├── metadata_creator.py
├── main.py
├── config.json
├── assets/
│ ├── Add your Asset Folders here (e.g. Face)/
│ └── Add your Asset Folders here(e.g. Eyes)/
├── output_images/
├── output_metadata/
└── README.md
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/srimur/Assets2NFT.git
   cd Assets2NFT
   ```
2. **Install Dependencies:**

Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. **Configure the Project:**

Edit `config.json` to set your directories and image size. Here’s the default setup:
```json
{
    "input_dir": "assets",
    "output_images_dir": "output_images",
    "output_metadata_dir": "output_metadata",
    "image_size": {
        "width": 512,
        "height": 512
    }
}

```

## Adding Your Assets

**Organize Your Images:** 
Place your asset images into the `assets/` folder. Create subdirectories for e.g. `eyes/`, `face/`, `head/` based on your NFT requirements and place your variants in them.
```
assets/
├── eyes/
├── face/
└── head/
```
## Usage

1. **Run the Script:**
Start the image and metadata generation process with:

```bash
python main.py
```

2. **Check Your Results:**

*Images:* Look in output_images/ for your NFT creations.
*Metadata:* Metadata files will be saved in output_metadata/.

   