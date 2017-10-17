# Auzazko argi izpiak

## Aukerak

- [Auzazko argi izpiak](sense-hat-random-sparkles.md) [Ingelesez] - Sense HAT (hardware)-arekin erabiltzeko 
- [Auzazko argi izpiak (aukera ezberdinekin)](sense-hat-random-sparkles-variations.md) - Sense HAT (hardware) - ekin erabili daiteke, edo ordenagailu zein webguneko emuladorearekin
    - [PDF version](pdf/Make-Random-Sparkles-on-the-Sense-HAT.pdf)

## Prestakuntza

- SenseHat erabili behar baduzu, konektatu zure Pi-ra
- Trinket emuladorea erabili behar baduzu, `sense.clear()` exekutatu hasi haurretik:

    ```python
    from sense_hat import SenseHat
    
    sense = SenseHat()
    
    sense.clear()
    ```

    ondoren kodea ezabatu eta hasieratik hasi zure txantiloila erabiliz.

## Oharrak

- Maiuskulak eta minuskulekin kontzu ibili Python erabiltzerakoan.
- Egiaztatu inportatu behar diren liburutegi guztiak kode hasieran inportatzen dituzula.

## Itzulpen oharrak

Bertsioa: 2017/09/28

Itzultzailea:
 - [Oier Echaniz](https://github.com/oiertwo)
