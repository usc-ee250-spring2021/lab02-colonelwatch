""" EE 250L Lab 02: GrovePi Sensors

Kenny Peng.

github.com/usc-ee250-spring2021/lab02-colonelwatch
"""

import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd

if __name__ == '__main__':
    pot_port = 0 # A0
    ultrasonic_port = 4    # D4

    grove_rgb_lcd.setRGB(255, 255, 255)

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        threshold = grovepi.analogRead(pot_port)
        distance = grovepi.ultrasonicRead(ultrasonic_port)

        if distance < threshold:
            grove_rgb_lcd.setText_norefresh('%4dcm OBJ PRES\n%4dcm' % (threshold, distance))
        else:
            grove_rgb_lcd.setText_norefresh('%4dcm         \n%4dcm' % (threshold, distance))

