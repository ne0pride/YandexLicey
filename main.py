import random, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter


class TMyWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.press)
        self.Flag = False

    def paintEvent(self, event):
        if self.Flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def press(self):
        self.Flag = True
        self.repaint()

    def draw_flag(self, qp):
        x = random.randint(0, 180)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, x, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win1 = TMyWindow()
    win1.show()
    sys.exit(app.exec())
