import wpilib, commands2, commands2.button, wpilib.event

import commands, constants

from robot_container import RobotContainer


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):

        wpilib.CameraServer.launch()
        self.container = RobotContainer()

        # self.maxSpeed = (
        #     Shuffleboard.getTab("Configuration")
        #     .add(title="Max Speed", defaultValue=1)
        #     .withWidget("Number Slider")
        #     .withPosition(1, 1)
        #     .withSize(2, 1)
        #     .getEntry()
        # )

        # Create a 'DriveBase' tab and add the drivetrain object to it.
        # driveBaseTab = Shuffleboard.getTab("Drivebase")
        # driveBaseTab.add(title="Differential Drive", defaultValue=self.container.drive_train.drive)
        
        self.autonomous_command = self.container.getAutonomousCommand()
        self.use_pneumatics = wpilib.SendableChooser()
        self.use_pneumatics.setDefaultOption("Pneumatics On", True)
        self.use_pneumatics.addOption("Pneumatics Off", False)
        wpilib.SmartDashboard.putData("Pneumatics Control", self.use_pneumatics)
        self.compressor = wpilib.Compressor(constants.PNEUMATICS_MODULE_ID, wpilib.PneumaticsModuleType.REVPH)

    def robotPeriodic(self):
        super().robotPeriodic()
        wpilib.SmartDashboard.putNumber("Gyro", round(self.container.gyroscope.getGyroAngleY(), 1))
        wpilib.SmartDashboard.putData("stabalize command", commands.Stabilize(self.container.drive_train, self.container.gyroscope))

        if self.use_pneumatics.getSelected():
            self.compressor.enableDigital()
        else:
            self.compressor.disable()
        
    def autonomousInit(self):
        self.autonomous_command.schedule()

    def teleopInit(self):
        self.autonomous_command.cancel()


        

wpilib.run(Robot)