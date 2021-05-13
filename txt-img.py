from PIL import Image, ImageDraw, ImageFont

from cs50 import get_string
 
#image color, asking the text, and font
img = Image.new('RGB', (100, 30), color = (73, 109, 137))

text = get_string("text:")
 
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10,10), text , font=fnt, fill=(255, 255, 0))
 
img.save('pil_text_font.png')
