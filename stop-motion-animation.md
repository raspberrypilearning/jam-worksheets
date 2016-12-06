# Stop Motion Animation

## Push button camera

1. Enter the following code:

    ```python
    from picamera import PiCamera
    from gpiozero import Button
    from time import sleep

    button = Button(17)
    camera = PiCamera()

    camera.start_preview()
    button.wait_for_press()
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()
    ```

1. Run your code with `F5`.

1. Once the preview has started, press the button connected to your Pi to capture an image.

1. Open the file manager window and you should see your `image.jpg`. Double-click to view.

## Stop motion animation

Now that you have successfully taken individual photographs with your camera, it's time to try combining a series of still images to make a stop motion animation.

1. Modify your code to add a loop to keep taking pictures every time the button is pressed:

    ```python
    from picamera import PiCamera
    from gpiozero import Button
    from time import sleep

    button = Button(17)
    camera = PiCamera()

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

1. Once that's done, you can play back your video with:

    ```bash
    omxplayer animation.mp4
    ```
