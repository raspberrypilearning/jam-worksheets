# Snapchat Photobooth

## Controlling the camera using Python

1. Start by opening a Terminal window. Enter the following command, and press Enter:

    ```bash
    raspistill -k
    ```

    You should see the camera preview for a few seconds - this is good as it means your camera is working correctly.

1. Open Python 3 and create a new file.

1. Enter the following code:

    ```python
    from picamera import PiCamera
    from time import sleep

    camera = PiCamera()

    camera.start_preview()
    sleep(3)
    camera.stop_preview()
    ```

1. Run the code with `F5`. You should see the camera preview appear for 3 seconds, and then close.

1. Now add in a line to flip the image horizontally (so it's like a mirror):

    ```python
    camera.start_preview()
    camera.hflip = True
    sleep(3)
    camera.stop_preview()
    ```

1. Run the code again - you should see the camera preview flipped like a mirror.

1. Add a line to set the output path, and to save a captured image:

    ```python
    output = '/home/pi/image.png'

    camera.start_preview()
    camera.hflip = True
    sleep(3)
    camera.capture(output)
    camera.stop_preview()
    ```

1. Run the code again - it should take a picture after 3 seconds.

1. Now open the File Manager to see your picture.

## Use a button

1. Now add a button into your code:

    ```python
    from picamera import PiCamera
    from gpiozero import Button
    from time import sleep

    camera = PiCamera()
    button = Button(16)

    output = '/home/pi/image.png'

    camera.start_preview()
    camera.hflip = True
    button.wait_for_press()
    sleep(3)
    camera.capture(output)
    camera.stop_preview()
    ```

1. Run the code - now it will wait for you to press the button before it takes the picture.

## Image overlays

1. Add the snapchat code, set the resolution of the camera, and include an overlay:

    ```python
    from picamera import PiCamera
    from gpiozero import Button
    from time import sleep
    from snapchat import *

    camera = PiCamera()
    camera.resolution = (1024, 768)
    button = Button(16)

    output = '/home/pi/image.png'
    overlay = 'flowers'

    camera.start_preview()
    camera.hflip = True
    preview_overlay(camera, overlay)
    button.wait_for_press()
    sleep(3)
    camera.capture(output)
    camera.stop_preview()
    remove_overlays(camera)
    output_overlay(output, overlay)
    ```

1. Run the code again - now it will add the `flowers` overlay to your preview, and to the captured image.

1. Try a different overlay! In the shell, enter `overlays` and press enter to see what's available.

1. Add a second button, and make it change the overlay:

    ```python
	from picamera import PiCamera
	from gpiozero import Button
	from time import sleep
	from snapchat import *

	camera = PiCamera()
	camera.resolution = (1024, 768)
	button1 = Button(16)
	button2 = Button(12)

	def next_overlay():
		global overlay
		overlay = next(all_overlays)
		preview_overlay(camera, overlay)

	output = gen_filename()
	button2.when_pressed = next_overlay

	camera.start_preview()
	camera.hflip = True
	button1.wait_for_press()
	sleep(3)
	camera.capture(output)
	camera.stop_preview()
	remove_overlays(camera)
	output_overlay(output, overlay)
    ```

1. Run the code, and use the second button to change the overlay (it will cycle through all available overlays), and use the first button to capture!
