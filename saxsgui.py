# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saxsgui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_SAXSgui(object):
    def setupUi(self, SAXSgui):
        SAXSgui.setObjectName(_fromUtf8("SAXSgui"))
        SAXSgui.resize(925, 630)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SAXSgui.sizePolicy().hasHeightForWidth())
        SAXSgui.setSizePolicy(sizePolicy)
        SAXSgui.setMinimumSize(QtCore.QSize(925, 630))
        SAXSgui.setFocusPolicy(QtCore.Qt.StrongFocus)
        SAXSgui.setWindowOpacity(1.0)
        SAXSgui.setAutoFillBackground(False)
        SAXSgui.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(SAXSgui)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Console = QtGui.QTabWidget(self.centralwidget)
        self.Console.setGeometry(QtCore.QRect(50, 30, 821, 541))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console.sizePolicy().hasHeightForWidth())
        self.Console.setSizePolicy(sizePolicy)
        self.Console.setObjectName(_fromUtf8("Console"))
        self.fourierspace_tab = QtGui.QWidget()
        self.fourierspace_tab.setObjectName(_fromUtf8("fourierspace_tab"))
        self.fourierView = GraphicsLayoutWidget(self.fourierspace_tab)
        self.fourierView.setGeometry(QtCore.QRect(10, 0, 511, 491))
        self.fourierView.setObjectName(_fromUtf8("fourierView"))
        self.checkLogY = QtGui.QCheckBox(self.fourierspace_tab)
        self.checkLogY.setGeometry(QtCore.QRect(540, 10, 131, 20))
        self.checkLogY.setObjectName(_fromUtf8("checkLogY"))
        self.checkLogX = QtGui.QCheckBox(self.fourierspace_tab)
        self.checkLogX.setGeometry(QtCore.QRect(540, 40, 131, 20))
        self.checkLogX.setObjectName(_fromUtf8("checkLogX"))
        self.beamview = GraphicsLayoutWidget(self.fourierspace_tab)
        self.beamview.setGeometry(QtCore.QRect(540, 300, 261, 191))
        self.beamview.setObjectName(_fromUtf8("beamview"))
        self.label_8 = QtGui.QLabel(self.fourierspace_tab)
        self.label_8.setGeometry(QtCore.QRect(550, 280, 121, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.nskip_spinbox = QtGui.QSpinBox(self.fourierspace_tab)
        self.nskip_spinbox.setGeometry(QtCore.QRect(550, 80, 57, 24))
        self.nskip_spinbox.setMaximum(1000)
        self.nskip_spinbox.setObjectName(_fromUtf8("nskip_spinbox"))
        self.label_19 = QtGui.QLabel(self.fourierspace_tab)
        self.label_19.setGeometry(QtCore.QRect(620, 80, 161, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.nskip2_spinbox = QtGui.QSpinBox(self.fourierspace_tab)
        self.nskip2_spinbox.setGeometry(QtCore.QRect(550, 110, 57, 24))
        self.nskip2_spinbox.setMinimum(0)
        self.nskip2_spinbox.setMaximum(1000)
        self.nskip2_spinbox.setProperty("value", 0)
        self.nskip2_spinbox.setObjectName(_fromUtf8("nskip2_spinbox"))
        self.label_20 = QtGui.QLabel(self.fourierspace_tab)
        self.label_20.setGeometry(QtCore.QRect(620, 110, 161, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_22 = QtGui.QLabel(self.fourierspace_tab)
        self.label_22.setGeometry(QtCore.QRect(550, 160, 62, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.fourierspace_tab)
        self.label_23.setGeometry(QtCore.QRect(550, 180, 62, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.qmin_label = QtGui.QLabel(self.fourierspace_tab)
        self.qmin_label.setGeometry(QtCore.QRect(605, 160, 206, 16))
        self.qmin_label.setObjectName(_fromUtf8("qmin_label"))
        self.qmax_label = QtGui.QLabel(self.fourierspace_tab)
        self.qmax_label.setGeometry(QtCore.QRect(605, 180, 206, 16))
        self.qmax_label.setObjectName(_fromUtf8("qmax_label"))
        self.Console.addTab(self.fourierspace_tab, _fromUtf8(""))
        self.guinierkratky_tab = QtGui.QWidget()
        self.guinierkratky_tab.setObjectName(_fromUtf8("guinierkratky_tab"))
        self.primaryanalysis_view = GraphicsLayoutWidget(self.guinierkratky_tab)
        self.primaryanalysis_view.setGeometry(QtCore.QRect(20, 10, 781, 401))
        self.primaryanalysis_view.setObjectName(_fromUtf8("primaryanalysis_view"))
        self.groupBox_4 = QtGui.QGroupBox(self.guinierkratky_tab)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 410, 341, 91))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.qRgmin = QtGui.QDoubleSpinBox(self.groupBox_4)
        self.qRgmin.setGeometry(QtCore.QRect(10, 30, 62, 24))
        self.qRgmin.setMaximum(1.0)
        self.qRgmin.setSingleStep(0.05)
        self.qRgmin.setProperty("value", 1.0)
        self.qRgmin.setObjectName(_fromUtf8("qRgmin"))
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(80, 30, 62, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(80, 60, 62, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.qRgmax = QtGui.QDoubleSpinBox(self.groupBox_4)
        self.qRgmax.setGeometry(QtCore.QRect(10, 60, 62, 24))
        self.qRgmax.setMaximum(3.0)
        self.qRgmax.setSingleStep(0.05)
        self.qRgmax.setProperty("value", 1.3)
        self.qRgmax.setObjectName(_fromUtf8("qRgmax"))
        self.guinierminpts = QtGui.QLineEdit(self.groupBox_4)
        self.guinierminpts.setGeometry(QtCore.QRect(180, 30, 61, 21))
        self.guinierminpts.setObjectName(_fromUtf8("guinierminpts"))
        self.label_18 = QtGui.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(250, 30, 71, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.autoguinier_button = QtGui.QPushButton(self.groupBox_4)
        self.autoguinier_button.setGeometry(QtCore.QRect(210, 55, 91, 26))
        self.autoguinier_button.setStyleSheet(_fromUtf8("background-color: #F1BF29; font-size: 12px; color: green;"))
        self.autoguinier_button.setObjectName(_fromUtf8("autoguinier_button"))
        self.runprimaryanalysis = QtGui.QPushButton(self.guinierkratky_tab)
        self.runprimaryanalysis.setGeometry(QtCore.QRect(580, 435, 111, 26))
        self.runprimaryanalysis.setStyleSheet(_fromUtf8("background-color: #F1BF29; font-size: 12px; color: blue;"))
        self.runprimaryanalysis.setObjectName(_fromUtf8("runprimaryanalysis"))
        self.lb_guinier_spinbox = QtGui.QSpinBox(self.guinierkratky_tab)
        self.lb_guinier_spinbox.setGeometry(QtCore.QRect(410, 435, 57, 24))
        self.lb_guinier_spinbox.setObjectName(_fromUtf8("lb_guinier_spinbox"))
        self.ub_guinier_spinbox = QtGui.QSpinBox(self.guinierkratky_tab)
        self.ub_guinier_spinbox.setGeometry(QtCore.QRect(495, 435, 57, 24))
        self.ub_guinier_spinbox.setMaximum(200)
        self.ub_guinier_spinbox.setObjectName(_fromUtf8("ub_guinier_spinbox"))
        self.label_6 = QtGui.QLabel(self.guinierkratky_tab)
        self.label_6.setGeometry(QtCore.QRect(475, 440, 16, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.guinierkratky_tab)
        self.label_7.setGeometry(QtCore.QRect(380, 440, 26, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_21 = QtGui.QLabel(self.guinierkratky_tab)
        self.label_21.setGeometry(QtCore.QRect(375, 470, 91, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.qRg_label = QtGui.QLabel(self.guinierkratky_tab)
        self.qRg_label.setGeometry(QtCore.QRect(465, 470, 126, 16))
        self.qRg_label.setObjectName(_fromUtf8("qRg_label"))
        self.label_4 = QtGui.QLabel(self.guinierkratky_tab)
        self.label_4.setGeometry(QtCore.QRect(375, 490, 36, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.guinierkratky_tab)
        self.label_5.setGeometry(QtCore.QRect(470, 490, 36, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.guinierRg_label = QtGui.QLabel(self.guinierkratky_tab)
        self.guinierRg_label.setGeometry(QtCore.QRect(405, 490, 62, 16))
        self.guinierRg_label.setObjectName(_fromUtf8("guinierRg_label"))
        self.I0_label = QtGui.QLabel(self.guinierkratky_tab)
        self.I0_label.setGeometry(QtCore.QRect(500, 490, 151, 16))
        self.I0_label.setObjectName(_fromUtf8("I0_label"))
        self.Console.addTab(self.guinierkratky_tab, _fromUtf8(""))
        self.realspace_tab = QtGui.QWidget()
        self.realspace_tab.setObjectName(_fromUtf8("realspace_tab"))
        self.realspaceView = GraphicsLayoutWidget(self.realspace_tab)
        self.realspaceView.setGeometry(QtCore.QRect(10, 0, 531, 491))
        self.realspaceView.setObjectName(_fromUtf8("realspaceView"))
        self.groupBox_3 = QtGui.QGroupBox(self.realspace_tab)
        self.groupBox_3.setGeometry(QtCore.QRect(550, 0, 261, 141))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.Nr_input = QtGui.QLineEdit(self.groupBox_3)
        self.Nr_input.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.Nr_input.setObjectName(_fromUtf8("Nr_input"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 166, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(90, 40, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(90, 100, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.logalpha_input = QtGui.QLineEdit(self.groupBox_3)
        self.logalpha_input.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.logalpha_input.setObjectName(_fromUtf8("logalpha_input"))
        self.dmax_input = QtGui.QLineEdit(self.groupBox_3)
        self.dmax_input.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.dmax_input.setObjectName(_fromUtf8("dmax_input"))
        self.groupBox = QtGui.QGroupBox(self.realspace_tab)
        self.groupBox.setGeometry(QtCore.QRect(550, 210, 151, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.varianceweighted = QtGui.QCheckBox(self.groupBox)
        self.varianceweighted.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.varianceweighted.setObjectName(_fromUtf8("varianceweighted"))
        self.smeared = QtGui.QCheckBox(self.groupBox)
        self.smeared.setGeometry(QtCore.QRect(10, 55, 87, 20))
        self.smeared.setObjectName(_fromUtf8("smeared"))
        self.solvepr_button = QtGui.QPushButton(self.realspace_tab)
        self.solvepr_button.setGeometry(QtCore.QRect(630, 440, 114, 32))
        self.solvepr_button.setStyleSheet(_fromUtf8("background-color: #0085ff; color: #ffffff;"))
        self.solvepr_button.setObjectName(_fromUtf8("solvepr_button"))
        self.iftresultout = QtGui.QLineEdit(self.realspace_tab)
        self.iftresultout.setGeometry(QtCore.QRect(550, 400, 261, 21))
        self.iftresultout.setObjectName(_fromUtf8("iftresultout"))
        self.saveiftresult = QtGui.QCheckBox(self.realspace_tab)
        self.saveiftresult.setGeometry(QtCore.QRect(550, 370, 241, 20))
        self.saveiftresult.setObjectName(_fromUtf8("saveiftresult"))
        self.Console.addTab(self.realspace_tab, _fromUtf8(""))
        self.bayesianift_tab = QtGui.QWidget()
        self.bayesianift_tab.setObjectName(_fromUtf8("bayesianift_tab"))
        self.biftgridView = matplotlibWidget(self.bayesianift_tab)
        self.biftgridView.setGeometry(QtCore.QRect(10, 0, 401, 411))
        self.biftgridView.setObjectName(_fromUtf8("biftgridView"))
        self.groupBox_2 = QtGui.QGroupBox(self.bayesianift_tab)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 0, 381, 161))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.Nalpha = QtGui.QLineEdit(self.groupBox_2)
        self.Nalpha.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.Nalpha.setObjectName(_fromUtf8("Nalpha"))
        self.Ndmax = QtGui.QLineEdit(self.groupBox_2)
        self.Ndmax.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.Ndmax.setObjectName(_fromUtf8("Ndmax"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(70, 30, 91, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(70, 60, 101, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.minlogalpha = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.minlogalpha.setGeometry(QtCore.QRect(20, 120, 62, 24))
        self.minlogalpha.setMinimum(-100.0)
        self.minlogalpha.setMaximum(100.0)
        self.minlogalpha.setObjectName(_fromUtf8("minlogalpha"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.maxlogalpha = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.maxlogalpha.setGeometry(QtCore.QRect(110, 120, 62, 24))
        self.maxlogalpha.setMinimum(-100.0)
        self.maxlogalpha.setMaximum(100.0)
        self.maxlogalpha.setObjectName(_fromUtf8("maxlogalpha"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(220, 100, 111, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.mindmax = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.mindmax.setGeometry(QtCore.QRect(220, 120, 62, 24))
        self.mindmax.setDecimals(3)
        self.mindmax.setMaximum(9999.0)
        self.mindmax.setObjectName(_fromUtf8("mindmax"))
        self.maxdmax = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.maxdmax.setGeometry(QtCore.QRect(310, 120, 62, 24))
        self.maxdmax.setDecimals(3)
        self.maxdmax.setMaximum(9999.0)
        self.maxdmax.setObjectName(_fromUtf8("maxdmax"))
        self.calcbiftgrid = QtGui.QPushButton(self.bayesianift_tab)
        self.calcbiftgrid.setGeometry(QtCore.QRect(520, 180, 191, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.calcbiftgrid.setFont(font)
        self.calcbiftgrid.setStyleSheet(_fromUtf8("background-color: #6495ed; color: #ffffff;"))
        self.calcbiftgrid.setObjectName(_fromUtf8("calcbiftgrid"))
        self.label_12 = QtGui.QLabel(self.bayesianift_tab)
        self.label_12.setGeometry(QtCore.QRect(510, 120, 10, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_14 = QtGui.QLabel(self.bayesianift_tab)
        self.label_14.setGeometry(QtCore.QRect(710, 120, 10, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.Ncalcerror_input = QtGui.QLineEdit(self.bayesianift_tab)
        self.Ncalcerror_input.setGeometry(QtCore.QRect(430, 310, 61, 20))
        self.Ncalcerror_input.setObjectName(_fromUtf8("Ncalcerror_input"))
        self.label_15 = QtGui.QLabel(self.bayesianift_tab)
        self.label_15.setGeometry(QtCore.QRect(500, 310, 211, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.refinebift = QtGui.QPushButton(self.bayesianift_tab)
        self.refinebift.setGeometry(QtCore.QRect(510, 350, 211, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.refinebift.setFont(font)
        self.refinebift.setStyleSheet(_fromUtf8("background-color:#87cc83; color: #ffffff;"))
        self.refinebift.setObjectName(_fromUtf8("refinebift"))
        self.line = QtGui.QFrame(self.bayesianift_tab)
        self.line.setGeometry(QtCore.QRect(420, 270, 391, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.Console.addTab(self.bayesianift_tab, _fromUtf8(""))
        SAXSgui.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SAXSgui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        SAXSgui.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SAXSgui)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SAXSgui.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(SAXSgui)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(SAXSgui)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionExit = QtGui.QAction(SAXSgui)
        self.actionExit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionGuinier_Plot = QtGui.QAction(SAXSgui)
        self.actionGuinier_Plot.setObjectName(_fromUtf8("actionGuinier_Plot"))
        self.actionKratky_Plot = QtGui.QAction(SAXSgui)
        self.actionKratky_Plot.setObjectName(_fromUtf8("actionKratky_Plot"))
        self.actionSAXSMoW = QtGui.QAction(SAXSgui)
        self.actionSAXSMoW.setObjectName(_fromUtf8("actionSAXSMoW"))
        self.actionFoXS_fit = QtGui.QAction(SAXSgui)
        self.actionFoXS_fit.setObjectName(_fromUtf8("actionFoXS_fit"))
        self.actionLoad_Beam_Profile = QtGui.QAction(SAXSgui)
        self.actionLoad_Beam_Profile.setObjectName(_fromUtf8("actionLoad_Beam_Profile"))
        self.actionSave_as_GNOM_file = QtGui.QAction(SAXSgui)
        self.actionSave_as_GNOM_file.setObjectName(_fromUtf8("actionSave_as_GNOM_file"))
        self.actionSAXSMoW_2 = QtGui.QAction(SAXSgui)
        self.actionSAXSMoW_2.setObjectName(_fromUtf8("actionSAXSMoW_2"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as_GNOM_file)
        self.menuFile.addAction(self.actionLoad_Beam_Profile)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(SAXSgui)
        self.Console.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SAXSgui)

    def retranslateUi(self, SAXSgui):
        SAXSgui.setWindowTitle(_translate("SAXSgui", "UCSFsaxs v0.6", None))
        self.checkLogY.setText(_translate("SAXSgui", "Log-scale Y-axis", None))
        self.checkLogX.setText(_translate("SAXSgui", "Log-scale X-axis", None))
        self.label_8.setText(_translate("SAXSgui", "Beam Profile", None))
        self.label_19.setText(_translate("SAXSgui", "Initial Points to skip", None))
        self.label_20.setText(_translate("SAXSgui", "End Points to skip", None))
        self.label_22.setText(_translate("SAXSgui", "q_min : ", None))
        self.label_23.setText(_translate("SAXSgui", "q_max : ", None))
        self.qmin_label.setText(_translate("SAXSgui", "None", None))
        self.qmax_label.setText(_translate("SAXSgui", "None", None))
        self.Console.setTabText(self.Console.indexOf(self.fourierspace_tab), _translate("SAXSgui", "Fourier Space (Scattering)", None))
        self.groupBox_4.setTitle(_translate("SAXSgui", "Automated Guinier Analysis", None))
        self.label_16.setText(_translate("SAXSgui", "qRg_min", None))
        self.label_17.setText(_translate("SAXSgui", "qRg_max", None))
        self.guinierminpts.setText(_translate("SAXSgui", "10", None))
        self.label_18.setText(_translate("SAXSgui", "Min. points", None))
        self.autoguinier_button.setText(_translate("SAXSgui", "Do it (Auto)!", None))
        self.runprimaryanalysis.setText(_translate("SAXSgui", "Do it (Manual)!", None))
        self.label_6.setText(_translate("SAXSgui", "to", None))
        self.label_7.setText(_translate("SAXSgui", "Fit", None))
        self.label_21.setText(_translate("SAXSgui", "current qRg : ", None))
        self.qRg_label.setText(_translate("SAXSgui", "None", None))
        self.label_4.setText(_translate("SAXSgui", "Rg : ", None))
        self.label_5.setText(_translate("SAXSgui", "I(0):", None))
        self.guinierRg_label.setText(_translate("SAXSgui", "None", None))
        self.I0_label.setText(_translate("SAXSgui", "None", None))
        self.Console.setTabText(self.Console.indexOf(self.guinierkratky_tab), _translate("SAXSgui", "Guinier, Kratky Plots", None))
        self.groupBox_3.setTitle(_translate("SAXSgui", "IFT parameters", None))
        self.label_2.setText(_translate("SAXSgui", "Log(alpha) - Smoothness", None))
        self.label.setText(_translate("SAXSgui", "Dmax", None))
        self.label_3.setText(_translate("SAXSgui", "# of points in P(r)", None))
        self.groupBox.setTitle(_translate("SAXSgui", "Data Parameters", None))
        self.varianceweighted.setText(_translate("SAXSgui", "σ^2 weighted", None))
        self.smeared.setText(_translate("SAXSgui", "Smeared", None))
        self.solvepr_button.setText(_translate("SAXSgui", "Solve P(r)!", None))
        self.saveiftresult.setText(_translate("SAXSgui", "Save File? Enter file name below:", None))
        self.Console.setTabText(self.Console.indexOf(self.realspace_tab), _translate("SAXSgui", "Real Space", None))
        self.groupBox_2.setTitle(_translate("SAXSgui", "Grid Search Parameters", None))
        self.label_9.setText(_translate("SAXSgui", "No. of alpha", None))
        self.label_10.setText(_translate("SAXSgui", "No. of Dmax", None))
        self.label_11.setText(_translate("SAXSgui", "log(alpha) Range", None))
        self.label_13.setText(_translate("SAXSgui", "Dmax Range", None))
        self.calcbiftgrid.setText(_translate("SAXSgui", "Calculate Grid", None))
        self.label_12.setText(_translate("SAXSgui", "-", None))
        self.label_14.setText(_translate("SAXSgui", "-", None))
        self.label_15.setText(_translate("SAXSgui", "No. of error calculations (>100)", None))
        self.refinebift.setText(_translate("SAXSgui", "Refine Solution (Simplex)", None))
        self.Console.setTabText(self.Console.indexOf(self.bayesianift_tab), _translate("SAXSgui", "BayesianIFT", None))
        self.menuFile.setTitle(_translate("SAXSgui", "File", None))
        self.actionOpen.setText(_translate("SAXSgui", "Open", None))
        self.actionOpen.setToolTip(_translate("SAXSgui", "Open SAXS data file", None))
        self.actionClose.setText(_translate("SAXSgui", "Close", None))
        self.actionExit.setText(_translate("SAXSgui", "Exit Program", None))
        self.actionGuinier_Plot.setText(_translate("SAXSgui", "Guinier Plot", None))
        self.actionKratky_Plot.setText(_translate("SAXSgui", "Kratky Plot", None))
        self.actionSAXSMoW.setText(_translate("SAXSgui", "SAXSMoW", None))
        self.actionFoXS_fit.setText(_translate("SAXSgui", "FoXS fit ...", None))
        self.actionLoad_Beam_Profile.setText(_translate("SAXSgui", "Load Beam Profile", None))
        self.actionSave_as_GNOM_file.setText(_translate("SAXSgui", "Save as GNOM file ...", None))
        self.actionSAXSMoW_2.setText(_translate("SAXSgui", "SAXSMoW", None))

from mplWidget import matplotlibWidget
from pyqtgraph import GraphicsLayoutWidget
