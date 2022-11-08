# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Signals(QObject):
    endInitSignal = Signal()
    writeSignal = Signal(str, str, str, str, str, str, str, str, str, str)
    addSignal = Signal(str, str, str, str, str, str, str, str, str, str)
    def __init__(self):
        super().__init__()

class ui(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        
        parent.sg.mesTxtSignal.connect(self.setMes)
        parent.sg.mesDateSignal.connect(self.setDate)
        self.sg = Signals()
        self.initUi()

    def initUi(self):
        self._width=720
        self._height=720
        self.setMinimumSize(self._width,self._height)
        self.setMaximumSize(self._width,self._height)
        self.setWindowTitle("Pograncotrol")
        self.textScroll=QScrollArea(self)
        self.textScroll.setFixedWidth(500)
        self.textScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textScroll.setWidgetResizable(True)
        self.textScroll.setContentsMargins(50, 50, 50 , 50)
        self.gridBox=QGridLayout(self)
        self.gridBox.setContentsMargins(5, 5, 5, 5)
        
        self.mesCntLabel = QLabel(self)
        self.mesCntLabel.setText("")
        self.mesText=QLabel(self)
        self.mesText.setFont("Sans Serif")
        self.mesText.setWordWrap(True)
        #self.mesText.setTextFormat()
        self.dateMesLabel=QLabel(self)
        self.mesText.setText("")
        #self.mesText.setFixedWidth(500)
        self.dateMesLabel.setText("")
        
        self.ageLabel=QLabel(self)
        self.ageLabel.setText('Возраст')
        self.ageText=QLineEdit(self)
        
        self.causeLabel=QLabel(self)
        self.causeLabel.setText('Причина')
        self.causeText=QLineEdit(self)
        
        self.vusLabel=QLabel(self)
        self.vusLabel.setText('ВУС')
        self.vusText=QLineEdit(self)
        
        self.countryLabel=QLabel(self)
        self.countryLabel.setText('Страна въезда')
        self.countryText=QLineEdit(self)
        
        self.kppLabel=QLabel(self)
        self.kppLabel.setText('КПП выезда')
        self.kppText=QLineEdit(self)
        
        self.yServiceLabel=QLabel(self)
        self.yServiceLabel.setText('Годы службы')
        self.yServiceText=QLineEdit(self)
        
        self.voenkLabel=QLabel(self)
        self.voenkLabel.setText('Военкомат')
        self.voenkText=QLineEdit(self)
        
        self.kategLabel=QLabel(self)
        self.kategLabel.setText('Категория годности')
        self.kategText=QLineEdit(self)
        
        self.katZLabel=QLabel(self)
        self.katZLabel.setText('Категория запаса')
        self.katZText=QLineEdit(self)
        
        self.dateLabel=QLabel(self)
        self.dateLabel.setText('Дата')
        self.dateText=QLineEdit(self)
        
        self.writeBut=QPushButton(self)
        self.writeBut.setText("Записать")
        
        self.addBut=QPushButton(self)
        self.addBut.setText("Добавить еще одну запись")
        
        self.contBut=QPushButton(self)
        self.contBut.setText("Пропустить")
        
        self.vbrosBut=QPushButton(self)
        self.vbrosBut.setText("Вброс")
        
        self.exitBut=QPushButton(self)
        self.exitBut.setText("Выход")
        
        self.gridBox.addWidget(self.dateMesLabel, 0, 1, 2, 1)
        self.gridBox.addWidget(self.mesCntLabel, 2, 1, 2, 1)
        self.gridBox.addWidget(self.textScroll, 4, 1, 22, 1)
        
        self.textScroll.setWidget(self.mesText)
        
        self.gridBox.addWidget(self.ageLabel, 0, 2, 1, 1)
        self.gridBox.addWidget(self.ageText, 1, 2, 1, 1)
        
        self.gridBox.addWidget(self.causeLabel, 2, 2, 1, 1)
        self.gridBox.addWidget(self.causeText, 3, 2, 1, 1)
        
        self.gridBox.addWidget(self.vusLabel, 4, 2, 1, 1)
        self.gridBox.addWidget(self.vusText, 5, 2, 1, 1)
        
        self.gridBox.addWidget(self.countryLabel, 6, 2, 1, 1)
        self.gridBox.addWidget(self.countryText, 7, 2, 1, 1)
        
        self.gridBox.addWidget(self.kppLabel, 8, 2, 1, 1)
        self.gridBox.addWidget(self.kppText, 9, 2, 1, 1)
        
        self.gridBox.addWidget(self.yServiceLabel, 10, 2, 1, 1)
        self.gridBox.addWidget(self.yServiceText, 11, 2, 1, 1)
        
        self.gridBox.addWidget(self.voenkLabel, 12, 2, 1, 1)
        self.gridBox.addWidget(self.voenkText, 13, 2, 1, 1)
        
        self.gridBox.addWidget(self.kategLabel, 14, 2, 1, 1)
        self.gridBox.addWidget(self.kategText, 15, 2, 1, 1)
        
        self.gridBox.addWidget(self.katZLabel, 16, 2, 1, 1)
        self.gridBox.addWidget(self.katZText, 17, 2, 1, 1)
        
        self.gridBox.addWidget(self.dateLabel, 18, 2, 1, 1)
        self.gridBox.addWidget(self.dateText, 19, 2, 1, 1)
        
        self.gridBox.addWidget(self.writeBut, 20, 2, 1, 1)
        self.gridBox.addWidget(self.addBut, 21, 2, 1, 1)
        self.gridBox.addWidget(self.contBut, 22, 2, 1, 1)
        self.gridBox.addWidget(self.vbrosBut, 23, 2, 1, 1)
        self.gridBox.addWidget(self.exitBut, 24, 2, 1, 1)
        
        self.setLayout(self.gridBox)
        
        self.writeBut.clicked.connect(self.getInfo)
        self.addBut.clicked.connect(self.getInfo_add)
    
    @Slot(str)
    def setMes(self, mes):
        self.mesText.setText(mes)
    
    @Slot(str, str)
    def setDate(self, date, msgCnt):
        self.dateMesLabel.setText(date)
        self.mesCntLabel.setText(msgCnt)
        self.dateText.setText(date)
        
    def getInfo(self):
        age = self.ageText.text()
        cause = self.causeText.text()
        vus = self.vusText.text()
        country = self.countryText.text()
        kpp = self.kppText.text()
        yService = self.yServiceText.text()
        voenk = self.voenkText.text()
        kategory = self.kategText.text()
        katZ = self.katZText.text()
        date = self.dateText.text()
        
        self.ageText.setText("")
        self.causeText.setText("")
        self.vusText.setText("")
        self.countryText.setText("")
        self.kppText.setText("")
        self.yServiceText.setText("")
        self.voenkText.setText("")
        self.kategText.setText("")
        self.katZText.setText("")
        self.dateText.setText("")
        
        if date == "":
            date = self.dateMesLabel.text()
        
        self.sg.writeSignal.emit(age, cause, vus, country, kpp, yService, voenk, kategory, katZ, date)
        
    def getInfo_add(self):
        age = self.ageText.text()
        cause = self.causeText.text()
        vus = self.vusText.text()
        country = self.countryText.text()
        kpp = self.kppText.text()
        yService = self.yServiceText.text()
        voenk = self.voenkText.text()
        kategory = self.kategText.text()
        katZ = self.katZText.text()
        date = self.dateText.text()
        
        self.ageText.setText("")
        self.causeText.setText("")
        self.vusText.setText("")
        self.countryText.setText("")
        self.kppText.setText("")
        self.yServiceText.setText("")
        self.voenkText.setText("")
        self.kategText.setText("")
        self.katZText.setText("")
        #self.dateText.setText("")
        
        if date == "":
            date = self.dateMesLabel.text()
        
        self.sg.addSignal.emit(age, cause, vus, country, kpp, yService, voenk, kategory, katZ, date)    
        #return age, cause, vus, country, kpp, yService, voenk, kategory, date
        
if __name__ == "__main__":
    app = QApplication([])
    window = ui()
    window.show()
    sys.exit(app.exec_())
