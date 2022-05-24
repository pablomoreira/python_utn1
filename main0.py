from PIL import Image

def run():
	img = Image.open("lena_std.tif")
	width,height = img.size
	white_black = Image.new("L",(width,height))

	for y in range(width):
		for x in range(height):
			r,g,b = img.getpixel( (x,y))
			white_black.putpixel( (x,y), int((r+g+b)/2))



	white_black.show(title="e")


if __name__ == "__main__":
	run()
