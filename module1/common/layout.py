import sys
from PyQt5.QtWidgets import *
from module1.converters import *


class BasicRadiobuttonExample(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.converter_temp = TemperatureConverter()
        self.converter_currency = CurrencyConverter()

    def init_ui(self):

        layout = QVBoxLayout()

        self.converter_settings = (0, 0)

        self.grid = QGridLayout()

        self.label = QLabel('Which type of converter you want to use?')
        self.btn_type_1 = QRadioButton('Temperature')
        self.btn_type_2 = QRadioButton('Currency')
        self.label2 = QLabel("")

        self.btn_sub_type_1 = QRadioButton('Select previous button')
        self.btn_sub_type_2 = QRadioButton('Select previous button')
        self.label4 = QLabel("")

        self.text = QLineEdit()
        self.text_send_btn = QPushButton('Check')

        self.answer_section = QLabel('Answer Section')
        self.answer_section_2 = QLabel('')

        self.grid.btngroup1 = QButtonGroup()
        self.grid.btngroup2 = QButtonGroup()

        self.grid.btngroup1.addButton(self.btn_type_1, 1)
        self.grid.btngroup1.addButton(self.btn_type_2)
        self.grid.btngroup2.addButton(self.btn_sub_type_1)
        self.grid.btngroup2.addButton(self.btn_sub_type_2)

        self.btn_type_1.toggled.connect(self.change_buttons_to_temp)
        self.btn_type_2.toggled.connect(self.change_buttons_to_currency)

        self.text_send_btn.clicked.connect(self.check_conversion)
        layout.addWidget(self.label)
        layout.addWidget(self.btn_type_1)
        layout.addWidget(self.btn_type_2)
        layout.addWidget(self.label2)

        layout.addWidget(self.btn_sub_type_1)
        layout.addWidget(self.btn_sub_type_2)
        layout.addWidget(self.label4)

        layout.addWidget(self.text)
        layout.addWidget(self.text_send_btn)
        layout.addWidget(self.answer_section)
        layout.addWidget(self.answer_section_2)
        self.text.setMaximumWidth(150)
        self.text.setMaximumHeight(25)

        self.setGeometry(200, 200, 300, 300)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Radio Button Example')

        self.show()

    def change_buttons_to_temp(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label2.setText("Please, select to which temperature you would like change")
            self.btn_sub_type_1.setText('Celsius')
            self.btn_sub_type_2.setText('Fahrenheit')

    def change_buttons_to_currency(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label2.setText("Please, select to which currency you would like exchange")
            self.btn_sub_type_1.setText('PLN')
            self.btn_sub_type_2.setText('USD')

    def check_none_output(self, output):
        if output is None:
            self.answer_section_2.setText("Something goes wrong")
            return None
        else:
            return True

    def check_conversion(self):
        btn = self.sender()
        if btn.isEnabled():
            if (self.btn_sub_type_1.isChecked() | self.btn_sub_type_2.isChecked()) is False:
                self.answer_section_2.setText("Please select all buttons")
                return
            if (self.btn_type_1.isChecked() | self.btn_type_2.isChecked()) is False:
                self.answer_section_2.setText("Please select all buttons")
                return

            else:
                self.answer_section_2.setText("Processing")
                text = self.text.text()
                output = None
                if self.btn_type_1.isChecked():
                    if self.btn_sub_type_1.isChecked():
                        output = self.converter_temp.convert_temperature(text, 'c')
                        if not self.check_none_output(output):
                            return
                        output = "{} Fahrenheit to Celsius is {}".format(text, output)
                    else:
                        output = self.converter_temp.convert_temperature(text, 'f')
                        if not self.check_none_output(output):
                            return
                        output = "{} Celsius to Fahrenheit is {}".format(text, output)
                else:
                    if self.btn_sub_type_1.isChecked():
                        output = self.converter_currency.convert_currency(text, 'p')
                        if not self.check_none_output(output):
                            return
                        output = "{} USD to PLN is {}".format(text, output)
                    else:
                        output = self.converter_currency.convert_currency(text, 'u')
                        if not self.check_none_output(output):
                            return
                        output = "{} PLN to USD is {}".format(text, output)

                self.answer_section_2.setText(output)

            print(21)
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BasicRadiobuttonExample()
    sys.exit(app.exec_())
