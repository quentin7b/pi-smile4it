#!/usr/bin/python

import picamera
import datetime
from time import sleep
from PIL import Image

RESOLUTION = 800
VERTICAL_SIZES = (200 + RESOLUTION, 800 + 4*RESOLUTION)
SQUARE_SIZES = (300 + 2*RESOLUTION, 700 + 2*RESOLUTION)
last_overlay = None
home =  Image.open('res/home_1.jpg')

def draw_home(camera):
    set_image_on_screen(camera, home, 255)
    
def display_rendered(camera, images, timeout):
    for image in images:
	    set_image_on_screen(camera, image, 255)
	    sleep(timeout)

def set_image_on_screen(camera, img, transparency = 100):
    global last_overlay
    # Create an image padded to the required size with mode 'RGB'
    pad = Image.new('RGB', (
		((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
    ))
    # Paste the original image into the padded one
    pad.paste(img, (0, 0))

    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    if last_overlay:
        camera.remove_overlay(last_overlay)
    o = camera.add_overlay(pad.tostring(), size=img.size)
    # By default, the overlay is in layer 0, beneath the
    # preview (which defaults to layer 2). Here we make
    # the new overlay semi-transparent, then move it above
    # the preview
    o.alpha = transparency
    o.layer = 3
    last_overlay = o
        
def take_picture(camera, countdown = 4):
    while countdown is not 0:
        set_image_on_screen(camera, Image.open('res/'+str(countdown)+'.png'))
        sleep(1)
        countdown = countdown-1
    picture_name = 'raw/'+str(datetime.datetime.now().isoformat())+'.jpeg'
    camera.capture(picture_name)
    return picture_name
