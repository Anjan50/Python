import cv2		#Image processing library 
import os,glob	#For os manipulation 
 
im_4k = 0		#Initializing counts for each category 
im_1080 = 0 
im_720 = 0 
 
os.system("mkdir 4K")	#Creating directories for each type 
os.system("mkdir 1080p") 
os.system("mkdir 720p") 
 
for image in glob.glob('*.jpg'):	#Selecting images one by one 
	print(image) 
	img = cv2.imread(image)		#Reading image 
	height, width, channel = img.shape	#getting image resolution 
	if(width>=3840 and height>=2160):	#Comparing image resolutions and moving them accordingly 
		os.system("move "+image+" 4K") 
		im_4k = im_4k+1 
		continue 
	if(width>=1920 and height>=1080): 
		os.system("move "+image+" 1080p") 
		im_1080 = im_1080+1 
		continue 
	if(width>=1280 and height>=720): 
		os.system("move "+image+" 720p") 
		im_720 = im_720+1 
		continue 
print(im_4k," 4K images moved to 4K folder")	#Printing counts for each type 
print(im_1080," 1080p images moved to 1080p folder")	 
print(im_720," 720p images moved to 720p folder")
