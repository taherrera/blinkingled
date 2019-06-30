# blinkingled
Blinking led implementations for different platforms for www.blinkingled.xyz

The structure is the following:

microcontrolers/<company>/<board or part name>/<all the necessary files>
microprocessors/<company>/<board or cpu name>/<all the necessary files>
FPGAs/<company>/<board or chip name>/<all the necesary files>
schematics/<appropiate name>/<all the necesary files>
platforms.html

Feel free to pull request a new implementation. Just add a new device and add it to platforms.html following the structure.

This is an example on how to add a new implementation:

Say you've got a blinking-led program for a PIC18F452A and you want to add it:

Fork this repo by pressing the button "Fork" on the upper right corner.
git clone https://github.com/<your_user_name>/blinkingled
cd blinkingled
git branch pr/pic18f452a
git checkout pr/pic18f452a
...
we add blinking\_led.c to microcontrollers/microchip/pic16f628a/blinking\_led.c
and we modify platforms.html and add <li> <a href=href=www.github.com/taherrera/blinkingled/microprocessors/microchip/pic16f628a>PIC18F628A</a> where it should go according to the hierarchy.
...
git add microcontrollers/microchip/pic16f628a/blinking\_led.c
git add platforms.html
git commit -m "Added implementation for the PIC18F628A"
git push --set-upstream origin pr/pic18f452a
...
Now go head to www.github.com/taherrera/blinkingled or to your forked repo using your browser and github will give you the option to pull request your changes !

Happy coding !


