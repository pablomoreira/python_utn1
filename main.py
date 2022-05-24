from PIL import Image

def run():
	img = Image.open("lena_std.tif")
	rimg = Image.new("RGB",img.size)
	gimg = Image.new("RGB",img.size)
	bimg = Image.new("RGB",img.size)
	cimg = Image.new("RGB",img.size)

	lrimg = Image.new("L",img.size)
	lgimg = Image.new("L",img.size)
	lbimg = Image.new("L",img.size)



	width,height = img.size
	for x in range(width):
		for y in range(height):
			r,g,b = img.getpixel( (x,y) )
			rimg.putpixel( (x,y), (r,0,0) )
			gimg.putpixel( (x,y), (0,g,0) )
			bimg.putpixel( (x,y), (0,0,b) )

			lrimg.putpixel( (x,y), (r) )
			lgimg.putpixel( (x,y), (g) )
			lbimg.putpixel( (x,y), (b) )

	rimg.show(title = "Luz roja")
	gimg.show(title = "Luz verde")
	bimg.show(title = "Luz azul")
	# lrimg.save("lr.jpg")
	# lgimg.save("lg.jpg")
	# lbimg.save("lb.jpg")


	r = 0
	g = 0
	b = 0

	for x in range(width):
		for y in range(height):

			r,_,_ = rimg.getpixel( (x,y) )
			_,g,_ = gimg.getpixel( (x,y) )
			_,_,b = bimg.getpixel( (x,y) )
			cimg.putpixel( (x,y), (r,g,b,) )

	cimg.show()


if __name__ == "__main__":
	run()
