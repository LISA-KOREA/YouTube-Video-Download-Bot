import os
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def fix_thumb(thumb_path: str):
    width = 0
    height = 0
    try:
        if thumb_path and os.path.exists(thumb_path):
            parser = createParser(thumb_path)
            metadata = extractMetadata(parser)
            if metadata and metadata.has("width") and metadata.has("height"):
                width = metadata.get("width")
                height = metadata.get("height")

            if width == 0 or height == 0:
                with Image.open(thumb_path) as img:
                    width, height = img.size

            with Image.open(thumb_path) as img:
                img = img.convert("RGB")
                aspect_ratio = height / width
                new_height = int(320 * aspect_ratio)
                resized_img = img.resize((320, new_height))
                resized_img.save(thumb_path, "JPEG")
    except Exception as e:
        print(f"[fix_thumb] Error: {e}")
        thumb_path = None

    return width, height, thumb_path
