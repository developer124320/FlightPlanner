# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DepartureNominal.ui'
#
# Created: Wed Nov 25 15:30:17 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DepartureNominal(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(666, 456)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        Form.setFont(font)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frmoMain = QtGui.QFrame(Form)
        self.frmoMain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmoMain.setFrameShadow(QtGui.QFrame.Raised)
        self.frmoMain.setObjectName(_fromUtf8("frmoMain"))
        self.vLayout_Main = QtGui.QVBoxLayout(self.frmoMain)
        self.vLayout_Main.setSpacing(0)
        self.vLayout_Main.setMargin(0)
        self.vLayout_Main.setObjectName(_fromUtf8("vLayout_Main"))
        self.gbP1 = QtGui.QGroupBox(self.frmoMain)
        self.gbP1.setObjectName(_fromUtf8("gbP1"))
        self.vLayout_P1 = QtGui.QVBoxLayout(self.gbP1)
        self.vLayout_P1.setObjectName(_fromUtf8("vLayout_P1"))
        self.frame_IasMA = QtGui.QFrame(self.gbP1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_IasMA.sizePolicy().hasHeightForWidth())
        self.frame_IasMA.setSizePolicy(sizePolicy)
        self.frame_IasMA.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_IasMA.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_IasMA.setObjectName(_fromUtf8("frame_IasMA"))
        self.horizontalLayout_27 = QtGui.QHBoxLayout(self.frame_IasMA)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setMargin(0)
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.label_4 = QtGui.QLabel(self.frame_IasMA)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(63, 0))
        self.label_4.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_27.addWidget(self.label_4)
        self.txtAltitudeM1 = QtGui.QLineEdit(self.frame_IasMA)
        self.txtAltitudeM1.setEnabled(False)
        self.txtAltitudeM1.setObjectName(_fromUtf8("txtAltitudeM1"))
        self.txtAltitudeM1.setMinimumSize(QtCore.QSize(90, 0))
        self.txtAltitudeM1.setMaximumSize(QtCore.QSize(90, 121221))
        self.horizontalLayout_27.addWidget(self.txtAltitudeM1)
        self.label_5 = QtGui.QLabel(self.frame_IasMA)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_27.addWidget(self.label_5)
        self.txtAltitude1 = QtGui.QLineEdit(self.frame_IasMA)
        self.txtAltitude1.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAltitude1.sizePolicy().hasHeightForWidth())
        self.txtAltitude1.setSizePolicy(sizePolicy)
        self.txtAltitude1.setMinimumSize(QtCore.QSize(90, 0))
        self.txtAltitude1.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtAltitude1.setFont(font)
        self.txtAltitude1.setText(_fromUtf8(""))
        self.txtAltitude1.setObjectName(_fromUtf8("txtAltitude1"))
        self.horizontalLayout_27.addWidget(self.txtAltitude1)
        self.label_6 = QtGui.QLabel(self.frame_IasMA)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_27.addWidget(self.label_6)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(horizontalSpacer)
        self.vLayout_P1.addWidget(self.frame_IasMA)
        self.vLayout_Main.addWidget(self.gbP1)
        self.gbP2 = QtGui.QGroupBox(self.frmoMain)
        self.gbP2.setObjectName(_fromUtf8("gbP2"))
        self.vLayout_p2 = QtGui.QVBoxLayout(self.gbP2)
        self.vLayout_p2.setObjectName(_fromUtf8("vLayout_p2"))
        self.frame_IasMA_2 = QtGui.QFrame(self.gbP2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_IasMA_2.sizePolicy().hasHeightForWidth())
        self.frame_IasMA_2.setSizePolicy(sizePolicy)
        self.frame_IasMA_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_IasMA_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_IasMA_2.setObjectName(_fromUtf8("frame_IasMA_2"))
        self.horizontalLayout_31 = QtGui.QHBoxLayout(self.frame_IasMA_2)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setMargin(0)
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.label_15 = QtGui.QLabel(self.frame_IasMA_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(63, 0))
        self.label_15.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_31.addWidget(self.label_15)
        self.txtAltitudeM2 = QtGui.QLineEdit(self.frame_IasMA_2)
        self.txtAltitudeM2.setEnabled(False)
        self.txtAltitudeM2.setObjectName(_fromUtf8("txtAltitudeM2"))
        self.txtAltitudeM2.setMinimumSize(QtCore.QSize(90, 0))
        self.txtAltitudeM2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.horizontalLayout_31.addWidget(self.txtAltitudeM2)
        self.label_7 = QtGui.QLabel(self.frame_IasMA_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_31.addWidget(self.label_7)
        self.txtAltitude2 = QtGui.QLineEdit(self.frame_IasMA_2)
        self.txtAltitude2.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAltitude2.sizePolicy().hasHeightForWidth())
        self.txtAltitude2.setSizePolicy(sizePolicy)
        self.txtAltitude2.setMinimumSize(QtCore.QSize(90, 0))
        self.txtAltitude2.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtAltitude2.setFont(font)
        self.txtAltitude2.setText(_fromUtf8(""))
        self.txtAltitude2.setObjectName(_fromUtf8("txtAltitude2"))
        self.horizontalLayout_31.addWidget(self.txtAltitude2)
        self.label_8 = QtGui.QLabel(self.frame_IasMA_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_31.addWidget(self.label_8)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(horizontalSpacer)
        self.vLayout_p2.addWidget(self.frame_IasMA_2)
        self.vLayout_Main.addWidget(self.gbP2)
        self.gbAeroData = QtGui.QGroupBox(self.frmoMain)
        self.gbAeroData.setObjectName(_fromUtf8("gbAeroData"))
        self.verticalLayout_gbAeroData = QtGui.QVBoxLayout(self.gbAeroData)
        self.verticalLayout_gbAeroData.setObjectName(_fromUtf8("verticalLayout_gbAeroData"))
        self.frame_RNVA_3 = QtGui.QFrame(self.gbAeroData)
        self.frame_RNVA_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_RNVA_3.sizePolicy().hasHeightForWidth())
        self.frame_RNVA_3.setSizePolicy(sizePolicy)
        self.frame_RNVA_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_RNVA_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_RNVA_3.setObjectName(_fromUtf8("frame_RNVA_3"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.frame_RNVA_3)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setMargin(0)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_10 = QtGui.QLabel(self.frame_RNVA_3)
        self.label_10.setMinimumSize(QtCore.QSize(70, 0))
        self.label_10.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_18.addWidget(self.label_10)
        self.cmbConstructionType = QtGui.QComboBox(self.frame_RNVA_3)
        self.cmbConstructionType.setMinimumSize(QtCore.QSize(60, 0))
        self.cmbConstructionType.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.cmbConstructionType.setFont(font)
        self.cmbConstructionType.setFrame(True)
        self.cmbConstructionType.setObjectName(_fromUtf8("cmbConstructionType"))
        self.horizontalLayout_18.addWidget(self.cmbConstructionType)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(horizontalSpacer)
        self.verticalLayout_gbAeroData.addWidget(self.frame_RNVA_3)
        self.frame = QtGui.QFrame(self.gbAeroData)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chbMarkAltitudes = QtGui.QCheckBox(self.frame)
        self.chbMarkAltitudes.setChecked(True)
        self.chbMarkAltitudes.setObjectName(_fromUtf8("chbMarkAltitudes"))
        self.gridLayout.addWidget(self.chbMarkAltitudes, 0, 0, 1, 1)
        self.chbMarkDistances = QtGui.QCheckBox(self.frame)
        self.chbMarkDistances.setChecked(True)
        self.chbMarkDistances.setObjectName(_fromUtf8("chbMarkDistances"))
        self.gridLayout.addWidget(self.chbMarkDistances, 1, 0, 1, 1)
        self.chbMarkSpeeds = QtGui.QCheckBox(self.frame)
        self.chbMarkSpeeds.setChecked(True)
        self.chbMarkSpeeds.setObjectName(_fromUtf8("chbMarkSpeeds"))
        self.gridLayout.addWidget(self.chbMarkSpeeds, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.cmbSpeedEvery = QtGui.QComboBox(self.frame)
        self.cmbSpeedEvery.setObjectName(_fromUtf8("cmbSpeedEvery"))
        self.gridLayout.addWidget(self.cmbSpeedEvery, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.txtDistanceEvery = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDistanceEvery.sizePolicy().hasHeightForWidth())
        self.txtDistanceEvery.setSizePolicy(sizePolicy)
        self.txtDistanceEvery.setObjectName(_fromUtf8("txtDistanceEvery"))
        self.gridLayout.addWidget(self.txtDistanceEvery, 1, 2, 1, 1)
        self.txtAltitudeEvery = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAltitudeEvery.sizePolicy().hasHeightForWidth())
        self.txtAltitudeEvery.setSizePolicy(sizePolicy)
        self.txtAltitudeEvery.setObjectName(_fromUtf8("txtAltitudeEvery"))
        self.gridLayout.addWidget(self.txtAltitudeEvery, 0, 2, 1, 1)
        self.verticalLayout_gbAeroData.addWidget(self.frame)
        self.vLayout_Main.addWidget(self.gbAeroData)
        self.horizontalLayout.addWidget(self.frmoMain)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_MocMA1_2 = QtGui.QFrame(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_MocMA1_2.sizePolicy().hasHeightForWidth())
        self.frame_MocMA1_2.setSizePolicy(sizePolicy)
        self.frame_MocMA1_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_MocMA1_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_MocMA1_2.setObjectName(_fromUtf8("frame_MocMA1_2"))
        self.horizontalLayout_35 = QtGui.QHBoxLayout(self.frame_MocMA1_2)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setMargin(0)
        self.horizontalLayout_35.setObjectName(_fromUtf8("horizontalLayout_35"))
        self.label_23 = QtGui.QLabel(self.frame_MocMA1_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QtCore.QSize(70, 0))
        self.label_23.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_35.addWidget(self.label_23)
        self.txtPdg = QtGui.QLineEdit(self.frame_MocMA1_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPdg.sizePolicy().hasHeightForWidth())
        self.txtPdg.setSizePolicy(sizePolicy)
        self.txtPdg.setMinimumSize(QtCore.QSize(60, 0))
        self.txtPdg.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtPdg.setFont(font)
        self.txtPdg.setObjectName(_fromUtf8("txtPdg"))
        self.horizontalLayout_35.addWidget(self.txtPdg)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(horizontalSpacer)
        self.verticalLayout.addWidget(self.frame_MocMA1_2)
        self.frame_MocMA1_3 = QtGui.QFrame(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_MocMA1_3.sizePolicy().hasHeightForWidth())
        self.frame_MocMA1_3.setSizePolicy(sizePolicy)
        self.frame_MocMA1_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_MocMA1_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_MocMA1_3.setObjectName(_fromUtf8("frame_MocMA1_3"))
        self.horizontalLayout_36 = QtGui.QHBoxLayout(self.frame_MocMA1_3)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setMargin(0)
        self.horizontalLayout_36.setObjectName(_fromUtf8("horizontalLayout_36"))
        self.label_24 = QtGui.QLabel(self.frame_MocMA1_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QtCore.QSize(70, 0))
        self.label_24.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_36.addWidget(self.label_24)
        self.txtIsa = QtGui.QLineEdit(self.frame_MocMA1_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtIsa.sizePolicy().hasHeightForWidth())
        self.txtIsa.setSizePolicy(sizePolicy)
        self.txtIsa.setMinimumSize(QtCore.QSize(60, 0))
        self.txtIsa.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtIsa.setFont(font)
        self.txtIsa.setObjectName(_fromUtf8("txtIsa"))
        self.horizontalLayout_36.addWidget(self.txtIsa)
        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(horizontalSpacer)
        self.verticalLayout.addWidget(self.frame_MocMA1_3)
        self.tblSpeeds = QtGui.QTableView(self.groupBox)
        self.tblSpeeds.setObjectName(_fromUtf8("tblSpeeds"))
        self.verticalLayout.addWidget(self.tblSpeeds)
        self.frame_2 = QtGui.QFrame(self.groupBox)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnEdit = QtGui.QPushButton(self.frame_2)
        self.btnEdit.setEnabled(False)
        self.btnEdit.setObjectName(_fromUtf8("btnEdit"))
        self.horizontalLayout_2.addWidget(self.btnEdit)
        self.btnReset = QtGui.QPushButton(self.frame_2)
        self.btnReset.setObjectName(_fromUtf8("btnReset"))
        self.horizontalLayout_2.addWidget(self.btnReset)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.groupBox)

        self.iconMulti= QtGui.QIcon()
        self.iconMulti.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/btnImage/multiPosition.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.gbP1.setTitle(_translate("Form", "Position1", None))
        self.label_4.setText(_translate("Form", "Altitude:", None))
        self.label_5.setText(_translate("Form", "m", None))
        self.label_6.setText(_translate("Form", "ft", None))
        self.gbP2.setTitle(_translate("Form", "Position2", None))
        self.label_15.setText(_translate("Form", "Altitude:", None))
        self.label_7.setText(_translate("Form", "m", None))
        self.label_8.setText(_translate("Form", "ft", None))
        self.gbAeroData.setTitle(_translate("Form", "Construction", None))
        self.label_10.setText(_translate("Form", "Type:", None))
        self.chbMarkAltitudes.setText(_translate("Form", "Mark Altitude", None))
        self.chbMarkDistances.setText(_translate("Form", "Mark Distances", None))
        self.chbMarkSpeeds.setText(_translate("Form", "Mark Speeds", None))
        self.label_2.setText(_translate("Form", "Every (nm):", None))
        self.label.setText(_translate("Form", "Every (ft):", None))
        self.label_3.setText(_translate("Form", "Every:", None))
        self.txtDistanceEvery.setText(_translate("Form", "1", None))
        self.txtAltitudeEvery.setText(_translate("Form", "100", None))
        self.groupBox.setTitle(_translate("Form", "Parameters", None))
        self.label_23.setText(_translate("Form", "PDG (%):", None))
        self.txtPdg.setText(_translate("Form", "3", None))
        self.label_24.setText(_translate("Form", "ISA ():", None))
        self.txtIsa.setText(_translate("Form", "15", None))
        self.btnEdit.setText(_translate("Form", "Edit", None))
        self.btnReset.setText(_translate("Form", "Reset", None))
