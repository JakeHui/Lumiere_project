import evdev
import math
import board
import time
from adafruit_motorkit import MotorKit
from evdev import InputDevice, categorize, ecodes      
power = MotorKit(i2c=board.I2C())            
gamepad = InputDevice('/dev/input/event2')    
left_joystick_x = 128
left_joystick_y = 128
right_joystick_x = 128
right_joystick_y = 128

def get_controller_input(left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y): #get input from ps5 controller
    if event.type == ecodes.EV_ABS and event.code == 0 or 1 or 3 or 4:
        #EVENT CODES
        # 0: 'left joystick left/right'          # 0 = left, 255 = right
        # 1: 'left joystick up/down'             # 0 = up, 255 = down
        # 3: 'right joystick left/right'         # 0 = left, 255 = right
        # 4: 'right joystick up/down'            # 0 = up, 255 = down
        
        #FOR LEFT JOYSTICK
        if event.code == 0:                     # left joystick, x-axis (left/right)
            if event.value > (128 - 6) and event.value < (128 + 6):   # joystick drift at centre
                left_joystick_x = 128
            elif event.value < (1): #hot fix becuase controller was returning 0
                i = 0 # do nothing
            else: left_joystick_x = event.value
        elif event.code == 1:                     # left joystick, y-axis (up/down)
            if event.value > (128 - 6) and event.value < (128 + 6):   # joystick drift at centre
                left_joystick_y = 128
            else: left_joystick_y = event.value


        #FOR RIGHT JOYSTICK
        if event.code == 3:                     # right joystick, x-axis (left/right)
            if event.value > (128 - 6) and event.value < (128 + 6):   # joystick drift at centre
                right_joystick_x = 128
            else: right_joystick_x = event.value
        elif event.code == 4:                     # right joystick, y-axis (up/down)
            if event.value > (128 - 6) and event.value < (128 + 6):   # joystick drift at centre
                right_joystick_y = 128
            else: right_joystick_y = event.value

        return (left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y) #return known values
                
def define_values():
    #turn the values from the controller into desired values for the swerve algorithm

def swerve_algorithm():
    global speed
    speed = (255 - math.sqrt(math.pow(left_joystick_x, 2) + math.pow(left_joystick_y, 2)))/255

def power_motors():
    #power motors to the speed
    #turn the turning motors until they reach the right position
    #values will be given by swerve algorithm
    while True:
        break

if __name__ == '__main__':
    try:
        for event in gamepad.read_loop(): #main loop based on controller update
            left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y = get_controller_input(left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y)
            print(left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y) # for testing
            define_values()
            swerve_algorithm()
            power_motors()
    finally:
        power.motor1.throttle = 0 #turn off power for all motors if no input