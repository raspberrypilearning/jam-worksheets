# Sense HAT Ausazko Argi izpiak

Ondorengo pausoak jarraitzeko Sense Hat hardwarea erabil dezaketu, edo Raspbianeko emuladorea edo webguneko emuladorea Trinket webgunean ere erabil daitezke.

- Sense Hat erabili behar baduzu konektatu Raspberry Pi-ra hau piztu aurretik.
- Trinket webguneko emuladorea erabili behar baduzu, ireki web nabigatzailea eta joan **trinket.io/sense-hat** webgunera.

## set_pixel erabiltzen

Lehenengo urrats modura, ausazko zenbakiak guk pentsatuko ditugu eta `set_pixel` funtzioa erabiliz auzasko toki batean ausazko kolorearekin argi bat piztuko dugu Sense Hat-ek duen display-ean. 

1. Raspbery Pi erabiltzen bazabiltza, ireki Python 3 eta sortu fitxategi berri bat. Webgunean bazaude ezabatu adibideko kodea hasi aurretik. 

1. Fitxategi berrian SenseHat moduloa inportatu.

    Sense HAT edo Trinket emuladorea erabiltzen bazaude, inportatzeko erabiliko dugun lerroa ondorengoa da:

    ```python
    from sense_hat import SenseHat
    ```

    Aldiz, Raspbian-en dagoen emuladorea bada, inportatzeko erabiliko dugun lerroa ondorengoa izango da:

    ```python
    from sense_emu import SenseHat
    ```

    Hemendik aurrerako kodea bi aukeretarako berdina izango da.

1. Ondoren, SenseHat-arekin konektatu  ondorengo lerroa gehituz:

    ```python
    sense = SenseHat()
    ```

1. Pentsatu 0 eta 7 arteko ausazko zenbaki baten eta `x` aldagaiari esleitu, adibidez:

    ```python
    x = 4
    ```

1. Pentsatu beste 0 eta 7 arteko ausazko zenbaki baten eta `y` aldagaiari esleitu:

    ```python
    y = 5
    ```

1. 0 eta 255 arteko hiru ausazko zenbakietan pentsatu, esleitu zenbakiak `r`, `g`, eta `b` aldagaileri:

    ```python
    r = 19
    g = 180
    b = 230
    ```

1. Orain erabili `set_pixel` funtzioa auzazko lekuan ausazko kolorea duen argia pizteko:

    ```python
    sense.set_pixel(x, y, r, g, b)
    ```

1. Exekutatu kodea **F5** saktuz (**Run** botoia Trinket webgunean). Pixel bat piztuta ikusi beharko zenuke.

1. Aukeratu beste ausazko zenbaki batzuk - aldatu zenbaki guztiak - eta exekutatu programa berriz. Beste pixel bat piztu da!

## Auza sortzeko moduloa erabiltzen (Random)

Orain arte ausazko zenbakiak sortu dituzu, baina ordenagailuari lan hau egiteko agindua eman ahal zaio. 

1. Gehitu ausazko moduloaren (random) `import` lerroa programaren hasieran, justu `import SenseHat`lerroaren jarraian :

    ```python
    from random import randint
    ```

1. Aldatu `x =` and `y =` aldagaiak automatikoki sortzeko:

    ```python
    x = randint(0, 7)
    y = randint(0, 7)
    ```

1. Exekutatu programa berriz ere, beste pixel bat piztuta agertuko zaizu orain. Seguruenez aurreko pixelaren kolore bera izango du, ez baitugu aldatu.

1. Koloreen aldagaiak aldatu:

    ```python
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    ```

    Orain programak sortuko ditu ausazko zenbakiak kolorea ezberdinak aukeratuz.

1. Exekutatu programa berriz ere, beste pixel bat agertuko da ausazko kolore batekin.

1. Exekutato kodea nahi beste aldiz, pantaila kolore ezberdinez betetzen joango dela ikusiko duzu.

## Buklea gehitzen

Programa behin eta berriz exekutatu beharrean buklea erabili dezakegu gure lana automatikoki egiteko.


1. Lehenengo, gehitu `import` tlerro bat programaren hasieran:

    ```python
    from time import sleep
    ```

    funtzio hau pixel-en artean etenaldi bat sortzeko erabiliko dugu.

1. Gehitu `while True:` buklea programari, `set_pixel` eta `sleep` buklearen barrualdean daudela ikus dezakezu:

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

1. Exekutatu programa eta argi izpiak ikusiko dituzu!

1. Saiatu `sleep`funtzioko denbora aldatzen argi izpien arteko denbora motzagoa izateko.
