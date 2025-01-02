import requests
import PySimpleGUI as sg
import tkinter as tk
from PIL import Image, ImageTk
from configparser import ConfigParser

config = ConfigParser()
config.read('followto.ini')

token = config.get('discord','token')
channel1 = config.get('channels','channel1')
channel2 = config.get('channels','channel2')
channel3 = config.get('channels','channel3')
altnum = int(config.get('accounts','altnum'))

error = False

enabledchannel1 = "0"
enabledchannel2 = "0"
enabledchannel3 = "0"

field="Rose"

headers = {
    "Authorization" : token
}


def checkchannel():
    if len(channel1) != 0 or len(channel2) != 0 or len(channel3) != 0:
        return True
    else: 
        return False

def checkchannel1():
    if len(channel1) != 0:
        return channel1
    elif len(channel2) != 0:
        return channel2
    elif len(channel3) != 0:
        return channel3
    else: 
        return 0

def checkchannel2():
    if len(channel1) and len(channel2) != 0:
        return 1
    elif len(channel1) and len(channel3) != 0:
        return 2
    elif len(channel2) and len(channel3) != 0:
        return 3
    else:
        return 0
    
def checkchannel3():
    if len(channel1) != 0 and len(channel2) != 0 and len(channel3) != 0:
        return True
    else:
        return False

def post1():
    payload = {
        "content" : "FollowTo "+field
    }
    requests.post(url1, payload, headers=headers)

def post2():
    payload = {
        "content" : "FollowTo "+field
    }
    requests.post(url2, payload, headers=headers)

def post3():
    payload = {
        "content" : "FollowTo "+field
    }
    requests.post(url3, payload, headers=headers)

def changefield(newfield):
    global field
    field = newfield

if altnum == 1:
    if checkchannel() == True:
        enabledchannel1 = checkchannel1()
    else:
        error = True
        print("Channel not found, script won't function properly, make sure followto.ini is set up correctly!")
        
elif altnum == 2:
    if checkchannel2() == 1:
        enabledchannel1 = channel1
        enabledchannel2 = channel2
    elif checkchannel2() == 2:
        enabledchannel1 = channel1
        enabledchannel2 = channel3
    elif checkchannel2() == 3:
        enabledchannel1 = channel2
        enabledchannel2 = channel3
    else:
        error = True
        print("Channels not found, script won't function properly, make sure followto.ini is set up correctly!")

elif altnum == 3:
    if checkchannel3() == True:
        enabledchannel1 = channel1
        enabledchannel2 = channel2
        enabledchannel3 = channel3
    else:
        error = True
        print("Channels not found, script won't function properly, make sure followto.ini is set up correctly!")
else:
    print("You can only run 1-3 alts")

url1 = "https://discord.com/api/v9/channels/"+enabledchannel1+"/messages"
url2 = "https://discord.com/api/v9/channels/"+enabledchannel2+"/messages"
url3 = "https://discord.com/api/v9/channels/"+enabledchannel3+"/messages"

if altnum == 1:
    r1 = sg.Radio("Send alt 1", "alts", size=(10, 1), key="1", default=True)
    r2 = sg.Text("Send alt 2 (disabled)", key="2")
    r3 = sg.Text("Send alt 3 (disabled)", key="3")

if altnum == 2:
    r1 = sg.Radio("Send alt 1", "alts", size=(10, 1), key="1", default=True)
    r2 = sg.Radio("Send alt 2", "alts", size=(10, 1), key="2")
    r3 = sg.Text("Send alt 3 (disabled)", key="3")

if altnum == 3:
    r1 = sg.Radio("Send alt 1", "alts", size=(10, 1), key="1", default=True)
    r2 = sg.Radio("Send alt 2", "alts", size=(10, 1), key="2")
    r3 = sg.Radio("Send alt 3", "alts", size=(10, 1), key="3")

image_path = "map.png"
image = Image.open(image_path)
image_width, image_height = image.size

layout = [
    [sg.Canvas(size=(image_width, image_height), key="-CANVAS-")],
    [r1],[r2],[r3],
    [sg.Button("Go to field!")],
    [sg.Text("Made by @pawselfie")],
]

