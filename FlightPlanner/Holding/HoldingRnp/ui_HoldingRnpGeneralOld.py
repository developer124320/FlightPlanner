# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HoldingRnp.ui'
#
# Created: Wed Jul 01 11:33:33 2015
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

class Ui_HoldingRnpGeneral(object):
    def setupUi(self, HoldingRnp):
        HoldingRnp.setObjectName(_fromUtf8("HoldingRnp"))
        HoldingRnp.resize(356, 358)
        self.verticalLayout = QtGui.QVBoxLayout(HoldingRnp)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.grbParameters = QtGui.QGroupBox(HoldingRnp)
        self.grbParameters.setObjectName(_fromUtf8("grbParameters"))
        self.vLayout_grbParameters = QtGui.QVBoxLayout(self.grbParameters)
        self.vLayout_grbParameters.setObjectName(_fromUtf8("vLayout_grbParameters"))
        self.frame_RnpValue = QtGui.QFrame(self.grbParameters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_RnpValue.sizePolicy().hasHeightForWidth())
        self.frame_RnpValue.setSizePolicy(sizePolicy)
        self.frame_RnpValue.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_RnpValue.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_RnpValue.setObjectName(_fromUtf8("frame_RnpValue"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.frame_RnpValue)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setMargin(0)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_9 = QtGui.QLabel(self.frame_RnpValue)
        self.label_9.setMinimumSize(QtCore.QSize(140, 0))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_19.addWidget(self.label_9)
        self.txtRnpValue = QtGui.QLineEdit(self.frame_RnpValue)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtRnpValue.sizePolicy().hasHeightForWidth())
        self.txtRnpValue.setSizePolicy(sizePolicy)
        self.txtRnpValue.setMinimumSize(QtCore.QSize(105, 0))
        self.txtRnpValue.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtRnpValue.setFont(font)
        self.txtRnpValue.setObjectName(_fromUtf8("txtRnpValue"))
        self.horizontalLayout_19.addWidget(self.txtRnpValue)
        self.vLayout_grbParameters.addWidget(self.frame_RnpValue)
        self.frame_ConstructionType_2 = QtGui.QFrame(self.grbParameters)
        self.frame_ConstructionType_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_ConstructionType_2.sizePolicy().hasHeightForWidth())
        self.frame_ConstructionType_2.setSizePolicy(sizePolicy)
        self.frame_ConstructionType_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_ConstructionType_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_ConstructionType_2.setObjectName(_fromUtf8("frame_ConstructionType_2"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.frame_ConstructionType_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setMargin(0)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_10 = QtGui.QLabel(self.frame_ConstructionType_2)
        self.label_10.setMinimumSize(QtCore.QSize(140, 0))
        self.label_10.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_18.addWidget(self.label_10)
        self.cmbAircraftCategory_2 = QtGui.QComboBox(self.frame_ConstructionType_2)
        self.cmbAircraftCategory_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.cmbAircraftCategory_2.setFont(font)
        self.cmbAircraftCategory_2.setFrame(True)
        self.cmbAircraftCategory_2.setObjectName(_fromUtf8("cmbAircraftCategory_2"))
        self.horizontalLayout_18.addWidget(self.cmbAircraftCategory_2)
        self.vLayout_grbParameters.addWidget(self.frame_ConstructionType_2)
        self.frame_Ias = QtGui.QFrame(self.grbParameters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_Ias.sizePolicy().hasHeightForWidth())
        self.frame_Ias.setSizePolicy(sizePolicy)
        self.frame_Ias.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Ias.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Ias.setObjectName(_fromUtf8("frame_Ias"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.frame_Ias)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setMargin(0)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_7 = QtGui.QLabel(self.frame_Ias)
        self.label_7.setMinimumSize(QtCore.QSize(140, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_16.addWidget(self.label_7)
        self.txtIas = QtGui.QLineEdit(self.frame_Ias)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtIas.sizePolicy().hasHeightForWidth())
        self.txtIas.setSizePolicy(sizePolicy)
        self.txtIas.setMinimumSize(QtCore.QSize(105, 0))
        self.txtIas.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtIas.setFont(font)
        self.txtIas.setObjectName(_fromUtf8("txtIas"))
        self.horizontalLayout_16.addWidget(self.txtIas)        
        self.btnIasHelp = QtGui.QPushButton(self.frame_Ias)
        self.btnIasHelp.setText(_fromUtf8("?"))
        self.btnIasHelp.setObjectName(_fromUtf8("btnIasHelp"))
        self.btnIasHelp.setFixedWidth(23)
        self.horizontalLayout_16.addWidget(self.btnIasHelp)
        self.vLayout_grbParameters.addWidget(self.frame_Ias)
        
        self.frame_Tas = QtGui.QFrame(self.grbParameters)
        self.frame_Tas.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_Tas.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Tas.setObjectName(_fromUtf8("frame_Tas"))
        self.horizontalLayout_Tas = QtGui.QHBoxLayout(self.frame_Tas)
        self.horizontalLayout_Tas.setSpacing(0)
        self.horizontalLayout_Tas.setMargin(0)
        self.horizontalLayout_Tas.setObjectName(_fromUtf8("horizontalLayout_Tas"))
        self.label_Tas = QtGui.QLabel(self.frame_Tas)
        self.label_Tas.setMinimumSize(QtCore.QSize(140, 0))
        self.label_Tas.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_Tas.setFont(font)
        self.label_Tas.setObjectName(_fromUtf8("label_Tas"))
        self.horizontalLayout_Tas.addWidget(self.label_Tas)
        self.txtTas = QtGui.QLineEdit(self.frame_Tas)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtIas.sizePolicy().hasHeightForWidth())
        self.txtTas.setSizePolicy(sizePolicy)
        self.txtTas.setMinimumSize(QtCore.QSize(105, 0))
        self.txtTas.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtTas.setFont(font)
        self.txtTas.setObjectName(_fromUtf8("txtTas"))
        self.horizontalLayout_Tas.addWidget(self.txtTas)
        self.vLayout_grbParameters.addWidget(self.frame_Tas)
        
        self.frame_Altitude = QtGui.QFrame(self.grbParameters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_Altitude.sizePolicy().hasHeightForWidth())
        self.frame_Altitude.setSizePolicy(sizePolicy)
        self.frame_Altitude.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Altitude.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Altitude.setObjectName(_fromUtf8("frame_Altitude"))
        self.horizontalLayout_27 = QtGui.QHBoxLayout(self.frame_Altitude)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setMargin(0)
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.label_17 = QtGui.QLabel(self.frame_Altitude)
        self.label_17.setMinimumSize(QtCore.QSize(140, 0))
        self.label_17.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_27.addWidget(self.label_17)
        self.txtAltitude = QtGui.QLineEdit(self.frame_Altitude)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAltitude.sizePolicy().hasHeightForWidth())
        self.txtAltitude.setSizePolicy(sizePolicy)
        self.txtAltitude.setMinimumSize(QtCore.QSize(105, 0))
        self.txtAltitude.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtAltitude.setFont(font)
        self.txtAltitude.setObjectName(_fromUtf8("txtAltitude"))
        self.horizontalLayout_27.addWidget(self.txtAltitude)
        self.vLayout_grbParameters.addWidget(self.frame_Altitude)
        self.frame_IasMA = QtGui.QFrame(self.grbParameters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_IasMA.sizePolicy().hasHeightForWidth())
        self.frame_IasMA.setSizePolicy(sizePolicy)
        self.frame_IasMA.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_IasMA.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_IasMA.setObjectName(_fromUtf8("frame_IasMA"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.frame_IasMA)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setMargin(0)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_3 = QtGui.QLabel(self.frame_IasMA)
        self.label_3.setMinimumSize(QtCore.QSize(140, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_11.addWidget(self.label_3)
        self.txtIsa = QtGui.QLineEdit(self.frame_IasMA)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtIsa.sizePolicy().hasHeightForWidth())
        self.txtIsa.setSizePolicy(sizePolicy)
        self.txtIsa.setMinimumSize(QtCore.QSize(105, 0))
        self.txtIsa.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtIsa.setFont(font)
        self.txtIsa.setObjectName(_fromUtf8("txtIsa"))
        self.horizontalLayout_11.addWidget(self.txtIsa)
        self.vLayout_grbParameters.addWidget(self.frame_IasMA)
        self.frame_Time = QtGui.QFrame(self.grbParameters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_Time.sizePolicy().hasHeightForWidth())
        self.frame_Time.setSizePolicy(sizePolicy)
        self.frame_Time.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Time.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Time.setObjectName(_fromUtf8("frame_Time"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.frame_Time)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setMargin(0)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_5 = QtGui.QLabel(self.frame_Time)
        self.label_5.setMinimumSize(QtCore.QSize(140, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_14.addWidget(self.label_5)
        self.txtTime = QtGui.QLineEdit(self.frame_Time)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTime.sizePolicy().hasHeightForWidth())
        self.txtTime.setSizePolicy(sizePolicy)
        self.txtTime.setMinimumSize(QtCore.QSize(105, 0))
        self.txtTime.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtTime.setFont(font)
        self.txtTime.setObjectName(_fromUtf8("txtTime"))
        self.horizontalLayout_14.addWidget(self.txtTime)
        self.vLayout_grbParameters.addWidget(self.frame_Time)
        self.frame_Moc = QtGui.QFrame(self.grbParameters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_Moc.sizePolicy().hasHeightForWidth())
        self.frame_Moc.setSizePolicy(sizePolicy)
        self.frame_Moc.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_Moc.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_Moc.setObjectName(_fromUtf8("frame_Moc"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.frame_Moc)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_4 = QtGui.QLabel(self.frame_Moc)
        self.label_4.setMinimumSize(QtCore.QSize(140, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_12.addWidget(self.label_4)
        self.txtMoc = QtGui.QLineEdit(self.frame_Moc)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtMoc.sizePolicy().hasHeightForWidth())
        self.txtMoc.setSizePolicy(sizePolicy)
        self.txtMoc.setMinimumSize(QtCore.QSize(105, 0))
        self.txtMoc.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.txtMoc.setFont(font)
        self.txtMoc.setObjectName(_fromUtf8("txtMoc"))
        self.horizontalLayout_12.addWidget(self.txtMoc)
        self.vLayout_grbParameters.addWidget(self.frame_Moc)
        self.frame_ConstructionType = QtGui.QFrame(self.grbParameters)
        self.frame_ConstructionType.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_ConstructionType.sizePolicy().hasHeightForWidth())
        self.frame_ConstructionType.setSizePolicy(sizePolicy)
        self.frame_ConstructionType.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_ConstructionType.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_ConstructionType.setObjectName(_fromUtf8("frame_ConstructionType"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.frame_ConstructionType)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setMargin(0)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_8 = QtGui.QLabel(self.frame_ConstructionType)
        self.label_8.setMinimumSize(QtCore.QSize(140, 0))
        self.label_8.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_17.addWidget(self.label_8)
        self.cmbConstruction = QtGui.QComboBox(self.frame_ConstructionType)
        self.cmbConstruction.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.cmbConstruction.setFont(font)
        self.cmbConstruction.setFrame(True)
        self.cmbConstruction.setObjectName(_fromUtf8("cmbConstruction"))
        self.horizontalLayout_17.addWidget(self.cmbConstruction)
        self.vLayout_grbParameters.addWidget(self.frame_ConstructionType)
        self.verticalLayout.addWidget(self.grbParameters)
        self.groupBox_2 = QtGui.QGroupBox(HoldingRnp)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_ThrFaf = QtGui.QFrame(self.groupBox_2)
        self.frame_ThrFaf.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_ThrFaf.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_ThrFaf.setObjectName(_fromUtf8("frame_ThrFaf"))
        self.horizontalLayout_65 = QtGui.QHBoxLayout(self.frame_ThrFaf)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setMargin(0)
        self.horizontalLayout_65.setObjectName(_fromUtf8("horizontalLayout_65"))
        self.label_73 = QtGui.QLabel(self.frame_ThrFaf)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_73.setFont(font)
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.horizontalLayout_65.addWidget(self.label_73)
        self.frame_APV_9 = QtGui.QFrame(self.frame_ThrFaf)
        self.frame_APV_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_APV_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_APV_9.setObjectName(_fromUtf8("frame_APV_9"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.frame_APV_9)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.txtTrack = QtGui.QLineEdit(self.frame_APV_9)
        self.txtTrack.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtTrack.setFont(font)
        self.txtTrack.setObjectName(_fromUtf8("txtTrack"))
        self.horizontalLayout_13.addWidget(self.txtTrack)
        self.btnCaptureTrack = QtGui.QToolButton(self.frame_APV_9)
        self.btnCaptureTrack.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/coordinate_capture.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCaptureTrack.setIcon(icon)
        self.btnCaptureTrack.setObjectName(_fromUtf8("btnCaptureTrack"))
        self.horizontalLayout_13.addWidget(self.btnCaptureTrack)
        self.horizontalLayout_65.addWidget(self.frame_APV_9)
        self.verticalLayout_2.addWidget(self.frame_ThrFaf)
        self.frame_60 = QtGui.QFrame(self.groupBox_2)
        self.frame_60.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_60.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_60.setObjectName(_fromUtf8("frame_60"))
        self.horizontalLayout_61 = QtGui.QHBoxLayout(self.frame_60)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setMargin(0)
        self.horizontalLayout_61.setObjectName(_fromUtf8("horizontalLayout_61"))
        self.label_69 = QtGui.QLabel(self.frame_60)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy)
        self.label_69.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_69.setFont(font)
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.horizontalLayout_61.addWidget(self.label_69)
        self.cmbOrientation = QtGui.QComboBox(self.frame_60)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbOrientation.sizePolicy().hasHeightForWidth())
        self.cmbOrientation.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cmbOrientation.setFont(font)
        self.cmbOrientation.setObjectName(_fromUtf8("cmbOrientation"))
        self.horizontalLayout_61.addWidget(self.cmbOrientation)
        self.verticalLayout_2.addWidget(self.frame_60)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(HoldingRnp)
        QtCore.QMetaObject.connectSlotsByName(HoldingRnp)

    def retranslateUi(self, HoldingRnp):
        HoldingRnp.setWindowTitle(_translate("HoldingRnp", "Form", None))
        self.grbParameters.setTitle(_translate("HoldingRnp", "Parameters", None))
        self.label_9.setText(_translate("HoldingRnp", "RNP Value:", None))
        self.txtRnpValue.setText(_translate("HoldingRnp", "1", None))
        self.label_10.setText(_translate("HoldingRnp", "Aircraft Category:", None))
        self.label_7.setText(_translate("HoldingRnp", "IAS (kts):", None))
        self.label_Tas.setText(_translate("HoldingRnp", "TAS (kts):", None))
        self.txtIas.setText(_translate("HoldingRnp", "250", None))
        self.label_17.setText(_translate("HoldingRnp", "Altitude (ft):", None))
        self.txtAltitude.setText(_translate("HoldingRnp", "10000", None))
        self.label_3.setText(_translate("HoldingRnp", "ISA (°C):", None))
        self.txtIsa.setText(_translate("HoldingRnp", "15", None))
        self.label_5.setText(_translate("HoldingRnp", "Time (min):", None))
        self.txtTime.setText(_translate("HoldingRnp", "1", None))
        self.label_4.setText(_translate("HoldingRnp", "MOC(m):", None))
        self.txtMoc.setText(_translate("HoldingRnp", "300", None))
        self.label_8.setText(_translate("HoldingRnp", "Construction Type:", None))
        self.groupBox_2.setTitle(_translate("HoldingRnp", "Orientation", None))
        self.label_73.setText(_translate("HoldingRnp", "In-bound Track ():", None))
        self.txtTrack.setText(_translate("HoldingRnp", "0", None))
        self.label_69.setText(_translate("HoldingRnp", "Turns:", None))

