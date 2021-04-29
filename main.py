from PIL import Image
import os, glob
A4_size = 1654, 2338
ch_size = 21, 55
cx, cy = ch_size
ax, ay = A4_size 
wh_im = Image.open('white.jpg')
wh_px = wh_im.load()
#print(wh_px[4,4]) /home/satyaki/Dropbox/work/py/image_assignment/fonts/satyaki
def nextwordlen(st, n):
    i = 0
    print('string index')
    #print(n+i)
    while(st[n+i] != ' '):
        print(n+i)
        i+=1
        if(n+i == len(st)):
            break
    return i
char_index = 0
starting_row_pixel = 91
t = 1
while(True):
    string = input()
    string_end = False
    char_index = 0
    for row in range(starting_row_pixel, 2238, cy):
        nextline = False
        for col in range(91, 1462, cx):
            if((1662-col)/cx >= nextwordlen(string, char_index)):
                present_char = string[char_index]
                if(present_char == ' '):
                    char_index+=1
                    continue
                if(present_char == '\n'):
                    starting_row_pixel = row + cy
                    string_end = True
                    char_index+=1
                    break
                print('character taken:'+present_char)
                present_im = Image.open('/home/satyaki/Dropbox/work/py/image_assignment/font/resized/' + present_char + '.jpg')
               # present_im.show()
                present_px = present_im.load()
                for cRow in range(55):
                    for cCol in range(21):
                        page_pixel = col + cCol, row + cRow
                        char_pixel = cCol, cRow
                        #print(page_pixel, char_pixel)
                        #x, y, z = present_im.getpixel(char_pixel)
                        wh_px[page_pixel] = present_px[char_pixel]
                        #print(wh_px[page_pixel])
                    #print('writing img...')
                char_index+=1
                if(char_index == len(string)):
                    starting_row_pixel = row + cy
                    string_end = True
                    char_index+=1
                    break
            else:
                nextline = True
                char_index+=1
            if(nextline):
                continue
        if(string_end):
            break
    wh_im.show()
    wh_im.save('/home/satyaki/Dropbox/work/py/image_assignment/output/out.jpg')