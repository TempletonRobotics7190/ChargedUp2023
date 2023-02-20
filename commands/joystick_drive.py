import wpilib, commands2

class JoystickDrive(commands2.CommandBase):
    def __init__(self, joystick, drive_train):
        super().__init__()
        self.joystick = joystick
        self.drive_train = drive_train
        self.addRequirements(drive_train)
    
    def execute(self):
        self.drive_train.move(-self.joystick.getRawAxis(1), self.joystick.getRawAxis(0))
    
