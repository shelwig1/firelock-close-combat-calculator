# take the relevant stats for the unit
from unit_class import UnitClass
import random
import copy
# We need to add 1 pin for each miss, 3 pin for each hit for a total of 6
# Does that even matter? Can we just add 6 pin, and have both add the appropraite debuff?

# I need to be able to give it multiple friendly and enemy units 

# This gets stupid when we have way too many fuckers in close combat... 1v1, 2v1, 2v2, we can have a lot more shit going on here
# How do we want to go about this problem... we need to build a moderately robust sim here
# Account for allowing multiple pax on both sides
# Pick different strategies for different fellas


class Experiment:
    def __init__(self, rounds, a_units, b_units):
        self.rounds = rounds
        self.a_units = a_units
        self.b_units = b_units
        self.run()

    def run(self):
        results = []
        total_rounds = 0
        a_wins = 0
        b_wins = 0
        draws = 0 

        for i in range(self.rounds):
            a_units_copy = copy.deepcopy(self.a_units)
            b_units_copy = copy.deepcopy(self.b_units)

            #round = CloseCombatSim(self.a_units[:], self.b_units[:])
            #round = CloseCombatSim(self.a_units, self.b_units)
            battle = CloseCombatSim(a_units_copy, b_units_copy)

            result = battle.run_battle()
            # create a new CloseCombatSim object
            a_count = len(result["a_units"])
            b_count = len(result["b_units"])

            if a_count > b_count:
                a_wins += 1
            elif b_count > a_count:
                b_wins += 1
            else:
                draws += 1

            total_rounds += result["rounds"]
            
            # if it's a win, append to appropriate team
        average_round_length = total_rounds / self.rounds

        print("a_wins: ", a_wins)
        print("b_wins: ", b_wins)
        print("draws: ", draws)
        print("average round length: ", average_round_length)

class CloseCombatSim:
    def __init__(self, a_units: list[UnitClass], b_units: list[UnitClass]):
        self.a_units = a_units
        self.b_units = b_units

    def hit_roll(self, attacker, target):
        target.added_pin += 1
        if self.roll_d6() >= attacker.accuracy:
            target.added_pin += 2
            return True
        return False
    
    def roll_d6(self):
        return random.randint(1, 6)


    def kill_roll(self, attacker, target):
        target_number = self.calculate_target_kill_roll(attacker, target)
        if self.roll_d6() >= target_number:
            target.health -= 1 

    def calculate_target_kill_roll(self, attacker, target):
        if attacker.strength == target.toughness:
            return 4
        elif attacker.strength < target.toughness:
            return 5
        elif attacker.strength > target.toughness:
            return 3

    def roll_d6(self):
        return random.randint(1, 6)
    
    def round_actions(self):
        for unit in self.a_units:
            # select a target from self.b_units
            target = self.b_units[0]
            for d in range(unit.attack_dice):
                if self.hit_roll(unit, target):
                    self.kill_roll(unit, target)

        for unit in self.b_units:
            target = self.a_units[0]
            for d in range(unit.attack_dice):
                if self.hit_roll(unit, target):
                    self.kill_roll(unit, target)

    def post_round_dead_check(self):
            self.a_units = [u for u in self.a_units if u.health > 0]
            self.b_units = [u for u in self.b_units if u.health > 0]

    def post_round_pin(self):
        for unit in self.a_units + self.b_units:
            unit.add_pin()

    def fight_is_over(self):
        if len(self.a_units) == 0 or len(self.b_units) == 0:
            return True
        else:
            return False

    def run_battle(self):
        rounds = 0
        while True:
            rounds += 1
            """ print(f"Starting round {rounds}")
            print(f"Current a_units: {self.a_units}")
            print(f"Current b_units: {self.b_units}")
 """
            self.round_actions()
            self.post_round_dead_check()
            #self.post_round_pin()
            
            if self.fight_is_over():
                # Build results
                # number of rounds
                # return the units for each
                results = {"a_units":self.a_units, "b_units":self.b_units, "rounds":rounds}
                return results
        
