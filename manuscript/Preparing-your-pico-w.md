# Preparing your Pico W

If you've met the Pico before, you'll probably know abut soldering headers and programming the Pico from your computer.

It's still worth reading the section _Save time with mpremote_. `mpremote` is useful program from the MicroPyton team 
that can simplify installation and testing of MicroPython and the code you write for it.

## Getting familiar with the Pico W

You'll need to know your way around the Pico.

When it arrives, your Pico W will probably look like this.

![image](http://images.rareschool.com/img/741dfe5e-1021-11ed-8568-a39c23c2a191-pico-in-a-packet.jpg)

Here are the front and back of the board:

![image](http://images.rareschool.com/img/19efab7c-1025-11ed-8568-a39c23c2a191-picow-front.jpg)

![image](http://images.rareschool.com/img/61b94030-1025-11ed-8568-a39c23c2a191-picow-back.jpg)

Here's an annotated image of the front.

![image](http://images.rareschool.com/img/208f1bee-1024-11ed-8568-a39c23c2a191-picow-front-annotated..png)

1. The two lines of holes at the top and bottom of the board are for power and GPIO (General Purpose I/O) 
connections. You'll need to solder header pins in those holes.
2. The connector at the side is the USB port which you'll connect to your host computer when you want to program the 
   Pico W.
3. The button marked `bootsel` is used to put the Pico in to bootsel mode. You can use that when you need to install 
   or re-install MicroPython, although you'll also learn an alternative approach.

There are three things you'll need to do to prepare your Pico W for use.

1. Solder headers to the Pico W if it doesn't have them already.
2. Install the software you'll be using on your computer
3. Install MicroPython on the Pico W

## Soldering the headers




## Installing MicroPython

TNext you'll need to install MicroPython on your Pico W. If you've done this before for the original Pico, the 
same process will work, but you will need to make sure you **use the correct version of MicroPython**. The version for 
the original Pico lacks the features you will need to connect to the Internet.

### Install MicroPython the standard way

You'll need to 
1. Download the [latest version](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2) of MicroPython for 
   the Pico W from the MicroPython Website. Save the `uf2` file and make a note of the location where you saved the 
   file.
2. Press the _bootsel_ button on the Pico W. (The _bootsel_ button was featured in the diagram above.)
3. Plug the USB cable in to connect the Pico W to your computer
4. Release the bootsel button. A new external drive called RP2-   drive will appear.
5. Drag the `uf2` file onto the external drive. It will copy over and then the drive will disappear. Your Pico W in 
   now ready for some MicroPython programming.

### Save time with mpremote







