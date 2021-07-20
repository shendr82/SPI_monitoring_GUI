# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SPI_GUI1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1157, 954)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Big_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Big_textBrowser.sizePolicy().hasHeightForWidth())
        self.Big_textBrowser.setSizePolicy(sizePolicy)
        self.Big_textBrowser.setMinimumSize(QtCore.QSize(400, 50))
        self.Big_textBrowser.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Big_textBrowser.setObjectName("Big_textBrowser")
        self.gridLayout.addWidget(self.Big_textBrowser, 3, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Advanced_tab = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Advanced_tab.sizePolicy().hasHeightForWidth())
        self.Advanced_tab.setSizePolicy(sizePolicy)
        self.Advanced_tab.setMinimumSize(QtCore.QSize(560, 0))
        self.Advanced_tab.setMaximumSize(QtCore.QSize(520, 16777215))
        self.Advanced_tab.setObjectName("Advanced_tab")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Parameters_group = QtWidgets.QGroupBox(self.tab_6)
        self.Parameters_group.setMinimumSize(QtCore.QSize(0, 270))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Parameters_group.setFont(font)
        self.Parameters_group.setObjectName("Parameters_group")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Parameters_group)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ParamterPlot_button = QtWidgets.QPushButton(self.Parameters_group)
        self.ParamterPlot_button.setMinimumSize(QtCore.QSize(200, 40))
        self.ParamterPlot_button.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ParamterPlot_button.setFont(font)
        self.ParamterPlot_button.setObjectName("ParamterPlot_button")
        self.gridLayout_6.addWidget(self.ParamterPlot_button, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 2, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.Parameters_group)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 514, 304))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Parameter_listView = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.Parameter_listView.setObjectName("Parameter_listView")
        self.gridLayout_5.addWidget(self.Parameter_listView, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 3)
        self.verticalLayout.addWidget(self.Parameters_group)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem2)
        self.Advanced_tab.addTab(self.tab_6, "")
        self.verticalLayout_3.addWidget(self.Advanced_tab)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 2, 3, 1)
        self.ShotID_box = QtWidgets.QLineEdit(self.centralwidget)
        self.ShotID_box.setMinimumSize(QtCore.QSize(300, 30))
        self.ShotID_box.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ShotID_box.setFont(font)
        self.ShotID_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ShotID_box.setAlignment(QtCore.Qt.AlignCenter)
        self.ShotID_box.setObjectName("ShotID_box")
        self.gridLayout.addWidget(self.ShotID_box, 1, 1, 1, 1)
        self.Big_graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.Big_graphicsView.setMinimumSize(QtCore.QSize(500, 600))
        self.Big_graphicsView.setObjectName("Big_graphicsView")
        self.gridLayout.addWidget(self.Big_graphicsView, 2, 0, 1, 2)
        self.SPI_sensor_title = QtWidgets.QLabel(self.centralwidget)
        self.SPI_sensor_title.setMinimumSize(QtCore.QSize(500, 0))
        self.SPI_sensor_title.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SPI_sensor_title.setFont(font)
        self.SPI_sensor_title.setObjectName("SPI_sensor_title")
        self.gridLayout.addWidget(self.SPI_sensor_title, 0, 0, 1, 2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.ShotID_label = QtWidgets.QLabel(self.centralwidget)
        self.ShotID_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShotID_label.sizePolicy().hasHeightForWidth())
        self.ShotID_label.setSizePolicy(sizePolicy)
        self.ShotID_label.setMinimumSize(QtCore.QSize(50, 30))
        self.ShotID_label.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ShotID_label.setFont(font)
        self.ShotID_label.setObjectName("ShotID_label")
        self.horizontalLayout_9.addWidget(self.ShotID_label)
        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1157, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_TDMS_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_TDMS_file.setObjectName("actionOpen_TDMS_file")
        self.menuFile.addAction(self.actionOpen_TDMS_file)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.Advanced_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Parameters_group.setTitle(_translate("MainWindow", "List of parameters"))
        self.ParamterPlot_button.setText(_translate("MainWindow", "Plot chosen parameter"))
        self.Advanced_tab.setTabText(self.Advanced_tab.indexOf(self.tab_6), _translate("MainWindow", "Advanced"))
        self.ShotID_box.setText(_translate("MainWindow", "shotID"))
        self.SPI_sensor_title.setText(_translate("MainWindow", "SPI sensor data"))
        self.ShotID_label.setText(_translate("MainWindow", "Shot ID:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_TDMS_file.setText(_translate("MainWindow", "Open TDMS file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())