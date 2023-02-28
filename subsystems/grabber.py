import wpilib, wpilib.drive, commands2, constants

class Grabber(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.solenoid_right = wpilib.Solenoid(constants.PNEUMATICS_MODULE_ID,wpilib.PneumaticsModuleType.REVPH,8)
        self.solenoid_left = wpilib.Solenoid(constants.PNEUMATICS_MODULE_ID,wpilib.PneumaticsModuleType.REVPH,9)
        self.is_closed = True

    def open(self):
        self.is_closed = False
        self.solenoid_right.set(False)
        self.solenoid_left.set(False)
    
    def close_half(self):
        self.is_closed = True
        self.solenoid_right.set(False)
        self.solenoid_left.set(True)

    def close_full(self):
        self.is_closed = True
        self.solenoid_right.set(True)
        self.solenoid_left.set(True)
    
    def toggle_full(self):
        if self.is_closed:
            self.open()
        else:
            self.close_full()
    
    def toggle_half(self):
        if self.is_closed:
            self.open()
        else:
            self.close_half()
        
        