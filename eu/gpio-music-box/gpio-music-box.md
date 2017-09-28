# GPIO Music Box

Wire up a series of buttons that play particular sounds when pressed.

## Pythonen soinuak sortzen

1. Ireki Python 3 (IDLE) aplikazioa menu nagusitik.

1. Egin klik **fitxategia > Fitxategi berria** Ingelesez: **File > New File**.

1. Idatzi ondorengo kodea danbor zarata entzuteko:

    ```python
    import pygame.mixer
    from pygame.mixer import Sound

    pygame.mixer.init()

    drum = Sound("samples/drum_tom_mid_hard.wav")

    drum.play()
    ```

1. Gorde fichategia `Ctrl + S` sakatuz eta exekutatu `F5` sakatuz.

    Danbor zarata entzun beharko zenuke. Errepikatu ondo dabilela ikusteko.

## Soinuak eta botoiak konektatzen

1. Itzuli kodea dagoen lehiora eta gehitu ondorengo lerroak:

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
