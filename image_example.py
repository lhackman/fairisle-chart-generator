
from PIL import Image, ImageColor, ImageDraw

num_cols = num_rows = 10


colour = [ImageColor.getcolor('Black', 'RGBA'),ImageColor.getcolor('White', 'RGBA')]
print(colour)

# you get a ratio of rows/stitches
stitch_ratio = 5/4
unit_size = 10

canvas = Image.new('RGB',(int(num_cols*unit_size*stitch_ratio), int(num_rows*unit_size)))

pen = ImageDraw.Draw(canvas)

for j in range(num_rows):
	for i in range(num_cols):
		x = i*unit_size*stitch_ratio
		y = j*unit_size
		pen.rectangle([x,y,x + unit_size*stitch_ratio, y+unit_size ],fill=colour[(i%2 + j%2)%2]) 
canvas.save("example", 'png')