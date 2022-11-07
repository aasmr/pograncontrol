# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Signals(QObject):
    endInitSignal = Signal()
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
        self.gridBox=QGridLayout(self)
        self.gridBox.setContentsMargins(5, 5, 5, 5)
        
        self.mesText=QLabel(self)
        self.dateMesLabel=QLabel(self)
        self.mesText.setText("")
        self.mesText.setFixedWidth(500)
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
        
        self.dateLabel=QLabel(self)
        self.dateLabel.setText('Дата')
        self.dateText=QLineEdit(self)
        
        self.nextBut=QPushButton(self)
        self.nextBut.setText("Следующая")
        
        self.contBut=QPushButton(self)
        self.contBut.setText("Пропустить")
        
        self.vbrosBut=QPushButton(self)
        self.vbrosBut.setText("Вброс")
        
        self.exitBut=QPushButton(self)
        self.exitBut.setText("Выход")
        
        self.gridBox.addWidget(self.mesText, 0, 1, 3, 1)
        self.gridBox.addWidget(self.dateMesLabel, 3, 1, 17, 1)
        
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
        
        self.gridBox.addWidget(self.dateLabel, 14, 2, 1, 1)
        self.gridBox.addWidget(self.dateText, 15, 2, 1, 1)
        
        self.gridBox.addWidget(self.nextBut, 16, 2, 1, 1)
        self.gridBox.addWidget(self.contBut, 17, 2, 1, 1)
        self.gridBox.addWidget(self.vbrosBut, 18, 2, 1, 1)
        self.gridBox.addWidget(self.exitBut, 19, 2, 1, 1)
        
        self.setLayout(self.gridBox)
        
        
    
    @Slot(str)
    def setMes(self, mes):
        self.mesText.setText(mes)
    
    @Slot(str)
    def setDate(self, date):
        self.dateMesLabel.setText(date)
        
    def getInfo(self):
        age = self.ageText.text()
        cause = self.causeText.text()
        vus = self.vusText.text()
        country = self.countryText.text()
        kpp = self.kppText.text()
        yService = self.yServiceText.text()
        voenk = self.voenkText.text()
        date = self.dateText.text()
        
        if date == "":
            date = self.dateMesLabel.text()
            
        return age, cause, vus, country, kpp, yService, voenk, date
        
if __name__ == "__main__":
    app = QApplication([])
    window = ui()
    window.show()
    sys.exit(app.exec_())
