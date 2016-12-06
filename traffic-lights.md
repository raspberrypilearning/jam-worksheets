# Traffic lights

![GPIO diagram](images/camjam1wiring.png)

| Component | GPIO pin |
| --------- | :------: |
| Button    | 21       |
| Red LED   | 25       |
| Amber LED | 8        |
| Green LED | 7        |
| Buzzer    | 15       |

## Button

1. Open Python 3, open a new file.

    ```python
    from gpiozero import Button

    button = Button(21)

    while True:
        if button.is_pressed:
            print("Pressed")
        else:
            print("Released")
    ```

1. Save and run: `Ctrl + S` and `F5`.

1. Modify the loop:

    ```python
    while True:
        button.wait_for_press()
        print("Hello")
        button.wait_for_release()
        print("Goodbye")
    ```

## Add an LED

1. Add an LED:

    ```python
    from gpiozero import Button, LED

    button = Button(21)
    led = LED(25)

    while True:
        button.wait_for_press()
        led.on()
        button.wait_for_release()
        led.off()
    ```

1. Run your code and the LED will come on when you press the button. Hold the button down to keep the LED lit.

1. Now swap the `on` and `off` lines to reverse the logic:

    ```python
    while True:
        led.on()
        button.wait_for_press()
        led.off()
        button.wait_for_release()
    ```

1. Run the code and you'll see the LED stays on until the button is pressed.

1. Now replace `led.on()` with `led.blink()`:

    ```python
    while True:
        led.blink()
        button.wait_for_press()
        led.off()
        button.wait_for_release()
    ```

## Traffic lights

1. Amend the `from gpiozero import...` line to replace `LED` with `TrafficLights`:

    ```python
    from gpiozero import Button, TrafficLights
    ```

1. Replace your `led = LED(25)` line with the following:

    ```python
    lights = TrafficLights(25, 8, 7)
    ```

1. Now amend your `while` loop to control the `TrafficLights` object:

    ```python
    while True:
        button.wait_for_press()
        lights.on()
        button.wait_for_release()
        lights.off()
    ```

1. Try the `blink` example:

    ```python
    while True:
        lights.blink()
        button.wait_for_press()
        lights.off()
        button.wait_for_release()
    ```

## Add a buzzer

Now you'll add your buzzer to make some noise.

1. Add `Buzzer` to the `from gpiozero import...` line:

    ```python
    from gpiozero import Button, TrafficLights, Buzzer
    ```

1. Add a line below your creation of `button` and `lights` to add a `Buzzer` object:

    ```python
    buzzer = Buzzer(15)
    ```

1. `Buzzer` works exactly like `LED`, so try adding a `buzzer.on()` and `buzzer.off()` into your loop:

    ```python
    while True:
        lights.on()
        buzzer.off()
        button.wait_for_press()
        lights.off()
        buzzer.on()
        button.wait_for_release()
    ```

1. `Buzzer` has a `beep()` method which works like `LED`'s `blink`. Try it out:

    ```python
    while True:
        lights.blink()
        buzzer.beep()
        button.wait_for_press()
        lights.off()
        buzzer.off()
        button.wait_for_release()
    ```

## Traffic lights sequence

As well as controlling the whole set of lights together, you can also control each LED individually. With traffic light LEDs, a button and a buzzer, you can create your own traffic lights sequence, complete with pedestrian crossing!

1. At the top of your file, below `from gpiozero import...`, add a line to import the `sleep` function:

    ```python
    from time import sleep
    ```

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
