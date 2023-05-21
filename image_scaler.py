from PIL import Image
from os import walk

folder = 'images/player/'

for folder1, _, image_total in walk(folder):
    for image_name in image_total:
        image_path = folder1 + '/' + image_name
        print(image_path)
        base_image = Image.open(image_path)

        width, height = base_image.size
        img = Image.new('RGBA', (width*4, height*4), (0, 0, 0, 0))

        for x in range(width):
            for y in range(height):
                pixel_color = base_image.getpixel((x, y))
                img.putpixel((x*4, y*4), pixel_color)
                img.putpixel((x*4+1, y*4), pixel_color)
                img.putpixel((x*4+2, y*4), pixel_color)
                img.putpixel((x*4+3, y*4), pixel_color)
                img.putpixel((x*4, y*4+1), pixel_color)
                img.putpixel((x*4+1, y*4+1), pixel_color)
                img.putpixel((x*4+2, y*4+1), pixel_color)
                img.putpixel((x*4+3, y*4+1), pixel_color)
                img.putpixel((x*4, y*4+2), pixel_color)
                img.putpixel((x*4+1, y*4+2), pixel_color)
                img.putpixel((x*4+2, y*4+2), pixel_color)
                img.putpixel((x*4+3, y*4+2), pixel_color)
                img.putpixel((x*4, y*4+3), pixel_color)
                img.putpixel((x*4+1, y*4+3), pixel_color)
                img.putpixel((x*4+2, y*4+3), pixel_color)
                img.putpixel((x*4+3, y*4+3), pixel_color)

        img.save(f'{folder1}/{image_name}.png')