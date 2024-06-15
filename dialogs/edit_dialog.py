# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.txtRating = QLineEdit(Dialog)
        self.txtRating.setObjectName(u"txtRating")

        self.gridLayout.addWidget(self.txtRating, 1, 1, 1, 2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.txtClient = QLineEdit(Dialog)
        self.txtClient.setObjectName(u"txtClient")

        self.gridLayout.addWidget(self.txtClient, 2, 1, 1, 2)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.txtProfit = QLineEdit(Dialog)
        self.txtProfit.setObjectName(u"txtProfit")

        self.gridLayout.addWidget(self.txtProfit, 3, 1, 1, 2)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.txtAge = QLineEdit(Dialog)
        self.txtAge.setObjectName(u"txtAge")

        self.gridLayout.addWidget(self.txtAge, 4, 1, 1, 2)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.txtCover = QLineEdit(Dialog)
        self.txtCover.setObjectName(u"txtCover")

        self.gridLayout.addWidget(self.txtCover, 5, 1, 1, 2)

        self.btnAdd = QPushButton(Dialog)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout.addWidget(self.btnAdd, 6, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(217, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 2, 1, 1)

        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")

        self.gridLayout.addWidget(self.btnCancel, 6, 3, 1, 1)

        self.cmbCompany = QComboBox(Dialog)
        self.cmbCompany.setObjectName(u"cmbCompany")

        self.gridLayout.addWidget(self.cmbCompany, 0, 1, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043b\u043e\u0436\u043a\u0430", None))
        self.btnAdd.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

