import microbit as mb

"""
Project Idea / Plan
-------------------

This project will be a servo (That I brought from home)
that is controlled by the microbit.

I plan on having a few ideas for the project can do:
    - Manually move the servo using the buttons on the microbit
    - The servo will change direction depending on the angle of the microbit
    
Wiring Instructions
-------------------
1. Connect the ground of the microbit to the ground of the servo
2. Connect the 3v of the microbit to the Vcc of the servo
3. Connect pin 0 on the microbit to the PWM of the servo
 __________            _______
/ microbit \          / Servo \
|   GND  ()|----------|GND    |
|   3v   ()|----------|Vcc    |
|        ()|    ------|PWM    |
|        ()|    |     \_______/
|   Pin0 ()|----|
\__________/
"""

class Servo():
    def __init__(self):
        self.testing_num = 0
        self.max = 131
        self.value = int(self.max / 2)
        self.move_speed = 10
    
    def move_clockwise(self):
        if self.value <= self.max + self.move_speed:
            self.value += self.move_speed
            
        mb.pin0.write_analog(self.value)
    
    def move_counter_clockwise(self):
        if self.value >= 0 + self.move_speed:
            self.value -= self.move_speed
            
        mb.pin0.write_analog(self.value)
    
    def check_input(self):
        if mb.button_a.is_pressed():
            self.testing_num += 1
            self.move_counter_clockwise()
            
        if mb.button_b.is_pressed():
            self.testing_num += 1
            self.move_clockwise()
            

servo = Servo()

while True:
    servo.check_input()
    mb.sleep(40)
    
    
    
    
    

