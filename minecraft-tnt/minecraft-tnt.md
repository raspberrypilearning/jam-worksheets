# Minecraft TNT

## Enter the Minecraft world

1. Open Minecraft Pi from the main menu. Start a game and create a new world.

1. Walk around using the WSAD keys on the keyboard. Use space to jump, and double tap space to fly.

1. Press Tab and the keyboard to release your mouse cursor, and open Python 3 from the main menu.

1. Move your windows around so Minecraft and Python are side-by-side.

## Controlling Minecraft with Python

1. Open a new Python window and enter the following code:

    ```python
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    mc.postToChat("Hello world")
    ```

1. Run the code with `F5` and you should see the message "Hello world" appear in the Minecraft window.

1. Add the following lines to your code:

    ```python
    x, y, z = mc.player.getPos()
    mc.setBlock(x+1, y, z, 1)
    ```

1. Run the code and you should see a block of stone appear near your player. If it's not in front of you, try looking around.

1. Change the `setBlock` line from a `1` to a `2`:

    ```python
    mc.setBlock(x+1, y, z, 2)
    ```

1. You should now see a block of grass appear. Try changing the number again and see which block gets placed.

1. Try changing `setBlock` to `setBlocks` to build a 10x10x10 cube rather than a single block:

    ```python
    mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 1)
    ```

     You should see a large solid cube of stone appear!

## TNT

The block ID for TNT is `46`. There are two types of TNT: unexplosive TNt and explosive TNT. You want explosive TNT.

1. Build a solid cube of TNt. To get explosive TNT, you need to add a `1` to the end of your `setBlocks` line:

    ```python
    mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 46, 1)
    ```

1. Go up to the cube of TNT and hit it with your sword using right-click. This will activate the TNT. Stand back and watch the show!