window = sg.Window("Riot's RBC Alt Sync v1.0", layout, finalize=True)

canvas_elem = window["-CANVAS-"]
canvas = canvas_elem.TKCanvas

tk_image = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor="nw", image=tk_image)

pine = tk.Button(canvas, text="Pine Tree Forest", command=lambda: changefield("PineTree"))
rose = tk.Button(canvas, text="Rose Field", command=lambda: changefield("Rose"))
bamb = tk.Button(canvas, text="Bamboo Field", command=lambda: changefield("Bamboo"))
dand = tk.Button(canvas, text="Dandelion Field", command=lambda: changefield("Dandelion"))
pumk = tk.Button(canvas, text="Pumpkin Patch", command=lambda: changefield("Pumpkin"))
sunf = tk.Button(canvas, text="Sunflower Field", command=lambda: changefield("Sunflower"))
mush = tk.Button(canvas, text="Mushroom Field", command=lambda: changefield("Mushroom"))
spide = tk.Button(canvas, text="Spider Field", command=lambda: changefield("Spider"))
pa = tk.Button(canvas, text="Pineapple Patch", command=lambda: changefield("Pineapple"))
pep = tk.Button(canvas, text="Pepper Patch", command=lambda: changefield("Pepper"))
top = tk.Button(canvas, text="Mountain Top Field", command=lambda: changefield("MountainTop"))
straw = tk.Button(canvas, text="Strawberry Field", command=lambda: changefield("Strawberry"))
coco = tk.Button(canvas, text="Coconut Field", command=lambda: changefield("Coconut"))
clov = tk.Button(canvas, text="Clover Field", command=lambda: changefield("Clover"))
bluf = tk.Button(canvas, text="Blue Flower Field", command=lambda: changefield("BlueFlower"))
stump = tk.Button(canvas, text="Stump Field", command=lambda: changefield("Stump"))
cac = tk.Button(canvas, text="Cactus Field", command=lambda: changefield("Cactus"))

canvas.create_window(530, 505, window=pine)
canvas.create_window(488, 320, window=rose)
canvas.create_window(239, 408, window=bamb)
canvas.create_window(325, 276, window=dand)
canvas.create_window(426, 507, window=pumk)
canvas.create_window(421, 296, window=sunf)
canvas.create_window(360, 335, window=mush)
canvas.create_window(327, 401, window=spide)
canvas.create_window(163, 522, window=pa)
canvas.create_window(618, 79, window=pep)
canvas.create_window(274, 526, window=top)
canvas.create_window(411, 401, window=straw)
canvas.create_window(469, 130, window=coco)
canvas.create_window(229, 288, window=clov)
canvas.create_window(232, 343, window=bluf)
canvas.create_window(67, 509, window=stump)
canvas.create_window(425, 461, window=cac)

if error == True:
        sg.popup_ok("Channels not found, script won't function properly, make sure followto.ini is set up correctly!")

while True:
    event, values = window.read()

    if event == "Go to field!" and altnum == 1:
        if values["1"] == True:
            if error == False:
                post1()
            else:
                sg.popup_ok("Channel not found, script won't function properly, make sure followto.ini is set up correctly!")

    elif event == "Go to field!" and altnum == 2:
        if values["1"] == True:
            if error == False:
                post1()
            else:
                sg.popup_ok("Channel not found, script won't function properly, make sure followto.ini is set up correctly!")
        else:
            if error == False:
                post2()
            else:
                sg.popup_ok("Channels not found, script won't function properly, make sure followto.ini is set up correctly!")

    elif event == "Go to field!" and altnum == 3:
        if values["1"] == True:
            if error == False:
                post1()
            else:
                sg.popup_ok("Channel not found, script won't function properly, make sure followto.ini is set up correctly!")
        elif values["2"] == True:
            if error == False:
                post2()
            else:
                sg.popup_ok("Channels not found, script won't function properly, make sure followto.ini is set up correctly!")
        else:
            if error == False:
                post3()
            else:
                sg.popup_ok("Channels not found, script won't function properly, make sure followto.ini is set up correctly!")

    if event == sg.WIN_CLOSED:
        break

window.close()
