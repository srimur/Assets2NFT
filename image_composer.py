from PIL import Image

def compose_images(image_paths, size=(512, 512)):
    base_image = Image.new('RGBA', size, (255, 255, 255, 0))
    
    for path in image_paths:
        img = Image.open(path).convert("RGBA")
        img = img.resize(size, Image.Resampling.LANCZOS)
        base_image.paste(img, (0, 0), img)
    
    return base_image
