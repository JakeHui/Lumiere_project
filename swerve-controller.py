# from wpilib_kinematics import wpilib as wpimath
from wpilib_kinematics.wpilib.geometry import *
from wpilib_kinematics.wpilib.kinematics import *
from wpilib_kinematics.wpilib.kinematics.swerve import *
MAXIMUM_WHEEL_SPEED = 5

wheellocation_1 = Translation2d(0.5,0.5)
wheellocation_2 = Translation2d(-0.5,0.5)
wheellocation_3 = Translation2d(0.5,-0.5)
wheellocation_4 = Translation2d(-0.5,-0.5)
chassis_speed =  ChassisSpeeds(1, 1, 20)
centreofrotation = Translation2d(0, 0)

swerve_kinematics = SwerveDriveKinematics(wheellocation_1, wheellocation_2,
                                                               wheellocation_3, wheellocation_4)
module_state = swerve_kinematics.toSwerveModuleStates(chassis_speed, centreofrotation)
# swerve_kinematics.desaturateWheelSpeeds(module_state, MAXIMUM_WHEEL_SPEED)
print(module_state[0])
print(module_state[1])
print(module_state[2])
print(module_state[3])
