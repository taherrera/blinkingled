# blinkingled
Blinking led implementations for different platforms for www.blinkingled.xyz

The structure is the following:

microcontrolers/<company>/<board or part name>/<all the necessary files>
microprocessors/<ompany>/<board or cpu name>/<all the necessary files>
FPGAs/<company>/<board or chip name>/<all the necesary files>
schematics/<appropiate name>/<all the necesary files>

platforms.html

Feel free to pull request a new implementation. Just add a new device and add it to platforms.html following the structure.

This is an example on how to add a new implementation:

Say you've got a blinking-led program for a PIC18F452
