from PIL import Image, ImageDraw, ImageFont
import os
A4_size = 1654, 2338
# name of the file to save
filename = "font.jpg"
char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_+={}|[]\\:";\'<>?,./'
# create new image
image = Image.open(filename)
rect_size_x, rect_size_y = 50, 115
image1 = ImageDraw.Draw(image)
rect_no = 0
text_font = ImageFont.truetype('Arial.ttf', 28)
for i in range(108, 2100, 200):
    for j in range(74, 1480, 133):
        image1.rectangle((j, i, j+rect_size_x, i+rect_size_y), fill=None, outline = 'blue', width = 1)
      #  image1.text((j + 15, i + rect_size_y+10), char_list[rect_no],font = text_font, fill = (100,100,100), )
        rect_no+=1
        if(rect_no == 92):
            break

image.show()

# save the file
#image.save(filename)
 
