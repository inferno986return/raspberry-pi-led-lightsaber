#!/usr/bin/env python

# Pull in the code libraries that the code will need to use.
from __future__ import division
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Tell the code the red LED is plugged into pin 35, and that pin 35
# is an output, and set the output to low (i.e. red LED is off)
RED_LED = 33
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(RED_LED, GPIO.LOW)

# Tell the code the green LED is plugged into pin 33, and that pin 33
# is an output, and set the output to low (i.e. green LED is off)
GREEN_LED = 35
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.output(GREEN_LED, GPIO.LOW)

# Tell the code the blue LED is plugged into pin 37, and that pin 37
# is an output, and set the output to low (i.e. blue LED is off)
BLUE_LED = 37
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.output(BLUE_LED, GPIO.LOW)

# Each pulse period is 1/100 second, and each colour is on for a different
# number amount of time each time round the loop.
pulse_period = 1/100

red_fraction = 1/500
red_on = 0

blue_fraction = 1/300
blue_on = 0

green_fraction = 1/200
green_on = 0

# This try and the except below allow the code to stop cleanly by
# capturing the exception from a keyboard ctrl-C. 
try:

  # Store off when the while loop starts.
  start_time = time.time()

  # Start looping around the code forever.  
  while True:

    # Work out what time it is since we started, and from that, the 
    # fraction of the pulse period.
    time.sleep(1/1000)
    clock_time = (time.time() - start_time) % pulse_period

    # For the LEDs, check how far through its fraction of the pulse it 
    # is and turn the LED on if it's less or off if it's more.
    # In this case, the fraction changes each time round the loop, so
    # the LEDs change their brightness.

    #============================= RED =============================#

    if clock_time < red_on * pulse_period:
        GPIO.output(RED_LED, GPIO.HIGH)
    else:
        GPIO.output(RED_LED, GPIO.LOW) 

    red_on += red_fraction 
    if red_on > 1 or red_on < 0:
        red_fraction = -red_fraction
        red_on += red_fraction

    #============================ GREEN =======-====================#

    if clock_time < green_on * pulse_period:
        GPIO.output(GREEN_LED, GPIO.HIGH)
    else:
        GPIO.output(GREEN_LED, GPIO.LOW)

    green_on += green_fraction
    if green_on > 1 or green_on < 0:
        green_fraction = -green_fraction
        green_on += green_fraction


    #============================= BLUE ============================#

    if clock_time < blue_on * pulse_period:
        GPIO.output(BLUE_LED, GPIO.HIGH)
    else:
        GPIO.output(BLUE_LED, GPIO.LOW)

    blue_on += blue_fraction
    if blue_on > 1 or blue_on < 0:
        blue_fraction = -blue_fraction
        blue_on += blue_fraction

# The except here needs to do nothing but has to do something; the pass
# statement means do nothing.
except KeyboardInterrupt as e:
  pass

# Finally turn off the LEDs and cleanup the GPIO.  
GPIO.output(RED_LED, GPIO.LOW)
GPIO.output(GREEN_LED, GPIO.LOW)
GPIO.output(BLUE_LED, GPIO.LOW)
GPIO.cleanup()
