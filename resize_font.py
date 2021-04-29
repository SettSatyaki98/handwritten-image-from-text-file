from PIL import Image
import os, glob

A4_size = 1654, 2338
os.chdir("fonts/satyaki")
for file in glob.glob("*.jpg"):
    im = Image.open(file)
            #px = im.load()
    new_size = 21, 55
    im2 = im.resize(new_size)
    #im2.show()
    im2.save("/home/satyaki/Dropbox/work/py/image_assignment/fonts/satyaki/resized/" + file)