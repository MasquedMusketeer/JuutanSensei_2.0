import time
import mouse
import keyboard
import getpixelcolor as gp 

BLcreds = ["1234", "abcd", "1234", "abcd"]

def succesLogin():
    pixel = gp.pixel(1265, 383)
    if pixel != (255, 255, 255):
        mouse.click("left")
        time.sleep(1)
        succesLogin()

def BLlogin():
    mouse.move(796, 313, absolute=True, duration=0.3)
    mouse.click("left")
    mouse.click("left")
    time.sleep(0.5)
    keyboard.write(BLcreds[0])
    mouse.move(783, 353, absolute=True, duration=0.3)
    mouse.click("left")
    time.sleep(0.5)
    keyboard.write(BLcreds[1])
    mouse.move(832, 429, absolute=True, duration=0.3)
    succesLogin()
    time.sleep(12)
    mouse.move(859, 443, absolute=True, duration=0.3)
    mouse.click("left")
    time.sleep(0.5)
    keyboard.write(BLcreds[2])
    mouse.move(869, 484, absolute=True, duration=0.3)
    mouse.click("left")
    time.sleep(0.5)
    keyboard.write(BLcreds[3])
    mouse.move(814, 539, absolute=True, duration=0.3)
    mouse.click("left")