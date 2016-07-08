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
    backImage = Image.new("RGB", VERTICAL_SIZES, "white") 
    backImage.paste(first, (100, 100))  
    backImage.paste(second, (100, 200 + RESOLUTION))
    backImage.paste(third, (100, 300 + 2*RESOLUTION))
    backImage.paste(fourth, (100, 400 + 3*RESOLUTION))
    file_name = 'merges/'+str(datetime.datetime.now().isoformat())+'-vertical.jpeg'
    backImage.save(file_name)
    return backImage
    
def square_merge(first, second, third, fourth):
    backImage = Image.new("RGB", SQUARE_SIZES, "white")     
    backImage.paste(first, (100, 100))
    backImage.paste(second, (200 + RESOLUTION, 100))
    backImage.paste(third, (100, 200 + RESOLUTION))
    backImage.paste(fourth, (200 + RESOLUTION, 200 + RESOLUTION))
    file_name = 'merges/'+str(datetime.datetime.now().isoformat())+'-square.jpeg'
    backImage.save(file_name)
    return backImage
