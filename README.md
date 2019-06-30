# It all starts with a blinking led...
Blinking led implementations for different platforms for [www.blinkingled.xyz](http://www.blinkingled.xyz)

Feel free to pull request a new implementation. Just add a new device and add it to platforms.html following the structure.

This is an example on how to add a new implementation:

Say you've got a blinking-led program for a PIC18F452A and you want to add it:

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
- Now go head to www.github.com/taherrera/blinkingled or to your forked repo using your browser and github will give you the option to pull request your changes !

Thanks for contributing and happy coding !


