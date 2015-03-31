#LIMBO SOFTWARE PRESENTS
#RASPBERRY PI MOTOR DRIVER CONTROLS

# Importing Modules
import time
import RPi.GPIO as GPIO
import sys, tty, termios, time
import os

# setting up the pins to use
# you may need to change these if you are running through different pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

#display user controls
print ('W forward')
print ('S Reverse')
print ('A Left')
print ('D Right')
print ('Q Stop')
print ('E Exit Programme')

# setting up the user input system
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# defining the different directions
# you may need to change these if you are using different pins
def forward():
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(17, True)
    GPIO.output(18, False)

def reverse():
    GPIO.output(22, False)
    GPIO.output(23, True)
    GPIO.output(17, False)
    GPIO.output(18, True)

def right():
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(17, False)
    GPIO.output(18, False)

def left():
    GPIO.output(22, False)
    GPIO.output(23, False)
    GPIO.output(17, True)
    GPIO.output(18, False)
    
def stop():
    GPIO.output(22, False)
    GPIO.output(23, False)
    GPIO.output(17, False)
    GPIO.output(18, False)


# setting up which input controls which direction 
while True:
    char = getch()
    if(char == "w"):
        forward()
    if(char == "q"):
        stop()
    if(char == "s"):
        reverse()
    if(char == "a"):
        left()
    if(char == "d"):
        right()
    if(char == "e"):
        quit()

# Hope the programme works for you! enjoy!
# Limbo Software
 



