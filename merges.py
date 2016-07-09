#!/usr/bin/python

import datetime
from PIL import Image
from screen import RESOLUTION, VERTICAL_SIZES, SQUARE_SIZES


def build_images(picture_list):
    first = Image.open(picture_list[0])
    second = Image.open(picture_list[1])
    third = Image.open(picture_list[2])
    fourth = Image.open(picture_list[3])
    return [square_merge(first, second, third, fourth),
            vertical_merge(first, second, third, fourth)]


def vertical_merge(first, second, third, fourth):
    back_image = Image.new("RGB", VERTICAL_SIZES, "white")
    back_image.paste(first, (100, 100))
    back_image.paste(second, (100, 200 + RESOLUTION))
    back_image.paste(third, (100, 300 + 2 * RESOLUTION))
    back_image.paste(fourth, (100, 400 + 3 * RESOLUTION))
    file_name = 'merges/' + str(datetime.datetime.now().isoformat()) + '-vertical.jpeg'
    back_image.save(file_name)
    return back_image


def square_merge(first, second, third, fourth):
    back_image = Image.new("RGB", SQUARE_SIZES, "white")
    back_image.paste(first, (100, 100))
    back_image.paste(second, (200 + RESOLUTION, 100))
    back_image.paste(third, (100, 200 + RESOLUTION))
    back_image.paste(fourth, (200 + RESOLUTION, 200 + RESOLUTION))
    file_name = 'merges/' + str(datetime.datetime.now().isoformat()) + '-square.jpeg'
    back_image.save(file_name)
    return back_image
