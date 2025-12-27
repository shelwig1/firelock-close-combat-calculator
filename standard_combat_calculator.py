from unit_class import Unit
from kill_roll_chart import get_kill_roll
# start with taking the accuracy of their given thing
# compare against the toughness of the victim to get the ultimate amount of roll we care about
def generate_attack_stats(attacker: Unit, target: Unit) -> dict:
    prob_hit = hit_probability(attacker, target)
    prob_kill = kill_propability(attacker, target)
    
    expected_hits = attacker.attack_dice * prob_hit
    expected_kills = expected_hits * prob_kill
    
    return {
        "prob_hit": prob_hit,
        "prob_kill": prob_kill,
        "expected_hits": expected_hits,
        "expected_kills": expected_kills
    }

def hit_probability(attacker: Unit, target: Unit) -> float:
    prob_hit = (7 - attacker.accuracy) / 6
    return prob_hit

def kill_propability(attacker: Unit, target: Unit) -> float:
    kill_roll = get_kill_roll(attacker.strength, target.toughness)

    return (7 - kill_roll) / 6