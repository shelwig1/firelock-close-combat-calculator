from unit_class import Unit

def add(a,b):
    return a + b

def get_kill_roll(attacker_strength: Unit, target_toughness: Unit) -> int:

    # Check if we have to do comparisons for special fellas
    if attacker_strength < 2 and target_toughness < 2:
        # handle the fellas
        if attacker_strength == target_toughness:
            return 4
        if attacker_strength > target_toughness:
            return 3
        if attacker_strength < target_toughness:
            return 5

    # Normalize 1-, 1, 1+ to 1 for comparison
    if attacker_strength >= 0.5 and attacker_strength <= 1.5:
        attacker_strength = 1
    if target_toughness >= 0.5 and target_toughness <= 1.5:
        target_toughness = 1 

    if attacker_strength == target_toughness:
        return 4
    
    elif attacker_strength <= ((1/4) * target_toughness):
        return 7
    elif attacker_strength <= ((1/2) * target_toughness):
        return 6
    elif attacker_strength < target_toughness:
        return 5
    elif attacker_strength == target_toughness:
        return 4
    elif (attacker_strength > target_toughness) and (attacker_strength < (2 * target_toughness)):
        return 3
    elif (attacker_strength >= (2 * target_toughness)) and (attacker_strength < (4 * target_toughness)):
        return 2
    elif attacker_strength >= (4 * target_toughness)  and (attacker_strength < (8 * target_toughness)):
        return 1
    else:
        return 0