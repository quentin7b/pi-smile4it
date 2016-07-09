#!/usr/bin/python

import picamera
import datetime
from merges import build_images
from screen import take_picture, draw_home, display_rendered, RESOLUTION

with picamera.PiCamera() as camera:
    camera.resolution = (RESOLUTION, RESOLUTION)
    camera.framerate = 24

    while True:
        # Wait for the user to start the program
        draw_home(camera)
        raw_input("Wait user input")
        print "Picture asking at " + str(datetime.datetime.now().isoformat())

        # Show the preview
        camera.start_preview()

        # Start the picture mode
        picture_count = 4
        picture_list = []
        while picture_count is not 0:
            picture_list.append(take_picture(camera))
            picture_count -= 1

        # Stop the preview
        camera.stop_preview()

        # Build images
        rendered = build_images(picture_list)

        # show rendered
        display_rendered(camera, rendered, 5)
