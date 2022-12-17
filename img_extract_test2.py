import os
from PIL import Image
from PIL.ExifTags import TAGS

img_name = "C:\\Users\\Famille\\Documents\\python\\labs python\\image_extrator\\talon reel 3.jpg"
my_img = Image.open(img_name)

exif_data = my_img.getexif()

for tagId in exif_data:
        tag= TAGS.get(tagId, tagId)
        data = exif_data.get(tagId)
        
        print(f"{tag:16}: {data}")