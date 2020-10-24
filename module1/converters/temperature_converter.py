class TemperatureConverter(object):
    def __init__(self):
        super(TemperatureConverter, self).__init__()

    def convert_temperature(self, temp_in, to_system: str):
        if type(temp_in) not in [int, float]:
            print('Incorrect temperature, please type it correctly')
            return None
        if to_system.lower() == 'f':
            return self.__convert_c_to_f(temp_in)
        elif to_system.lower() == 'c':
            return self.__convert_f_c(temp_in)
        else:
            print('Incorrect temperature system selection, please select it correctly')
            return None

    @staticmethod
    def __convert_c_to_f(temp_in):
        temp_out = (temp_in*9/5)+32
        return temp_out

    @staticmethod
    def __convert_f_c(temp_in):
        temp_out = (temp_in-32)*5/9
        return temp_out
