from PIL import Image, ImageColor, ImageDraw
import sys

helptext = """
I require 4 commandline arguements:

1) Filename for an black & white ascii chart --- first line of file must be in the formate:
number of stitches, number of rows, dark symbol, light symbol

2) File name for the colour palette for your design --- each line gives a colour as an R,G,B,A value, separated by commas

3) File name for the row colouring ---  each line gives the index of the colour in the palette for the dark stitches and the light stitches separated by a comma

4) output filename

example:

python3 fairisle.py example/eg_bw.txt example/eg_palette.txt example/eg_colouring.txt example.png
(see example folder for files)
"""

# you get a ratio of rows/stitches
stitch_ratio = 5/4
unit_size = 10

if len(sys.argv) < 5:
	print(helptext)
	sys.exit(1)
with open(sys.argv[1], 'r') as bwFile:
	header = bwFile.readline().split(',')
	num_cols = int(header[0])
	num_rows = int(header[1])
	dark_symbol = header[2].strip()
	light_symbol = header[3].strip()
	bwMap = []
	for line in bwFile.readlines():
		row = []
		for c in line.strip():
			if not c in (dark_symbol, light_symbol):
				print("Invalid symbol in BWFILE" + c)
			else:
				row.append(0 if c == dark_symbol else 1)
		bwMap.append(row)
		
	
with open(sys.argv[2], 'r') as palette:
	colours = []
	for line in palette.readlines():
		colour = tuple(int(c) for c in line.split(','))
		
		colours.append(colour)
		
with open(sys.argv[3], 'r') as rowColours:
	colouring = []
	for line in rowColours.readlines():
		colouring.append([int(c) for c in line.split(',')])



canvas = Image.new('RGB',(int(num_cols*unit_size*stitch_ratio), int(num_rows*unit_size)))

pen = ImageDraw.Draw(canvas)

for j in range(num_rows):
	for i in range(num_cols):
		x = i*unit_size*stitch_ratio
		y = j*unit_size

		colour = colours[colouring[j][bwMap[j][i]]]
		pen.rectangle([x,y,x + unit_size*stitch_ratio, y+unit_size ],fill=colour) 
canvas.save(sys.argv[4], 'png')
				
				
		
	