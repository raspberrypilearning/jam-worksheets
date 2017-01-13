# Push button camera

## Capture

1. Enter the following code:

    ```python
    from picamera import PiCamera
    from gpiozero import Button

    camera = PiCamera()
    button = Button(25)

    camera.start_preview()
    button.wait_for_press()
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    ```

1. Run your code with `F5`.

1. Once the preview has started, press the button to capture an image.

1. Open the file manager window and you should see your `image.jpg`. Double-click to view.

## Multiple photos

Now that you have successfully taken individual photographs with your camera, it's time to try combining a series of still images to make a stop motion animation.

1. Modify your code to add a loop to keep taking pictures every time the button is pressed:

    ```python
    from picamera import PiCamera
    from gpiozero import Button

    camera = PiCamera()
    button = Button(25)

    camera.start_preview()
    for i in range(5):
        button.wait_for_press()
        camera.capture('/home/pi/Desktop/frame%03d.jpg' % i)
    camera.stop_preview()
    ```
