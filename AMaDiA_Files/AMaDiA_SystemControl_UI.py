# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AMaDiA_SystemControl_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SystemControlWindow(object):
    def setupUi(self, SystemControlWindow):
        SystemControlWindow.setObjectName("SystemControlWindow")
        SystemControlWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SystemControlWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.ControlSystems_tabWidget = MTabWidget(self.centralwidget)
        self.ControlSystems_tabWidget.setObjectName("ControlSystems_tabWidget")
        self.ControlSystems_1 = QtWidgets.QWidget()
        self.ControlSystems_1.setObjectName("ControlSystems_1")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.ControlSystems_1)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.ControlSystems_1_Splitter_M = QtWidgets.QSplitter(self.ControlSystems_1)
        self.ControlSystems_1_Splitter_M.setOrientation(QtCore.Qt.Horizontal)
        self.ControlSystems_1_Splitter_M.setObjectName("ControlSystems_1_Splitter_M")
        self.ControlSystems_1_Splitter_L = QtWidgets.QSplitter(self.ControlSystems_1_Splitter_M)
        self.ControlSystems_1_Splitter_L.setOrientation(QtCore.Qt.Vertical)
        self.ControlSystems_1_Splitter_L.setObjectName("ControlSystems_1_Splitter_L")
        self.layoutWidget = QtWidgets.QWidget(self.ControlSystems_1_Splitter_L)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.ControlSystems_1_SystemOrder_Confrim = QtWidgets.QPushButton(self.layoutWidget)
        self.ControlSystems_1_SystemOrder_Confrim.setObjectName("ControlSystems_1_SystemOrder_Confrim")
        self.gridLayout_15.addWidget(self.ControlSystems_1_SystemOrder_Confrim, 1, 1, 1, 1)
        self.ControlSystems_1_NameInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.ControlSystems_1_NameInput.setObjectName("ControlSystems_1_NameInput")
        self.gridLayout_15.addWidget(self.ControlSystems_1_NameInput, 1, 2, 1, 1)
        self.ControlSystems_1_SystemOrder_Spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ControlSystems_1_SystemOrder_Spinbox.sizePolicy().hasHeightForWidth())
        self.ControlSystems_1_SystemOrder_Spinbox.setSizePolicy(sizePolicy)
        self.ControlSystems_1_SystemOrder_Spinbox.setMinimum(1)
        self.ControlSystems_1_SystemOrder_Spinbox.setProperty("value", 3)
        self.ControlSystems_1_SystemOrder_Spinbox.setObjectName("ControlSystems_1_SystemOrder_Spinbox")
        self.gridLayout_15.addWidget(self.ControlSystems_1_SystemOrder_Spinbox, 1, 0, 1, 1)
        self.ControlSystems_1_SavePlotButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ControlSystems_1_SavePlotButton.setObjectName("ControlSystems_1_SavePlotButton")
        self.gridLayout_15.addWidget(self.ControlSystems_1_SavePlotButton, 1, 4, 1, 1)
        self.ControlSystems_1_SaveButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ControlSystems_1_SaveButton.setObjectName("ControlSystems_1_SaveButton")
        self.gridLayout_15.addWidget(self.ControlSystems_1_SaveButton, 1, 3, 1, 1)
        self.ControlSystems_1_System_tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.ControlSystems_1_System_tabWidget.setObjectName("ControlSystems_1_System_tabWidget")
        self.ControlSystems_1_System_4ATF = QtWidgets.QWidget()
        self.ControlSystems_1_System_4ATF.setObjectName("ControlSystems_1_System_4ATF")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.ControlSystems_1_System_4ATF)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.ControlSystems_1_System_4ATF_Ys = AMaDiA_LineEdit(self.ControlSystems_1_System_4ATF)
        self.ControlSystems_1_System_4ATF_Ys.setObjectName("ControlSystems_1_System_4ATF_Ys")
        self.gridLayout_27.addWidget(self.ControlSystems_1_System_4ATF_Ys, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.ControlSystems_1_System_4ATF)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(4)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout_27.addWidget(self.line_3, 1, 0, 1, 1)
        self.ControlSystems_1_System_4ATF_Xs = AMaDiA_LineEdit(self.ControlSystems_1_System_4ATF)
        self.ControlSystems_1_System_4ATF_Xs.setObjectName("ControlSystems_1_System_4ATF_Xs")
        self.gridLayout_27.addWidget(self.ControlSystems_1_System_4ATF_Xs, 2, 0, 1, 1)
        self.gridLayout_28.addLayout(self.gridLayout_27, 0, 0, 1, 1)
        self.ControlSystems_1_System_tabWidget.addTab(self.ControlSystems_1_System_4ATF, "")
        self.ControlSystems_1_System_1TF = QtWidgets.QWidget()
        self.ControlSystems_1_System_1TF.setObjectName("ControlSystems_1_System_1TF")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.ControlSystems_1_System_1TF)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.ControlSystems_1_System_1TF_tableWidget = TableWidget(self.ControlSystems_1_System_1TF)
        self.ControlSystems_1_System_1TF_tableWidget.setRowCount(2)
        self.ControlSystems_1_System_1TF_tableWidget.setColumnCount(5)
        self.ControlSystems_1_System_1TF_tableWidget.setObjectName("ControlSystems_1_System_1TF_tableWidget")
        self.ControlSystems_1_System_1TF_tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.ControlSystems_1_System_1TF_tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_25.addWidget(self.ControlSystems_1_System_1TF_tableWidget, 0, 0, 1, 1)
        self.ControlSystems_1_System_tabWidget.addTab(self.ControlSystems_1_System_1TF, "")
        self.ControlSystems_1_System_2SS = QtWidgets.QWidget()
        self.ControlSystems_1_System_2SS.setObjectName("ControlSystems_1_System_2SS")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.ControlSystems_1_System_2SS)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.ControlSystems_1_System_2SS_tabWidget = QtWidgets.QTabWidget(self.ControlSystems_1_System_2SS)
        self.ControlSystems_1_System_2SS_tabWidget.setObjectName("ControlSystems_1_System_2SS_tabWidget")
        self.ControlSystems_1_System_2SS_A = QtWidgets.QWidget()
        self.ControlSystems_1_System_2SS_A.setObjectName("ControlSystems_1_System_2SS_A")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.ControlSystems_1_System_2SS_A)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.ControlSystems_1_System_2SS_A_tableWidget = TableWidget(self.ControlSystems_1_System_2SS_A)
        self.ControlSystems_1_System_2SS_A_tableWidget.setRowCount(3)
        self.ControlSystems_1_System_2SS_A_tableWidget.setColumnCount(3)
        self.ControlSystems_1_System_2SS_A_tableWidget.setObjectName("ControlSystems_1_System_2SS_A_tableWidget")
        self.ControlSystems_1_System_2SS_A_tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.gridLayout_21.addWidget(self.ControlSystems_1_System_2SS_A_tableWidget, 0, 0, 1, 1)
        self.ControlSystems_1_System_2SS_tabWidget.addTab(self.ControlSystems_1_System_2SS_A, "")
        self.ControlSystems_1_System_2SS_B = QtWidgets.QWidget()
        self.ControlSystems_1_System_2SS_B.setObjectName("ControlSystems_1_System_2SS_B")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.ControlSystems_1_System_2SS_B)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.ControlSystems_1_System_2SS_B_tableWidget = TableWidget(self.ControlSystems_1_System_2SS_B)
        self.ControlSystems_1_System_2SS_B_tableWidget.setRowCount(3)
        self.ControlSystems_1_System_2SS_B_tableWidget.setColumnCount(1)
        self.ControlSystems_1_System_2SS_B_tableWidget.setObjectName("ControlSystems_1_System_2SS_B_tableWidget")
        self.gridLayout_22.addWidget(self.ControlSystems_1_System_2SS_B_tableWidget, 0, 0, 1, 1)
        self.ControlSystems_1_System_2SS_tabWidget.addTab(self.ControlSystems_1_System_2SS_B, "")
        self.ControlSystems_1_System_2SS_C = QtWidgets.QWidget()
        self.ControlSystems_1_System_2SS_C.setObjectName("ControlSystems_1_System_2SS_C")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.ControlSystems_1_System_2SS_C)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.ControlSystems_1_System_2SS_C_tableWidget = TableWidget(self.ControlSystems_1_System_2SS_C)
        self.ControlSystems_1_System_2SS_C_tableWidget.setRowCount(1)
        self.ControlSystems_1_System_2SS_C_tableWidget.setColumnCount(3)
        self.ControlSystems_1_System_2SS_C_tableWidget.setObjectName("ControlSystems_1_System_2SS_C_tableWidget")
        self.ControlSystems_1_System_2SS_C_tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.gridLayout_23.addWidget(self.ControlSystems_1_System_2SS_C_tableWidget, 0, 0, 1, 1)
        self.ControlSystems_1_System_2SS_tabWidget.addTab(self.ControlSystems_1_System_2SS_C, "")
        self.ControlSystems_1_System_2SS_D = QtWidgets.QWidget()
        self.ControlSystems_1_System_2SS_D.setObjectName("ControlSystems_1_System_2SS_D")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.ControlSystems_1_System_2SS_D)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.ControlSystems_1_System_2SS_D_tableWidget = TableWidget(self.ControlSystems_1_System_2SS_D)
        self.ControlSystems_1_System_2SS_D_tableWidget.setRowCount(1)
        self.ControlSystems_1_System_2SS_D_tableWidget.setColumnCount(1)
        self.ControlSystems_1_System_2SS_D_tableWidget.setObjectName("ControlSystems_1_System_2SS_D_tableWidget")
        self.gridLayout_24.addWidget(self.ControlSystems_1_System_2SS_D_tableWidget, 0, 0, 1, 1)
        self.ControlSystems_1_System_2SS_tabWidget.addTab(self.ControlSystems_1_System_2SS_D, "")
        self.gridLayout_19.addWidget(self.ControlSystems_1_System_2SS_tabWidget, 0, 0, 1, 1)
        self.ControlSystems_1_System_tabWidget.addTab(self.ControlSystems_1_System_2SS, "")
        self.ControlSystems_1_System_3DE = QtWidgets.QWidget()
        self.ControlSystems_1_System_3DE.setObjectName("ControlSystems_1_System_3DE")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.ControlSystems_1_System_3DE)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.label = QtWidgets.QLabel(self.ControlSystems_1_System_3DE)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_29.addWidget(self.label, 0, 0, 1, 1)
        self.ControlSystems_1_System_tabWidget.addTab(self.ControlSystems_1_System_3DE, "")
        self.gridLayout_15.addWidget(self.ControlSystems_1_System_tabWidget, 0, 0, 1, 5)
        self.gridLayoutWidget = QtWidgets.QWidget(self.ControlSystems_1_Splitter_L)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.ControlSystems_1_SystemList = ListWidget(self.gridLayoutWidget)
        self.ControlSystems_1_SystemList.setObjectName("ControlSystems_1_SystemList")
        self.gridLayout_20.addWidget(self.ControlSystems_1_SystemList, 0, 0, 1, 1)
        self.ControlSystems_1_Splitter_R = QtWidgets.QSplitter(self.ControlSystems_1_Splitter_M)
        self.ControlSystems_1_Splitter_R.setOrientation(QtCore.Qt.Vertical)
        self.ControlSystems_1_Splitter_R.setObjectName("ControlSystems_1_Splitter_R")
        self.ControlSystems_1_Output_tabWidget = QtWidgets.QTabWidget(self.ControlSystems_1_Splitter_R)
        self.ControlSystems_1_Output_tabWidget.setObjectName("ControlSystems_1_Output_tabWidget")
        self.ControlSystems_1_Output_2L = QtWidgets.QWidget()
        self.ControlSystems_1_Output_2L.setObjectName("ControlSystems_1_Output_2L")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.ControlSystems_1_Output_2L)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.ControlSystems_1_Output_2L_LaTeXDisplay = MplWidget_LaTeX(self.ControlSystems_1_Output_2L)
        self.ControlSystems_1_Output_2L_LaTeXDisplay.setObjectName("ControlSystems_1_Output_2L_LaTeXDisplay")
        self.gridLayout_18.addWidget(self.ControlSystems_1_Output_2L_LaTeXDisplay, 0, 0, 1, 1)
        self.ControlSystems_1_Output_tabWidget.addTab(self.ControlSystems_1_Output_2L, "")
        self.ControlSystems_1_Output_1R = QtWidgets.QWidget()
        self.ControlSystems_1_Output_1R.setObjectName("ControlSystems_1_Output_1R")
        self.ControlSystems_1_Output_tabWidget.addTab(self.ControlSystems_1_Output_1R, "")
        self.ControlSystems_1_Input_tabWidget = QtWidgets.QTabWidget(self.ControlSystems_1_Splitter_R)
        self.ControlSystems_1_Input_tabWidget.setObjectName("ControlSystems_1_Input_tabWidget")
        self.ControlSystems_1_Input_1I = QtWidgets.QWidget()
        self.ControlSystems_1_Input_1I.setObjectName("ControlSystems_1_Input_1I")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.ControlSystems_1_Input_1I)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.ControlSystems_1_Input_InputFunction = AMaDiA_LineEdit(self.ControlSystems_1_Input_1I)
        self.ControlSystems_1_Input_InputFunction.setObjectName("ControlSystems_1_Input_InputFunction")
        self.gridLayout_30.addWidget(self.ControlSystems_1_Input_InputFunction, 1, 1, 1, 1)
        self.ControlSystems_1_Input_InputFunction_Label = QtWidgets.QLabel(self.ControlSystems_1_Input_1I)
        self.ControlSystems_1_Input_InputFunction_Label.setWordWrap(True)
        self.ControlSystems_1_Input_InputFunction_Label.setObjectName("ControlSystems_1_Input_InputFunction_Label")
        self.gridLayout_30.addWidget(self.ControlSystems_1_Input_InputFunction_Label, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.ControlSystems_1_Input_1I)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_30.addWidget(self.line_4, 0, 0, 1, 2)
        self.ControlSystems_1_Input_tabWidget.addTab(self.ControlSystems_1_Input_1I, "")
        self.ControlSystems_1_Input_2P = QtWidgets.QWidget()
        self.ControlSystems_1_Input_2P.setObjectName("ControlSystems_1_Input_2P")
        self.ControlSystems_1_Input_tabWidget.addTab(self.ControlSystems_1_Input_2P, "")
        self.gridLayout_26.addWidget(self.ControlSystems_1_Splitter_M, 0, 0, 1, 1)
        self.ControlSystems_tabWidget.addTab(self.ControlSystems_1, "")
        self.ControlSystems_2 = QtWidgets.QWidget()
        self.ControlSystems_2.setObjectName("ControlSystems_2")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.ControlSystems_2)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.ControlSystems_2_Display = MplWidget_CONTROL(self.ControlSystems_2)
        self.ControlSystems_2_Display.setObjectName("ControlSystems_2_Display")
        self.gridLayout_14.addWidget(self.ControlSystems_2_Display, 0, 0, 1, 1)
        self.ControlSystems_tabWidget.addTab(self.ControlSystems_2, "")
        self.ControlSystems_3 = QtWidgets.QWidget()
        self.ControlSystems_3.setObjectName("ControlSystems_3")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.ControlSystems_3)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.ControlSystems_3_SingleDisplay = MplWidget_CONTROL_single_plot(self.ControlSystems_3)
        self.ControlSystems_3_SingleDisplay.setObjectName("ControlSystems_3_SingleDisplay")
        self.gridLayout_17.addWidget(self.ControlSystems_3_SingleDisplay, 0, 0, 1, 1)
        self.ControlSystems_tabWidget.addTab(self.ControlSystems_3, "")
        self.ControlSystems_4 = QtWidgets.QWidget()
        self.ControlSystems_4.setObjectName("ControlSystems_4")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.ControlSystems_4)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.ControlSystems_4_Dirty_Input = AMaDiA_TextEdit(self.ControlSystems_4)
        self.ControlSystems_4_Dirty_Input.setObjectName("ControlSystems_4_Dirty_Input")
        self.gridLayout_16.addWidget(self.ControlSystems_4_Dirty_Input, 0, 0, 1, 1)
        self.ControlSystems_tabWidget.addTab(self.ControlSystems_4, "")
        self.gridLayout.addWidget(self.ControlSystems_tabWidget, 0, 0, 1, 1)
        SystemControlWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SystemControlWindow)
        self.ControlSystems_tabWidget.setCurrentIndex(0)
        self.ControlSystems_1_System_tabWidget.setCurrentIndex(0)
        self.ControlSystems_1_System_2SS_tabWidget.setCurrentIndex(0)
        self.ControlSystems_1_Output_tabWidget.setCurrentIndex(0)
        self.ControlSystems_1_Input_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SystemControlWindow)

    def retranslateUi(self, SystemControlWindow):
        _translate = QtCore.QCoreApplication.translate
        SystemControlWindow.setWindowTitle(_translate("SystemControlWindow", "System Control Window"))
        self.ControlSystems_1_SystemOrder_Confrim.setToolTip(_translate("SystemControlWindow", "Not necessary for Transfer-Tab"))
        self.ControlSystems_1_SystemOrder_Confrim.setText(_translate("SystemControlWindow", "Set Order"))
        self.ControlSystems_1_NameInput.setPlaceholderText(_translate("SystemControlWindow", "Name"))
        self.ControlSystems_1_SavePlotButton.setText(_translate("SystemControlWindow", "Save and Plot"))
        self.ControlSystems_1_SaveButton.setText(_translate("SystemControlWindow", "Save"))
        self.ControlSystems_1_System_4ATF_Ys.setPlaceholderText(_translate("SystemControlWindow", "Y(s)"))
        self.ControlSystems_1_System_4ATF_Xs.setPlaceholderText(_translate("SystemControlWindow", "X(s)"))
        self.ControlSystems_1_System_tabWidget.setTabText(self.ControlSystems_1_System_tabWidget.indexOf(self.ControlSystems_1_System_4ATF), _translate("SystemControlWindow", "Transfer"))
        self.ControlSystems_1_System_tabWidget.setTabText(self.ControlSystems_1_System_tabWidget.indexOf(self.ControlSystems_1_System_1TF), _translate("SystemControlWindow", "TF Table"))
        self.ControlSystems_1_System_2SS_tabWidget.setTabText(self.ControlSystems_1_System_2SS_tabWidget.indexOf(self.ControlSystems_1_System_2SS_A), _translate("SystemControlWindow", "A: State Matrix"))
        self.ControlSystems_1_System_2SS_tabWidget.setTabText(self.ControlSystems_1_System_2SS_tabWidget.indexOf(self.ControlSystems_1_System_2SS_B), _translate("SystemControlWindow", "B: Input Vector"))
        self.ControlSystems_1_System_2SS_tabWidget.setTabText(self.ControlSystems_1_System_2SS_tabWidget.indexOf(self.ControlSystems_1_System_2SS_C), _translate("SystemControlWindow", "C: Output Vector"))
        self.ControlSystems_1_System_2SS_tabWidget.setTabText(self.ControlSystems_1_System_2SS_tabWidget.indexOf(self.ControlSystems_1_System_2SS_D), _translate("SystemControlWindow", "D: Feedthrough Vector"))
        self.ControlSystems_1_System_tabWidget.setTabText(self.ControlSystems_1_System_tabWidget.indexOf(self.ControlSystems_1_System_2SS), _translate("SystemControlWindow", "State Space"))
        self.label.setText(_translate("SystemControlWindow", "Not implemented yet"))
        self.ControlSystems_1_System_tabWidget.setTabText(self.ControlSystems_1_System_tabWidget.indexOf(self.ControlSystems_1_System_3DE), _translate("SystemControlWindow", "ODE"))
        self.ControlSystems_1_Output_tabWidget.setTabText(self.ControlSystems_1_Output_tabWidget.indexOf(self.ControlSystems_1_Output_2L), _translate("SystemControlWindow", "LaTeX"))
        self.ControlSystems_1_Output_tabWidget.setTabText(self.ControlSystems_1_Output_tabWidget.indexOf(self.ControlSystems_1_Output_1R), _translate("SystemControlWindow", "Results"))
        self.ControlSystems_1_Input_InputFunction.setPlaceholderText(_translate("SystemControlWindow", "u(s)"))
        self.ControlSystems_1_Input_InputFunction_Label.setToolTip(_translate("SystemControlWindow", "This function will be used for the \"Forced Response\" plot"))
        self.ControlSystems_1_Input_InputFunction_Label.setText(_translate("SystemControlWindow", "Input Function:"))
        self.ControlSystems_1_Input_tabWidget.setTabText(self.ControlSystems_1_Input_tabWidget.indexOf(self.ControlSystems_1_Input_1I), _translate("SystemControlWindow", "Input"))
        self.ControlSystems_1_Input_tabWidget.setTabText(self.ControlSystems_1_Input_tabWidget.indexOf(self.ControlSystems_1_Input_2P), _translate("SystemControlWindow", "Plot Config"))
        self.ControlSystems_tabWidget.setTabText(self.ControlSystems_tabWidget.indexOf(self.ControlSystems_1), _translate("SystemControlWindow", "Input"))
        self.ControlSystems_tabWidget.setTabText(self.ControlSystems_tabWidget.indexOf(self.ControlSystems_2), _translate("SystemControlWindow", "Plots"))
        self.ControlSystems_tabWidget.setTabText(self.ControlSystems_tabWidget.indexOf(self.ControlSystems_3), _translate("SystemControlWindow", "Single Plot"))
        self.ControlSystems_tabWidget.setTabText(self.ControlSystems_tabWidget.indexOf(self.ControlSystems_4), _translate("SystemControlWindow", "Code Input"))

from AGeLib.AGeMain import ListWidget, MTabWidget, MplWidget_LaTeX, TableWidget
from AMaDiA_Files.AMaDiA_SystemControl_Widgets import MplWidget_CONTROL, MplWidget_CONTROL_single_plot
from AMaDiA_Files.AMaDiA_Widgets import AMaDiA_LineEdit, AMaDiA_TextEdit