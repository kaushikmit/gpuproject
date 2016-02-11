
#to delete .sift extension files

from os import walk

import os
import sys


files = []
for (dirpath, dirnames, filenames) in walk('croppedframes/'):
    files.extend(filenames)

print files

for i in filenames:
	if i.endswith('.sift'):
		os.remove('croppedframes/'+i)


