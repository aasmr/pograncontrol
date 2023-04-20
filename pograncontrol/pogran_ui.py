# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Signals(QObject):
    endInitSignal = Signal()
    writeSignal = Signal(str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str)
    addSignal = Signal(str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str)
    def __init__(self):
        super().__init__()

class fullMesUi(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        parent.sg.mesTxtFullSignal.connect(self.setMes)
        self.initUi()
    def initUi(self):
        self._width=500
        self._height=720
        self.setMinimumSize(self._width,self._height)
        self.setMaximumSize(self._width,self._height)
        self.setWindowTitle("Pograncotrol")
        self.mesText=QLabel(self)
        self.mesText.setFont("Sans Serif")
        self.mesText.setWordWrap(True)
        self.textScroll=QScrollArea(self)
        self.textScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textScroll.setWidgetResizable(True)
        self.textScroll.setContentsMargins(50, 50, 50 , 50)
        self.textScroll.setWidget(self.mesText)
        self.VBoxL = QVBoxLayout(self)
        self.VBoxL.addWidget(self.textScroll)
        self.setLayout(self.VBoxL)
    
    @Slot(str)
    def setMes(self, mes):
        self.mesText.setText(mes)
        
class ui(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        
        parent.sg.mesTxtSignal.connect(self.setMes)
        parent.sg.mesDateSignal.connect(self.setDate)
        parent.sg.mesSetCompleter.connect(self.setComplt)
        parent.sg.mesStatus.connect(self.setStatus)
        self.sg = Signals()
        self.initUi()        

    def initUi(self):
        self._width=720
        self._height=720
        self.setMinimumSize(self._width,self._height)
        self.setMaximumSize(self._width,self._height)
        self.setWindowTitle("Pograncotrol")
        self.textScroll=QScrollArea(self)
        self.VBoxL = QVBoxLayout(self)
        self.otherScroll=QScrollArea(self)
        self.textScroll.setFixedWidth(350)
        self.textScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textScroll.setWidgetResizable(True)
        self.textScroll.setContentsMargins(50, 50, 50 , 50)
        self.otherScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.otherScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.otherScroll.setWidgetResizable(True)
        self.otherScroll.setContentsMargins(50, 50, 50 , 50)
        self.gridBox=QGridLayout(self)
        self.gridBox.setContentsMargins(5, 5, 5, 5)
        
        self.statusLabel = QLabel(self)
        self.statusLabel.setText("")
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
        
        self.typeLabel=QLabel(self)
        self.typeLabel.setText('Тип случая')
        self.typeText=QLineEdit(self)
        
        self.sexLabel=QLabel(self)
        self.sexLabel.setText('Пол')
        self.sexText=QLineEdit(self)
        
        self.ageLabel=QLabel(self)
        self.ageLabel.setText('Возраст')
        self.ageText=QLineEdit(self)
        
        self.causeLabel=QLabel(self)
        self.causeLabel.setText('Причина')
        self.causeText=QLineEdit(self)
        self.causeCmplt=QCompleter(self)
        self.causeCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.causeText.setCompleter(self.causeCmplt)
        
        self.armyRelLabel=QLabel(self)
        self.armyRelLabel.setText('Отношение к военной службе')
        self.armyRelText=QLineEdit(self)
        self.armyRelCmplt=QCompleter(self)
        self.armyRelCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.armyRelText.setCompleter(self.armyRelCmplt)
        
        self.vusLabel=QLabel(self)
        self.vusLabel.setText('ВУС')
        self.vusText=QLineEdit(self)
        self.vusCmplt=QCompleter(self)
        self.vusCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.vusText.setCompleter(self.vusCmplt)
        
        self.armyTypeLabel=QLabel(self)
        self.armyTypeLabel.setText('Вид войск')
        self.armyTypeText=QLineEdit(self)
        self.armyTypeCmplt=QCompleter(self)
        self.armyTypeCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.armyTypeText.setCompleter(self.armyTypeCmplt)
        
        self.armySecTypeLabel=QLabel(self)
        self.armySecTypeLabel.setText('Род войск')
        self.armySecTypeText=QLineEdit(self)
        self.armySecTypeCmplt=QCompleter(self)
        self.armySecTypeCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.armySecTypeText.setCompleter(self.armySecTypeCmplt)
        
        self.armyOtherLabel=QLabel(self)
        self.armyOtherLabel.setText('Другая информация о военной службе')
        self.armyOtherText=QLineEdit(self)
        self.armyOtherCmplt=QCompleter(self)
        self.armyOtherCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.armyOtherText.setCompleter(self.armyOtherCmplt)
        
        self.countryLabel=QLabel(self)
        self.countryLabel.setText('Страна въезда')
        self.countryText=QLineEdit(self)
        self.countryCmplt=QCompleter(self)
        self.countryCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.countryText.setCompleter(self.countryCmplt)
        
        self.kppLabel=QLabel(self)
        self.kppLabel.setText('КПП выезда')
        self.kppText=QLineEdit(self)
        self.kppCmplt=QCompleter(self)
        self.kppCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.kppText.setCompleter(self.kppCmplt)
        
        self.yServiceLabel=QLabel(self)
        self.yServiceLabel.setText('Годы службы')
        self.yServiceText=QLineEdit(self)
        self.yServiceCmplt=QCompleter(self)
        self.yServiceCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.yServiceText.setCompleter(self.yServiceCmplt)
        
        self.voenkRegLabel=QLabel(self)
        self.voenkRegLabel.setText('Военкомат (регион или город федерального значения)')
        self.voenkRegText=QLineEdit(self)
        self.voenkRegCmplt=QCompleter(self)
        self.voenkRegCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.voenkRegText.setCompleter(self.voenkRegCmplt)
        
        self.voenkCityLabel=QLabel(self)
        self.voenkCityLabel.setText('Военкомат (город(а)/городской округ/район(ы) области)')
        self.voenkCityText=QLineEdit(self)
        self.voenkCityCmplt=QCompleter(self)
        self.voenkCityCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.voenkCityText.setCompleter(self.voenkCityCmplt)
        
        self.voenkDistrictLabel=QLabel(self)
        self.voenkDistrictLabel.setText('Военкомат (район(ы) города)')
        self.voenkDistrictText=QLineEdit(self)
        self.voenkDistrictCmplt=QCompleter(self)
        self.voenkDistrictCmplt.setCaseSensitivity(Qt.CaseInsensitive)
        self.voenkDistrictText.setCompleter(self.voenkDistrictCmplt)
        
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
        
        self.dltBut=QPushButton(self)
        self.dltBut.setText("Удалить это сообщение из БД")
        
        self.showBut=QPushButton(self)
        self.showBut.setText("Показать сообщение целиком")
        
        self.exitBut=QPushButton(self)
        self.exitBut.setText("Выход")
        
        self.gridBox.addWidget(self.statusLabel, 0, 1, 1, 1)
        self.gridBox.addWidget(self.dateMesLabel, 1, 1, 1, 1)
        self.gridBox.addWidget(self.mesCntLabel, 2, 1, 1, 1)
        self.gridBox.addWidget(self.textScroll, 3, 1, 9, 1)
        self.gridBox.addWidget(self.otherScroll, 0, 2, 12, 1)
        
        self.textScroll.setWidget(self.mesText)
        
        self.wdg=QWidget(self)
        
        self.VBoxL.addWidget(self.typeLabel)
        self.VBoxL.addWidget(self.typeText)
        
        self.VBoxL.addWidget(self.sexLabel)
        self.VBoxL.addWidget(self.sexText)
        
        self.VBoxL.addWidget(self.ageLabel)
        self.VBoxL.addWidget(self.ageText)
        
        self.VBoxL.addWidget(self.causeLabel)
        self.VBoxL.addWidget(self.causeText)
        
        self.VBoxL.addWidget(self.armyRelLabel)
        self.VBoxL.addWidget(self.armyRelText)
        
        self.VBoxL.addWidget(self.vusLabel)
        self.VBoxL.addWidget(self.vusText)
        
        self.VBoxL.addWidget(self.armyTypeLabel)
        self.VBoxL.addWidget(self.armyTypeText)
        
        self.VBoxL.addWidget(self.armySecTypeLabel)
        self.VBoxL.addWidget(self.armySecTypeText)
        
        self.VBoxL.addWidget(self.armyOtherLabel)
        self.VBoxL.addWidget(self.armyOtherText)
        
        self.VBoxL.addWidget(self.countryLabel)
        self.VBoxL.addWidget(self.countryText)
        
        self.VBoxL.addWidget(self.kppLabel)
        self.VBoxL.addWidget(self.kppText)
        
        self.VBoxL.addWidget(self.yServiceLabel)
        self.VBoxL.addWidget(self.yServiceText)
        
        self.VBoxL.addWidget(self.voenkRegLabel)
        self.VBoxL.addWidget(self.voenkRegText)
        
        self.VBoxL.addWidget(self.voenkCityLabel)
        self.VBoxL.addWidget(self.voenkCityText)
        
        self.VBoxL.addWidget(self.voenkDistrictLabel)
        self.VBoxL.addWidget(self.voenkDistrictText)
        
        self.VBoxL.addWidget(self.kategLabel)
        self.VBoxL.addWidget(self.kategText)
        
        self.VBoxL.addWidget(self.katZLabel)
        self.VBoxL.addWidget(self.katZText)
        
        self.VBoxL.addWidget(self.dateLabel)
        self.VBoxL.addWidget(self.dateText)
        
        self.VBoxL.addWidget(self.writeBut)
        self.VBoxL.addWidget(self.addBut)
        self.VBoxL.addWidget(self.contBut)
        self.VBoxL.addWidget(self.vbrosBut)
        self.VBoxL.addWidget(self.dltBut)
        self.VBoxL.addWidget(self.showBut)
        self.VBoxL.addWidget(self.exitBut)
        
        self.wdg.setLayout(self.VBoxL)
        self.otherScroll.setWidget(self.wdg)
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
        
    @Slot(list, list, list, list, list, list, list, list, list, list, list, list)
    def setComplt(self, cause, army_rel, vus, army_type, army_sec_type, army_other, country, kpp, yService, voenk_reg, voenk_city, voenk_dis):
        cause_m=QStringListModel(self)
        cause_m.setStringList(cause)
        self.causeCmplt.setModel(cause_m)
        
        army_rel_m=QStringListModel(self)
        army_rel_m.setStringList(army_rel)
        self.armyRelCmplt.setModel(army_rel_m)
        
        vus_m=QStringListModel(self)
        vus_m.setStringList(vus)   
        self.vusCmplt.setModel(vus_m)
        
        army_type_m=QStringListModel(self)
        army_type_m.setStringList(army_type)
        self.armyTypeCmplt.setModel(army_type_m)
        
        army_sec_type_m=QStringListModel(self)
        army_sec_type_m.setStringList(army_sec_type)
        self.armySecTypeCmplt.setModel(army_sec_type_m)
        
        army_other_m=QStringListModel(self)
        army_other_m.setStringList(army_other)
        self.armyOtherCmplt.setModel(army_other_m)
        
        country_m=QStringListModel(self)
        country_m.setStringList(country) 
        self.countryCmplt.setModel(country_m)
        
        kpp_m=QStringListModel(self)
        kpp_m.setStringList(kpp) 
        self.kppCmplt.setModel(kpp_m)
        
        yService_m=QStringListModel(self)
        yService_m.setStringList(yService) 
        self.yServiceCmplt.setModel(yService_m)
        
        voenk_reg_m=QStringListModel(self)
        voenk_reg_m.setStringList(voenk_reg) 
        self.voenkRegCmplt.setModel(voenk_reg_m)
        
        voenk_city_m=QStringListModel(self)
        voenk_city_m.setStringList(voenk_city) 
        self.voenkCityCmplt.setModel(voenk_city_m)
        
        voenk_dis_m=QStringListModel(self)
        voenk_dis_m.setStringList(voenk_dis) 
        self.voenkDistrictCmplt.setModel(voenk_dis_m)
    @Slot(str)
    def setStatus(self, status):
        self.statusLabel.setText(status)
    def getInfo(self):
        type = self.typeText.text()
        sex = self.sexText.text()
        age = self.ageText.text()
        cause = self.causeText.text()
        army_rel = self.armyRelText.text()
        vus = self.vusText.text()
        army_type = self.armyTypeText.text()
        army_sec_type = self.armySecTypeText.text()
        army_other = self.armyOtherText.text()
        country = self.countryText.text()
        kpp = self.kppText.text()
        yService = self.yServiceText.text()
        voenk_reg = self.voenkRegText.text()
        voenk_city = self.voenkCityText.text()
        voenk_dis = self.voenkDistrictText.text()
        kategory = self.kategText.text()
        katZ = self.katZText.text()
        date = self.dateText.text()
        
        self.typeText.setText("")
        self.sexText.setText("")
        self.ageText.setText("")
        self.causeText.setText("")
        self.armyRelText.setText("")
        self.vusText.setText("")
        self.armyTypeText.setText("")
        self.armySecTypeText.setText("")
        self.armyOtherText.setText("")
        self.countryText.setText("")
        self.kppText.setText("")
        self.yServiceText.setText("")
        self.voenkRegText.setText("")
        self.voenkCityText.setText("")
        self.voenkDistrictText.setText("")
        self.kategText.setText("")
        self.katZText.setText("")
        self.dateText.setText("")
        
        if date == "":
            date = self.dateMesLabel.text()
        
        self.sg.writeSignal.emit(type, sex, age, cause, army_rel, vus, army_type, army_sec_type, army_other, country, kpp, yService, voenk_reg, voenk_city, voenk_dis, kategory, katZ, date)
        
    def getInfo_add(self):
        type = self.typeText.text()
        sex = self.sexText.text()
        age = self.ageText.text()
        cause = self.causeText.text()
        army_rel = self.armyRelText.text()
        vus = self.vusText.text()
        army_type = self.armyTypeText.text()
        army_sec_type = self.armySecTypeText.text()
        army_other = self.armyOtherText.text()
        country = self.countryText.text()
        kpp = self.kppText.text()
        yService = self.yServiceText.text()
        voenk_reg = self.voenkRegText.text()
        voenk_city = self.voenkCityText.text()
        voenk_dis = self.voenkDistrictText.text()
        kategory = self.kategText.text()
        katZ = self.katZText.text()
        date = self.dateText.text()
        
        #self.ageText.setText("")
        #self.causeText.setText("")
        #self.vusText.setText("")
        #self.countryText.setText("")
        #self.kppText.setText("")
        #self.yServiceText.setText("")
        #self.voenkText.setText("")
        #self.kategText.setText("")
        #self.katZText.setText("")
        #self.dateText.setText("")
        
        if date == "":
            date = self.dateMesLabel.text()
        
        self.sg.addSignal.emit(type, sex, age, cause, army_rel, vus, army_type, army_sec_type, army_other, country, kpp, yService, voenk_reg, voenk_city, voenk_dis, kategory, katZ, date)    
        #return age, cause, vus, country, kpp, yService, voenk, kategory, date
        
if __name__ == "__main__":
    app = QApplication([])
    window = ui()
    window.show()
    sys.exit(app.exec_())
