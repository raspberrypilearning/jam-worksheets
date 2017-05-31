# Traffic Lights controller

## Variations

- [Traffic Lights controller](traffic-lights-controller.md)

## Presentations

- [LibreOffice](traffic-lights-controller.odp)
- [PDF](traffic-lights-controller.pdf)

## Preparation

- Install guizero using pip:
    - `sudo pip3 install guizero`
- Place a traffic lights set (e.g. pi-stop) on the GPIO pins
- Alternatively, wire up three LEDs (red, yellow and green) to the GPIO pins using a breadboard

## Notes

- Be careful with capitalisation in Python!
- Make sure the pins used are the same as in the code
- Note that guizero is an new experimental library currently in beta - usage is likely to change as the library is developed
    - The current version of this worksheet uses guizero v0.2.1
- Refer to [GPIO Zero](http://gpiozero.readthedocs.io/) docs and [guziero docs](https://lawsie.github.io/guizero/)
