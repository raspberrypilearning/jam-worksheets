# Semaforoa

## Aukerak

- [pi-stop Semaforoa](pi-stop-traffic-lights.md) - pi-stop ekin erabiltzeko.
    - [PDF version](pdf/Controlling-a-traffic-lights-sequence-with-GPIO-Zero.pdf)
- [Traffic Lights](traffic-lights.md) [Ingelesez] - Semaforoa, botoia eta txirrina - breadborad edo pi-stop plaka batekin jarraitu daiteke tutoriala.

## Prestakunza

Pi-stop-en ariketak jarraitzeko ez duzu ezer egin behar aurretik. 

Bertsio osoan lan egin nahi baduzu breadboard baten egitura osatu beharko duzu edo Traffic Hat bat erabili beharko duzu. 

- Breadborad bat erabiltzera bazoaz konektatu konponentean ondoren azaltzen den moduan:
    - Green: GPIO22
    - Yellow: GPIO23
    - Red: GPIO24
    - Button: GPIO25
    - Buzzer: GPIO5
- Traffic Hat erabiltzera bazoaz, konektatu Raspberry Pi-ra hasi aurretik.

## Oharrak

- Kontuz ibili maiuskulekin Python erabiltzerakoan! 
- Pin zenbakiak ondo dituzula ziurtatu
- Baldin baduzu, erabili portuen etiketa adierazten duen gehigarria:
    - Erori bat http://rasp.io/portsplus/
    - Inprimatu zurea https://github.com/splitbrain/rpibplusleaf

## Itzulpen oharrak

Bertsioa: 2017/09/28

Itzultzailea:
 - [Oier Echaniz](https://github.com/oiertwo)
