from PIL import Image, ImageDraw, ImageFont
import os
A4_size = 1654, 2338

username = 'satyaki_auto'

save_dir = 'fonts/'+username +'/'
filename = "font.jpg"
if(os.path.isdir('fonts/' + username + '/') == False):
    os.mkdir('fonts/' + username)
#char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_+={}|[]\\:";\'<>?,./'
# create new image
image = Image.open(filename)
rect_size_x, rect_size_y = 55, 120
rect_no = 0
for i in range(40, 2060, 200):
    for j in range(140, 1490, 140):
        t_img = image.crop((j, i, j + rect_size_x, i + rect_size_y))
        t_img.save(save_dir+'im'+ str(rect_no +1)+'.jpg')
        rect_no+=1
        if(rect_no == 92):
            break