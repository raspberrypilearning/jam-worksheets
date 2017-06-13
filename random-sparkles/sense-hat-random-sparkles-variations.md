# Sense HAT Random Sparkles

For this activity, you can either use the real Sense HAT hardware, the desktop emulator in Raspbian, or the web-based emulator on Trinket.

- If you're using the Sense HAT, attach it to your Raspberry Pi before booting.
- If you're using the Trinket emulator, open a web browser and go to **trinket.io/sense-hat**

## Using set_pixel

First, we'll think up some random numbers and use the `set_pixel` function to place a random colour on a random location on the Sense HAT display.

1. If you're using a Raspberry Pi, open Python 3 and create a new file. If you're using the web emulator, delete the example code before you begin.

1. In the new file, start by importing the Sense HAT module.

    If you're using a real Sense HAT or the Trinket emulator, the import line is:

    ```python
    from sense_hat import SenseHat
    ```

    If you're using the desktop emulator, the import line is:

    ```python
    from sense_emu import SenseHat
    ```

    The rest of the code will be identical for all versions.

1. Next, create a connection to your Sense HAT by adding:

    ```python
    sense = SenseHat()
    ```

1. Now think of a random number between 0 and 7 and assign it to the variable `x`, for example:

    ```python
    x = 4
    ```

1. Think of another random number between 0 and 7, then assign it to `y`:

    ```python
    y = 5
    ```

1. Think of three random numbers between 0 and 255, then assign them to `r`, `g`, and `b`:

    ```python
    r = 19
    g = 180
    b = 230
    ```

1. Now use the `set_pixel` function to place your random colour at your random location on the display:

    ```python
    sense.set_pixel(x, y, r, g, b)
    ```

1. Now run your code by pressing **F5** (or the **Run** button in Trinket). You should see a single pixel light up.

1. Now pick some new random numbers - change them all - and run the program again. A second pixel should appear on the display!

## Using the random module

So far you've picked your own random numbers, but you can let the computer choose them instead.

1. Add another `import` line at the top of your program, below `import SenseHat`:

    ```python
    from random import randint
    ```

1. Now change your `x =` and `y =` lines to automatically select a random position:

    ```python
    x = randint(0, 7)
    y = randint(0, 7)
    ```

1. Run your program again, and you should see another random pixel being placed on the display. It will be the same colour you chose previously.

1. Now change your colour value lines to:

    ```python
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    ```

    Now your program will automatically select a random colour.

1. Run it again, and you should see another pixel appear in a random location with a random colour.

1. Run it a few more times, and you should see more of the grid fill up with random pixels.

## Add a loop

Rather than have to keep running your program, you can add a loop so that it will keep going.

1. First, add an `import` to the top of your file:

    ```python
    from time import sleep
    ```

    You'll use this to pause the program between pixels.

1. Add a `while True:` to your code so that the random lines, `set_pixel` and `sleep` are all within the loop:

    ```python
    while True:
        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        sense.set_pixel(x, y, r, g, b)
        sleep(0.1)
    ```

1. Run the code and you should see random sparkles in action!

1. Try changing the sleep time to make it even shorter.
