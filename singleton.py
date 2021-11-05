    """
    Implementation xxample of a Singleton class

    Singleton is a desgin pattern to object creation 
    wich makes sure a class has a unique instance 
    with global access 

    Use Case: Data base connection
    """

class MySingleton():
    __instance = None

    def __init__(self):
        print("New instance")

    @classmethod
    def getInstance(self):
        if self.__instance is None:
            self.__instance = MySingleton()
        return self.__instance