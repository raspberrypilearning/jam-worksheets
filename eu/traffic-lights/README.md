# Traffic Lights

## Variations

- [pi-stop Traffic Lights](pi-stop-traffic-lights.md) - traffic lights only, using a pi-stop
    - [PDF version](pdf/Controlling-a-traffic-lights-sequence-with-GPIO-Zero.pdf)
- [Traffic Lights](traffic-lights.md) - traffic lights, button and buzzer - can be used with a breadboard or with the Traffic HAT

## Preparation

If following the pi-stop only worksheet, no preparation is required - just hand out pi-stops, and port labels if you have them.

If following the full version, you'll need to either wire up components on a breadboard, or use a Traffic HAT:

- If using a breadboard, wire up the components to the following pins:
    - Green: GPIO22
    - Yellow: GPIO23
    - Red: GPIO24
    - Button: GPIO25
    - Buzzer: GPIO5
- If using a Traffic HAT, place this on the Pi before starting

## Notes

- Be careful with capitalisation in Python!
- Check the correct pin numbers are used
- Use a port label if you have one available:
    - Buy one from http://rasp.io/portsplus/
    - Print your own from https://github.com/splitbrain/rpibplusleaf
