# Should you read this ebook?

If you're familiar with Python  and you want to start using the new Raspberry Pi Pico W, this guide is for you.

It's a short, free ebook in PDF format. Feel free to give a copy to your friends.

## Getting started

### What you need to know

It assumes that you're familiar with the Python language.

It doesn't assume familiarity with electronics or the original Raspberry Pi Pico.

To use the guide you'll need a computer running Windows, Linux (including Raspberry Pi/OS) or Mac/OS.
You'll also need a Raspberry Pi Pico W and a USB cable to connect the two.

You'll need an editor on you computer, and you'll need to have Python installed.
You can use any editor, but most people staring with the Pico use the free Thonny editor.
You'll find more detailed advice about choosing, installing and using editors in Appendix A.

TODO: Add appendices A, B

### What you'll learn

You'll learn how to
* Write and run MicroPython programs on the Pico W
* Connect your Pico W to the Internet
* Install extra MicroPython Packages using `upip`
* Control a LED via a web page
* Build a Raspberry Pi Stock detector that tells you when Raspberry Pis are in stock near you.
* Build a webserver on the Pico that will allow you to buzz a remote buzzer.
  * Great for summoning family members for meals, chores or interesting TV programs
* Build a simple weather station and connect it to the Internet of Things using MQTT

## Using this guide

Several of the sections of this guide will point you to some excellent instructions on the Raspberry Pi and Adafruit websites, so you will need an internet connection when you read the guide.

You may already know how to do some things covered in the guide. Here's a flowchart that will show you which parts you need to read based on your previous experience.

![image](http://images.rareschool.com/img/1b40a8f8-101d-11ed-8568-a39c23c2a191-flowchart.png)


### Hardware you'll need

You'll need a few extra electronic components, detailed below.
I'll add a table with links to vendors that supply the parts, but 

1. stock changes daily, so you'll need to check availability and 
2. you may have to order from more than one vendor, which will increase postage costs.

At the time of writing, you will have to do a little soldering. You'll need to 
solder headers onto the Pico so that you can plug it into a breadboard.
A version of the Pico W with headers has been announced, but it's not yet available.

You'll find a [guide to soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering) 
on the Adafruit website and a guide to soldering headers in
_Get started with MicroPython on Raspberry Pi Pico_.

So you'll need
Headers for the Pico
A breadboard
Jump wires to connect stuff up
A TMP36 thermometer sensor
A Photo-transistor 
A buzzer
Access to a soldering iron, and some solder.

### The breadboard

You can build the projects on a half-size breadboard.

I recommend the monkmakes Pico BB as it has a guide to the Pico pin functions on the board.
It's a great time-saver!

![image](http://images.rareschool.com/img/4da9380a-0a9b-11ed-93be-0b3de4b72aa8-monk-pico-bb.jpg)


### Jump wires

You'll find offers of inexpensive jump wires all over the internet, and I use them, but they can be a bt unreliable. 
That's the last thing you want when you're starting out, so I suggest you get jump wires like these:

![image](http://images.rareschool.com/img/02e659f0-0a9c-11ed-93be-0b3de4b72aa8-jumpers-m2m.png)

Make sure they are male-to-male wires as that's what you'll need for the breadboard.

### The TMP36 sensor

This is an inexpensive analogue temperature sensor which is really easy to use. Details in Chapter 5.


### Something to measure the light level

I used to use an [LDR](https://en.wikipedia.org/wiki/Photoresistor)
(Light dependent resistor, or Photoresistor) to measure light levels.
Then I asked my friends at Pimoroni why they no longer sell them.
Here's what they explained.

Most LDRs  use CdS (Cadmium Sulphide), and Cadmium is nasty stuff. 
It's prohibited under the RoHS regulations.
It's toxic, and I'm not going to use it for future projects.

Instead, I now use this photo-transistor from Adafruit, also available from vendors in the UK.

![image](http://images.rareschool.com/img/771cc2f8-1016-11ed-8568-a39c23c2a191-board-with-adafuit-led.jpg)


### A buzzer

The remote buzzer project uses an 'active' buzzer - one which makes a noise when powered. These are widely available,
but you'll need to make sure your buzzer works with a 3 V supply. If not, you can build your own mini-breakout board.
Details in appendix B.


### Soldering Kit

You'll find advice on the soldering hardware you need in the 

This is a work in progress. I'll post about updates on the website, in [my blog](https://blog.rareschool.com/)
and as [@RAREblog](https://twitter.com/rareblog) on Twitter.

