import cv2
import crop_morphology
from subprocess import call
import os


vidcap = cv2.VideoCapture('15f.mp4')

success,image = vidcap.read()

count = 0;

fpsrate = vidcap.get(5)


print fpsrate


print fpsrate

while count<=300:

		success,image = vidcap.read()


		if count%fpsrate == 0:
			print 'Extracting frame #'+str(count)
			cv2.imwrite("frames/frame%d.jpg" % count,image)
			crop_morphology.process_image("frames/frame"+str(count)+".jpg","croppedframes/frame"+str(count)+"cropped.jpg")

		if cv2.waitKey(10) == 27:
			break

		count += 1



#Call to Tamil Classifier
os.system("python classify.py -c trainingimages/tamil/tamilcodebook.file -m trainingimages/tamil/trainingdatatamil.svm.model -i tamiltestdata.svm")
os.system("python deletesift.py")
#Call to English Classifier
os.system("python classify.py -c trainingimages/english/englishcodebook.file -m trainingimages/english/trainingdataenglish.svm.model -i englishtestdata.svm")
os.system("python deletesift.py")
#Call to Malayalam Classifier
os.system("python classify.py -c trainingimages/malayalam/malayalamcodebook.file -m trainingimages/tamil/trainingdatamalayalam.svm.model -i malayalamtestdata.svm")
os.system("python deletesift.py")
#Call to Hindi Classifier
os.system("python classify.py -c trainingimages/hindi/hindicodebook.file -m trainingimages/hindi/trainingdatahindi.svm.model -i hinditestdata.svm")
os.system("python deletesift.py")
os.system("python clean.py")
