# Traffic Lights with Python

## Connect the LEDs

1. Connect your LEDs to the following pins:

| LED       | GPIO pin |
| --------- | :------: |
| Red       | 22       |
| Amber     | 27       |
| Green     | 17       |

## Control the LEDs

1. Open Python 3 from the main menu, and open a new file.

1. Enter the following code:

    ```python
    from gpiozero import LED

    red = LED(22)

    red.blink()
    ```

1. Now save your program and press **F5** to run your code. You should see the red light flash on and off continuously.

1. Now modify your code to introduce the other two lights, and make them blink at different speeds:

    ```python
    from gpiozero import LED

    red = LED(22)
    amber = LED(27)
    green = LED(17)

    red.blink(1, 1)
    amber.blink(2, 2)
    green.blink(3, 3)
    ```

1. Run your code again and you should see the three lights flashing at different rates.

1. If a larger number makes a light blink slower, what number would make it run faster? Try to make your lights blink faster.

## Traffic lights sequence

1. The `on` function allows you to turn a light on. You can use `sleep` to pause between commands. Try this example to turn the lights on in sequence:

    ```python
    from gpiozero import LED
    from time import sleep

    red = LED(22)
    amber = LED(27)
    green = LED(17)

    red.on()
    sleep(1)
    amber.on()
    sleep(1)
    green.on()
    sleep(1)
    ```

    The main controls for LEDs are `on`, `off`, `toggle` and `blink`.

1. Try turning the lights on and off in sequence:

    ```python
    red.on()
    sleep(1)
    amber.on()
    sleep(1)
    green.on()
    sleep(1)
    red.off()
    sleep(1)
    amber.off()
    sleep(1)
    green.off()
    ```

1. Try repeating this by putting the code inside a `while` loop:

    ```python
    while True:
        red.on()
        sleep(1)
        amber.on()
        sleep(1)
        green.on()
        sleep(1)
        red.off()
        sleep(1)
        amber.off()
        sleep(1)
        green.off()
    ```

1. Now you know how to control the lights individually, and time the pauses between commands, can you create a traffic lights sequence? The sequence goes:

    - Green on
    - Amber on
    - Red on
    - Red and amber on
    - Green on

It's important to think about timing. How long should the lights stay on for at each stage?

Once you have completed the traffic lights sequence, you might want to try adding in a button and a buzzer to make an interactive version.
