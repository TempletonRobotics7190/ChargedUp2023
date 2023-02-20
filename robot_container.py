import wpilib, constants, commands2, commands2.button
import commands, subsystems

class RobotContainer:
    def __init__(self):
        self.joystick = wpilib.Joystick(0)

        # The robot's subsystems
        self.drive_train = subsystems.DriveTrain()
        self.shooter = subsystems.Shooter()
        self.intake = subsystems.Intake()
        self.belt = subsystems.Belt()

        # Commands
        self.shoot = commands.Shoot(self.shooter, self.belt)

        # Autonomous routine
        self.autonomous = commands.Autonomous()


        # set up default drive command
        self.drive_train.setDefaultCommand(
            commands.JoystickDrive(self.joystick, self.drive_train)
        )

        self.configureButtonBindings()


    def configureButtonBindings(self):
        trigger = commands2.button.JoystickButton(self.joystick, 1)
        button2 = commands2.button.JoystickButton(self.joystick, 2)
        button3 = commands2.button.JoystickButton(self.joystick, 3)
        trigger.whileHeld(
            self.shoot
        )
        button2.whileHeld(
            commands2.StartEndCommand(self.intake.start, self.intake.stop)  
        )

        

    def getAutonomousCommand(self):
        return self.autonomous