# Traffic Lights controller

Create a traffic lights controller GUI (graphical user interface) using gpiozero and guizero.

## Flash the LEDs

1. Open Python 3 from the main menu. Open a new window and save it.

1. Try flashing the red LED by entering the following code into the new window:

    ```python
    from gpiozero import LED

    red = LED(22)

    red.blink()
    ```

1. Press `F5` to run your code.

1. Create a set of traffic lights and try flashing all three LEDs at different rates:

    ```python
    from gpiozero import TrafficLights

    lights = TrafficLights(22, 27, 17)

    lights.red.blink(1, 1)
    lights.amber.blink(2, 2)
    lights.green.blink(3, 3)
    ```

## Create a GUI

1. Create a GUI button to turn the red LED on:

    ```python
    from guizero import App, Text, PushButton
    from gpiozero import TrafficLights

    lights = TrafficLights(22, 27, 17)

    app = App()

    PushButton(app, command=lights.red.on, text="on")

    app.display()
    ```

1. Add a text label and a second button to turn the red LED off:

    ```python
    Text(app, "Red")
    PushButton(app, command=lights.red.on, text="on")
    PushButton(app, command=lights.red.off, text="off")
    ```

1. Give your app a name, and use the grid layout:

    ```python
    app = App("Traffic Lights controller", layout="grid")

    Text(app, "Red", grid=[0, 0])
    PushButton(app, command=red.on, text="on", grid=[1, 0])
    PushButton(app, command=red.off, text="off", grid=[2, 0])
    ```

## Challenges

1. Try adding on/off buttons for all 3 LEDs, making sure they're aligned properly in the grid

1. Try adding a blink button for each LED

1. Try adding buttons for all on / all off

1. Try writing your own function to do the traffic lights sequence

    - Use `def sequence()` and set the command to `sequence`
    - Make sure to include `from time import sleep`
