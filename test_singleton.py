from singleton import MySingleton

def test_singleton():
    s1 = MySingleton.getInstance()
    s2 = MySingleton.getInstance()
    assert id(s1) == id(s2)