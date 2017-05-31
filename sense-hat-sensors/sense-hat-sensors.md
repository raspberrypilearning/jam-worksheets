# Sense HAT Sensors

## Test the Sense HAT

1. Open Python 3 and enter the following commands directly into the shell:

    (do not type the chevrons `>>>`)

    ```python
    >>> from sense_hat import SenseHat
    >>> sense = SenseHat()
    >>> sense.show_message(“Hello world”)
    ```

    Press Enter after each line, and after the third line, the message should appear on the Sense HAT's display.

1. Now try retreiving the sensor values:

    ```python
    >>> sense.temperature
    >>> sense.humidity
    >>> sense.pressure
    >>> sense.accelerometer
    >>> sense.gyroscope
    >>> sense.orientation
    ```

    When you press Enter, you will see the sensor's value.

## Faces

1. Open a new window and type:

    ```python
    from sense_hat import SenseHat
    from faces import normal, happy, sad
    from time import sleep

    sense = SenseHat()

    sense.set_pixels(sad)
    sleep(1)
    sense.set_pixels(normal)
    sleep(1)
    sense.set_pixels(happy)
    ```

1. Run the code with `F5` and you should see a sad face, a normal face and a happy face appear.

## And breathe...

1. Replace the last 5 lines with:

    ```python
    start_humidity = sense.humidity

    while True:
        print(sense.humidity)
        if sense.humidity > start_humidity + 10:
            sense.set_pixels(happy)
        elif sense.humidity > start_humidity + 5:
            sense.set_pixels(normal)
        else:
            sense.set_pixels(sad)
        sleep(1)
    ```

1. Run the code again. Now breathe on the Sense HAT and see if you can make it smile!
