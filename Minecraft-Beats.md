# Minecraft Beats

## Enter the Minecraft world

1. Open Minecraft Pi from the main menu. Start a game and create a new world.

1. Walk around using the WSAD keys on the keyboard. Use space to jump, and double tap space to fly.

1. Press Tab and the keyboard to release your mouse cursor, and open Sonic Pi from the main menu.

1. Move your windows around so Minecraft and Sonic Pi are side-by-side.

## Giving Steve a beat

Here's nice simple exmaple of how Sonic Pi can be used to combine music with game play. You're going to pick up the player by half a block and play a drum beat at the same time, thiswill make the world appear to be bouncing to Steve's drum beats.

1. First get a rhythm going using an infinite loop:

    ```ruby
    loop do
        sample :drum_heavy_kick
        sleep 0.5
    end
    ```
    When you click **Run** or press `Alt + R` your composition should play and you should hear a regular drum beat.

1. Next lets find out the player's location (as an x, y, z coordinate) before setting a new loaction which is the same x and z positions but at y + 0.5, this will pick Steve up and allow him to fall in time to the beat.

    ```ruby
    loop do
        sample :drum_heavy_kick
        x, y, z = mc_location
        mc_set_pos x, y+0.5, z
        sleep 0.5
    end
    ```

    Now when you play your code, Steve will be able to move around the world, accomopanied by his own beat!

## Creating a teleport effect
Next you'll create a simple teleport action with an appropriate sound effect. First open a new **buffer** in the bottom part of the Sonic Pi window.

1. First lets warn the player and add play a suitable sound effect.

    ``` ruby
    mc_message "Preparing to teleport...."
    sample :ambi_lunar_land, rate: -1
    ```

    When you press **Run** you should hear a weird teleporting sound effect.

2. You can then add a series of messages and pauses to create a countdown to teleportation.

    ``` ruby
    mc_message "Preparing to teleport...."
    sample :ambi_lunar_land, rate: -1

    sleep 1
    mc_message "3"
    sleep 1
    mc_message "2"
    sleep 1
    mc_message "1"
    sleep 1
    mc_teleport 90, 20, 10
    mc_message "Whoooosh!"
   ```

Run your code and you hear a creepy teleportation sound before being transported across the worl. Experiment with other sound files and different teleport locations.

## Minecraft Dance Floor
Finally for your most advanced project you're going to create dance floor for the mincraft player with a simple randomised tune.

1. Start a new **buffer** and enter the following 3 lines:

    ```ruby
    x, y, z = mc_location
    mc_set_area :glass, x, y-1, z, x+4, y-1, z+4
    notes = (scale :e3, major_pentatonic, num_octaves: 3).shuffle
   ```

    The first 2 lines find the current location of the player and build a 5x5 glass "dance floor" beneath them. The 3rd line sets up a randomised scale of notes and calls it "notes" which will be used to form the tune.

1. The next step is to add a loop to create the dance floor
   
    ```ruby
    loop do
    b = (ring :melow, :brick, :glass, :tnt, :lapis).tick
    mc_set_block b, x+rand_i(5), y-1, z+rand_i(5)
    end
    ```

    The code creates a ring of block types which it cycles through each pass through the loop. It places each new block in a random location inside the 5x5 grid.

1. Next we need a tune, so lets add 2 lines to cycle through our scale of notes and pauses briefly after each one.

    ```ruby
    loop do
    b = (ring :melow, :brick, :glass, :tnt, :lapis).tick
    mc_set_block b, x+rand_i(5), y-1, z+rand_i(5)
    
    play note: notes.tick
    sleep 0.125

    end
    ```

    Your should now have randomly flashing dance floor with random notes playing in the background. Once that works you could experiment with changing the notes and the blocks used, you could alter the timings or even incorporate the dance mat into a more complicated piece.




