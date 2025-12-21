from unit_class import UnitClass
from core import Experiment, CloseCombatSim
grenadier = UnitClass(
    health=2,
    accuracy=3,
    strength = 1,
    toughness = 1,
    attack_dice = 2,
)

chasseur = UnitClass(
    health=2,
    accuracy=0,
    strength=1,
    toughness=1.5,
    attack_dice=2,
)

new = Experiment(1000, [grenadier, grenadier], [chasseur])
#new = CloseCombatSim( [grenadier], [chasseur])
#new.run_battle()
