# Should you read this ebook?

If you're familiar with Python  and you want to start using the new Raspberry Pi Pico W, this guide is for you.

It's a short, free ebook in PDF format. Feel free to give a copy top your friends.

## Getting started

### What you need to know

It assumes that you're familiar with the Python language.

It doesn't assume familiarity with electronics or the original Raspberry Pi Pico.

To use the guide you'll need a computer running Windows, Linux (including Raspberry Pi/OS) or Mac/OS.
You'll also need a Raspberry Pi Pico W and a USB cable to connect the two.

You'll need an editor on you computer, and you'll need to have Python installed.
You can use any editor, but most people staring with the Pico use the free Thonny editor.
You'll find more detailed advice about choosing, installing and using editors in Appendix A.

TODO: Add appendix

### What you'll learn

You'll learn how to
* Write and run MicroPython programs on the Pico W
* Connect your Pico W to the Internet
* Control a LED via a web page
* Install MicroPython Packages using `upip`
* Build a simple weather station and connect it to the Internet using MQTT

### Hardware you'll need

If you want to try the mini-weather station project, you'll need a few extra 
electronic components, detailed below. I've added a table with links to the products on Pimoroni and Adafruit, but 
of course you can buy them from the vendor of your choice. They are all widely available.

At the time of writing, you will have to do a little soldering for the weather station project. You'll need to 
solder headers onto the Pico so that you can plug it into a breadboard. A version of the Pico W with headers has been 
announced, but it's not yet available. 

You'll find a [guide to soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering) 
on the Adafruit website and a guide to soldering headers in
_Get started with MicroPython on Raspberry Pi Pico_.

So you'll need
Headers for the Pico
A breadboard
Jump wires to connect stuff up
A TMP36 thermometer sensor
A Photosensor (there are several possibilities)
A 10K Ohm Resistor.
Access to a soldering iron, and some solder.

### The breadboard

The weather station project is very simple, You can use any size of breadboard, including the very compact and 
inexpensive 170-point versions.

![image](http://images.rareschool.com/img/2568161e-0a9a-11ed-93be-0b3de4b72aa8-bb170.png)

If you're planning to use the Pico or Pico W a lot, I recommend the monkmakes Pico 
BB as it has a guide to the Pico pin functions on the board - a great time-saver!

![image](http://images.rareschool.com/img/4da9380a-0a9b-11ed-93be-0b3de4b72aa8-monk-pico-bb.jpg)


### Jump wires

You'll find offers of inexpensive jump wires all over the internet, and I use them, but they can be a bt unreliable. 
That's the last thing you want when you're starting out, so I suggest you get jump wires like these:

![image](http://images.rareschool.com/img/02e659f0-0a9c-11ed-93be-0b3de4b72aa8-jumpers-m2m.png)

Make sure they are male-to-male wires as that's what you'll need for the breadboard.

### The TMP36 sensor

This is an inexpensive analogue temperature sensor which is really easy to use. Details in Chapter 5.



### An LDR

You can use an [LDR]() (Light dependent resistor) to measure light levels, The weather station uses is to measure 
sunlight.

### The 10K resistor

You'll connect this to the LDR to act as a [voltage divider](). (More about that in chapter 5).

You won't be able to buy a single resistor, but they don't cost much and spares will be useful. If you 
thiok you're going to get bitten by the Pico bug, you might consider getting a resistor kit which will keep you 
going for quite a while,

### Soldering Kit

You'll find advice on the soldering hardware you need in the 

This is a work in progress. I'll post about updates on the website, in [my blog](https://blog.rareschool.com/)
and as [@RAREblog](https://twitter.com/rareblog) on Twitter.

