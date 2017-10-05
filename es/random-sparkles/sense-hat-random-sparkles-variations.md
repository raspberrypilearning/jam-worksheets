# Sense HAT Destellos aleatorios

Para esta actividad puedes usar tanto un hardware Sense Hat, el emulador de escritorio de Raspban incluso el emulador web alojado en Trinket.

- Si vas a usar la Sense HAT, conectalo a la Raspberry Pi antes de encenderla. 
- Si vas a usar el emulador de Trinket, abre un navegador web y entra a la web **trinket.io/sense-hat**

## Usando set_pixel

Para empezar vamos a pensar en numeros aleatorios para usar en la función `set_pixel`. Con estos números pondremos colores aleatorios en lugares aleatorios del display de la Sense HAT.

1. Si estas usando una Raspberry Pi, abre Python 3 y crea un nuevo fichero. Si estas usando el emulador de la web borra todo el codigo antes de empezar.

1. En el nuevo fichero, comienza importando el modulo de Sense Hat. 

    Si estas usando un hardware Sense HAT o el emulador de Trinket, la manera de importar es de esta manera:
    ```python
    from sense_hat import SenseHat
    ```

    Si estas usando el emulador de escritorio, la linea para importar es esta:

    ```python
    from sense_emu import SenseHat
    ```

    El resto del codigo para ambas versiones sera identico.
    
1. Acto seguido, crea una conexion a la Sense HAT añadiendo:

    ```python
    sense = SenseHat()
    ```

1. Ahora piensa en un numero aleatorio entre 0 y 7 y asignale al variable `x`, por ejemplo: 

    ```python
    x = 4
    ```

1. Piensa en otro numero entre 0 y 7, asignaselo a `y`:

    ```python
    y = 5
    ```

1. Piensa en tres numeros entre 0 y 255, asignaselos a `r`, `g` y `b`:

    ```python
    r = 19
    g = 180
    b = 230
    ```

1. Ahora usa la funcion `set_pixel` para colocar en la pantalla un color aleatorio en un lugar aleatorio:

    ```python
    sense.set_pixel(x, y, r, g, b)
    ```

1. Ejecuta el código presionando **F5** (el botón **Run** en Trinket). Deberias de ver encenderse un pixel.

1. Ahora selecciona nuevos numeros aleatorios - cambialos todos - y ejecuta el programa otra vez. Un segundo pixel deberia de aparecer en la pantalla! 

## Usando el modulo aleatorio (random)

Hasta ahora hemos seleccionado nuestros numeros aleatorios, pero puedes dejar que el ordenador seleccione estos numeros por ti.

1. Añade una nueva linea de `import` al principio del programa, justo despues de `import SenseHat`:

    ```python
    from random import randint
    ```

1. Ahora cambia las lineas de `x =` y `y =` para que automaticamente seleccionen un lugar aleatorio:

    ```python
    x = randint(0, 7)
    y = randint(0, 7)
    ```

1. Ejecuta el programa otra vez, deberia de aparecer otro pixel iluminado en la pantalla. Deberia de ser del mismo color que el ultimo pixel.

1. Cambia los valores de los colores a los siguientes:

    ```python
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    ```

    Ahora tu programa seleccionara un color aleatorio.

1. Ejecuta otra vez,vers aparecer otro pixel en un lugar aleatorio con un color aleatorio. 

1. ejecuta el programa varias veces ms, la pantalla se ira llenando de más pixeles iluminados de diferentes colores.

## Añade un bucle

En vez de ejecutar el programa manualmente podemos añadir un bucle para que ejecute repetidamente.

1. Primero, vamos a añadir una nueva linea de `import` al principio del código:

    ```python
    from time import sleep
    ```

    Usaremos esto para pausar el programa entre los pixeles. 
    
1. Añade un `while True:` al codigo, de manera que las asignaciones aleatorias, `set_pixel` y `sleep` queden dentro del bucle:

    ```python
    while True:
        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        sense.set_pixel(x, y, r, g, b)
        sleep(0.1)
    ```

1. Ejecuta el codigo y veras destellos aleatorios en acción!

1. Prueba a cambiar el tiempo de pausa (sleep) para que los destellos ses ms rápidos.
