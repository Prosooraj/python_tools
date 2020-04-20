import random
import os.path

path = "/home/sun/batch/"             #Give file path here
newname="NewFile "                    #Give file name here

for filename in enumerate(os.listdir(path)):
    file=os.rename(path+filename[1],  path+'/'+newname+str(random.randint(1,10000)))


