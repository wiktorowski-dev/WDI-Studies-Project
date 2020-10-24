from module1.converters import *


def run_non_gui():
    # None GUI interface
    print('Please, select type of converter')
    type_converter = input('T - temperature converter, C - currency converter\n')

    if type_converter.lower() == 't':
        temp = TemperatureConverter()
        print('Please select to which temperature you would like convert')
        type_temp_converter = input('C - to celsius, F - to fahrenheit\n')
        temp_in = input('Please select a temperature\n')
        temp_out = temp.convert_temperature(temp_in, type_temp_converter)
        if not temp_out:
            return

        if type_temp_converter.lower() == 'c':
            s1 = 'celsius'
            s2 = 'fahrenheit'
        else:
            s1 = 'fahrenheit'
            s2 = 'celsius'

        print('From {} to {}, temperature is {}'.format(s1, s2, temp_out))
        input()
        return

    elif type_converter.lower() == 'c':
        print('Please select to which currency you would like convert')
        type_temp_converter = input('U - to USD, P - to PLN\n')
        currency_in = input('Please select a currency\n')
        currency = CurrencyConverter()
        currency_out = currency.convert_currency(currency_in, type_temp_converter)
        if not currency_out:
            return

        if type_temp_converter.lower() == 'u':
            s1 = 'PLN'
            s2 = 'USD'
        else:
            s1 = 'USD'
            s2 = 'PLN'

        print('From {} to {}, currency is {}'.format(s1, s2, currency_out))
        input()
        return


if __name__ == '__main__':
    run_non_gui()
