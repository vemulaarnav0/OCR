import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def text2png(text, fullpath, color = "#000", bgcolor = "#FFF", fontfullpath = None, fontsize = 13, leftpadding = 3, rightpadding = 3, width = 200):
 REPLACEMENT_CHARACTER = u'\uFFFD'
	NEWLINE_REPLACEMENT_STRING = ' ' + REPLACEMENT_CHARACTER + ' '
 
 
 #prepare for linkback
	linkback = "created via http://ourdomain.com"
	fontlinkback = ImageFont.truetype('font.ttf', 8)
	linkbackx = fontlinkback.getsize(linkback)[0]
	linkback_height = fontlinkback.getsize(linkback)[1]
	#end of the one and only linkback
 
 font = ImageFont.load_default() if fontfullpath == None else ImageFont.truetype(fontfullpath, fontsize)
	text = text.replace('\n', NEWLINE_REPLACEMENT_STRING)
 
 line = []
 line = u""
 
 for word in text.split():
  print word
  if word == REPLACEMENT_CHARACTER:
   lines.append(line[1: ])
   lines = u""
   lines.append(u"")
  elif font.getsize(line + '' + word)[0] <= (width - rightpadding - leftpadding):
   line += ' ' + word
  else: #start a new line
			lines.append( line[1:] ) #slice the white space in the begining of the line
			line = u""

			#TODO: handle too long words at this point
			line += ' ' + word #for now, assume no word alone can exceed the line width

 if len(line) != 0:
		lines.append( line[1:] ) #add the last line

	line_height = font.getsize(text)[1]
	img_height = line_height * (len(lines) + 1)

	img = Image.new("RGBA", (width, img_height), bgcolor)
	draw = ImageDraw.Draw(img)

	y = 0
	for line in lines:
		draw.text( (leftpadding, y), line, color, font=font)
		y += line_height

	# add linkback at the bottom
	draw.text( (width - linkbackx, img_height - linkback_height), linkback, color, font=fontlinkback)

	img.save(fullpath)

#show time
text2png(u"YOU GOT SCAMMED", 'test.png', fontfullpath = "font.ttf")   
   
  
