# Minecraft TNT

## Minecraft mundua ezagutzen

1. Ireki Minecraft Pi menu nagusitik. Hasi joko berri bat eta sordu mundu berri bat (new world).

1. Munduan zear ibiltzeko erabili WASD teklak teklatuan. Erabili hutsunea behin salto egiteko, bi aldiz hegan egiteko.

1. Sakatu Tab teklatuan xaguaren kursorea ikusteko eta ireki Python 3 menu nagusitik.

1. Mugitu leihoak minecraft eta Python-en lehioak osorik ikusi ahal dituzun arte. 

## Python Minecraft kontrolatzeko erabiltzen

1. Ireki Python leiho berri bat eta idatzi ondorengoa:

    ```python
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    mc.postToChat("Hello world")
    ```

1. Exekutatu kodea `F5` tekla sakatuz eta ondorioz Minecarft leihoan "Hello world" dioen mezu bat agertu dela ikusi beharko duzu. 

1. Gehitu ondorengo lerroak zure aurreko kodeari:

    ```python
    x, y, z = mc.player.getPos()
    mc.setBlock(x+1, y, z, 1)
    ```

1. Exekutatu kodea eta zure pertsonaiaren inguruan harrizko bloke bat azaldu dela ikusi beharko duzu. Zure ondoan ez badago saiatu zure ingurunean begiratzen. 

1. Aldatu `setBlock`-ean agertzen den `1` zenbakia `2` zenbakiarekin:

    ```python
    mc.setBlock(x+1, y, z, 2)
    ```

1. Orain belar bloke bat ikusi beharko zenduke zure inguruan. Saiatu berriz zenbakia aldatzen eta ikusi zein motatako blokea sortzen den.

1. Saiatu `setBlock` jarri beharrean `setBlocks` jartzen 10x10x10 tamainako egitura bat sortzeko, bloke bakarra izan beharrean:

    ```python
    mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 1)
    ```

     Bloke anddiago bat ikusi beharko zenuke orain!

## TNT

TNT-ak duen identifikazio zenbakia '46' da. Bi TNT mota daude: ez leherkorrak eta leherkorrak. Guk leherkorrak erabiliko ditugu.

1. sortu TNT bloke bat. TNT leherkorra izateko `1` zenbakia gehitu behar zaio `setBlocks` lerroari:

    ```python
    mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 46, 1)
    ```

1. Joan TNT blokea sortu den lekura eta xaguaren eskuineko btaia erabiliz jo zure espatarekin blkea. Honek blokea aktibatuko du. Itxaron eta gozatu ikuskizunaz.
