from wpilib.command import Command
import subsystems
import oi
from robotmap import axes
class FollowJoystick(Command):
    '''
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    '''

    def __init__(self):
        super().__init__('Follow Joystick')

        self.requires(subsystems.drivetrain)
        



    def execute(self):
      #  self.getRobot().motor.setSpeed(self.getRobot().joystick.getY())
        subsystems.drivetrain.set(oi.joystick.getRawAxis(axes.Left_x),
                                  oi.joystick.getRawAxis(axes.Left_y),
                                 oi.joystick.getRawAxis(axes.Right_x), 0)
      # 0 is for the gyro


