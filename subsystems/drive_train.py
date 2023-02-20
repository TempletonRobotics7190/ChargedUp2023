import wpilib, wpilib.drive, rev, commands2

class DriveTrain(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.back_left = rev.CANSparkMax(9)
        self.front_right = rev.CANSparkMax(9)
        self.back_right = rev.CANSparkMax(9)
        self.front_left = rev.CANSparkMax(9)

        left_side = wpilib.MotorControllerGroup(self.front_left, self.back_left)
        right_side = wpilib.MotorControllerGroup(self.front_right, self.back_right)
        self.drive = wpilib.drive.DifferentialDrive(left_side, right_side)
    
    def move(self, forward_speed, rotation_speed):
        self.drive.arcadeDrive(rotation_speed, forward_speed)
    
    def stop(self):
        self.drive.arcadeDrive(0.0, 0.0)