from toontown.coghq import DistributedCashbotBossCraneAI
from direct.fsm import FSM

class DistributedCashbotBossSideCraneAI(DistributedCashbotBossCraneAI.DistributedCashbotBossCraneAI, FSM.FSM):

    def __init__(self, air, boss, index):
        DistributedCashbotBossCraneAI.DistributedCashbotBossCraneAI.__init__(self, air, boss, index)
        FSM.FSM.__init__(self, 'DistributedCashbotBossSideCraneAI')
