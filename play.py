from unit_class import Unit
from close_combat import Experiment, CloseCombatSim

grenadier = Unit(
    health=2,
    accuracy=3,
    strength = 1.5,
    toughness = 1,
    attack_dice = 2,
    assault_specialist = True
)


chasseur = Unit(
    health=2,
    accuracy=1,
    strength=1,
    toughness=1.5,
    attack_dice=2,
)

new = Experiment(10000, [grenadier, grenadier], [chasseur])
#new = CloseCombatSim( [grenadier], [chasseur])
#new.run_battle()
