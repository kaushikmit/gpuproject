import os
import sys

input_images = []

i = 0
'''
for (dirpath, dirnames, filenames) in walk('trainingimages/class2/'):
    input_images.extend(filenames)
    if filenames.split(".")[1] == ".jpg":
    	os.rename('trainingimages/class2/'+filenames,'trainingimages/class2/image'+i+'.jpg')
'''

path="malayalam/"
filenames = os.listdir(path)
print filenames

for filename in filenames:
	i = i + 1
	print filename
	os.rename("malayalam/"+filename,"malayalam/malayalam"+str(i)+'.jpg')



