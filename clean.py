
#to delete .sift extension files

from os import walk

import os
import sys

import shutil


#shutil.copyfile("reviewtest/tam.jpg","tamilwords/tam.jpg")
shutil.copyfile("reviewtest/72.gif","tamilwords/72.gif")
shutil.copyfile("reviewtest/7.jpg","hindiwords/7.jpg")
shutil.copyfile("reviewtest/8.jpg","hindiwords/8.jpg")
shutil.copyfile("reviewtest/malayalam16.jpg","malayalamwords/malayalam16.jpg")
shutil.copyfile("reviewtest/imgproject3.jpg","englishwords/imgproject3.jpg")
shutil.copyfile("reviewtest/imgproject4.jpg","englishwords/imgproject4.jpg")
#shutil.copyfile("reviewtest/frame0cropped.jpg","croppedimages/frame0cropped.jpg")

for i in os.listdir("croppedframes/"):
	os.remove("croppedframes/"+i)

shutil.copyfile("reviewtest/1.jpg","croppedframes/1.jpg")
shutil.copyfile("reviewtest/2.jpg","croppedframes/2.jpg")

