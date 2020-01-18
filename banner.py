# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:00:21 2020

@author: Kamil Chrustowski
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Banner(QWidget):
    def __init__(self, pixmap,height, parent=None):
        super(Banner, self).__init__(parent)
        self.pixmap = pixmap
        self.setFixedHeight(height)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setStyleSheet("background-color: transparent;background: none; background-repeat: none; border: 10px;")
    def paintEvent(self, event):
         painter = QPainter()
         painter.begin(self)
         painter.drawPixmap(220,0, self.pixmap.scaled(QSize(self.width()-440, self.height())))
    