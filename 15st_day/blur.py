from PIL import Image,ImageFilter
import os
im = Image.open('image.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')
if os.path.exists('blur.jpg'):
	print('success!')