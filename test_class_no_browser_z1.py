from class_no_browser_z1 import Counter

def test_class_no_browser_z1_starting_value():
    c = Counter()
    assert c.value == 0

def test_class_no_browser_z1_plus_3():
    c = Counter()
    c.add()
    c.add()
    c.add()
    assert c.value == 3
def test_class_no_browser_z1_reset():
    c = Counter()
    c.add()
    c.reset()
    assert c.value == 0