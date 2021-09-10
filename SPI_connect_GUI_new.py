# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:21:44 2021

@author: ShendR
"""

from SPI_GUI1 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QDialog

import spi_class_new

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class SPI_GUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
            # Canvas on GUI       
        self.Big_graphicsView = Canvas(parent=self.centralwidget)
        self.Big_graphicsView.setMinimumSize(QtCore.QSize(500, 400))
        self.Big_graphicsView.setObjectName("Big_graphicsView")
        self.gridLayout.addWidget(self.Big_graphicsView, 2, 0, 1, 2)
            # Toolbar on GUI
        self.toolbar = NavigationToolbar(self.Big_graphicsView, self.Big_graphicsView)       
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
            # SPI data Class
        self.spi_tdms = spi_class_new.SPI_tDMS_Data()
            # Open file with GUI - button or Ctrl+O
        self.menuFile.triggered.connect((lambda: self.open_file()))
        self.actionOpen_TDMS_file.setShortcut('Ctrl+O')
        
            # Set up TextBox - for adding text messages
        self.setup_logbook()
            
            # Button cliked - select channel from list
        self.ParamterPlot_button.clicked.connect(lambda: self.plot_button(self.Big_graphicsView, self.selected_item))
        
        

        # After a file is opened - update GUI        
    def open_file(self):  
        self.spi_tdms.run_open_tdms()
        shot_id = self.spi_tdms.root_obj_values[0]
        self.ShotID_box.setText(shot_id)
        self.Parameter_listView.clear()
        self.Parameter_listView.setAlternatingRowColors(True)
        channels = self.spi_tdms.channels
        for i in channels:
            self.Parameter_listView.addItem(str(i))
        self.Parameter_listView.itemClicked.connect(self.listitemclicked)


        # Button cliked - select channel from list
    def listitemclicked(self):
        self.selected_item = self.Parameter_listView.currentItem().text()
        self.logbook.append('Item in the list is clicked:  ' + self.selected_item)
        return self.selected_item
    
    
        # Set up TextBox - for adding messages
    def setup_logbook(self, text='check'):
        self.logbook = self.Big_textBrowser
        font = self.logbook.font()
        font.setFamily("Courier")
        font.setPointSize(8)        
        self.logbook.append("Welcome to SPI sensor data: Open file")
        self.logbook.moveCursor(QtGui.QTextCursor.End)
        self.logbook.setStyleSheet("color: black; background-color: white;")
        self.logbook.ensureCursorVisible()
        
        
        # When Plot Button is pushed - running this method
    def plot_button(self, canvas, item):
        try:
            self.spi_tdms.plot_clicked(canvas, item)
            self.logbook.append('Plotting selected item: ' + item)
        except:
            self.logbook.append("No item selected")
        

    # Canvas on GUI to plot on
class Canvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        super(Canvas, self).__init__(self.fig)      
        
       
         
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    
    widget = SPI_GUI()
    widget.show()
    
    app.exec_()