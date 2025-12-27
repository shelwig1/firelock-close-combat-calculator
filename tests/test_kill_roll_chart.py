from kill_roll_chart import add, get_kill_roll_needed

def test_add():
    assert add(2,2) == 4

def test_get_kill_roll_needed():
    # Handles standard rolls
    assert get_kill_roll_needed(8,1) == 0
    assert get_kill_roll_needed(4,1) == 1
    assert get_kill_roll_needed(2,1) == 2
    assert get_kill_roll_needed(1,4) == 7
    assert get_kill_roll_needed(2,2) == 4
    assert get_kill_roll_needed(2,4) == 6
    assert get_kill_roll_needed(3,4) == 5
    assert get_kill_roll_needed(4,3) == 3

    assert get_kill_roll_needed(20,3) == 1

    # Handles 1-, 1, 1+ versus normal numbers
    assert get_kill_roll_needed(0.5,2) == 6
    assert get_kill_roll_needed(1,2) == 6
    assert get_kill_roll_needed(1.5,2) == 6
    assert get_kill_roll_needed(2,0.5) == 2

# but when they're different we need to handle this
    # Handles 1-, 1, 1+ versus 1-, 1, 1+
    assert get_kill_roll_needed(0.5,0.5) == 4
    assert get_kill_roll_needed(1,1) == 4
    assert get_kill_roll_needed(1.5,1.5) == 4

    assert get_kill_roll_needed(1,0.5) == 3

    assert get_kill_roll_needed(0.5,1) == 5
    assert get_kill_roll_needed(1.5,0.5) == 3
    assert get_kill_roll_needed(0.5,1.5) == 5