#!/usr/bin/python

import datetime
from time import sleep
from PIL import Image

SCREEN_RESOLUTION = (1184, 624)
RESOLUTION = 800
VERTICAL_SIZES = (200 + RESOLUTION, 800 + 4 * RESOLUTION)
SQUARE_SIZES = (300 + 2 * RESOLUTION, 700 + 2 * RESOLUTION)
last_overlay = None
home = Image.open('res/home_1.jpg').resize(SCREEN_RESOLUTION, Image.ANTIALIAS)


def draw_home(camera):
    set_image_on_screen(camera, home, 255)


def display_rendered(camera, images, timeout):
    for image in images:
        img = resize(image)
        set_image_on_screen(camera, img, 255)
        sleep(timeout)


def resize(image):
    width, height = image.size
    if width > height:
        # horizontal image
        if width > SCREEN_RESOLUTION[0]:
            # image width is larger than screen
            ratio = math.floor(width / SCREEN_RESOLUTION[0])
            resize = (SCREEN_RESOLUTION[0], ratio * SCREEN_RESOLUTION[1])
            return image.resize(resize, Image.ANTIALIAS)
        else:
            # image width is lower than screen
            return image
    else:
        # vertical image
        if height > SCREEN_RESOLUTION[1]:
            # image height smaller than screen
            return image
        else:
            # image height bigger than screen
            ratio = math.floor(height / SCREEN_RESOLUTION[1])
            resize = (width * SCREEN_RESOLUTION[0], SCREEN_RESOLUTION[1])
            return image.resize(resize, Image.ANTIALIAS)


def set_image_on_screen(camera, img, transparency=100):
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


def take_picture(camera, countdown=4):
    while countdown is not 0:
        set_image_on_screen(camera, Image.open('res/' + str(countdown) + '.png'))
        sleep(1)
        countdown -= 1
    picture_name = 'raw/' + str(datetime.datetime.now().isoformat()) + '.jpeg'
    camera.capture(picture_name)
    return picture_name
