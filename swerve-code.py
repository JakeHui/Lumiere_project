import evdev
import math
import board
import time
from adafruit_motorkit import MotorKit
from evdev import InputDevice, categorize, ecodes      
from wpilib_kinematics.wpilib.geometry import *
from wpilib_kinematics.wpilib.kinematics import *
from wpilib_kinematics.wpilib.kinematics.swerve import *
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
                
def define_values(left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y):
    #turn the values from the controller into desired values for the swerve algorithm
    global vx
    global vy
    global omega


def swerve_algorithm():
    MAXIMUM_WHEEL_SPEED = (((96*3.141592)/1000)*150)/60 #~0.75m/s kind of slow

    wheellocation_1 = Translation2d(0.5,0.5) #positions of all the modules
    wheellocation_2 = Translation2d(-0.5,0.5)
    wheellocation_3 = Translation2d(0.5,-0.5)
    wheellocation_4 = Translation2d(-0.5,-0.5)

    chassis_speed =  ChassisSpeeds(vx, vy, omega) #desired speed and direction
    centreofrotation = Translation2d(0, 0) #centre of rotation

    swerve_kinematics = SwerveDriveKinematics(wheellocation_1, wheellocation_2, wheellocation_3, wheellocation_4)
    global module_state
    module_state = swerve_kinematics.toSwerveModuleStates(chassis_speed, centreofrotation) 
    #determines heading for each of the wheels
    module_state = swerve_kinematics.normalizeWheelSpeeds(module_state, MAXIMUM_WHEEL_SPEED)
    #scales all wheel speeds down relative to max velocity



def power_motors():
    #power motors to the speed
    #turn the turning motors until they reach the right position
    #values will be given by swerve algorithm
    module_state[0]
    module_state[1]
    module_state[2]
    module_state[3]
    while True:
        break

if __name__ == '__main__':
    try:
        for event in gamepad.read_loop(): #main loop based on controller update
            left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y = get_controller_input(left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y)
            print(left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y) # for testing
            define_values(left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y)
            swerve_algorithm()
            power_motors()
    finally:
        power.motor1.throttle = 0 #turn off power for all motors if no input