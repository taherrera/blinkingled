# It all starts with a blinking led...
Blinking led implementations/tutorials/code for different platforms.

[platforms.html](platforms.html) shows up in [www.blinkingled.xyz](http://www.blinkingled.xyz)

Feel free to pull request a new implementation or existing tutorial.

There are two ways you can contribute:

1. Add a link to an external tutorial to README.md on target platform: See [PIC16F628A example](microcontrollers/microchip/parts/pic16f628a)
2. Add code or tutorial in this repo for a blinking led implementation.

Note: one device may have external links to tutorials and also code or tutorials on this repo. See [PIC16F628A example](microcontrollers/microchip/parts/pic16f628a)

This is an example on how to add a tutorial to this github:  

Say you've got a blinking-led program or tutorial for a PIC18F452A and you want to add it to this repo:  

- Fork this repo by pressing the button "Fork" on the upper right corner.
- Use the following commands on a terminal and replace your\_user\_name with your github username:
```
git clone https://github.com/your_user_name/blinkingled
cd blinkingled
git branch pr/pic18f452a
git checkout pr/pic18f452a
```
- Two ways you can contribute:
1. Add blinking\_led.c to microcontrollers/microchip/pic16f628a/implementation_2/blinking\_led.c and a README.md and optionally: add how to, images, schematics, or whatever you think can be helpfull.
2. Add to microcontrollers/microchip/pic16f628a/README.md a link to external tutorial.

- Use the following commands on a terminal:
```
git add --all
git commit -m "Added implementation for the PIC18F628A"
git push --set-upstream origin pr/pic18f452a
```
- Check that your changes look OK and now go head to www.github.com/taherrera/blinkingled or to your forked repo using your browser and github will give you the option to pull request your changes !

Thanks for contributing and happy blinking !


