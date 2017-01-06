# Stop Motion Animation

## Push button camera

1. Enter the following code:

    ```python
    from picamera import PiCamera
    from sense_hat import SenseHat
    from time import sleep

    sense = SenseHat()
    camera = PiCamera()

    camera.start_preview()
    sense.stick.wait_for_event(True)
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()
    ```

1. Run your code with `F5`.

1. Once the preview has started, press the joystick to capture an image.

1. Open the file manager window and you should see your `image.jpg`. Double-click to view.

## Multiple photos

Now that you have successfully taken individual photographs with your camera, it's time to try combining a series of still images to make a stop motion animation.

1. Modify your code to add a loop to keep taking pictures every time the joystick is pressed:

    ```python
    from picamera import PiCamera
    from sense_hat import SenseHat
    from time import sleep

    sense = SenseHat()
    camera = PiCamera()

    camera.start_preview()
    for i in range(5):
        sense.stick.wait_for_event(True)
        camera.capture('/home/pi/frame%03d.jpg' % i)
    camera.stop_preview()
    ```
