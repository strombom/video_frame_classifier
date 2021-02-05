
import glob
from PIL import Image 

filenames = glob.glob('images/*.jpg')

for filename in filenames:
	im = Image.open(filename)
	if im.size[0] > 550 and im.size[1] > 400:
		im = im.crop((600, 70, 1150, 470))
		im.save(filename)
