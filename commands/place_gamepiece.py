import wpilib, commands2

import subsystems
from commands.rotate_arm import RotateArm
from commands.drive_time import DriveTime


class PlaceGamepiece(commands2.SequentialCommandGroup):
    """
    Command for autonomous to place the 

    :param float time: Time to drive for in seconds
    :param float speed: How fast to drive (-1.0 to 1.0)
    :param float rotation: How fast to rotate (-1.0 to 1.0)
    :param DriveTrain drive_train: DriveTrain to execute command on
    """

    def __init__(self, arm: subsystems.Arm, 
                 drive_train: subsystems.DriveTrain, 
                 grabber: subsystems.Grabber):
        super().__init__(
            RotateArm(arm, "down", 1),
            DriveTime(1, 0.5, 0, drive_train),
            commands2.InstantCommand(grabber.open),
            DriveTime(5, -0.5, 0, drive_train)
        )