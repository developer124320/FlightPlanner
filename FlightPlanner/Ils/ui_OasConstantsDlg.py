# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OasConstantsDlg.ui'
#
# Created: Fri Mar 20 08:46:07 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OasConstantsDlg(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 218)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.txtWA = QtGui.QLineEdit(self.groupBox)
        self.txtWA.setObjectName(_fromUtf8("txtWA"))
        self.gridLayout.addWidget(self.txtWA, 1, 1, 1, 1)
        self.txtWSA = QtGui.QLineEdit(self.groupBox)
        self.txtWSA.setObjectName(_fromUtf8("txtWSA"))
        self.gridLayout.addWidget(self.txtWSA, 2, 1, 1, 1)
        self.txtXA = QtGui.QLineEdit(self.groupBox)
        self.txtXA.setObjectName(_fromUtf8("txtXA"))
        self.gridLayout.addWidget(self.txtXA, 3, 1, 1, 1)
        self.txtYA = QtGui.QLineEdit(self.groupBox)
        self.txtYA.setObjectName(_fromUtf8("txtYA"))
        self.gridLayout.addWidget(self.txtYA, 4, 1, 1, 1)
        self.txtZA = QtGui.QLineEdit(self.groupBox)
        self.txtZA.setObjectName(_fromUtf8("txtZA"))
        self.gridLayout.addWidget(self.txtZA, 5, 1, 1, 1)
        self.txtXB = QtGui.QLineEdit(self.groupBox)
        self.txtXB.setObjectName(_fromUtf8("txtXB"))
        self.gridLayout.addWidget(self.txtXB, 3, 2, 1, 1)
        self.txtYB = QtGui.QLineEdit(self.groupBox)
        self.txtYB.setObjectName(_fromUtf8("txtYB"))
        self.gridLayout.addWidget(self.txtYB, 4, 2, 1, 1)
        self.txtWC = QtGui.QLineEdit(self.groupBox)
        self.txtWC.setObjectName(_fromUtf8("txtWC"))
        self.gridLayout.addWidget(self.txtWC, 1, 3, 1, 1)
        self.txtWSC = QtGui.QLineEdit(self.groupBox)
        self.txtWSC.setObjectName(_fromUtf8("txtWSC"))
        self.gridLayout.addWidget(self.txtWSC, 2, 3, 1, 1)
        self.txtXC = QtGui.QLineEdit(self.groupBox)
        self.txtXC.setObjectName(_fromUtf8("txtXC"))
        self.gridLayout.addWidget(self.txtXC, 3, 3, 1, 1)
        self.txtYC = QtGui.QLineEdit(self.groupBox)
        self.txtYC.setObjectName(_fromUtf8("txtYC"))
        self.gridLayout.addWidget(self.txtYC, 4, 3, 1, 1)
        self.txtZC = QtGui.QLineEdit(self.groupBox)
        self.txtZC.setObjectName(_fromUtf8("txtZC"))
        self.gridLayout.addWidget(self.txtZC, 5, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
#         QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "OAS Constants", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "W", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "W\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "B", None, QtGui.QApplication.UnicodeUTF8))

