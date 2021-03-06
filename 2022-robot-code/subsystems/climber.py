# Import APIs
import ctre
import commands2
import wpilib
# Import Constants Module
import constants

class Climber(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        #Start Climber controls
        self.m_left_hook = ctre.WPI_VictorSPX(constants.C_M_LEFT_HOOK)
        self.m_right_hook = ctre.WPI_VictorSPX(constants.C_M_RIGHT_HOOK)

        self.m_climber = wpilib.SpeedControllerGroup(self.m_left_hook, self.m_right_hook)

        self.height = 0

    def move_up(self):
        #TODO: implementar movimentação dos motores 

        self.height += 1
        print(self.height)

    def is_height_positive(self):
        return self.height > 0

    def move_down(self):
        if not self.is_height_positive():
            return

        self.height -= 1
        print(self.height)