# GPIO Music Box

## Variations

- [GPIO Music Box](gpio-music-box.md)

## What you will need

- breadboard
- 2 x buttons
- 3 (or more) x male-to-female jumper wires
- 2 (or more) x male-to-male jumper wires
- speakers, headphones or HDMI monitor

## Preparation

- Download sound files and extract:
    ```
    wget http://rpf.io/sounds -O sounds.zip
    unzip sounds.zip
    ```
- Wire up two buttons to GPIO2 and GPIO3 ([wiring diagram](images/gpio-connect-buttons.png))
- Make sure audio is correctly [configured](https://www.raspberrypi.org/documentation/configuration/audio-config.md) to headphones or HDMI.

## Notes

- Be careful with capitalisation in Python!
