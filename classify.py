from __future__ import division
import time
import libsvm
import argparse
from cPickle import load
from learn import extractSift, computeHistograms, writeHistogramsToFile
from os import walk
import shutil
import os

#English
HISTOGRAMS_FILE = 'testdata.svm'
CODEBOOK_FILE = 'codebook.file'
MODEL_FILE = 'trainingdata.svm.model'

'''
#Tamil
tamil_HISTOGRAMS_FILE = 'tamiltestdata.svm'
tamil_CODEBOOK_FILE = 'tamilcodebook.file'
tamil_MODEL_FILE = 'trainingdatatamil.svm.model'

#Malayalam
malayalam_HISTOGRAMS_FILE = 'testdata.svm'
malayalam_CODEBOOK_FILE = 'codebook.file'
malayalam_MODEL_FILE = 'trainingdata.svm.model'

#Hindi
hindi_HISTOGRAMS_FILE = 'testdata.svm'
hindi_CODEBOOK_FILE = 'codebook.file'
hindi_MODEL_FILE = 'trainingdata.svm.model'

'''


#to get and parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='classify images with a visual bag of words model')
    parser.add_argument('-c', help='path to the codebook file', required=False, default=CODEBOOK_FILE)
    parser.add_argument('-m', help='path to the model  file', required=False, default=MODEL_FILE)
    parser.add_argument('-i', help='path to histogram file', required=False)
    #parser.add_argument('input_images', help='images to classify', nargs='+')
    args = parser.parse_args()
    return args

input_images = []
for (dirpath, dirnames, filenames) in walk('croppedframes/'):
    input_images.extend(filenames)

for index,i in enumerate(input_images):
  filenames[index] = 'croppedframes' + '/' + filenames[index]


print "---------------------"
print "extract Sift features"
all_files = []
all_files_labels = {}
all_features = {}

args = parse_arguments()
model_file = args.m
codebook_file = args.c
HISTOGRAMS_FILE = args.i
fnames = filenames

#extract SIFT features for the testdata for classification
all_features = extractSift(fnames)


for i in fnames:
    all_files_labels[i] = 0  # initial label assignment

print "---------------------"
print "loading codebook from " + codebook_file
with open(codebook_file, 'rb') as f:
    codebook = load(f)

print "---------------------"
print "computing visual word histograms"
hist_start = time.time()
all_word_histgrams = {}
for imagefname in all_features:
    word_histgram = computeHistograms(codebook, all_features[imagefname])
    all_word_histgrams[imagefname] = word_histgram
hist_end = time.time()
print "time taken for histogram computation ",hist_end-hist_start


print "---------------------"
print "write the histograms to file to pass it to the svm"
histwrite_start=time.time()
nclusters = codebook.shape[0]
writeHistogramsToFile(nclusters,
                      all_files_labels,
                      fnames,
                      all_word_histgrams,
                      HISTOGRAMS_FILE)

histwrite_end = time.time()
print "time taken for writing histograms to file: ",histwrite_end-histwrite_start
print "---------------------"
print "Test Data Classification with SVM"



#src = 'testdata/'
if HISTOGRAMS_FILE == "tamiltestdata.svm":
  dest1 = 'tamilwords/'
if HISTOGRAMS_FILE == "englishtestdata.svm":
  dest1 = 'englishwords/'
if HISTOGRAMS_FILE == "malayalamtestdata.svm":
  dest1 = 'malayalamwords/'
if HISTOGRAMS_FILE == "hinditestdata.svm":
  dest1 = 'hindiwords/'



def copyFile(src, dest):
    try:
        shutil.copy(src, dest)

    except shutil.Error as e:
        parserrint('Error: %s' % e)

    except IOError as e:
        print('Error: %s' % e.strerror)

kanmisclass = []
engmisclass = []

count = 0


for index,i in enumerate(libsvm.test(HISTOGRAMS_FILE,model_file)):
  #print 'File:',filenames[index]
  count += 1
  print count
  if i == 0 :
    copyFile(filenames[index],dest1)
    os.remove(filenames[index])
  else:
    continue
