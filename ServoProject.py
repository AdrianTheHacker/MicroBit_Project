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
        self.control_system = "buttons" # Either controlled by buttons or using accelorometer.
        
        self.testing_num = 0
        self.max_rotation_value = 131
        self.current_rotation_value = int(self.max_rotation_value / 2)
        self.rotation_speed = 10
        
        self.level()
    
    def check_control_system(self):
        # By connecting a wire from 3v to either pin 2 or pin 1,
        # we can switch between either button controls or auto.
        
        if mb.pin1.read_digital():
            self.control_system = "buttons"
            
        if mb.pin2.read_digital():
            self.control_system = "Auto"
            
    def level(self):
        self.current_rotation_value = int(self.max_rotation_value / 2)
        mb.pin0.write_analog(self.current_rotation_value)
        
    def move_clockwise(self):
        if not mb.button_a.is_pressed():
            return
            
        if self.current_rotation_value <= self.max_rotation_value + self.rotation_speed:
            self.current_rotation_value += self.rotation_speed
            
        mb.pin0.write_analog(self.current_rotation_value)
    
    def move_counter_clockwise(self):
        if not mb.button_b.is_pressed():
            return
        
        if self.current_rotation_value >= 0 + self.rotation_speed:
            self.current_rotation_value -= self.rotation_speed
            
        mb.pin0.write_analog(self.current_rotation_value)
    
    def balance(self):
        # Repeats the actions you do
        if mb.accelerometer.is_gesture("face up"):
            self.level()
            
        elif mb.accelerometer.is_gesture("right"):
            mb.pin0.write_analog(self.max_rotation_value - self.rotation_speed)
            
        elif mb.accelerometer.is_gesture("left"):
            mb.pin0.write_analog(5)
    
        print(mb.accelerometer.current_gesture())
        
    def check_input(self):
        self.check_control_system()
        
        if self.control_system == "buttons":
            self.move_clockwise()
            self.move_counter_clockwise()
            
        if self.control_system == "Auto":
            self.balance()
            

servo = Servo()

while True:
    servo.check_input()
    mb.sleep(40)
    
    
    
    
    

