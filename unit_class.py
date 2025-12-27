from dataclasses import dataclass

@dataclass
class Unit:
    health: int
    accuracy: int
    strength: float
    toughness: float
    attack_dice: int
    pin: int = 0
    added_pin: int = 0
    vehicle: bool = False
    assault_specialist: bool = False
    # This needs to factor in other modifiers, silly billy
    # Have this be input arguments to the UnitClass and go from there

    # Throw in modifiers as appropriate as a separate component here, go from there
    def get_accuracy(self):
        return self.accuracy - 1  + (self.pin // 2)# adjust for 1/2 range bonus
    
    def add_pin(self):
        self.pin += self.added_pin
        
        if self.pin > 6:
            self.pin = 6
        
        self.added_pin = 0