# Traffic lights

| Component | GPIO pin |
| --------- | :------: |
| Button    | 25       |
| Red LED   | 24       |
| Amber LED | 23       |
| Green LED | 22       |
| Buzzer    | 5        |

## GPIO components

1. Open Python 3 from the main menu, and open a new file.

1. Enter the following code:

    ```python
    from gpiozero import LED, Button

    led = LED(22)
    button = Button(25)

    while True:
        if button.is_pressed:
            led.on()
        else:
            led.off()
    ```

1. Run your code with `F5`. Now when you press the button, the green LED will come on.

1. Try creating three LEDs:

    ```python
    from gpiozero import LED, Button

    red = LED(24)
    amber = LED(23)
    green = LED(22)

    button = Button(25)
    ```

1. Get them to come on when the button is pressed:

    ```python
    while True:
        if button.is_pressed:
            green.on()
            amber.on()
            red.on()
        else:
            green.off()
            amber.off()
            red.off()
    ```

1. Run the code and press the button.

## Traffic lights

You can use the built-in `TrafficLights` interface instead of three LEDs.

1. Amend the `from gpiozero import...` line to replace `LED` with `TrafficLights`:

    ```python
    from gpiozero import TrafficLights, Button

    button = Button(25)
    lights = TrafficLights(24, 23, 22)

    while True:
        button.wait_for_press()
        lights.on()
        button.wait_for_release()
        lights.off()
    ```

1. Try changing the lights to `blink`:

    ```python
    while True:
        lights.blink()
        button.wait_for_press()
        lights.off()
        button.wait_for_release()
    ```

## Traffic lights sequence

As well as controlling the whole set of lights together, you can also control each LED individually. With traffic light LEDs, a button and a buzzer, you can create your own traffic lights sequence, complete with pedestrian crossing!

1. Modify your loop to perform an automated sequence of LEDs being lit:

    ```python
    while True:
        lights.green.on()
        sleep(1)
        lights.amber.on()
        sleep(1)
        lights.red.on()
        sleep(1)
        lights.off()
    ```

1. Add a `wait_for_press()` so that pressing the button initiates the sequence:

    ```python
    while True:
        button.wait_for_press()
        lights.green.on()
        sleep(1)
        lights.amber.on()
        sleep(1)
        lights.red.on()
        sleep(1)
        lights.off()
    ```

    Try some more sequences of your own.

1. Now try creating the full traffic lights sequence:

    - Green on
    - Amber on
    - Red on
    - Red and amber on
    - Green on

    Be sure to turn the correct lights on and off at the right time, and make sure you use `sleep` to time the sequence perfectly.

1. Try adding the button for a pedestrian crossing. The button should move the lights to red (not immediately), and give the pedestrians time to cross before moving back to green until the button is pressed again.

1. Now try adding a buzzer to beep quickly to indicate that it is safe to cross, for the benefit of visually impaired pedestrians.
