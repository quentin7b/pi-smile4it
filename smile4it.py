#!/usr/bin/python

import picamera
import datetime
from PIL import Image
from time import sleep

last_overlay = None
RESOLUTION = 800

def fusion_vertical(first, second, third, fourth):
    backImage = Image.open('res/4_vertical.png')
    
    overImage = Image.open(first)
    offset = (100, 100)
    backImage.paste(overImage, offset)
    
    overImage = Image.open(second)
    offset = (100, 1000)
    backImage.paste(overImage, offset)
    
    overImage = Image.open(third)
    offset = (100, 1900)
    backImage.paste(overImage, offset)
    
    overImage = Image.open(fourth)
    offset = (100, 2800)
    backImage.paste(overImage, offset)
    
    backImage.save(str(datetime.datetime.now().isoformat())+'.png')
    
def fusion_square(first, second, third, fourth):
    backImage = Image.open('res/4_block.png')
    
    overImage = Image.open(first)
    offset = (100, 100)
    backImage.paste(overImage, offset)
    
    overImage = Image.open(second)
    offset = (1000, 100)
    backImage.paste(overImage, offset)
    
    overImage = Image.open(third)
    offset = (100, 1000)
    backImage.paste(overImage, offset)
    
    overImage = Image.open(fourth)
    offset = (1000, 1000)
    backImage.paste(overImage, offset)
    
    backImage.save(str(datetime.datetime.now().isoformat())+'.png')

def set_count_down_on_screen(timeleft):
    global last_overlay
    img = Image.open('res/'+str(timeleft)+'.png')
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
    o.alpha = 128
    o.layer = 3
    last_overlay = o
    
def take_picture(camera):
    index = 5;
    while index is not 0:
        set_count_down_on_screen(index)
        sleep(1)
        index = index-1
    pictureName = str(datetime.datetime.now().isoformat())+'.png'
    camera.capture(pictureName)
    return pictureName

with picamera.PiCamera() as camera:
    camera.resolution = (RESOLUTION, RESOLUTION)
    camera.framerate = 24
    camera.start_preview()

    picture_count = 4
    picture_list = []
    while picture_count is not 0:
        picture_list.append(take_picture(camera))
        picture_count = picture_count-1
    
    camera.stop_preview()
    fusion_vertical(picture_list[0], picture_list[1], picture_list[2], picture_list[3])
    fusion_square(picture_list[0], picture_list[1], picture_list[2], picture_list[3])

