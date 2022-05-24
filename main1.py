from PIL import Image

def run():

	#img = Image.open("lena_std.tif")
	width,heigth = (8,8)
	white_black = Image.new("1",(width,heigth))

	pixel = 1
	for y in range(width):
		if pixel == 0:
			pixel = 1
		else:
			pixel = 0

		for x in range(heigth):
			white_black.putpixel( (x,y), pixel)
			if pixel == 0:
				pixel = 1
			else:
				pixel = 0
	#with_zoom = white_black.resize((width * 10, heigth * 10),Image.Resampling.BICUBIC )
	white_black.show(title="e")

if __name__ == "__main__":
	run()
