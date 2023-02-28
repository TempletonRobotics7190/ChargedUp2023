import wpilib, wpilib.drive, rev, commands2, constants

class Arm(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.extension_motor = rev.CANSparkMax(5, rev.CANSparkMax.MotorType.kBrushed)
        self.rotation_motor = rev.CANSparkMax(6, rev.CANSparkMax.MotorType.kBrushed)

    def extend_forward(self):
        print("Extending forward")
        self.extension_motor.set(constants.EXTEND_SPEED)

    def extend_backward(self):
        print("Extending backward")
        self.extension_motor.set(-constants.EXTEND_SPEED)

    def rotate_down(self):
        print("Rotating down")
        self.rotation_motor.set(constants.ROTATE_SPEED)

    def rotate_up(self):
        print("Rotating up")
        self.rotation_motor.set(-constants.ROTATE_SPEED)
        
    def stop_extending(self):
        self.extension_motor.set(0)
   
    def stop_rotating(self):
        self.rotation_motor.set(0)
  