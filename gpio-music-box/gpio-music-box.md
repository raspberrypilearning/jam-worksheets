# GPIO Music Box

Wire up a series of buttons that play particular sounds when pressed.

## Playing sounds with Python

1. Open Python 3 (IDLE) from the main menu.

1. Click **File > New File**.

1. Write the following code to play a drum sound:

    ```python
    import pygame.mixer
    from pygame.mixer import Sound

    pygame.mixer.init()

    drum = Sound("samples/drum_tom_mid_hard.wav")

    drum.play()
    ```

1. Save the file with `Ctrl + S` and run with `F5`.

    It should play the drum sound. Run it again to repeat.

## Connect first button to sound file

1. Return to the code window and add another two lines to the top section of imports:

    ```python
    import pygame.mixer
    from pygame.mixer import Sound
    from gpiozero import Button

    pygame.mixer.init()

    button = Button(2)
    drum = Sound("samples/drum_tom_mid_hard.wav")

    button.when_pressed = drum.play
    ```

1. Run the program again, then press the button and you should hear the drum sound played. Each time you press the button it should play the sound.

## Add a second button

1. Replace the last two lines with a dictionary of buttons and sounds:

    ```python
    button_sounds = {
        Button(2): Sound("samples/drum_tom_mid_hard.wav"),
        Button(3): Sound("samples/drum_cymbal_open.wav"),
    }

    for button, sound in button_sounds.items():
        button.when_pressed = sound.play
    ```

1. Now run the program again and try pressing each button. Each button should play its own sound.
