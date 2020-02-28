import os
from PIL import Image
from datetime import datetime
import time

time_initial = int(round(time.time() * 1000))

current_time = datetime.today().strftime('%Y-%m-%d-%H;%M;%S')

directory = os.getcwd()

os.mkdir( current_time )
for file in os.listdir(directory):
    if file.endswith(".tga"):
        fileExt = file
        fileExp = current_time + "/" + file[:-4] + ".png"
        Image.open (fileExt).save (fileExp)
        print("one file converted")
time_ending = int(round(time.time() * 1000))
print("Time taken: ", time_ending - time_initial, " miliseconds")