#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4.QtGui import QIcon, QSystemTrayIcon, QApplication, QMenu, QAction,\
     qApp, QMessageBox, QPushButton, QLineEdit, QLabel, QWidget
from PyQt4.QtCore import QString
from weather_client import WeatherClient
import weather_consts
import pdb

class Eventer:
    ''' Cuida dos eventos disparados'''

    @staticmethod
    def show_weather_forecast_message(tray):

        wc = WeatherClient()
        forecast, temperature = wc.reload_weather_info()

        ico = weather_consts.weather_types.get(forecast)
        if ico:
            tray.setIcon(QIcon.fromTheme())
        tray.showMessage('Tempo agora:', (temperature + '°C ' + forecast).decode('utf-8'))

    @staticmethod
    def show_about():
        box = QMessageBox()
        title = 'Sobre o JLWeather'
        text = ''' Este aplicativo foi constru&iacute;do por <b>Jean Lopes</b><br/>
                   Para mais informa&ccedil;&otilde;es, consulte o
                   <a href='http://github.com/jeanlopes'>reposit&oacute;rio</a>
               '''
        box.about(None, QString(title), QString(text))

    @staticmethod
    def show_settings():
        LocalityWidGet()


    @staticmethod
    def save_new_locality(widget):
        locality_text = widget.locality_input_text.getText()
        locality_text = locality_text.split(',')

        if len(locality_text) > 0:
            wc = WeatherClient()
            wc.set_place(locality_text[0].strip(),\
                         locality_text[1].strip() if len(locality_text) > 1 else '')
        widget.close()


class LocalityWidGet(QWidget):
    """Modal para alterer a localidade da previção do tempo"""
    
    def __init__(self):
        super(LocalityWidGet, self).__init__()
        
        self.setWindowTitle = 'Settings'
        self.setGeometry(450, 300, 400, 200)

        self.locality_label = QLabel('Localidade: ',self)
        self.locality_label.move(20, 35)

        self.locality_label_example = QLabel('Exemplo: Porto Alegre, RS', self)
        self.locality_label_example.move(100, 60)

        self.locality_input_text = QLineEdit(self)
        self.locality_input_text.move(100, 30)

        wc = WeatherClient()
        current_locality = wc.get_place()
        self.locality_input_text.setText(current_locality.replace('+', ', ').decode('utf-8'))

        self.btnOk = QPushButton('OK', self)
        self.btnOk.move(250, 150)
        self.btnOk.clicked.connect(lambda: Eventer.save_new_locality(self))


        self.show()



class Menu(QMenu):

    def __init__(self):
        super(Menu, self).__init__()

        self.addAction(QAction('Mostrar Clima', self))
        
        action_about = QAction(QIcon.fromTheme('help-about'),'Sobre', self)
        action_about.triggered.connect(Eventer.show_about)
        self.addAction(action_about)

        action_settings = QAction(QIcon.fromTheme('emblem-system'), u'Configurações', self)
        action_settings.triggered.connect(Eventer.show_settings)
        self.addAction(action_settings)
        
        exitAction = QAction(QIcon.fromTheme('application-exit'),'Sair', self)
        exitAction.triggered.connect(qApp.quit)
        self.addAction(exitAction)


class WeatherTray(QSystemTrayIcon):

    def __init__(self):
        super(WeatherTray, self).__init__(QIcon.fromTheme('weather-clear'))
        self.setContextMenu(Menu())
        self.show()

        self.contextMenu()\
            .actions()[0]\
            .triggered\
            .connect(lambda: Eventer.show_weather_forecast_message(self))




app = QApplication([])
tray = WeatherTray()
app.exec_()