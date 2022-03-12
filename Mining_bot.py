from pynput.keyboard import Key, Controller
import time
import ctypes
import pyautogui
from pynput.mouse import Button, Controller as MouseController
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearch_loop
import cv2
import numpy as np
import pyautogui
import random
import time
import platform
import subprocess
import os
import mss
import sys
import keyboard

mouse = MouseController()
SendInput = ctypes.windll.user32.SendInput

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
UP = 0xC8
LEFT = 0xCB
RIGHT = 0xCD
DOWN = 0xD0
ENTER = 0x1C
ESC = 0x01
TWO = 0x03

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actuals Functions
def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0,
                        ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# directx scan codes
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

path="C:\\Users\\Owner\\Pictures\\Minecraft Textures"
file="\\diamond.jpg"

valid_images = [".jpg", ".gif", ".png", ".jpeg"]

one = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle1.jpg"
two = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle2.jpg"
three = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle3.jpg"
four = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\diamond.jpg"
five = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle5.jpg"
six = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle6.jpg" 
seven = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle7.jpg"
eight = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle8.jpg"
nine = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle9.jpg"
ten = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle10.jpg"
eleven = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle11.jpg"
twelve = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle12.jpg"
thirteen = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle13.jpg"
fourteen = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle14.jpg"
fifteen = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle15.jpg"
sixteen = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle16.jpg"
seventeen = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle17.jpg"
eighteen = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle18.jpg"
nineteen = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle19.jpg"
twenty = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle20.jpg"
twentyone = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle21.jpg"
twentytwo = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle22.jpg"
twentythree = "C:\\Users\\Owner\\Pictures\\Minecraft Textures\\angle23.jpg"

is_retina = False
if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)

'''
grabs a region (topx, topy, bottomx, bottomy)
to the tuple (topx, topy, width, height)
input : a tuple containing the 4 coordinates of the region to capture
output : a PIL image of the area selected.
'''


def region_grabber(region):
    if is_retina: region = [n * 2 for n in region]
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1

    region = x1, y1, width, height
    with mss.mss() as sct:
        return sct.grab(region)

'''
Searchs for an image within an area
input :
image : path to the image file (see opencv imread for supported types)
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements
returns :
the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
'''
def move():
        mouse.press(Button.left)
        time.sleep(0.78)
        mouse.release(Button.left)
        ReleaseKey(0x2E) #C
        PressKey(0x2E) #C
        PressKey(0x11) #W
        time.sleep(0.78)
        ReleaseKey(0x11) #W


def imagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None):
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
        # im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


'''
click on the center of an image with a bit of random.
eg, if an image is 100*100 with an offset of 5 it may click at 52,50 the first time and then 55,53 etc
Usefull to avoid anti-bot monitoring while staying precise.
this function doesn't search for the image, it's only ment for easy clicking on the images.
input :
image : path to the image file (see opencv imread for supported types)
pos : array containing the position of the top left corner of the image [x,y]
action : button of the mouse to activate : "left" "right" "middle", see pyautogui.click documentation for more info
time : time taken for the mouse to move from where it was to the new position
'''

timestamp=1
action='left'
def click_image(image, pos, action, timestamp, offset=5):
    img = cv2.imread(image)
    height, width, channels = img.shape
    pyautogui.moveTo(pos[0] + r(width / 2, offset), pos[1] + r(height / 2, offset),
                     timestamp)
    pyautogui.click(button=action)


'''
Searchs for an image on the screen
input :
image : path to the image file (see opencv imread for supported types)
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements
returns :
the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
'''

