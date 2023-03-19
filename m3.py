class Celsius:
    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temp(self):
        return self.__temperature

    def set_temp(self, text):
        self.__temperature = text

    def del_temp(self):
        del self.__temperature

    temp = property(get_temp, set_temp, del_temp)


tempt = Celsius(12)
print(tempt.temp)
tempt.temp = 25
print(tempt.temp)
del tempt.temp
