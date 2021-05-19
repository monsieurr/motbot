from PIL import Image, ImageDraw, ImageFont
import random
import colorsys


def generate_random_color():
    color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    return color

def read_random_color(random_color):
    print("Random color is : ", random_color)
    print("Random color is : ", random_color[2])
    print(colorsys.rgb_to_hls(
        random_color[0]/255, random_color[1]/255, random_color[2]/255))


def get_color_brightness(random_color):
    random_color_hls = colorsys.rgb_to_hls(random_color[0]/255, random_color[1]/255, random_color[2]/255)
    print ("RANDOM COLOR HLS : ", random_color_hls)
    print(f"Hue : {random_color_hls[0]}\n Light : {random_color_hls[1]}\n Saturation : {random_color_hls[2]}\n")
    return random_color_hls[1]

def generate_simple_art(filename, random_color, quote, dark=True):
    img = Image.new('RGB', (1920, 1080), random_color)
    W, H = (1920, 1080)

    ## TODO maybe could adapt the font size given the length of the quote
    title_font = ImageFont.truetype('fonts/Roboto-Bold.ttf', 48)

    #im = Image.new("RGBA", (W, H), "yellow")
    #draw = ImageDraw.Draw(im)
    print(type(quote))
    img_editable = ImageDraw.Draw(img)
    w, h = img_editable.textsize(quote)


    w, h = img_editable.textsize(quote, font=title_font)
    if(dark): 
        img_editable.text(((W-w)/2, (H-h)/2), quote, font=title_font, fill="white")
    else:
        img_editable.text(((W-w)/2, (H-h)/2), quote, font=title_font, fill="black")

    
    #img_editable.text((10, 10), quote, font=title_font, fill=(255,255,255,128))

    img.save(filename)


if __name__ == "__main__":
    random_color = generate_random_color()
    print("random_color : ", random_color)

    size = [1000, 1000]
    quote = "il ne faut pas se moquer de la peine du voisin, car la vôtre arrive le lendemain matin"

    color_brightness = get_color_brightness(random_color)
    
    if color_brightness > 0.5:
        dark = False
        print("Color is bright today !")
    else:
        dark = True
        print("Color is dark today !")

    read_random_color(random_color)

    generate_simple_art("test.png", random_color, quote, dark)

    random_color = '#%02X%02X%02X' % random_color
    print(random_color)
