from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def qr_read(self):
        import qrtools
        qr = qrtools.QR()
        filename = self.textEdit_5.toPlainText()
        qr.decode(filename)
        self.textEdit_6.setText(qr.data)
    def qr_generate(self):
        import qrcode
        qr = qrcode.QRCode(version=1, box_size=40, border=6)
        data = self.textEdit_4.toPlainText()
        qr.add_data(data)
        qr.make(fit=True)
        image = qr.make_image(fill_color="black", back_color="white")
        image.save("qr_code.png")
    def playSoundFile(self):
        import os, playsound
        speech = os.path.basename(filename)
        playsound.playsound(f"{speech}")
    def getSaveFileName(self):
        from PyQt5.QtWidgets import QFileDialog
        file_filter = 'Sound File (*.mp3)'
        default = f"speech.mp3"
        response = QFileDialog.getSaveFileName(
            caption = 'Save your generated speech file',
            directory = default,
            filter = file_filter,
            initialFilter = 'Sound File (*.mp3)'
        )
        global filename
        filename = response[0]
        tts.save(filename)
        self.playSoundFile()
    def text_to_speech_code(self):
        from gtts import gTTS
        text = self.textEdit_3.toPlainText()
        global tts
        tts = gTTS(text=text)
        self.getSaveFileName()
    def translator_code(self):
        from googletrans import Translator
        translator = Translator()
        dest_lang = self.comboBox.currentText()
        text = self.textEdit.toPlainText()
        translated_text = translator.translate(text, dest=dest_lang)
        self.textEdit_2.setText(translated_text.text)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 911, 651))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QtCore.QRect(410, 0, 102, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QtCore.QRect(20, 60, 251, 51))
        font1 = QtGui.QFont()
        font1.setPointSize(11)
        self.label_7.setFont(font1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(410, 0, 108, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(60, 200, 351, 311))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(480, 200, 351, 311))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 358, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(540, 170, 71, 21))
        self.comboBox.setObjectName("comboBox")
        import googletrans
        countries = googletrans.LANGUAGES
        self.comboBox.addItems(countries)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(480, 110, 368, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(680, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.translator_code)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(390, 0, 156, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(240, 130, 441, 331))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(250, 80, 258, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 490, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.text_to_speech_code)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_8 = QLabel(self.tab_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(390, 0, 144, 51))
        font_label_eight = QtGui.QFont()
        font_label_eight.setPointSize(14)
        self.label_8.setFont(font_label_eight)
        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 70, 86, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_9.setFont(font2)
        self.textEdit_4 = QTextEdit(self.tab_4)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(30, 130, 401, 411))
        self.generate = QPushButton(self.tab_4)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(180, 550, 75, 23))
        self.generate.clicked.connect(self.qr_generate)
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(660, 70, 64, 51))
        self.label_10.setFont(font2)
        self.textEdit_5 = QTextEdit(self.tab_4)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(530, 120, 271, 31))
        self.textEdit_6 = QTextEdit(self.tab_4)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(460, 200, 421, 341))
        self.read = QPushButton(self.tab_4)
        self.read.setObjectName(u"read")
        self.read.setGeometry(QRect(630, 170, 75, 23))
        self.read.clicked.connect(self.qr_read)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setStatusBar(self.statusbar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("AryaSoft_Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", u"AryaSoft Toolbox", None))
        self.tabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.tabWidget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Aryasoft Toolbox.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter the text to translate here:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter language to translate to and click Translate.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Translator", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Text To Speech", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter the text to convert to speech:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Text To Speech", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"QR Code Station", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Generator", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Reader", None))
        self.textEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter path to filename", None))
        self.read.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"QR Code Station", None))


if __name__ == "__main__":
    import darkdetect
    if darkdetect.isDark() == True:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    if darkdetect.isLight() == True:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
