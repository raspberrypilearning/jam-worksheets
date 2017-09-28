# Push Button Camera

## Variations

- [GPIO button](push-button-camera.md)
- [Sense HAT joystick](sense-hat-joystick-camera.md)

## Preparation

- When using GPIO button, wire the button to GPIO25 and GND.
- The Traffic HAT can be used without changes to the worksheet as its button is on GPIO25
- When using the Sense HAT, connect the Sense HAT to the Pi before booting up.

## Notes

- When using the Sense HAT, the joystick is used to trigger the camera.
- Be careful with capitalisation in Python!
- Try to make sure users check their code is correct before running it because they may end up getting stuck in the camera preview
- If the user gets stuck on the camera preview, there is probably an error in the code (in between start and stop preview) - this is a difficult problem to have as you can't see the error messages. Some things to try:
    - `Alt + F4` (followed by `Enter` if it doesn't close right away)
    - `Ctrl + F6`
    - Repeat the above
    - `Ctrl + Alt + T` opens a terminal - then blindly type `sudo pkill python3` (or `python` for Python 2) and `Enter`
    - If all else fails, force a reboot
- One way to avoid this issue is to use `camera.start_preview(alpha=100)` - this sets the transparency to 100/255 so you can see the error.
