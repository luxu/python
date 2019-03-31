# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contentor = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.contentor)
        self.menu = QHBoxLayout()
        self.adicionar = QPushButton(self.contentor)
        self.menu.addWidget(self.adicionar)
        self.listar = QPushButton(self.contentor)
        self.menu.addWidget(self.listar)
        self.configurar = QPushButton(self.contentor)
# ----------------------------------------------------#
        self.configurar.clicked.connect(self.muda)    #
# ----------------------------------------------------#
        self.menu.addWidget(self.configurar)          #
        self.ajuda = QPushButton(self.contentor)      #
        self.menu.addWidget(self.ajuda)               #
        self.verticalLayout.addLayout(self.menu)      #
# ----------------------------------------------------#
        self.conteudo = Inicio(self.contentor)        #
#-----------------------------------------------------#
        self.verticalLayout.addWidget(self.conteudo)  #
        self.setCentralWidget(self.contentor)         #
        QMetaObject.connectSlotsByName(self)          #
        #

    def muda(self):
        self.conteudo = Configuracao(self.contentor)


class Inicio(QWidget):
    def __init__(self, Form):
        super().__init__()
        self.gridLayout = QGridLayout(self)
        spacerItem = QSpacerItem(
            20, 131, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QSpacerItem(
            70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.label = QLabel(Form)
        self.label.setText("Inicio")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem2 = QSpacerItem(
            69, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QSpacerItem(
            20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)


class Configuracao(QWidget):
    def __init__(self, contentor):
        super().__init__()
        self.verticalLayout = QVBoxLayout(self)
        spacer = QSpacerItem(20, 87,
                             QSizePolicy.Minimum,
                             QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer)
        self.login = QPushButton(self)
        self.verticalLayout.addWidget(self.login)
        self.horizontalLayout = QHBoxLayout()
        self.label_tema = QLabel(self)
        self.horizontalLayout.addWidget(self.label_tema)
        self.tema = QComboBox(self)
        self.horizontalLayout.addWidget(self.tema)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addItem(spacer)
        self.faz_bkp = QPushButton(self)
        self.verticalLayout.addWidget(self.faz_bkp)
        self.imp_bkp = QPushButton(self)
        self.verticalLayout.addWidget(self.imp_bkp)


if __name__ == "__main__":
    aplicativo = QApplication(sys.argv)
    janela = Janela()
    janela.show()

    aplicativo.exec_()