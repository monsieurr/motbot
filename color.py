from PIL import Image, ImageDraw, ImageFont
import random


def generate_random_color():
    color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    return color


def generate_simple_art(filename, random_color, quote):
    img = Image.new('RGB', (800, 400), random_color)
    W, H = (800, 400)
    title_font = ImageFont.truetype('fonts/Roboto-Bold.ttf', 15)

    #im = Image.new("RGBA", (W, H), "yellow")
    #draw = ImageDraw.Draw(im)
    print(type(quote))
    img_editable = ImageDraw.Draw(img)
    w, h = img_editable.textsize(quote)


    w, h = img_editable.textsize(quote, font=title_font)
    img_editable.text(((W-w)/2, (H-h)/2), quote, font=title_font, fill="black")
    
    #img_editable.text((10, 10), quote, font=title_font, fill=(255,255,255,128))

    img.save(filename)


if __name__ == "__main__":
    random_color = generate_random_color()

    size = [1000, 1000]
    quote = "Tel est pris qui croyait prendre !"

    generate_simple_art("test.png", random_color, quote)

    random_color = '#%02X%02X%02X' % random_color
    print(random_color)
