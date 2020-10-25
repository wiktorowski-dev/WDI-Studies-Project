import sys
from module1.common.layout import BasicRadiobuttonExample, QApplication


def run():
    app = QApplication(sys.argv)
    ex = BasicRadiobuttonExample()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
