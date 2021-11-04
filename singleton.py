class MySingleton():
    __instance = None

    def __init__(self):
        print("New instance")

    @classmethod
    def getInstance(self):
        if self.__instance is None:
            self.__instance = MySingleton()
        return self.__instance