# Random sparkles

## Variations

- [Random sparkles](sense-hat-random-sparkles.md) - uses the Sense HAT (hardware)
- [Random sparkles (variations)](sense-hat-random-sparkles-variations.md) - can be used with Sense HAT (hardware), or the desktop or web-based emulator
    - [PDF version](pdf/Make-Random-Sparkles-on-the-Sense-HAT.pdf)

## Preparation

- If using the Sense HAT, connect it to the Pi before booting up.
- If using the Trinket emulator, run `sense.clear()` before starting:

    ```python
    from sense_hat import SenseHat
    
    sense = SenseHat()
    
    sense.clear()
    ```

    then delete the code and let the user start from scratch.

## Notes

- Be careful with capitalisation in Python!
- Make sure all required modules are imported at the top of the file at each stage.
