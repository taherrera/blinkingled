/* 
 * @file	led.c
 * @author	www.sltech.cl
 * @brief	turns on and off the GPIOs of port B (RB0,RB1,RB2,RB3,RB4,RB5,RB6,RB7) cada 500ms	
 *
 * Created on June 16, 2019, 5:42 PM
 */


// PIC16F628A Configuration Bit Settings

#pragma config FOSC = INTOSCIO  // Oscillator Selection bits (INTOSC oscillator: I/O function on RA6/OSC2/CLKOUT pin, I/O function on RA7/OSC1/CLKIN)
#pragma config WDTE = OFF       // Watchdog Timer Enable bit (WDT disabled)
#pragma config PWRTE = OFF      // Power-up Timer Enable bit (PWRT disabled)
#pragma config MCLRE = OFF      // RA5/MCLR/VPP Pin Function Select bit (RA5/MCLR/VPP pin function is digital input, MCLR internally tied to VDD)
#pragma config BOREN = ON       // Brown-out Detect Enable bit (BOD enabled)
#pragma config LVP = OFF        // Low-Voltage Programming Enable bit (RB4/PGM pin has digital I/O function, HV on MCLR must be used for programming)
#pragma config CPD = OFF        // Data EE Memory Code Protection bit (Data memory code protection off)
#pragma config CP = OFF         // Flash Program Memory Code Protection bit (Code protection off)

#define _XTAL_FREQ 4000000
#include 

int main(void) {
    TRISB = 0x00;
    
    while (1){
        PORTB ^= 0xff;
        __delay_ms(500);
    }
    
    return 0;
}
