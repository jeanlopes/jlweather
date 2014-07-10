#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4.QtGui import QIcon, QSystemTrayIcon, QApplication, QMenu, QAction,\
     qApp, QMessageBox
from PyQt4.QtCore import QString

class Eventer:

    @staticmethod
    def show_message(tray):
        tray.showMessage('info','temperatura')

    @staticmethod
    def show_about():
        box = QMessageBox()
        title = 'Sobre o JLWeather'
        text = ''' Este aplicativo foi constru&iacute;do por <b>Jean Lopes</b><br/>
                   Para mais informa&ccedil;&otilde;es, consulte o
                   <a href='http://github.com/jeanlopes'>reposit&oacute;rio</a>
               '''
        box.about(None, QString(title), QString(text))



class Menu(QMenu):

    def __init__(self):
        super(Menu, self).__init__()
        self.addAction(QAction('Mostrar Clima', self))
        self.addAction(QAction(QIcon.fromTheme('help-about'),'Sobre', self))
        exitAction = QAction(QIcon.fromTheme('application-exit'),'Sair', self)
        self.addAction(exitAction)


class WeatherTray(QSystemTrayIcon):

    def __init__(self):
        super(WeatherTray, self).__init__(QIcon.fromTheme('weather-clear'))
        self.setContextMenu(Menu())
        self.show()

        self.contextMenu()\
            .actions()[0]\
            .triggered\
            .connect(lambda: Eventer.show_message(self))

        self.contextMenu()\
            .actions()[1]\
            .triggered\
            .connect(Eventer.show_about)

        self.contextMenu()\
            .actions()[2]\
            .triggered\
            .connect(qApp.quit)
    

app = QApplication([])
tray = WeatherTray()
app.exec_()
