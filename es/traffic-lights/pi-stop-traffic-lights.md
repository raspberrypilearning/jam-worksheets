# Semáforo

## Conectar la pi-stop

1. Coge la pi-stop y colócalo en los pines GPIO de la Raspberry Pi como se muestra a continuación: 

| pi-stop   | GPIO pin |
| --------- | :------: |
| Rojo (Red)       | 22       |
| Naranja (Amber)     | 27       |
| Verde (Green)     | 17       |
| Tierra (Ground)    | GND      |

![](images/pi-stop.png)

## Control de los LEDs

1. Abre Python 3 desde el menú principal y abre un nuevo fichero.

1. Añade este código:

    ```python
    from gpiozero import LED

    red = LED(22)

    red.blink()
    ```

1. Guarda el programa y presiona **F5** para ejecutar tu código. La luz roja parpadeara constantemente.


1. Ahora modifica el código para añadir las otras dos luces, las haremos parpadear a diferentes velocidades:


    ```python
    from gpiozero import LED

    red = LED(22)
    amber = LED(27)
    green = LED(17)

    red.blink(1, 1)
    amber.blink(2, 2)
    green.blink(3, 3)
    ```

1. Ejecuta el código otra vez y observa parpadear las tres luces a diferentes velocidades.

1. Si un numero ms grande hace parpadear ms despacio, ¿que numero deberiamos de usar para un parpadeo más rápido? Intenta que alguna luz parpadee más rápido.

## La secuencia del semáforo

1. La función `on` te permite encender la luz. Puedes usar la funcion `sleep` para crear una pausa entre diferentes comandos. Prueba este código para encender las luces de manera secuencial:

    ```python
    from gpiozero import LED
    from time import sleep

    red = LED(22)
    amber = LED(27)
    green = LED(17)

    red.on()
    sleep(1)
    amber.on()
    sleep(1)
    green.on()
    sleep(1)
    ```

    Los controles más importantes para los LEDs son `on`, `off`, `toggle` y `blink`.

1. Prueba a encender y apagar las luces en una secuencia:

    ```python
    red.on()
    sleep(1)
    amber.on()
    sleep(1)
    green.on()
    sleep(1)
    red.off()
    sleep(1)
    amber.off()
    sleep(1)
    green.off()
    ```

1. Prueba a repetir la secuencia anterior usando un bucle de tipo `while`:

    ```python
    while True:
        red.on()
        sleep(1)
        amber.on()
        sleep(1)
        green.on()
        sleep(1)
        red.off()
        sleep(1)
        amber.off()
        sleep(1)
        green.off()
    ```

1. Ahora que sabes controlar las luces de manera individual, sabes crear pausas entre comandos, podrías crear una secuencia real de semáforo? La secuencia real es:

    - Luz verde
    - Luz naranja
    - Luz roja
    - Luz verde

Es importante pensar en el tiempo. Cuanto tiempo debería de estar encendido cada luz?

Una vez que ya has creado la secuencia real de semáforo, puedes probar en añadir un botón y un timbre (Buzzer) para hacer una versión interactiva.
