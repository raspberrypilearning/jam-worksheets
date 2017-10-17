# Semáforo

## Variaciones

- [pi-stop Semaforo](pi-stop-traffic-lights.md) - Semáforo, usinando pi-stop
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

- Cuidado con las mayúsculas y las minúsculas en Python!
- Comprueba que los números de pines sean los correctos. 
- En caso de tener usa una placa con los identificadores de los pines:
    - Compra en http://rasp.io/portsplus/
    - Imprime desde https://github.com/splitbrain/rpibplusleaf

## Notas de traducción

Versión: 2017/09/28

Traductor:
 - [Oier Echaniz](https://github.com/oiertwo)

