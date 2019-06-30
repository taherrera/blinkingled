# It all starts with a blinking led...
Blinking led implementations/tutorials/code for different platforms.

[platforms.html](platforms.html) shows up in [www.blinkingled.xyz](http://www.blinkingled.xyz)

Feel free to pull request a new implementation.

There are two ways you can contribute:

1. Add a link to an external tutorial to README.md on target platform: See [PIC16F628A example](microcontrollers/microchip/parts/pic16f628a)
2. Add code or tutorial in this repo for a blinking led implementation.

Note: one device may have external links to tutorials and also code or tutorials on this repo. See [PIC16F628A example](microcontrollers/microchip/parts/pic16f628a)

**if a link does not exist in platflorms.html Please add the link to this github device path to platforms.html**

This is an example on how to add a tutorial to this github:  

Say you've got a blinking-led program/tutorial for a PIC18F452A and you want to add it to this repo (Second way you can contribute (2.)):  

- Fork this repo by pressing the button "Fork" on the upper right corner.
- Use the following commands on a terminal and replace your\_user\_name with your github username:
```
git clone https://github.com/your_user_name/blinkingled
cd blinkingled
git branch pr/pic18f452a
git checkout pr/pic18f452a
```
- Add blinking\_led.c to microcontrollers/microchip/pic16f628a/blinking\_led.c and add to platforms.html the line that links to your work according to the hierarchy: 
`<li> <a href=href=www.github.com/taherrera/blinkingled/tree/master/microprocessors/microchip/pic16f628a>PIC18F628A</a>`
Optional: add README.md, how to, images, schematics, or whatever you think can be helpfull.
- Use the following commands on a terminal
```
git add microcontrollers/microchip/pic16f628a/blinking\_led.c
git add platforms.html
git commit -m "Added implementation for the PIC18F628A"
git push --set-upstream origin pr/pic18f452a
```
- Check that your changes look OK and now go head to www.github.com/taherrera/blinkingled or to your forked repo using your browser and github will give you the option to pull request your changes !

Thanks for contributing and happy coding !