def imagesearch(files, precision=0.0001):
    with mss.mss() as sct:
        im = sct.grab(sct.monitors[0])
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
        # im.save('testarea.png') useful for debugging purposes, this will save the captured region as "testarea.png"
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    
        x=1
    while x<20:
        template = cv2.imread(one, 0)
        print("one")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision: 
            
            
            return max_loc
            break
        template = cv2.imread(two, 0)
        print("two")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:  
            return max_loc
            break
        template = cv2.imread(three, 0)
        print("three")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            
            return max_loc
            break

        template = cv2.imread(four, 0)
        print("four")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(five, 0)
        print("five")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break
        template = cv2.imread(six, 0)
        print("six")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(seven, 0)
        print("seven")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(eight, 0)
        print("eight")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(nine, 0)
        print("nine")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(ten, 0)
        print("ten")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(eleven, 0)
        print("eleven")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(twelve, 0)
        print("twelve")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(thirteen, 0)
        print("thriteen")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(fourteen, 0)
        print("fourteen")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(fifteen, 0)
        print("fifteen")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(sixteen, 0)
        print("sixteen")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(seventeen, 0)
        print("seventeen")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(eighteen, 0)
        print("eighteen")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(nineteen, 0)
        print("nineteen")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(twenty, 0)
        print("twenty")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(twentyone, 0)
        print("twentyone")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break\

        template = cv2.imread(twentytwo, 0)
        print("twentytwo")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        if max_val > precision:
            return max_loc
            break

        template = cv2.imread(twentythree, 0)
        print("twentythree")
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        x+=1
        move()
        if max_val > precision:
            return max_loc
            break

        if x>20:
            imagesearch_loop(one, timesample, precision)
        


'''
Searches for an image on screen continuously until it's found.
input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
returns :
the top left corner coordinates of the element if found as an array [x,y]
'''

timesample=2
def imagesearch_loop(one, timesample, precision=0.0001):
    pos = imagesearch(one, precision)
    
    try:
        while pos[0] == -1:
            print(path + " not found, waiting")
            time.sleep(timesample)
            pos = imagesearch(one, precision)
        print(pos)
        cont = input("Continue? (y/n): ")
        if cont == y:
            imagesearch(one, precision)
        else:
            os._exit()


    except:
       imagesearch(one, precision)

'''
Searchs for an image on screen continuously until it's found or max number of samples reached.
input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image
maxSamples: maximum number of samples before function times out.
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
returns :
the top left corner coordinates of the element if found as an array [x,y]
'''


def imagesearch_numLoop(image, timesample, maxSamples, precision=0.8):
    pos = imagesearch(files, precision)
    count = 0
    while pos[0] == -1:
        print(image + " not found, waiting")
        time.sleep(timesample)
        pos = imagesearch(image, precision)
        count = count + 1
        if count > maxSamples:
            break

    return pos


'''
Searchs for an image on a region of the screen continuously until it's found.
input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
returns :
the top left corner coordinates of the element as an array [x,y]
'''


def imagesearch_region_loop(image, timesample, x1, y1, x2, y2, precision=0.8):
    pos = imagesearcharea(image, x1, y1, x2, y2, precision)

    while pos[0] == -1:
        time.sleep(timesample)
        pos = imagesearcharea(image, x1, y1, x2, y2, precision)
    return pos


'''
Searches for an image on the screen and counts the number of occurrences.
input :
image : path to the target image file (see opencv imread for supported types)
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.9
returns :
the number of times a given image appears on the screen.
optionally an output image with all the occurances boxed with a red outline.
'''


def imagesearch_count(image, precision=0.9):
    with mss.mss() as sct:
        img_rgb = sct.grab()
        if is_retina:
            img_rgb.thumbnail((round(img_rgb.size[0] * 0.5), round(img_rgb.size[1] * 0.5)))
        img_rgb = np.array(img_rgb)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= precision)
        count = 0
        for pt in zip(*loc[::-1]):  # Swap columns and rows
            # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2) // Uncomment to draw boxes around found occurrences
            count = count + 1
        # cv2.imwrite('result.png', img_rgb) // Uncomment to write output image with boxes drawn around occurrences
        return count


'''
Get all screens on the provided folder and search them on screen.
input :
path : path of the folder with the images to be searched on screen
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
returns :
A dictionary where the key is the path to image file and the value is the position where was found.
'''


def imagesearch_from_folder(path, precision):
   
   pos=imagesearch(valid_images, precision)
   while pos[0] == -1:
        print(path)
        imagesPos = {}
        
        for file in files:
            pos = imagesearch(list, precision)
            imagesPos[path+file] = pos
            

        return imagesPos


def r(num, rand):
    return num + rand * random.random()

i=1
#imagesearch_from_folder(valid_images, precision=0.8)
imagesearch_loop(valid_images, timesample, precision=0.8)
