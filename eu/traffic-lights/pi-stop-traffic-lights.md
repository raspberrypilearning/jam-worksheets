# Semaforoa

## Konektatu pi-stop

1. Pi-stop hartu eta zuzenean konektatu Raspberry Pi-aren GPIO pinetara, pinak ondoren agertzen diren moduan egon beharko dira:

| pi-stop   | GPIO pin |
| --------- | :------: |
| Gorria (Red)       | 22       |
| Laranja (Amber)     | 27       |
| Berdea (Green)     | 17       |
| Lurra (Ground)    | GND      |

![](images/pi-stop.png)

## LEDak kontrolatzen

1. Ireki Python 3 menu nagusitik eta bertan ireki fitxategi berri bar.

1. Ondorengo kodea idatzi:

    ```python
    from gpiozero import LED

    red = LED(22)

    red.blink()
    ```

1. Gorde programa eta sakatu **F5** kodea exekutatzeko. Argi gorria pizten eta itzaltzen ikusi beharko litzateke orain. 

1. Orain aurreko kodea aldatuko dugu beste bi argiak gehitzeko eta 


    ```python
    from gpiozero import LED

    red = LED(22)
    amber = LED(27)
    green = LED(17)

    red.blink(1, 1)
    amber.blink(2, 2)
    green.blink(3, 3)
    ```

1. Exekutatu kodea berriz ere eta orain hiru argiak ikusi beharko dituzu pizten eta itzaltzen, bakoitza abiadura ezberdinarekin.

1. Zenbaki handiago batek argiak polikiago pizten eta itzaltzen badire, zer eragingo du hauek azkarrago aldatzea? Saiatu argiak azkarrago pizten eta itzaltzen.

## Semaforoaren ordena jarraitzen

1. `on` funtzioak argi bat pizten du. `sleep` funtzioak komandoen artean etenaldi bat sortzen du. Saiatu zaitez ondorengo adibidea erabiliz semaforoaren argiak ordenean pizten.

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

    LED argientzako erabiltzen diren funtzio nagusiak `on`, `off`, `toggle` eta `blink` dira.

1. Saiatu zaitez argiak piztu eta itzaltzen ordena mantenduz:

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

1. `while` bukle baten barruan jarriz aurrekoa kodea automatikoki errepikatu:

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

1. Argiak banan banan erabiltzen dakizu, baita komando lerroen artean etenaldiak sortzen, bururatzen zaizu nola programatu semaforoetan agertzen den ordena? Gogoratu ordena:

    - Berdea piztu
    - Laranja piztu
    - Gorria piztu
    - Berdea piztu

Denboraz gogoratu. Zenbat denbora egon behar da argi bakoitza piztuta?

Semaforoen ordena programatzen bukatu duzunean, soinua eta pultsadorea gehitu ahal dituzu semaforo elkarreragile bat izateko.
