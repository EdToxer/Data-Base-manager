# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(943, 651)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnRemove = QPushButton(self.centralwidget)
        self.btnRemove.setObjectName(u"btnRemove")

        self.gridLayout_2.addWidget(self.btnRemove, 1, 0, 1, 1)

        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setObjectName(u"btnEdit")

        self.gridLayout_2.addWidget(self.btnEdit, 0, 1, 1, 1)

        self.cmbCompanies = QComboBox(self.centralwidget)
        self.cmbCompanies.setObjectName(u"cmbCompanies")

        self.gridLayout_2.addWidget(self.cmbCompanies, 1, 1, 1, 1)

        self.QChartView3 = QChartView(self.centralwidget)
        self.QChartView3.setObjectName(u"QChartView3")

        self.gridLayout_2.addWidget(self.QChartView3, 0, 2, 3, 1)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout_2.addWidget(self.btnAdd, 0, 0, 1, 1)

        self.tblItems = QTableView(self.centralwidget)
        self.tblItems.setObjectName(u"tblItems")

        self.gridLayout_2.addWidget(self.tblItems, 2, 0, 2, 2)

        self.QChartView2 = QChartView(self.centralwidget)
        self.QChartView2.setObjectName(u"QChartView2")

        self.gridLayout_2.addWidget(self.QChartView2, 3, 2, 2, 1)

        self.QChartView1 = QChartView(self.centralwidget)
        self.QChartView1.setObjectName(u"QChartView1")

        self.gridLayout_2.addWidget(self.QChartView1, 1, 3, 4, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbStatistics = QLabel(self.groupBox)
        self.lbStatistics.setObjectName(u"lbStatistics")
        self.lbStatistics.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout.addWidget(self.lbStatistics, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 4, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnEdit.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.lbStatistics.setText("")
    # retranslateUi

