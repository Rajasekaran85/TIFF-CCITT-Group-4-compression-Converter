import sys
import os
from PIL import Image
import glob
import wand.image

# pillow library used
# OpenCV library used
# wand (imagicMagick) library used

# *** TIFF Image CCITT Group 4 compression Converter ***
# Group4 compression apply only for Black & White mode images
# So tool should check the images, it is present in Black & White mode and then convert to Group4 compression

print("\n TIF Image: Group4 Compression converter \n")

filepath = input("Enter the Input Image file path: ")
output_directory = "Group4"
output = filepath + "/" + output_directory + "/"

if os.path.exists(output):
    pass
else:
    os.mkdir(output)

for fname in glob.glob(filepath + "/" + "*.tif"):
	input_image = fname
	name1 = os.path.basename(fname)
	print(name1)
	image1 = Image.open(input_image)
	mode_img = str(image1.mode)
	text_file = filepath + "/" + "output.log"
	value1 = str(1)
	comp_img = str(image1.info['compression'])
	if mode_img != value1:
		f = open(text_file, "a+")
		f.write(name1 + ": Image not in Black & White Mode\n")
		f.close()
	elif comp_img == "group4":
		f = open(text_file, "a+")
		f.write(name1 + ": Image already in Group4 Compression\n")
		f.close()
	else:
		with wand.image.Image(filename = input_image) as img:
			img.compression = "group4"
			img.save(filename=output + name1)
