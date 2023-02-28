import wpilib, commands2, subsystems

class XboxcontrollerDrive(commands2.CommandBase):
    def __init__(self, xboxcontroller: wpilib.XboxController, drive_train: subsystems.DriveTrain):
        super().__init__()
        self.xboxcontroller = xboxcontroller
        self.drive_train = drive_train
        self.addRequirements(drive_train)
    
    def execute(self):
        self.drive_train.move(self.xboxcontroller.getLeftY(), -self.xboxcontroller.getRightX())
    
