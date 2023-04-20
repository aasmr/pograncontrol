import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Signals(QObject):
    endInitSignal = Signal()
    writeSignal = Signal(str)
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
        self.mesText.setTextInteractionFlags(Qt.TextSelectableByMouse)
        #self.mesText.setTextFormat()
        self.dateMesLabel=QLabel(self)
        self.mesText.setText("")
        #self.mesText.setFixedWidth(500)
        self.dateMesLabel.setText("")

        self.sepLabel=QLabel(self)
        self.sepLabel.setText('Сепаратор:')
        self.sepText=QLineEdit(self)
        self.passBut=QPushButton(self)
        self.passBut.setText("Пропустить")
        self.separate1But=QPushButton(self)
        self.separate1But.setText("Разделить")
        self.writeBut=QPushButton(self)
        self.writeBut.setText("Записать")
       
        self.exitBut=QPushButton(self)
        self.exitBut.setText("Выход")
        
        self.gridBox.addWidget(self.dateMesLabel, 0, 1, 2, 1)
        self.gridBox.addWidget(self.mesCntLabel, 2, 1, 2, 1)
        self.gridBox.addWidget(self.textScroll, 4, 1, 22, 1)
        
        self.textScroll.setWidget(self.mesText)
        self.gridBox.addWidget(self.sepLabel, 0, 2, 1, 1)
        self.gridBox.addWidget(self.sepText, 1, 2, 1, 1)
        self.gridBox.addWidget(self.separate1But, 2, 2, 1, 1)
        self.gridBox.addWidget(self.writeBut, 3, 2, 1, 1)
        self.gridBox.addWidget(self.passBut, 4, 2, 1, 1)
        self.gridBox.addWidget(self.exitBut, 5, 2, 1, 1)
        
        self.setLayout(self.gridBox)

        self.separate1But.clicked.connect(self.getInfo)

    
    @Slot(str)
    def setMes(self, mes):
        self.mesText.setText(mes)
	
    @Slot(str)
    def setDate(self, msgCnt):
        self.mesCntLabel.setText(msgCnt)

    def getInfo(self):
        sep = self.sepText.text()
        self.sg.writeSignal.emit(sep)
        
        
if __name__ == "__main__":
    app = QApplication([])
    window = ui()
    window.show()
    sys.exit(app.exec_())
