from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget,QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets
import txtSpeech
import sys

def printClick():
    #print(txtUI.text())
    lblHistorico.setText(lblHistorico.text() + "\n" + txtUI.text())
    txtSpeech.SpeakText(txtUI.text())

def rateChanged():
    txtSpeech.setRate(knobRate.value())
    #print(knobRate.value())

def typeChanged():
    txtSpeech.setVoice(knobType.value())
    #print(knobType.value())

def volChanged():
    txtSpeech.setVolume((knobVol.value()/100))
    #print(knobVol.value())

ui_criada = QUiLoader()
app = QApplication(sys.argv)
tela = ui_criada.load("guiTxt.ui")
tela.setWindowFlag(Qt.FramelessWindowHint)# flat window

txtUI = tela.findChild(QtWidgets.QLineEdit, 'lineEdit')
btnFalar = tela.findChild(QtWidgets.QPushButton, 'pushButton')
btnFalar.clicked.connect(printClick)
lblHistorico = tela.findChild(QtWidgets.QLabel,'label')

knobRate = tela.findChild(QtWidgets.QDial,'rate')
knobType = tela.findChild(QtWidgets.QDial,'type')
knobVol  = tela.findChild(QtWidgets.QDial,'volume')

knobRate.valueChanged.connect(rateChanged)
knobType.valueChanged.connect(typeChanged)
knobVol.valueChanged.connect(volChanged)

#btnSelMidis = tela.findChild(QtWidgets.QPushButton, 'selmidis')
#btnSelMidis.clicked.connect(printClick)

tela.show()
app.exec_()