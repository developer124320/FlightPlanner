# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlightPlannerBaseWidget.ui'
#
# Created: Fri Jan 29 14:51:49 2016
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

class Ui_FlightPlannerBaseWidget(object):
    def setupUi(self, FlightPlannerBaseWidget):
        FlightPlannerBaseWidget.setObjectName(_fromUtf8("FlightPlannerBaseWidget"))
        FlightPlannerBaseWidget.resize(579, 558)
        self.verticalLayout = QtGui.QVBoxLayout(FlightPlannerBaseWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabCtrlGeneral = QtGui.QTabWidget(FlightPlannerBaseWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.tabCtrlGeneral.setFont(font)
        self.tabCtrlGeneral.setAutoFillBackground(False)
        self.tabCtrlGeneral.setStyleSheet(_fromUtf8(""))
        self.tabCtrlGeneral.setObjectName(_fromUtf8("tabCtrlGeneral"))
        self.tab_General = QtGui.QWidget(FlightPlannerBaseWidget)
        self.tab_General.setObjectName(_fromUtf8("tab_General"))
        self.horizontalLayout_29 = QtGui.QHBoxLayout(self.tab_General)
        self.horizontalLayout_29.setMargin(3)
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.grbGeneral = QtGui.QGroupBox(self.tab_General)
        self.grbGeneral.setTitle(_fromUtf8(""))
        self.grbGeneral.setObjectName(_fromUtf8("grbGeneral"))
        self.vlGeneral = QtGui.QVBoxLayout(self.grbGeneral)
        self.vlGeneral.setMargin(5)
        self.vlGeneral.setObjectName(_fromUtf8("vlGeneral"))
        self.horizontalLayout_29.addWidget(self.grbGeneral)
        self.frmGeneralButtons = QtGui.QFrame(self.tab_General)
        self.frmGeneralButtons.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frmGeneralButtons.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGeneralButtons.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGeneralButtons.setObjectName(_fromUtf8("frmGeneralButtons"))
        self.vlGeneralBtns = QtGui.QVBoxLayout(self.frmGeneralButtons)
        self.vlGeneralBtns.setObjectName(_fromUtf8("vlGeneralBtns"))
        self.btnOpenData = QtGui.QPushButton(self.frmGeneralButtons)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnOpenData.setFont(font)
        self.btnOpenData.setObjectName(_fromUtf8("btnOpenData"))
        self.vlGeneralBtns.addWidget(self.btnOpenData)
        self.btnSaveData = QtGui.QPushButton(self.frmGeneralButtons)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnSaveData.setFont(font)
        self.btnSaveData.setObjectName(_fromUtf8("btnSaveData"))
        self.vlGeneralBtns.addWidget(self.btnSaveData)
        self.btnConstruct = QtGui.QPushButton(self.frmGeneralButtons)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnConstruct.setFont(font)
        self.btnConstruct.setObjectName(_fromUtf8("btnConstruct"))
        self.vlGeneralBtns.addWidget(self.btnConstruct)
        self.btnPDTCheck = QtGui.QPushButton(self.frmGeneralButtons)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnPDTCheck.setFont(font)
        self.btnPDTCheck.setObjectName(_fromUtf8("btnPDTCheck"))
        self.vlGeneralBtns.addWidget(self.btnPDTCheck)
        self.btnEvaluate = QtGui.QPushButton(self.frmGeneralButtons)
        self.btnEvaluate.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnEvaluate.setFont(font)
        self.btnEvaluate.setObjectName(_fromUtf8("btnEvaluate"))
        self.vlGeneralBtns.addWidget(self.btnEvaluate)
        self.btnUpdateQA = QtGui.QPushButton(self.frmGeneralButtons)
        self.btnUpdateQA.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnUpdateQA.setFont(font)
        self.btnUpdateQA.setObjectName(_fromUtf8("btnUpdateQA"))
        self.vlGeneralBtns.addWidget(self.btnUpdateQA)
        self.btnExportResult = QtGui.QPushButton(self.frmGeneralButtons)
        self.btnExportResult.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnExportResult.setFont(font)
        self.btnExportResult.setObjectName(_fromUtf8("btnExportResult"))
        self.vlGeneralBtns.addWidget(self.btnExportResult)
        self.btnClose = QtGui.QPushButton(self.frmGeneralButtons)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.vlGeneralBtns.addWidget(self.btnClose)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlGeneralBtns.addItem(spacerItem)
        self.horizontalLayout_29.addWidget(self.frmGeneralButtons)
        self.tabCtrlGeneral.addTab(self.tab_General, _fromUtf8(""))
        self.tab_Results = QtGui.QWidget(FlightPlannerBaseWidget)
        self.tab_Results.setObjectName(_fromUtf8("tab_Results"))
        self.hlResults = QtGui.QHBoxLayout(self.tab_Results)
        self.hlResults.setSpacing(3)
        self.hlResults.setMargin(3)
        self.hlResults.setObjectName(_fromUtf8("hlResults"))
        self.grbResult = QtGui.QGroupBox(self.tab_Results)
        self.grbResult.setTitle(_fromUtf8(""))
        self.grbResult.setObjectName(_fromUtf8("grbResult"))
        self.vlResultGroup = QtGui.QVBoxLayout(self.grbResult)
        self.vlResultGroup.setMargin(3)
        self.vlResultGroup.setObjectName(_fromUtf8("vlResultGroup"))
        self.grbMostCritical = QtGui.QGroupBox(self.grbResult)
        self.grbMostCritical.setObjectName(_fromUtf8("grbMostCritical"))
        self.vlMostCritical = QtGui.QVBoxLayout(self.grbMostCritical)
        self.vlMostCritical.setContentsMargins(-1, 0, -1, 3)
        self.vlMostCritical.setObjectName(_fromUtf8("vlMostCritical"))
        self.frame_2 = QtGui.QFrame(self.grbMostCritical)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.frame_3 = QtGui.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_19.setMargin(0)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.frame_107 = QtGui.QFrame(self.frame_3)
        self.frame_107.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_107.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_107.setObjectName(_fromUtf8("frame_107"))
        self.horizontalLayout_94 = QtGui.QHBoxLayout(self.frame_107)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setMargin(0)
        self.horizontalLayout_94.setObjectName(_fromUtf8("horizontalLayout_94"))
        self.label_115 = QtGui.QLabel(self.frame_107)
        self.label_115.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_115.setFont(font)
        self.label_115.setObjectName(_fromUtf8("label_115"))
        self.horizontalLayout_94.addWidget(self.label_115)
        self.txtCriticalID = QtGui.QLineEdit(self.frame_107)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtCriticalID.setFont(font)
        self.txtCriticalID.setObjectName(_fromUtf8("txtCriticalID"))
        self.horizontalLayout_94.addWidget(self.txtCriticalID)
        self.verticalLayout_19.addWidget(self.frame_107)
        self.frame_109 = QtGui.QFrame(self.frame_3)
        self.frame_109.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_109.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_109.setObjectName(_fromUtf8("frame_109"))
        self.horizontalLayout_96 = QtGui.QHBoxLayout(self.frame_109)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setMargin(0)
        self.horizontalLayout_96.setObjectName(_fromUtf8("horizontalLayout_96"))
        self.label_119 = QtGui.QLabel(self.frame_109)
        self.label_119.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_119.setFont(font)
        self.label_119.setObjectName(_fromUtf8("label_119"))
        self.horizontalLayout_96.addWidget(self.label_119)
        self.txtCriticalX = QtGui.QLineEdit(self.frame_109)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtCriticalX.setFont(font)
        self.txtCriticalX.setObjectName(_fromUtf8("txtCriticalX"))
        self.horizontalLayout_96.addWidget(self.txtCriticalX)
        self.verticalLayout_19.addWidget(self.frame_109)
        self.frame_110 = QtGui.QFrame(self.frame_3)
        self.frame_110.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_110.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_110.setObjectName(_fromUtf8("frame_110"))
        self.horizontalLayout_97 = QtGui.QHBoxLayout(self.frame_110)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setMargin(0)
        self.horizontalLayout_97.setObjectName(_fromUtf8("horizontalLayout_97"))
        self.label_120 = QtGui.QLabel(self.frame_110)
        self.label_120.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_120.setFont(font)
        self.label_120.setObjectName(_fromUtf8("label_120"))
        self.horizontalLayout_97.addWidget(self.label_120)
        self.txtCriticalY = QtGui.QLineEdit(self.frame_110)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtCriticalY.setFont(font)
        self.txtCriticalY.setObjectName(_fromUtf8("txtCriticalY"))
        self.horizontalLayout_97.addWidget(self.txtCriticalY)
        self.verticalLayout_19.addWidget(self.frame_110)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.btnCriticalLocate = QtGui.QToolButton(self.frame_2)
        self.btnCriticalLocate.setMaximumSize(QtCore.QSize(25, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/gnss_item/mActionZoomFullExtent.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCriticalLocate.setIcon(icon)
        self.btnCriticalLocate.setObjectName(_fromUtf8("btnCriticalLocate"))
        self.horizontalLayout_4.addWidget(self.btnCriticalLocate)
        self.vlMostCritical.addWidget(self.frame_2)
        self.frmMostCriticalAltitude = QtGui.QFrame(self.grbMostCritical)
        self.frmMostCriticalAltitude.setFrameShape(QtGui.QFrame.NoFrame)
        self.frmMostCriticalAltitude.setFrameShadow(QtGui.QFrame.Raised)
        self.frmMostCriticalAltitude.setObjectName(_fromUtf8("frmMostCriticalAltitude"))
        self.horizontalLayout_95 = QtGui.QHBoxLayout(self.frmMostCriticalAltitude)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setMargin(0)
        self.horizontalLayout_95.setObjectName(_fromUtf8("horizontalLayout_95"))
        self.label_116 = QtGui.QLabel(self.frmMostCriticalAltitude)
        self.label_116.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_116.setFont(font)
        self.label_116.setObjectName(_fromUtf8("label_116"))
        self.horizontalLayout_95.addWidget(self.label_116)
        self.txtCriticalAltitudeM = QtGui.QLineEdit(self.frmMostCriticalAltitude)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtCriticalAltitudeM.setFont(font)
        self.txtCriticalAltitudeM.setObjectName(_fromUtf8("txtCriticalAltitudeM"))
        self.horizontalLayout_95.addWidget(self.txtCriticalAltitudeM)
        self.label_117 = QtGui.QLabel(self.frmMostCriticalAltitude)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_117.setFont(font)
        self.label_117.setObjectName(_fromUtf8("label_117"))
        self.horizontalLayout_95.addWidget(self.label_117)
        self.txtCriticalAltitudeFt = QtGui.QLineEdit(self.frmMostCriticalAltitude)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtCriticalAltitudeFt.setFont(font)
        self.txtCriticalAltitudeFt.setObjectName(_fromUtf8("txtCriticalAltitudeFt"))
        self.horizontalLayout_95.addWidget(self.txtCriticalAltitudeFt)
        self.label_118 = QtGui.QLabel(self.frmMostCriticalAltitude)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_118.setFont(font)
        self.label_118.setObjectName(_fromUtf8("label_118"))
        self.horizontalLayout_95.addWidget(self.label_118)
        self.vlMostCritical.addWidget(self.frmMostCriticalAltitude)
        self.frmMostCriticalSurface = QtGui.QFrame(self.grbMostCritical)
        self.frmMostCriticalSurface.setFrameShape(QtGui.QFrame.NoFrame)
        self.frmMostCriticalSurface.setFrameShadow(QtGui.QFrame.Raised)
        self.frmMostCriticalSurface.setObjectName(_fromUtf8("frmMostCriticalSurface"))
        self.horizontalLayout_98 = QtGui.QHBoxLayout(self.frmMostCriticalSurface)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setMargin(0)
        self.horizontalLayout_98.setObjectName(_fromUtf8("horizontalLayout_98"))
        self.label_121 = QtGui.QLabel(self.frmMostCriticalSurface)
        self.label_121.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_121.setFont(font)
        self.label_121.setObjectName(_fromUtf8("label_121"))
        self.horizontalLayout_98.addWidget(self.label_121)
        self.txtCriticalSurface = QtGui.QLineEdit(self.frmMostCriticalSurface)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtCriticalSurface.setFont(font)
        self.txtCriticalSurface.setObjectName(_fromUtf8("txtCriticalSurface"))
        self.horizontalLayout_98.addWidget(self.txtCriticalSurface)
        self.vlMostCritical.addWidget(self.frmMostCriticalSurface)
        self.vlResultGroup.addWidget(self.grbMostCritical)
        self.grbResult_2 = QtGui.QGroupBox(self.grbResult)
        self.grbResult_2.setObjectName(_fromUtf8("grbResult_2"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.grbResult_2)
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 3)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.frame_112 = QtGui.QFrame(self.grbResult_2)
        self.frame_112.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_112.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_112.setObjectName(_fromUtf8("frame_112"))
        self.horizontalLayout_99 = QtGui.QHBoxLayout(self.frame_112)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setMargin(0)
        self.horizontalLayout_99.setObjectName(_fromUtf8("horizontalLayout_99"))
        self.label_122 = QtGui.QLabel(self.frame_112)
        self.label_122.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_122.setFont(font)
        self.label_122.setObjectName(_fromUtf8("label_122"))
        self.horizontalLayout_99.addWidget(self.label_122)
        self.cmbUnits = QtGui.QComboBox(self.frame_112)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbUnits.sizePolicy().hasHeightForWidth())
        self.cmbUnits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.cmbUnits.setFont(font)
        self.cmbUnits.setEditable(False)
        self.cmbUnits.setObjectName(_fromUtf8("cmbUnits"))
        self.horizontalLayout_99.addWidget(self.cmbUnits)
        self.verticalLayout_17.addWidget(self.frame_112)
        self.frame_113 = QtGui.QFrame(self.grbResult_2)
        self.frame_113.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_113.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_113.setObjectName(_fromUtf8("frame_113"))
        self.horizontalLayout_100 = QtGui.QHBoxLayout(self.frame_113)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setMargin(0)
        self.horizontalLayout_100.setObjectName(_fromUtf8("horizontalLayout_100"))
        self.txtOCH = QtGui.QLineEdit(self.frame_113)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtOCH.setFont(font)
        self.txtOCH.setObjectName(_fromUtf8("txtOCH"))
        self.horizontalLayout_100.addWidget(self.txtOCH)
        self.txtOCHResults = QtGui.QLineEdit(self.frame_113)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtOCHResults.setFont(font)
        self.txtOCHResults.setObjectName(_fromUtf8("txtOCHResults"))
        self.horizontalLayout_100.addWidget(self.txtOCHResults)
        self.verticalLayout_17.addWidget(self.frame_113)
        self.frame_114 = QtGui.QFrame(self.grbResult_2)
        self.frame_114.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_114.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_114.setObjectName(_fromUtf8("frame_114"))
        self.horizontalLayout_101 = QtGui.QHBoxLayout(self.frame_114)
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setMargin(0)
        self.horizontalLayout_101.setObjectName(_fromUtf8("horizontalLayout_101"))
        self.txtOCA = QtGui.QLineEdit(self.frame_114)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtOCA.setFont(font)
        self.txtOCA.setObjectName(_fromUtf8("txtOCA"))
        self.horizontalLayout_101.addWidget(self.txtOCA)
        self.txtOCAResults = QtGui.QLineEdit(self.frame_114)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtOCAResults.setFont(font)
        self.txtOCAResults.setObjectName(_fromUtf8("txtOCAResults"))
        self.horizontalLayout_101.addWidget(self.txtOCAResults)
        self.verticalLayout_17.addWidget(self.frame_114)
        self.vlResultGroup.addWidget(self.grbResult_2)
        self.grbObstacles = QtGui.QGroupBox(self.grbResult)
        self.grbObstacles.setObjectName(_fromUtf8("grbObstacles"))
        self.vlObstacles = QtGui.QVBoxLayout(self.grbObstacles)
        self.vlObstacles.setContentsMargins(-1, 0, -1, 3)
        self.vlObstacles.setObjectName(_fromUtf8("vlObstacles"))
        self.frame_115 = QtGui.QFrame(self.grbObstacles)
        self.frame_115.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_115.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_115.setObjectName(_fromUtf8("frame_115"))
        self.horizontalLayout_102 = QtGui.QHBoxLayout(self.frame_115)
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setMargin(0)
        self.horizontalLayout_102.setObjectName(_fromUtf8("horizontalLayout_102"))
        self.label_123 = QtGui.QLabel(self.frame_115)
        self.label_123.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_123.setFont(font)
        self.label_123.setObjectName(_fromUtf8("label_123"))
        self.horizontalLayout_102.addWidget(self.label_123)
        self.cmbObstSurface = QtGui.QComboBox(self.frame_115)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbObstSurface.sizePolicy().hasHeightForWidth())
        self.cmbObstSurface.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.cmbObstSurface.setFont(font)
        self.cmbObstSurface.setObjectName(_fromUtf8("cmbObstSurface"))
        self.horizontalLayout_102.addWidget(self.cmbObstSurface)
        self.vlObstacles.addWidget(self.frame_115)
        self.tblObstacles = QtGui.QTableView(self.grbObstacles)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tblObstacles.setFont(font)
        self.tblObstacles.setObjectName(_fromUtf8("tblObstacles"))
        self.vlObstacles.addWidget(self.tblObstacles)
        self.vlResultGroup.addWidget(self.grbObstacles)
        self.hlResults.addWidget(self.grbResult)
        self.frmResultButtons = QtGui.QFrame(self.tab_Results)
        self.frmResultButtons.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frmResultButtons.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmResultButtons.setFrameShadow(QtGui.QFrame.Raised)
        self.frmResultButtons.setObjectName(_fromUtf8("frmResultButtons"))
        self.vlResultBtns = QtGui.QVBoxLayout(self.frmResultButtons)
        self.vlResultBtns.setObjectName(_fromUtf8("vlResultBtns"))
        self.btnLocate = QtGui.QPushButton(self.frmResultButtons)
        self.btnLocate.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnLocate.setFont(font)
        self.btnLocate.setObjectName(_fromUtf8("btnLocate"))
        self.vlResultBtns.addWidget(self.btnLocate)
        self.btnUpdateQA_2 = QtGui.QPushButton(self.frmResultButtons)
        self.btnUpdateQA_2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnUpdateQA_2.setFont(font)
        self.btnUpdateQA_2.setObjectName(_fromUtf8("btnUpdateQA_2"))
        self.vlResultBtns.addWidget(self.btnUpdateQA_2)
        self.btnClose_2 = QtGui.QPushButton(self.frmResultButtons)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnClose_2.setFont(font)
        self.btnClose_2.setObjectName(_fromUtf8("btnClose_2"))
        self.vlResultBtns.addWidget(self.btnClose_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlResultBtns.addItem(spacerItem1)
        self.hlResults.addWidget(self.frmResultButtons)
        self.tabCtrlGeneral.addTab(self.tab_Results, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabCtrlGeneral)

        self.retranslateUi(FlightPlannerBaseWidget)
        self.tabCtrlGeneral.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FlightPlannerBaseWidget)

    def retranslateUi(self, FlightPlannerBaseWidget):
        FlightPlannerBaseWidget.setWindowTitle(_translate("FlightPlannerBaseWidget", "Form", None))
        self.btnOpenData.setText(_translate("FlightPlannerBaseWidget", "Open Data", None))
        self.btnSaveData.setText(_translate("FlightPlannerBaseWidget", "Save Data", None))
        self.btnConstruct.setText(_translate("FlightPlannerBaseWidget", "Construct", None))
        self.btnPDTCheck.setText(_translate("FlightPlannerBaseWidget", "PDT Check", None))
        self.btnEvaluate.setText(_translate("FlightPlannerBaseWidget", "Evaluate", None))
        self.btnUpdateQA.setText(_translate("FlightPlannerBaseWidget", "Update QA", None))
        self.btnExportResult.setText(_translate("FlightPlannerBaseWidget", "Export Result", None))
        self.btnClose.setText(_translate("FlightPlannerBaseWidget", "Close", None))
        self.tabCtrlGeneral.setTabText(self.tabCtrlGeneral.indexOf(self.tab_General), _translate("FlightPlannerBaseWidget", "General", None))
        self.grbMostCritical.setTitle(_translate("FlightPlannerBaseWidget", "The Most Critical Obstacle", None))
        self.label_115.setText(_translate("FlightPlannerBaseWidget", "ID:", None))
        self.label_119.setText(_translate("FlightPlannerBaseWidget", "X:", None))
        self.label_120.setText(_translate("FlightPlannerBaseWidget", "Y:", None))
        self.btnCriticalLocate.setText(_translate("FlightPlannerBaseWidget", "...", None))
        self.label_116.setText(_translate("FlightPlannerBaseWidget", "Altitude:", None))
        self.label_117.setText(_translate("FlightPlannerBaseWidget", " m ", None))
        self.label_118.setText(_translate("FlightPlannerBaseWidget", "ft", None))
        self.label_121.setText(_translate("FlightPlannerBaseWidget", "Surface:", None))
        self.grbResult_2.setTitle(_translate("FlightPlannerBaseWidget", "Results", None))
        self.label_122.setText(_translate("FlightPlannerBaseWidget", "Units:", None))
        self.txtOCH.setText(_translate("FlightPlannerBaseWidget", "OCH", None))
        self.txtOCA.setText(_translate("FlightPlannerBaseWidget", "OCA", None))
        self.grbObstacles.setTitle(_translate("FlightPlannerBaseWidget", "Checked Ostacles", None))
        self.label_123.setText(_translate("FlightPlannerBaseWidget", "Surface:", None))
        self.btnLocate.setText(_translate("FlightPlannerBaseWidget", "Locate", None))
        self.btnUpdateQA_2.setText(_translate("FlightPlannerBaseWidget", "Update QA", None))
        self.btnClose_2.setText(_translate("FlightPlannerBaseWidget", "Close", None))
        self.tabCtrlGeneral.setTabText(self.tabCtrlGeneral.indexOf(self.tab_Results), _translate("FlightPlannerBaseWidget", "Results/Checked Obstacles", None))

