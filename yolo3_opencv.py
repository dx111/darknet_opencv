from glob import glob
import shutil
import random


files=glob("./data/jpeg/*.jpg")

random.shuffle(files)



for i,f in enumerate(files):
    new_name="./data/jpeg2/"+str(i+1)+".jpg"
    shutil.copy(f,new_name)