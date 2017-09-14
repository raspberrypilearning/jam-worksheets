# Sense HAT Sensors

## Test the Sense HAT

1. Open Python 3 and enter the following commands directly into the shell:

    (do not type the chevrons `>>>`)

    ```python
    >>> from sense_hat import SenseHat
    >>> sense = SenseHat()
    >>> sense.show_message(“Hello world”)
    ```

    Press `Enter` after each line, and after the third line, the message should appear on the Sense HAT's display.

1. Now try retrieving the sensor values:

    ```python
    >>> sense.temperature
    >>> sense.humidity
    >>> sense.pressure
    ```

    When you press `Enter`, you will see the sensor's value.

## Faces

1. Open a new window and type:

    ```python
    from sense_hat import SenseHat
    from time import sleep

    sense = SenseHat()

    r = (255, 0, 0)
    g = (0, 255, 0)
    b = (0, 0, 255)
    y = (255, 255, 0)
    p = (255, 0, 255)
    c = (0, 255, 255)
    w = (255, 255, 255)
    e = (0, 0, 0)

    icon = [
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, b, e, e, b, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, b, e, e, e, e, b, e,
        e, b, b, b, b, b, b, e,
        e, e, e, e, e, e, e, e,
    ]

    sense.set_pixels(icon)
    ```

1. Now make your own icon using the colours (`r` is red, `g` is green, `b` is blue and so on). Your icon must be 8x8 like the example.

1. Run the code with `F5` and you should see your icon on the Sense HAT display.

## Make it hot

1. Replace the last line with:

    ```python
    start_temperature = sense.temperature

    while True:
        print(sense.temperature)
        if sense.temperature > start_temperature + 2:
            sense.set_pixels(icon)
        else:
            sense.clear()
        sleep(1)
    ```

1. Run the code again. Now press your finger against the temperature sensor on the Sense HAT and see if you can make your icon appear!
