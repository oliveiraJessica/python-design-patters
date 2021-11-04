from singleton import MySingleton
def test_singleton():
    s1 = MySingleton.getInstance()
    s2 = MySingleton.getInstance()
    assert s1 == s2