import RPi.GPIO as GPIO

from os import system
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)


def turn_on_screen():
    system('raspi-gpio set 19 op a5')
    GPIO.output(18, GPIO.HIGH)


def turn_off_screen():
    system('raspi-gpio set 19 ip')
    GPIO.output(18, GPIO.LOW)


def wait_release():
    input = not GPIO.input(4)
    while input:
        sleep(0.2)
        input = not GPIO.input(4)


turn_off_screen()
screen_on = False

while True:
    input = not GPIO.input(4)

    if input:
        screen_on = not screen_on

        if screen_on:
            turn_on_screen()
        else:
            turn_off_screen()

        wait_release()

    sleep(0.2)
