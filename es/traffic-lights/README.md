# Semáforo

## Variaciones

- [pi-stop Traffic Lights](pi-stop-traffic-lights.md) - Semáforo, usinando pi-stop
    - [PDF version](pdf/Controlling-a-traffic-lights-sequence-with-GPIO-Zero.pdf)
- [Traffic Lights](traffic-lights.md) [Inglés]- traffic lights, button and buzzer - can be used with a breadboard or with the Traffic HAT

## Preparativos

Si vas a usar las hojas de trabajo de pi-stop, no hacen falta preparativos - simplemente repartir pi-stops, y repartir las chapas con las etiquetas de los pines, en caso de tenerlas.

Si vas a usa las hojas de trabajo completas, necesitaras conectar los diferentes componentes con una breadboard o usar la placa TrafficHat:

- Si usas una breadboard, conecta los componentes de la siguiente manera:
    - Verde: GPIO22
    - Amarillo: GPIO23
    - Rojo: GPIO24
    - Botton: GPIO25
    - Buzzer (Sonido): GPIO5
- Si vas a usar Traffic HAT, conectalo a la Pi antes de encenderlo.

## Notas

- Cuidado con las mayusculas y las minusculas en Python!
- Comprueba que los numeros de pines sean los correctos. 
- Use a port label if you have one available:
    - Buy one from http://rasp.io/portsplus/
    - Print your own from https://github.com/splitbrain/rpibplusleaf

## Notas de traduccion

Version: 2017/09/28

Traductor:
 - [Oier Echaniz](https://github.com/oiertwo)

