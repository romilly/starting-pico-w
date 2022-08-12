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

## Detailed preparations

There are three things you'll need to do to prepare your Pico W for use.

1. Solder headers to the Pico W if it doesn't have them already.
2. Install the software you'll be using on your computer
3. Install MicroPython on the Pico W

### Soldering the headers

As mentioned in the introduction, you'll find advice on soldering, including the hardware you need, in the
[Pimoroni Soldering Guide](https://learn.pimoroni.com/article/the-ultimate-guide-to-soldering) and the Adafruit 
[guide to soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering). 

There's also a guide that covers soldering Pico headers in [Get started with MicroPython on Raspberry Pi Pico]().

If you're new to soldering, you'll need to take extra care to check for dry joints (where the solder doesn't make a 
good electrical connection) and solder bridges (where the solder connects things where it shouldn't).

I find that a good lamp with a magnifier works really well for checking soldering before I apply any power. It seems the
model below is no longer available, but there are plenty of great alternatives; just search for _Magnifying Lamp_.

![image](http://images.rareschool.com/img/eecdeb3e-1a2e-11ed-99c1-61a7fad8dd76-mag-lamp.jpg)

## Preparing your main computer

You'll need an editor on your main computer. It's possible to use any text editor, but most Pico owners use an editor 
called `Thonny`.

Thonny has good support for MicroPython, and it works very well with the Pico and Pico W. It's 
pre-installed on the Raspberry Pi OS, but you'll need to amke sure you have a recent version of the Operating System 
installed. Bullseye is fine, but some earlier version had a version of Thonny that lacked support fo the Pico.

You'll see how to install Thonny on other operating systems below.

If you prefer to use another editor, that's fine. You'll find a discussion of the pros and cons of some popular 
editors in Appendix A, along with additional explanation of how to install and run your code on the Pico.

Whichever editor you use, I strongly recommend that you also install a program called `mpremote`. As you'll see later,
`mpremote` can simplify a lot of tasks when you're installing, developing or debugging software on your Pico.

### Installing Thonny

Thonny comes pre-installed on Raspberry Pi OS, but you may need to install it if you're using a Windows, MacOS or 
other Linux computer. You'll find installation instructions some way done the [Thonny home page](https://thonny.org/).

I'm using version 3.3.14. That or later versions work well with the Pico.

### Installing Python 3

If you want to use `mpremote` you'll also need Python 3 on your main computer. You'll find advice about installing 
Python on the [Python website](https://www.python.org/). 

### Installing mpremote

If you have a full installation of Python 3 on your computer, you can install `mpremote` using

`pip3 install mpremote`.

You'll find details of how to use `mpremote` on its
[main documentation page](https://docs. micropython.org/en/latest/reference/mpremote.html).


## Installing MicroPython

Finally, you'll need to install MicroPython on your Pico W. If you've done this before for the original Pico, the 
same process will work, but you will need to make sure you **use the correct version of MicroPython**. The version for 
the original Pico lacks the features you will need to connect to the Internet.

### Install MicroPython the standard way

You'll need to 
1. Download the [latest version](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2) of MicroPython for 
   the Pico W from the MicroPython Website. Save the `uf2` file and make a note of the location where you saved it.
2. If you've already installed a version of MicroPython, you'll need to press the _bootsel_ button on the Pico W. (The 
   _bootsel_button was featured in an earlier diagram.)
3. Plug the USB cable in to connect the Pico W to your computer
4. If you pressed it, release the _bootsel_ button. A new external drive called RP2- will appear.
5. Drag or copy the `uf2` file onto the external drive. After a few seconds the drive will disappear. Your Pico 
   W is now ready for some MicroPython programming.

### Save time when rebooting

The _bootsel_ button is small, and can be hard to reach if you have headers on top of the Pico for some reason. Also, 
it's a nuisance having to unplug and replug the USB cable.

Luckily there are two easy ways to put the Pico into bootloader mode.

The first is to use the mpremote program mentioned above.

If you run `mpremote bootloader` on the host computer it wil put your Pico into bootloader mode, allowing you to 
copy a `.uf2` file onto the storage device that appears.

The second method requires you to use a _REPL_ - a Read-Evaluate-Print_Loop session that lets you execute MicroPython 
code on your Pico. You'll see how to enter and use a REPL in the section that follows.

You've soldered the headers, installed a suitable editor, and copied MicorPython onto your Pico.

Now it's time to check that everything is working.

## Check your installation

This section assumes that you're using the Thonny editor. If you're using another editor, Appendix A explains how to 
install and run MicroPython code on your Pico.

You'll probably still have your Pico connected to your main computer with your USB cable. If not, connect them now.

Start Thonny. It should show a screen line this:

![image](http://images.rareschool.com/img/8e305be2-1a36-11ed-99c1-61a7fad8dd76-thonny-01.png)














