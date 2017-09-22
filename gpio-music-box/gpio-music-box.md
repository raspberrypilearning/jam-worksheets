# GPIO music box

Wire up a series of buttons that play particular sounds when pressed.

## Playing sounds with Python

1. Open Python 3 from the main menu and open a new file.

1. Write the following code to play a drum sound:

    ```python
    import pygame.mixer
    from pygame.mixer import Sound

    pygame.mixer.init()

    drum = Sound("sounds/drum_tom_mid_hard.wav")

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
    drum = Sound("sounds/drum_tom_mid_hard.wav")

    button.when_pressed = drum.play
    ```

1. Run the program again, then press the button. You should hear the drum sound. Each time you press the button it should play the sound.

## Add a second button

1. Replace the last line with a dictionary of two buttons and sounds:

    ```python
    button_sounds = {
        Button(2): Sound("sounds/drum_tom_mid_hard.wav"),
        Button(3): Sound("sounds/drum_cymbal_open.wav"),
    }
    ```

1. Now add a loop to make each button press make a sound:

    ```
    for button, sound in button_sounds.items():
        button.when_pressed = sound.play
    ```

1. Now run the program again and try pressing the buttons. Each button should play its own sound.

You can try adding more buttons and more sounds. Wire up more buttons like the others, add buttons and sounds to the dictionary, and look in the `sounds` folder for more sounds.
