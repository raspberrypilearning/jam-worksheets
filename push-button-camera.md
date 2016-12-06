# Push Button Stop Motion

## Test the camera

1. Open a Terminal window from the desktop or application menu. Enter the following command:

    ```bash
    raspistill -o image1.jpg
    ```

1. Run the command `ls` to see the files in your home directory; you should see `image1.jpg` listed.

1. Click the file manager icon in the taskbar and you should see some folders and files. Double-click `image1.jpg` to preview it.

## Take a picture with Python

1. Open Python 3 and open a new window.

1. Carefully enter the following code into the new window (case is important!):

    ```python
    from picamera import PiCamera
    from time import sleep

    camera = PiCamera()

    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/image2.jpg')
    camera.stop_preview()
    ```

1. Press `F5` to run the script.

1. Without closing the Python window, return to the file manager window and you'll see the new file `image2.jpg`. Double-click to view the picture.

## Push button

1. Import `Button` from the `gpiozero` module at the top of the code, create up a `Button` connected to pin 17, and change the `sleep` line to use `button.wait_for_press` like so:

    ```python
    from picamera import PiCamera
    from time import sleep
    from gpiozero import Button

    button = Button(17)
    camera = PiCamera()

    camera.start_preview()
    button.wait_for_press()
    camera.capture('/home/pi/image3.jpg')
    camera.stop_preview()
    ```

1. Save and run your script.

1. Once the preview has started, press the button connected to your Pi to capture an image.

1. Return to the file manager window and you should see your `image3.jpg`. Again, double-click to view.

## Take a selfie

If you want to take a photograph of yourself with the camera board, you are going to have to add in a delay to enable you to get into position. You can do this by modifying your program.

1. Add a line to your code to tell the program to sleep briefly before capturing an image, as below:

    ```python
    camera.start_preview()
    button.wait_for_press()
    sleep(3)
    camera.capture('/home/pi/image3.jpg')
    camera.stop_preview()
    ```

1. Save and run your script.

1. Press the button and try to take a selfie. Be sure to keep the camera still! Ideally, it should be mounted in position.

1. Again, feel free to check the image in the file manager. You can run the program again to take another selfie.

## Stop motion animation

Now that you have successfully taken individual photographs with your camera, it's time to try combining a series of still images to make a stop motion animation.

1. Modify your code to add a loop to keep taking pictures every time the button is pressed:

    ```python
    camera.start_preview()
    for i in range(20):
        button.wait_for_press()
        camera.capture('/home/pi/frame%03d.jpg' % i)
    camera.stop_preview()
    ```

1. Get in position, and use the button to take 20 photos for your animation.

## Generate the video

1. Run the video rendering command in the Terminal window:

    ```bash
    avconv -r 10 -qscale 2 -i frame%03d.jpg animation.mp4
    ```

1. You can adjust the frame rate by editing the rendering command. Try changing `-r 10` (10 frames per second) to another number.

    ```bash
    omxplayer animation.mp4
    ```
