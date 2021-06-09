from PIL import Image
from icrawler.builtin import GoogleImageCrawler
import os
from colouring import Colour


def download_img(query):
    google_crawler = GoogleImageCrawler(storage={'root_dir': './'})
    google_crawler.crawl(keyword=query, max_num=1)


def get_pixels(image):
    art = []
    rgb_of_image = image.convert("RGB")
    pixels = list(rgb_of_image.getdata())
    width = image.size[0]
    pixels = [pixels[x: x + width] for x in range(0, len(pixels), width)]
    for y, row in enumerate(pixels):
        art.append([])
        for x, column in enumerate(row):
            art[y].append(Colour.exact_rgb("■ ", rgb_of_image.getpixel((x, y)))) if mode == "2" else art[y].append(
                get_coloured_square(rgb_of_image.getpixel((x, y))))
    return art


def get_coloured_square(rgb):
    colour_differences = []
    colours = {
        (255, 255, 255): Colour.white("■ "),
        (255, 0, 0): Colour.red("■ "),
        (0, 0, 255): Colour.blue("■ "),
        (0, 255, 0): Colour.green("■ "),
        (0, 0, 0): Colour.black("■ "),
        (0, 255, 255): Colour.cyan("■ "),
        (255, 255, 0): Colour.yellow("■ "),
        (255, 0, 255): Colour.magenta("■ ")}
    r, g, b = rgb
    for colour in list(colours.keys()):
        cr, cg, cb = colour
        colour_difference = (abs(r - cr) ** 2 + abs(g - cg) ** 2 + abs(b - cb) ** 2) ** 0.5
        colour_differences.append((colour_difference, colour))
    return colours[min(colour_differences)[1]]


query = input("Enter a title for your generated art.\n\nInput:\t")
mode = input("What mode of art generation do you want?\n\n1) Abstract\n2) Realistic\n\nInput:\t")
if mode not in "1 2".split(" "):
    print("\nInvalid mode!")
    exit()

download_img(query)

if os.path.exists("000001.png"):
    to_open = "000001.png"
else:
    to_open = "000001.jpg"

with Image.open(to_open) as image:
    image.thumbnail((128, 128), Image.ANTIALIAS)
    pixels = get_pixels(image)
os.remove(to_open)

result = ''''''
for row in pixels:
    result += ("".join(row) + "\n")
print(result)
