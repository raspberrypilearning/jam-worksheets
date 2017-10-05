# Minecraft TNT

## Entra al mundo de Minecraft 

1. Abre Minecraft Pi desde el menu principal. Comienza la partida y crea un mundo nuevo.

1. Camina por el mundo usando las teclas WASD del teclado. Usa el espacio para saltar, usalo dos veces para volar.

1. Presiona Tab para hacer aparecer el cursor del raton, y abre Python 3 desde el menu principal.

1. Mueve las ventanas hasta que puedas ver comodamente las dos ventanas abiertas.

## Controlando Minecraft con Python

1. Obre una nueva ventana de Python y añade el siguiente codigo:

    ```python
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    mc.postToChat("Hello world")
    ```

1. Ejecuta el codigo usando `F5`. Deberias de ver una mensaje que dice "Hello world" en la ventana de Minecraft.

1. Añade las siguientes lineas al codigo:

    ```python
    x, y, z = mc.player.getPos()
    mc.setBlock(x+1, y, z, 1)
    ```

1. Ejecutalo y deberia de ver un bloque de piedra aparecer alrededor tuyo. Si no esta enfrente tuyo mira a tu alrededor!

1. Cambia el numero `1` al final de la linea `setBlock` a `2`:

    ```python
    mc.setBlock(x+1, y, z, 2)
    ```

1. Ejecutalo y veras aparecer un bloque de hierba. Prueba cambiando el numero y comprueba que ocurre.


1. Cambia `setBlock` a `setBlocks` para construir un cubo de 10x10x10 en vez de un simple bloque:

    ```python
    mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 1)
    ```

     Verás aparecer un cubo enorme!

## TNT

El ID para un bloque de TNT es el `46`. Existen dos tipos de TNT: TNT no explosivo y TNT explosivo. Nosotros nos centraremos en los que explotan.

1. Crea un cubo solido de TNT. Para crear TNT explosivo tienes que añadir un `1` al final de la linea de `setBlocks`:

    ```python
    mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 46, 1)
    ```

1. Acercate al cubo de TNT y golpealo con la espada. Puedes usar la espada clickando el boton secundario del ratón. Esto activara el TNT. Observa y disfruta del espectaculo.
