import wpilib, commands2, commands2.button

from robot_container import RobotContainer


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        self.container = RobotContainer()
        self.autonomous_command = self.container.getAutonomousCommand()
        self.gyro = wpilib.ADIS16448_IMU()
        super().robotInit()
    
    def robotPeriodic(self) -> None:
        print(round(self.gyro.getGyroAngleY()))
        return super().robotPeriodic()

    def autonomousInit(self):
        self.autonomous_command.schedule()
        super().autonomousInit()

    def teleopInit(self):
        self.autonomous_command.cancel()
        super().teleopInit()

        

wpilib.run(Robot)