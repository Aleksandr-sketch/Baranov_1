# -*- coding: utf-8 -*-
import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        
    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            
    def paint(self):
        self.do_paint = True
        self.repaint()
        
    def draw_circle(self, qp):
        k = random.randint(0, 300)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(150, 150, k, k)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())
