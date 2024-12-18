# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WF_ParCurveGui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(430, 708)
        Form.setMinimumSize(QSize(0, 0))
        self.gridLayout_41 = QGridLayout(Form)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_quit = QPushButton(Form)
        self.button_quit.setObjectName(u"button_quit")

        self.horizontalLayout.addWidget(self.button_quit)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_17)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.label_release = QLabel(Form)
        self.label_release.setObjectName(u"label_release")

        self.horizontalLayout.addWidget(self.label_release)


        self.gridLayout_41.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.tabWidget_6 = QTabWidget(Form)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_8 = QScrollArea(self.tab)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setMinimumSize(QSize(398, 500))
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 394, 599))
        self.gridLayout_38 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.tabWidget_8 = QTabWidget(self.scrollAreaWidgetContents_8)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_8.sizePolicy().hasHeightForWidth())
        self.tabWidget_8.setSizePolicy(sizePolicy)
        self.Wire_Tab1_3 = QWidget()
        self.Wire_Tab1_3.setObjectName(u"Wire_Tab1_3")
        self.gridLayout_20 = QGridLayout(self.Wire_Tab1_3)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.tabWidget_4 = QTabWidget(self.Wire_Tab1_3)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        sizePolicy.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy)
        self.tabWidget_4.setMinimumSize(QSize(332, 450))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_19 = QGridLayout(self.tab_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.Reg2DCurve_button_select_points = QPushButton(self.tab_5)
        self.Reg2DCurve_button_select_points.setObjectName(u"Reg2DCurve_button_select_points")

        self.gridLayout_19.addWidget(self.Reg2DCurve_button_select_points, 0, 0, 1, 1)

        self.Reg2DCurve_input_textEdit = QTextEdit(self.tab_5)
        self.Reg2DCurve_input_textEdit.setObjectName(u"Reg2DCurve_input_textEdit")
        sizePolicy.setHeightForWidth(self.Reg2DCurve_input_textEdit.sizePolicy().hasHeightForWidth())
        self.Reg2DCurve_input_textEdit.setSizePolicy(sizePolicy)
        self.Reg2DCurve_input_textEdit.setMinimumSize(QSize(312, 400))

        self.gridLayout_19.addWidget(self.Reg2DCurve_input_textEdit, 1, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_33 = QGridLayout(self.tab_6)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.Reg2DCurve_comboBox = QComboBox(self.tab_6)
        self.Reg2DCurve_comboBox.addItem("")
        self.Reg2DCurve_comboBox.setObjectName(u"Reg2DCurve_comboBox")

        self.gridLayout_33.addWidget(self.Reg2DCurve_comboBox, 0, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label = QLabel(self.tab_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_18.addWidget(self.label)

        self.Reg2DCurve_degree_select = QSpinBox(self.tab_6)
        self.Reg2DCurve_degree_select.setObjectName(u"Reg2DCurve_degree_select")
        self.Reg2DCurve_degree_select.setMinimum(1)
        self.Reg2DCurve_degree_select.setValue(2)

        self.horizontalLayout_18.addWidget(self.Reg2DCurve_degree_select)


        self.gridLayout_33.addLayout(self.horizontalLayout_18, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_33.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.tab_6)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_34 = QGridLayout(self.groupBox_20)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.checkBox_points_reg1 = QCheckBox(self.groupBox_20)
        self.checkBox_points_reg1.setObjectName(u"checkBox_points_reg1")
        self.checkBox_points_reg1.setAutoExclusive(True)

        self.gridLayout_34.addWidget(self.checkBox_points_reg1, 0, 0, 1, 1)

        self.checkBox_polyline_reg1 = QCheckBox(self.groupBox_20)
        self.checkBox_polyline_reg1.setObjectName(u"checkBox_polyline_reg1")
        self.checkBox_polyline_reg1.setChecked(True)
        self.checkBox_polyline_reg1.setAutoExclusive(True)

        self.gridLayout_34.addWidget(self.checkBox_polyline_reg1, 0, 1, 1, 1)

        self.checkBox_bezier_reg1 = QCheckBox(self.groupBox_20)
        self.checkBox_bezier_reg1.setObjectName(u"checkBox_bezier_reg1")
        self.checkBox_bezier_reg1.setEnabled(True)
        self.checkBox_bezier_reg1.setChecked(False)
        self.checkBox_bezier_reg1.setAutoExclusive(True)

        self.gridLayout_34.addWidget(self.checkBox_bezier_reg1, 1, 0, 1, 1)

        self.checkBox_bspline_reg1 = QCheckBox(self.groupBox_20)
        self.checkBox_bspline_reg1.setObjectName(u"checkBox_bspline_reg1")
        self.checkBox_bspline_reg1.setEnabled(True)
        self.checkBox_bspline_reg1.setChecked(False)
        self.checkBox_bspline_reg1.setAutoExclusive(True)

        self.gridLayout_34.addWidget(self.checkBox_bspline_reg1, 1, 1, 1, 1)


        self.gridLayout_33.addWidget(self.groupBox_20, 3, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_37 = QGridLayout(self.tab_7)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.scrollArea_3 = QScrollArea(self.tab_7)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 338, 441))
        self.gridLayout_35 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.Reg2DCurve_function_textEdit = QTextEdit(self.scrollAreaWidgetContents_2)
        self.Reg2DCurve_function_textEdit.setObjectName(u"Reg2DCurve_function_textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Reg2DCurve_function_textEdit.sizePolicy().hasHeightForWidth())
        self.Reg2DCurve_function_textEdit.setSizePolicy(sizePolicy1)

        self.gridLayout_35.addWidget(self.Reg2DCurve_function_textEdit, 0, 0, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_regmin_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_regmin_1.setObjectName(u"label_regmin_1")
        self.label_regmin_1.setMaximumSize(QSize(70, 16777215))
        self.label_regmin_1.setLayoutDirection(Qt.LeftToRight)
        self.label_regmin_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_regmin_1)

        self.Reg2DCurve_min = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Reg2DCurve_min.setObjectName(u"Reg2DCurve_min")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Reg2DCurve_min.sizePolicy().hasHeightForWidth())
        self.Reg2DCurve_min.setSizePolicy(sizePolicy2)
        self.Reg2DCurve_min.setMinimumSize(QSize(40, 0))
        self.Reg2DCurve_min.setMaximumSize(QSize(150, 16777215))
        self.Reg2DCurve_min.setMaxLength(32769)

        self.horizontalLayout_28.addWidget(self.Reg2DCurve_min)


        self.gridLayout_25.addLayout(self.horizontalLayout_28, 0, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_regmax_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_regmax_1.setObjectName(u"label_regmax_1")
        self.label_regmax_1.setMaximumSize(QSize(70, 16777215))
        self.label_regmax_1.setLayoutDirection(Qt.LeftToRight)
        self.label_regmax_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_regmax_1)

        self.Reg2DCurve_max = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Reg2DCurve_max.setObjectName(u"Reg2DCurve_max")
        sizePolicy2.setHeightForWidth(self.Reg2DCurve_max.sizePolicy().hasHeightForWidth())
        self.Reg2DCurve_max.setSizePolicy(sizePolicy2)
        self.Reg2DCurve_max.setMinimumSize(QSize(40, 0))
        self.Reg2DCurve_max.setMaximumSize(QSize(150, 16777215))
        self.Reg2DCurve_max.setMaxLength(32769)

        self.horizontalLayout_29.addWidget(self.Reg2DCurve_max)


        self.gridLayout_25.addLayout(self.horizontalLayout_29, 1, 0, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_regstep_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_regstep_1.setObjectName(u"label_regstep_1")
        self.label_regstep_1.setMaximumSize(QSize(70, 16777215))
        self.label_regstep_1.setLayoutDirection(Qt.LeftToRight)
        self.label_regstep_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_regstep_1)

        self.Reg2DCurve_step = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Reg2DCurve_step.setObjectName(u"Reg2DCurve_step")
        sizePolicy2.setHeightForWidth(self.Reg2DCurve_step.sizePolicy().hasHeightForWidth())
        self.Reg2DCurve_step.setSizePolicy(sizePolicy2)
        self.Reg2DCurve_step.setMinimumSize(QSize(40, 0))
        self.Reg2DCurve_step.setMaximumSize(QSize(150, 16777215))
        self.Reg2DCurve_step.setMaxLength(32769)

        self.horizontalLayout_30.addWidget(self.Reg2DCurve_step)


        self.gridLayout_25.addLayout(self.horizontalLayout_30, 2, 0, 1, 1)


        self.gridLayout_35.addLayout(self.gridLayout_25, 1, 0, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_Reg2DCurve_z = QLabel(self.scrollAreaWidgetContents_2)
        self.label_Reg2DCurve_z.setObjectName(u"label_Reg2DCurve_z")
        self.label_Reg2DCurve_z.setMaximumSize(QSize(70, 16777215))
        self.label_Reg2DCurve_z.setLayoutDirection(Qt.LeftToRight)
        self.label_Reg2DCurve_z.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_Reg2DCurve_z)

        self.Reg2DCurve_z = QLineEdit(self.scrollAreaWidgetContents_2)
        self.Reg2DCurve_z.setObjectName(u"Reg2DCurve_z")
        sizePolicy2.setHeightForWidth(self.Reg2DCurve_z.sizePolicy().hasHeightForWidth())
        self.Reg2DCurve_z.setSizePolicy(sizePolicy2)
        self.Reg2DCurve_z.setMinimumSize(QSize(40, 0))
        self.Reg2DCurve_z.setMaximumSize(QSize(150, 16777215))
        self.Reg2DCurve_z.setMaxLength(32769)

        self.horizontalLayout_32.addWidget(self.Reg2DCurve_z)


        self.gridLayout_35.addLayout(self.horizontalLayout_32, 2, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_37.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_7, "")

        self.gridLayout_20.addWidget(self.tabWidget_4, 0, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.Reg2DCurve_button_apply = QPushButton(self.Wire_Tab1_3)
        self.Reg2DCurve_button_apply.setObjectName(u"Reg2DCurve_button_apply")
        self.Reg2DCurve_button_apply.setMinimumSize(QSize(40, 0))
        self.Reg2DCurve_button_apply.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_19.addWidget(self.Reg2DCurve_button_apply)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)


        self.gridLayout_20.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)

        self.tabWidget_8.addTab(self.Wire_Tab1_3, "")
        self.Wire_Tab2_3 = QWidget()
        self.Wire_Tab2_3.setObjectName(u"Wire_Tab2_3")
        self.gridLayout_36 = QGridLayout(self.Wire_Tab2_3)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.scrollArea_2 = QScrollArea(self.Wire_Tab2_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -104, 337, 638))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.ParCurve_comboBox_2 = QComboBox(self.scrollAreaWidgetContents_5)
        self.ParCurve_comboBox_2.setObjectName(u"ParCurve_comboBox_2")

        self.horizontalLayout_59.addWidget(self.ParCurve_comboBox_2)

        self.ParCurve_button_edit_2 = QPushButton(self.scrollAreaWidgetContents_5)
        self.ParCurve_button_edit_2.setObjectName(u"ParCurve_button_edit_2")
        self.ParCurve_button_edit_2.setMinimumSize(QSize(40, 0))
        self.ParCurve_button_edit_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_59.addWidget(self.ParCurve_button_edit_2)


        self.gridLayout.addLayout(self.horizontalLayout_59, 0, 0, 1, 1)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_name_2 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_name_2.setObjectName(u"label_name_2")
        self.label_name_2.setFrameShape(QFrame.Box)
        self.label_name_2.setFrameShadow(QFrame.Raised)
        self.label_name_2.setLineWidth(3)
        self.label_name_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_name_2)

        self.ParCurve_name_2 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.ParCurve_name_2.setObjectName(u"ParCurve_name_2")

        self.horizontalLayout_60.addWidget(self.ParCurve_name_2)


        self.gridLayout.addLayout(self.horizontalLayout_60, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_dim_2 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_dim_2.setObjectName(u"label_dim_2")

        self.horizontalLayout_2.addWidget(self.label_dim_2)

        self.ParCurve_combo_dim_2D = QComboBox(self.scrollAreaWidgetContents_5)
        self.ParCurve_combo_dim_2D.addItem("")
        self.ParCurve_combo_dim_2D.addItem("")
        self.ParCurve_combo_dim_2D.addItem("")
        self.ParCurve_combo_dim_2D.addItem("")
        self.ParCurve_combo_dim_2D.addItem("")
        self.ParCurve_combo_dim_2D.addItem("")
        self.ParCurve_combo_dim_2D.setObjectName(u"ParCurve_combo_dim_2D")
        self.ParCurve_combo_dim_2D.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.ParCurve_combo_dim_2D)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.groupBox_16 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_2 = QGridLayout(self.groupBox_16)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_points_2 = QCheckBox(self.groupBox_16)
        self.checkBox_points_2.setObjectName(u"checkBox_points_2")
        self.checkBox_points_2.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.checkBox_points_2, 0, 0, 1, 1)

        self.checkBox_polyline_2 = QCheckBox(self.groupBox_16)
        self.checkBox_polyline_2.setObjectName(u"checkBox_polyline_2")
        self.checkBox_polyline_2.setChecked(True)
        self.checkBox_polyline_2.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.checkBox_polyline_2, 0, 1, 1, 1)

        self.checkBox_bezier_2 = QCheckBox(self.groupBox_16)
        self.checkBox_bezier_2.setObjectName(u"checkBox_bezier_2")
        self.checkBox_bezier_2.setEnabled(True)
        self.checkBox_bezier_2.setChecked(False)
        self.checkBox_bezier_2.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.checkBox_bezier_2, 1, 0, 1, 1)

        self.checkBox_bspline_2 = QCheckBox(self.groupBox_16)
        self.checkBox_bspline_2.setObjectName(u"checkBox_bspline_2")
        self.checkBox_bspline_2.setEnabled(True)
        self.checkBox_bspline_2.setChecked(False)
        self.checkBox_bspline_2.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.checkBox_bspline_2, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_16, 4, 0, 1, 1)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.checkBox_close_2 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_close_2.setObjectName(u"checkBox_close_2")
        self.checkBox_close_2.setEnabled(True)

        self.horizontalLayout_61.addWidget(self.checkBox_close_2)

        self.checkBox_face_2 = QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_face_2.setObjectName(u"checkBox_face_2")
        self.checkBox_face_2.setEnabled(False)

        self.horizontalLayout_61.addWidget(self.checkBox_face_2)


        self.gridLayout.addLayout(self.horizontalLayout_61, 5, 0, 1, 1)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.ParCurve_button_store_2 = QPushButton(self.scrollAreaWidgetContents_5)
        self.ParCurve_button_store_2.setObjectName(u"ParCurve_button_store_2")
        self.ParCurve_button_store_2.setMinimumSize(QSize(40, 0))
        self.ParCurve_button_store_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_62.addWidget(self.ParCurve_button_store_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_8)

        self.ParCurve_button_apply_2 = QPushButton(self.scrollAreaWidgetContents_5)
        self.ParCurve_button_apply_2.setObjectName(u"ParCurve_button_apply_2")
        self.ParCurve_button_apply_2.setMinimumSize(QSize(40, 0))
        self.ParCurve_button_apply_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_62.addWidget(self.ParCurve_button_apply_2)


        self.gridLayout.addLayout(self.horizontalLayout_62, 6, 0, 1, 1)

        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents_5)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Equation_tab_2 = QWidget()
        self.Equation_tab_2.setObjectName(u"Equation_tab_2")
        self.gridLayout_23 = QGridLayout(self.Equation_tab_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.groupBox_14 = QGroupBox(self.Equation_tab_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_22 = QGridLayout(self.groupBox_14)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_a_3 = QLabel(self.groupBox_14)
        self.label_a_3.setObjectName(u"label_a_3")
        self.label_a_3.setMaximumSize(QSize(70, 16777215))
        self.label_a_3.setLayoutDirection(Qt.LeftToRight)
        self.label_a_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_a_3)

        self.ParCurve_a_2 = QLineEdit(self.groupBox_14)
        self.ParCurve_a_2.setObjectName(u"ParCurve_a_2")
        sizePolicy2.setHeightForWidth(self.ParCurve_a_2.sizePolicy().hasHeightForWidth())
        self.ParCurve_a_2.setSizePolicy(sizePolicy2)
        self.ParCurve_a_2.setMinimumSize(QSize(40, 0))
        self.ParCurve_a_2.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_a_2.setMaxLength(32769)

        self.horizontalLayout_3.addWidget(self.ParCurve_a_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_b_3 = QLabel(self.groupBox_14)
        self.label_b_3.setObjectName(u"label_b_3")
        self.label_b_3.setMaximumSize(QSize(70, 16777215))
        self.label_b_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_b_3)

        self.ParCurve_b_2 = QLineEdit(self.groupBox_14)
        self.ParCurve_b_2.setObjectName(u"ParCurve_b_2")
        sizePolicy2.setHeightForWidth(self.ParCurve_b_2.sizePolicy().hasHeightForWidth())
        self.ParCurve_b_2.setSizePolicy(sizePolicy2)
        self.ParCurve_b_2.setMinimumSize(QSize(40, 0))
        self.ParCurve_b_2.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_b_2.setMaxLength(32769)

        self.horizontalLayout_4.addWidget(self.ParCurve_b_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)


        self.gridLayout_22.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.checkBox_polar_2 = QCheckBox(self.groupBox_14)
        self.checkBox_polar_2.setObjectName(u"checkBox_polar_2")
        self.checkBox_polar_2.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.checkBox_polar_2, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_x_2 = QLabel(self.groupBox_14)
        self.label_x_2.setObjectName(u"label_x_2")
        self.label_x_2.setMaximumSize(QSize(70, 16777215))
        self.label_x_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_x_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.ParCurve_x_2 = QLineEdit(self.groupBox_14)
        self.ParCurve_x_2.setObjectName(u"ParCurve_x_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ParCurve_x_2.sizePolicy().hasHeightForWidth())
        self.ParCurve_x_2.setSizePolicy(sizePolicy4)
        self.ParCurve_x_2.setMinimumSize(QSize(0, 0))
        self.ParCurve_x_2.setMaximumSize(QSize(16777215, 16777215))
        self.ParCurve_x_2.setMaxLength(32769)

        self.gridLayout_4.addWidget(self.ParCurve_x_2, 1, 0, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_y_2 = QLabel(self.groupBox_14)
        self.label_y_2.setObjectName(u"label_y_2")
        self.label_y_2.setMaximumSize(QSize(70, 16777215))
        self.label_y_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_y_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.gridLayout_21.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.ParCurve_y_2 = QLineEdit(self.groupBox_14)
        self.ParCurve_y_2.setObjectName(u"ParCurve_y_2")
        sizePolicy4.setHeightForWidth(self.ParCurve_y_2.sizePolicy().hasHeightForWidth())
        self.ParCurve_y_2.setSizePolicy(sizePolicy4)
        self.ParCurve_y_2.setMinimumSize(QSize(0, 0))
        self.ParCurve_y_2.setMaximumSize(QSize(16777215, 16777215))
        self.ParCurve_y_2.setMaxLength(32769)

        self.gridLayout_21.addWidget(self.ParCurve_y_2, 1, 0, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_21, 3, 0, 1, 1)


        self.gridLayout_23.addWidget(self.groupBox_14, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Equation_tab_2, "")
        self.Variables_tab_2 = QWidget()
        self.Variables_tab_2.setObjectName(u"Variables_tab_2")
        self.gridLayout_6 = QGridLayout(self.Variables_tab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_15 = QGroupBox(self.Variables_tab_2)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_44 = QGridLayout(self.groupBox_15)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_tmin_3 = QLabel(self.groupBox_15)
        self.label_tmin_3.setObjectName(u"label_tmin_3")
        self.label_tmin_3.setMaximumSize(QSize(70, 16777215))
        self.label_tmin_3.setLayoutDirection(Qt.LeftToRight)
        self.label_tmin_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_tmin_3)

        self.ParCurve_tmin_2 = QLineEdit(self.groupBox_15)
        self.ParCurve_tmin_2.setObjectName(u"ParCurve_tmin_2")
        sizePolicy2.setHeightForWidth(self.ParCurve_tmin_2.sizePolicy().hasHeightForWidth())
        self.ParCurve_tmin_2.setSizePolicy(sizePolicy2)
        self.ParCurve_tmin_2.setMinimumSize(QSize(40, 0))
        self.ParCurve_tmin_2.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_tmin_2.setMaxLength(32769)

        self.horizontalLayout_8.addWidget(self.ParCurve_tmin_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_tmax_3 = QLabel(self.groupBox_15)
        self.label_tmax_3.setObjectName(u"label_tmax_3")
        self.label_tmax_3.setMaximumSize(QSize(70, 16777215))
        self.label_tmax_3.setLayoutDirection(Qt.LeftToRight)
        self.label_tmax_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_tmax_3)

        self.ParCurve_tmax_2 = QLineEdit(self.groupBox_15)
        self.ParCurve_tmax_2.setObjectName(u"ParCurve_tmax_2")
        sizePolicy2.setHeightForWidth(self.ParCurve_tmax_2.sizePolicy().hasHeightForWidth())
        self.ParCurve_tmax_2.setSizePolicy(sizePolicy2)
        self.ParCurve_tmax_2.setMinimumSize(QSize(40, 0))
        self.ParCurve_tmax_2.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_tmax_2.setMaxLength(32769)

        self.horizontalLayout_9.addWidget(self.ParCurve_tmax_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_tstep_3 = QLabel(self.groupBox_15)
        self.label_tstep_3.setObjectName(u"label_tstep_3")
        self.label_tstep_3.setMaximumSize(QSize(70, 16777215))
        self.label_tstep_3.setLayoutDirection(Qt.LeftToRight)
        self.label_tstep_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_tstep_3)

        self.ParCurve_tstep_2 = QLineEdit(self.groupBox_15)
        self.ParCurve_tstep_2.setObjectName(u"ParCurve_tstep_2")
        sizePolicy2.setHeightForWidth(self.ParCurve_tstep_2.sizePolicy().hasHeightForWidth())
        self.ParCurve_tstep_2.setSizePolicy(sizePolicy2)
        self.ParCurve_tstep_2.setMinimumSize(QSize(40, 0))
        self.ParCurve_tstep_2.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_tstep_2.setMaxLength(32769)

        self.horizontalLayout_10.addWidget(self.ParCurve_tstep_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)


        self.gridLayout_44.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_44.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(17, 125, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_44.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_15, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Variables_tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_36.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.Wire_Tab2_3, "")
        self.Wire_Tab3_3 = QWidget()
        self.Wire_Tab3_3.setObjectName(u"Wire_Tab3_3")
        self.gridLayout_27 = QGridLayout(self.Wire_Tab3_3)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.scrollArea_6 = QScrollArea(self.Wire_Tab3_3)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 358, 534))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.ParCurve_comboBox_3 = QComboBox(self.scrollAreaWidgetContents_4)
        self.ParCurve_comboBox_3.setObjectName(u"ParCurve_comboBox_3")

        self.horizontalLayout_63.addWidget(self.ParCurve_comboBox_3)

        self.ParCurve_button_edit_3 = QPushButton(self.scrollAreaWidgetContents_4)
        self.ParCurve_button_edit_3.setObjectName(u"ParCurve_button_edit_3")
        self.ParCurve_button_edit_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_button_edit_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_63.addWidget(self.ParCurve_button_edit_3)


        self.gridLayout_15.addLayout(self.horizontalLayout_63, 0, 0, 1, 1)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_name_3 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_name_3.setObjectName(u"label_name_3")
        self.label_name_3.setFrameShape(QFrame.Box)
        self.label_name_3.setFrameShadow(QFrame.Raised)
        self.label_name_3.setLineWidth(3)
        self.label_name_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label_name_3)

        self.ParCurve_name_3 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.ParCurve_name_3.setObjectName(u"ParCurve_name_3")

        self.horizontalLayout_64.addWidget(self.ParCurve_name_3)


        self.gridLayout_15.addLayout(self.horizontalLayout_64, 1, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_3 = QGridLayout(self.groupBox_19)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_points_3 = QCheckBox(self.groupBox_19)
        self.checkBox_points_3.setObjectName(u"checkBox_points_3")
        self.checkBox_points_3.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.checkBox_points_3, 0, 1, 1, 1)

        self.checkBox_polyline_3 = QCheckBox(self.groupBox_19)
        self.checkBox_polyline_3.setObjectName(u"checkBox_polyline_3")
        self.checkBox_polyline_3.setChecked(True)
        self.checkBox_polyline_3.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.checkBox_polyline_3, 0, 2, 1, 1)

        self.checkBox_bspline_3 = QCheckBox(self.groupBox_19)
        self.checkBox_bspline_3.setObjectName(u"checkBox_bspline_3")
        self.checkBox_bspline_3.setChecked(False)
        self.checkBox_bspline_3.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.checkBox_bspline_3, 1, 2, 1, 1)

        self.checkBox_bezier_3 = QCheckBox(self.groupBox_19)
        self.checkBox_bezier_3.setObjectName(u"checkBox_bezier_3")
        self.checkBox_bezier_3.setEnabled(True)
        self.checkBox_bezier_3.setChecked(False)
        self.checkBox_bezier_3.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.checkBox_bezier_3, 1, 1, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_19, 3, 0, 1, 1)

        self.checkBox_close_3 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.checkBox_close_3.setObjectName(u"checkBox_close_3")

        self.gridLayout_15.addWidget(self.checkBox_close_3, 4, 0, 1, 1)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.ParCurve_button_store_3 = QPushButton(self.scrollAreaWidgetContents_4)
        self.ParCurve_button_store_3.setObjectName(u"ParCurve_button_store_3")
        self.ParCurve_button_store_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_button_store_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_65.addWidget(self.ParCurve_button_store_3)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_9)

        self.ParCurve_button_apply_3 = QPushButton(self.scrollAreaWidgetContents_4)
        self.ParCurve_button_apply_3.setObjectName(u"ParCurve_button_apply_3")
        self.ParCurve_button_apply_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_button_apply_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_65.addWidget(self.ParCurve_button_apply_3)


        self.gridLayout_15.addLayout(self.horizontalLayout_65, 5, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.Equation_tab_3 = QWidget()
        self.Equation_tab_3.setObjectName(u"Equation_tab_3")
        self.gridLayout_18 = QGridLayout(self.Equation_tab_3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.scrollArea_4 = QScrollArea(self.Equation_tab_3)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 301, 378))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_a_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_a_4.setObjectName(u"label_a_4")
        self.label_a_4.setMaximumSize(QSize(70, 16777215))
        self.label_a_4.setLayoutDirection(Qt.LeftToRight)
        self.label_a_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_a_4)

        self.ParCurve_a_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.ParCurve_a_3.setObjectName(u"ParCurve_a_3")
        sizePolicy2.setHeightForWidth(self.ParCurve_a_3.sizePolicy().hasHeightForWidth())
        self.ParCurve_a_3.setSizePolicy(sizePolicy2)
        self.ParCurve_a_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_a_3.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_a_3.setMaxLength(32769)

        self.horizontalLayout_11.addWidget(self.ParCurve_a_3)


        self.gridLayout_9.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_b_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_b_4.setObjectName(u"label_b_4")
        self.label_b_4.setMaximumSize(QSize(70, 16777215))
        self.label_b_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_b_4)

        self.ParCurve_b_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.ParCurve_b_3.setObjectName(u"ParCurve_b_3")
        sizePolicy2.setHeightForWidth(self.ParCurve_b_3.sizePolicy().hasHeightForWidth())
        self.ParCurve_b_3.setSizePolicy(sizePolicy2)
        self.ParCurve_b_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_b_3.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_b_3.setMaxLength(32769)

        self.horizontalLayout_12.addWidget(self.ParCurve_b_3)


        self.gridLayout_9.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_c_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_c_2.setObjectName(u"label_c_2")
        self.label_c_2.setMaximumSize(QSize(70, 16777215))
        self.label_c_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_c_2)

        self.ParCurve_c_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.ParCurve_c_3.setObjectName(u"ParCurve_c_3")
        sizePolicy2.setHeightForWidth(self.ParCurve_c_3.sizePolicy().hasHeightForWidth())
        self.ParCurve_c_3.setSizePolicy(sizePolicy2)
        self.ParCurve_c_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_c_3.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_c_3.setMaxLength(32769)

        self.horizontalLayout_13.addWidget(self.ParCurve_c_3)


        self.gridLayout_9.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_9)


        self.gridLayout_14.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.checkBox_cylind_3 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_cylind_3.setObjectName(u"checkBox_cylind_3")
        self.checkBox_cylind_3.setAutoExclusive(False)

        self.gridLayout_13.addWidget(self.checkBox_cylind_3, 0, 0, 1, 1)

        self.checkBox_spheric_3 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_spheric_3.setObjectName(u"checkBox_spheric_3")
        self.checkBox_spheric_3.setAutoExclusive(False)

        self.gridLayout_13.addWidget(self.checkBox_spheric_3, 0, 1, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_13, 1, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_x_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_x_3.setObjectName(u"label_x_3")
        self.label_x_3.setMaximumSize(QSize(100, 16777215))
        self.label_x_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_x_3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_11)


        self.gridLayout_12.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.ParCurve_x_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.ParCurve_x_3.setObjectName(u"ParCurve_x_3")
        sizePolicy4.setHeightForWidth(self.ParCurve_x_3.sizePolicy().hasHeightForWidth())
        self.ParCurve_x_3.setSizePolicy(sizePolicy4)
        self.ParCurve_x_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_x_3.setMaximumSize(QSize(16777215, 16777215))
        self.ParCurve_x_3.setMaxLength(32769)

        self.gridLayout_12.addWidget(self.ParCurve_x_3, 1, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_12, 2, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_y_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_y_3.setObjectName(u"label_y_3")
        self.label_y_3.setMaximumSize(QSize(100, 16777215))
        self.label_y_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_y_3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_10)


        self.gridLayout_11.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)

        self.ParCurve_y_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.ParCurve_y_3.setObjectName(u"ParCurve_y_3")
        sizePolicy4.setHeightForWidth(self.ParCurve_y_3.sizePolicy().hasHeightForWidth())
        self.ParCurve_y_3.setSizePolicy(sizePolicy4)
        self.ParCurve_y_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_y_3.setMaximumSize(QSize(16777215, 16777215))
        self.ParCurve_y_3.setMaxLength(32769)

        self.gridLayout_11.addWidget(self.ParCurve_y_3, 1, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_11, 3, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_z_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_z_3.setObjectName(u"label_z_3")
        self.label_z_3.setMaximumSize(QSize(100, 16777215))
        self.label_z_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_z_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)


        self.gridLayout_10.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)

        self.ParCurve_z_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.ParCurve_z_3.setObjectName(u"ParCurve_z_3")
        sizePolicy4.setHeightForWidth(self.ParCurve_z_3.sizePolicy().hasHeightForWidth())
        self.ParCurve_z_3.setSizePolicy(sizePolicy4)
        self.ParCurve_z_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_z_3.setMaximumSize(QSize(16777215, 16777215))
        self.ParCurve_z_3.setMaxLength(32769)

        self.gridLayout_10.addWidget(self.ParCurve_z_3, 1, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_10, 4, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_18.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.Equation_tab_3, "")
        self.Variables_tab_3 = QWidget()
        self.Variables_tab_3.setObjectName(u"Variables_tab_3")
        self.gridLayout_16 = QGridLayout(self.Variables_tab_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_tmin_4 = QLabel(self.Variables_tab_3)
        self.label_tmin_4.setObjectName(u"label_tmin_4")
        self.label_tmin_4.setMaximumSize(QSize(70, 16777215))
        self.label_tmin_4.setLayoutDirection(Qt.LeftToRight)
        self.label_tmin_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_tmin_4, 0, 0, 1, 1)

        self.ParCurve_tmin_3 = QLineEdit(self.Variables_tab_3)
        self.ParCurve_tmin_3.setObjectName(u"ParCurve_tmin_3")
        sizePolicy2.setHeightForWidth(self.ParCurve_tmin_3.sizePolicy().hasHeightForWidth())
        self.ParCurve_tmin_3.setSizePolicy(sizePolicy2)
        self.ParCurve_tmin_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_tmin_3.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_tmin_3.setMaxLength(32769)

        self.gridLayout_17.addWidget(self.ParCurve_tmin_3, 0, 1, 1, 1)

        self.label_tmax_4 = QLabel(self.Variables_tab_3)
        self.label_tmax_4.setObjectName(u"label_tmax_4")
        self.label_tmax_4.setMaximumSize(QSize(70, 16777215))
        self.label_tmax_4.setLayoutDirection(Qt.LeftToRight)
        self.label_tmax_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_tmax_4, 1, 0, 1, 1)

        self.ParCurve_tmax_3 = QLineEdit(self.Variables_tab_3)
        self.ParCurve_tmax_3.setObjectName(u"ParCurve_tmax_3")
        sizePolicy2.setHeightForWidth(self.ParCurve_tmax_3.sizePolicy().hasHeightForWidth())
        self.ParCurve_tmax_3.setSizePolicy(sizePolicy2)
        self.ParCurve_tmax_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_tmax_3.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_tmax_3.setMaxLength(32769)

        self.gridLayout_17.addWidget(self.ParCurve_tmax_3, 1, 1, 1, 1)

        self.label_tstep_4 = QLabel(self.Variables_tab_3)
        self.label_tstep_4.setObjectName(u"label_tstep_4")
        self.label_tstep_4.setMaximumSize(QSize(70, 16777215))
        self.label_tstep_4.setLayoutDirection(Qt.LeftToRight)
        self.label_tstep_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_tstep_4, 2, 0, 1, 1)

        self.ParCurve_tstep_3 = QLineEdit(self.Variables_tab_3)
        self.ParCurve_tstep_3.setObjectName(u"ParCurve_tstep_3")
        sizePolicy2.setHeightForWidth(self.ParCurve_tstep_3.sizePolicy().hasHeightForWidth())
        self.ParCurve_tstep_3.setSizePolicy(sizePolicy2)
        self.ParCurve_tstep_3.setMinimumSize(QSize(40, 0))
        self.ParCurve_tstep_3.setMaximumSize(QSize(150, 16777215))
        self.ParCurve_tstep_3.setMaxLength(32769)

        self.gridLayout_17.addWidget(self.ParCurve_tstep_3, 2, 1, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_17, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(29, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_12, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 162, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.Variables_tab_3, "")

        self.gridLayout_15.addWidget(self.tabWidget_2, 2, 0, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_27.addWidget(self.scrollArea_6, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.Wire_Tab3_3, "")
        self.Surface_Tab1 = QWidget()
        self.Surface_Tab1.setObjectName(u"Surface_Tab1")
        self.gridLayout_40 = QGridLayout(self.Surface_Tab1)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.scrollArea_7 = QScrollArea(self.Surface_Tab1)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 358, 534))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.Surf_comboBox = QComboBox(self.scrollAreaWidgetContents_7)
        self.Surf_comboBox.setObjectName(u"Surf_comboBox")

        self.horizontalLayout_68.addWidget(self.Surf_comboBox)

        self.Surf_button_edit = QPushButton(self.scrollAreaWidgetContents_7)
        self.Surf_button_edit.setObjectName(u"Surf_button_edit")
        self.Surf_button_edit.setMinimumSize(QSize(40, 0))
        self.Surf_button_edit.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_68.addWidget(self.Surf_button_edit)


        self.gridLayout_7.addLayout(self.horizontalLayout_68, 0, 0, 1, 1)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_name_4 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_name_4.setObjectName(u"label_name_4")
        self.label_name_4.setFrameShape(QFrame.Box)
        self.label_name_4.setFrameShadow(QFrame.Raised)
        self.label_name_4.setLineWidth(3)
        self.label_name_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.label_name_4)

        self.Surf_name = QLineEdit(self.scrollAreaWidgetContents_7)
        self.Surf_name.setObjectName(u"Surf_name")

        self.horizontalLayout_67.addWidget(self.Surf_name)


        self.gridLayout_7.addLayout(self.horizontalLayout_67, 1, 0, 1, 1)

        self.tabWidget_5 = QTabWidget(self.scrollAreaWidgetContents_7)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_26 = QGridLayout(self.tab_8)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.scrollArea = QScrollArea(self.tab_8)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 301, 340))
        self.gridLayout_24 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_a_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_a_5.setObjectName(u"label_a_5")
        self.label_a_5.setMaximumSize(QSize(70, 16777215))
        self.label_a_5.setLayoutDirection(Qt.LeftToRight)
        self.label_a_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_a_5)

        self.Surf_a = QLineEdit(self.scrollAreaWidgetContents)
        self.Surf_a.setObjectName(u"Surf_a")
        sizePolicy2.setHeightForWidth(self.Surf_a.sizePolicy().hasHeightForWidth())
        self.Surf_a.setSizePolicy(sizePolicy2)
        self.Surf_a.setMinimumSize(QSize(40, 0))
        self.Surf_a.setMaximumSize(QSize(150, 16777215))
        self.Surf_a.setMaxLength(32769)

        self.horizontalLayout_20.addWidget(self.Surf_a)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_b_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_b_5.setObjectName(u"label_b_5")
        self.label_b_5.setMaximumSize(QSize(70, 16777215))
        self.label_b_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_b_5)

        self.Surf_b = QLineEdit(self.scrollAreaWidgetContents)
        self.Surf_b.setObjectName(u"Surf_b")
        sizePolicy2.setHeightForWidth(self.Surf_b.sizePolicy().hasHeightForWidth())
        self.Surf_b.setSizePolicy(sizePolicy2)
        self.Surf_b.setMinimumSize(QSize(40, 0))
        self.Surf_b.setMaximumSize(QSize(150, 16777215))
        self.Surf_b.setMaxLength(32769)

        self.horizontalLayout_21.addWidget(self.Surf_b)


        self.verticalLayout.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_c_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_c_3.setObjectName(u"label_c_3")
        self.label_c_3.setMaximumSize(QSize(70, 16777215))
        self.label_c_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_c_3)

        self.Surf_c = QLineEdit(self.scrollAreaWidgetContents)
        self.Surf_c.setObjectName(u"Surf_c")
        sizePolicy2.setHeightForWidth(self.Surf_c.sizePolicy().hasHeightForWidth())
        self.Surf_c.setSizePolicy(sizePolicy2)
        self.Surf_c.setMinimumSize(QSize(40, 0))
        self.Surf_c.setMaximumSize(QSize(150, 16777215))
        self.Surf_c.setMaxLength(32769)

        self.horizontalLayout_22.addWidget(self.Surf_c)


        self.verticalLayout.addLayout(self.horizontalLayout_22)


        self.gridLayout_24.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_x_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_x_4.setObjectName(u"label_x_4")
        self.label_x_4.setMaximumSize(QSize(80, 16777215))
        self.label_x_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_x_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_5)


        self.gridLayout_29.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)

        self.Surf_x = QLineEdit(self.scrollAreaWidgetContents)
        self.Surf_x.setObjectName(u"Surf_x")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Surf_x.sizePolicy().hasHeightForWidth())
        self.Surf_x.setSizePolicy(sizePolicy5)
        self.Surf_x.setMinimumSize(QSize(0, 0))
        self.Surf_x.setMaximumSize(QSize(16777215, 16777215))
        self.Surf_x.setMaxLength(32769)

        self.gridLayout_29.addWidget(self.Surf_x, 1, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_y_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_y_4.setObjectName(u"label_y_4")
        self.label_y_4.setMaximumSize(QSize(80, 16777215))
        self.label_y_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_y_4)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_13)


        self.gridLayout_29.addLayout(self.horizontalLayout_24, 2, 0, 1, 1)

        self.Surf_y = QLineEdit(self.scrollAreaWidgetContents)
        self.Surf_y.setObjectName(u"Surf_y")
        sizePolicy5.setHeightForWidth(self.Surf_y.sizePolicy().hasHeightForWidth())
        self.Surf_y.setSizePolicy(sizePolicy5)
        self.Surf_y.setMinimumSize(QSize(0, 0))
        self.Surf_y.setMaximumSize(QSize(16777215, 16777215))
        self.Surf_y.setMaxLength(32769)

        self.gridLayout_29.addWidget(self.Surf_y, 3, 0, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_z_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_z_2.setObjectName(u"label_z_2")
        self.label_z_2.setMaximumSize(QSize(80, 16777215))
        self.label_z_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_z_2)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_14)


        self.gridLayout_29.addLayout(self.horizontalLayout_25, 4, 0, 1, 1)

        self.Surf_z = QLineEdit(self.scrollAreaWidgetContents)
        self.Surf_z.setObjectName(u"Surf_z")
        sizePolicy5.setHeightForWidth(self.Surf_z.sizePolicy().hasHeightForWidth())
        self.Surf_z.setSizePolicy(sizePolicy5)
        self.Surf_z.setMinimumSize(QSize(0, 0))
        self.Surf_z.setMaximumSize(QSize(16777215, 16777215))
        self.Surf_z.setMaxLength(32769)

        self.gridLayout_29.addWidget(self.Surf_z, 5, 0, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_29, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_26.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_28 = QGridLayout(self.tab_9)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_umin = QLabel(self.tab_9)
        self.label_umin.setObjectName(u"label_umin")
        self.label_umin.setMaximumSize(QSize(70, 16777215))
        self.label_umin.setLayoutDirection(Qt.LeftToRight)
        self.label_umin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.label_umin, 0, 0, 1, 1)

        self.Surf_umin = QLineEdit(self.tab_9)
        self.Surf_umin.setObjectName(u"Surf_umin")
        sizePolicy2.setHeightForWidth(self.Surf_umin.sizePolicy().hasHeightForWidth())
        self.Surf_umin.setSizePolicy(sizePolicy2)
        self.Surf_umin.setMinimumSize(QSize(40, 0))
        self.Surf_umin.setMaximumSize(QSize(150, 16777215))
        self.Surf_umin.setMaxLength(32769)

        self.gridLayout_28.addWidget(self.Surf_umin, 0, 1, 1, 1)

        self.label_umax = QLabel(self.tab_9)
        self.label_umax.setObjectName(u"label_umax")
        self.label_umax.setMaximumSize(QSize(70, 16777215))
        self.label_umax.setLayoutDirection(Qt.LeftToRight)
        self.label_umax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.label_umax, 1, 0, 1, 1)

        self.Surf_umax = QLineEdit(self.tab_9)
        self.Surf_umax.setObjectName(u"Surf_umax")
        sizePolicy2.setHeightForWidth(self.Surf_umax.sizePolicy().hasHeightForWidth())
        self.Surf_umax.setSizePolicy(sizePolicy2)
        self.Surf_umax.setMinimumSize(QSize(40, 0))
        self.Surf_umax.setMaximumSize(QSize(150, 16777215))
        self.Surf_umax.setMaxLength(32769)

        self.gridLayout_28.addWidget(self.Surf_umax, 1, 1, 1, 1)

        self.label_ustep = QLabel(self.tab_9)
        self.label_ustep.setObjectName(u"label_ustep")
        self.label_ustep.setMaximumSize(QSize(70, 16777215))
        self.label_ustep.setLayoutDirection(Qt.LeftToRight)
        self.label_ustep.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.label_ustep, 2, 0, 1, 1)

        self.Surf_ustep = QLineEdit(self.tab_9)
        self.Surf_ustep.setObjectName(u"Surf_ustep")
        sizePolicy2.setHeightForWidth(self.Surf_ustep.sizePolicy().hasHeightForWidth())
        self.Surf_ustep.setSizePolicy(sizePolicy2)
        self.Surf_ustep.setMinimumSize(QSize(40, 0))
        self.Surf_ustep.setMaximumSize(QSize(150, 16777215))
        self.Surf_ustep.setMaxLength(32769)

        self.gridLayout_28.addWidget(self.Surf_ustep, 2, 1, 1, 1)

        self.label_umin_2 = QLabel(self.tab_9)
        self.label_umin_2.setObjectName(u"label_umin_2")
        self.label_umin_2.setMaximumSize(QSize(70, 16777215))
        self.label_umin_2.setLayoutDirection(Qt.LeftToRight)
        self.label_umin_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.label_umin_2, 3, 0, 1, 1)

        self.Surf_vmin = QLineEdit(self.tab_9)
        self.Surf_vmin.setObjectName(u"Surf_vmin")
        sizePolicy2.setHeightForWidth(self.Surf_vmin.sizePolicy().hasHeightForWidth())
        self.Surf_vmin.setSizePolicy(sizePolicy2)
        self.Surf_vmin.setMinimumSize(QSize(40, 0))
        self.Surf_vmin.setMaximumSize(QSize(150, 16777215))
        self.Surf_vmin.setMaxLength(32769)

        self.gridLayout_28.addWidget(self.Surf_vmin, 3, 1, 1, 1)

        self.label_umax_2 = QLabel(self.tab_9)
        self.label_umax_2.setObjectName(u"label_umax_2")
        self.label_umax_2.setMaximumSize(QSize(70, 16777215))
        self.label_umax_2.setLayoutDirection(Qt.LeftToRight)
        self.label_umax_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.label_umax_2, 4, 0, 1, 1)

        self.Surf_vmax = QLineEdit(self.tab_9)
        self.Surf_vmax.setObjectName(u"Surf_vmax")
        sizePolicy2.setHeightForWidth(self.Surf_vmax.sizePolicy().hasHeightForWidth())
        self.Surf_vmax.setSizePolicy(sizePolicy2)
        self.Surf_vmax.setMinimumSize(QSize(40, 0))
        self.Surf_vmax.setMaximumSize(QSize(150, 16777215))
        self.Surf_vmax.setMaxLength(32769)

        self.gridLayout_28.addWidget(self.Surf_vmax, 4, 1, 1, 1)

        self.label_ustep_2 = QLabel(self.tab_9)
        self.label_ustep_2.setObjectName(u"label_ustep_2")
        self.label_ustep_2.setMaximumSize(QSize(70, 16777215))
        self.label_ustep_2.setLayoutDirection(Qt.LeftToRight)
        self.label_ustep_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_28.addWidget(self.label_ustep_2, 5, 0, 1, 1)

        self.Surf_vstep = QLineEdit(self.tab_9)
        self.Surf_vstep.setObjectName(u"Surf_vstep")
        sizePolicy2.setHeightForWidth(self.Surf_vstep.sizePolicy().hasHeightForWidth())
        self.Surf_vstep.setSizePolicy(sizePolicy2)
        self.Surf_vstep.setMinimumSize(QSize(40, 0))
        self.Surf_vstep.setMaximumSize(QSize(150, 16777215))
        self.Surf_vstep.setMaxLength(32769)

        self.gridLayout_28.addWidget(self.Surf_vstep, 5, 1, 1, 1)

        self.tabWidget_5.addTab(self.tab_9, "")

        self.gridLayout_7.addWidget(self.tabWidget_5, 2, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_43 = QGridLayout(self.groupBox_9)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.Surf_points = QCheckBox(self.groupBox_9)
        self.Surf_points.setObjectName(u"Surf_points")
        self.Surf_points.setChecked(False)
        self.Surf_points.setAutoExclusive(True)

        self.gridLayout_31.addWidget(self.Surf_points, 0, 0, 1, 1)

        self.Surf_polyline = QCheckBox(self.groupBox_9)
        self.Surf_polyline.setObjectName(u"Surf_polyline")
        self.Surf_polyline.setChecked(False)
        self.Surf_polyline.setAutoExclusive(True)

        self.gridLayout_31.addWidget(self.Surf_polyline, 0, 1, 1, 1)

        self.Surf_bspline = QCheckBox(self.groupBox_9)
        self.Surf_bspline.setObjectName(u"Surf_bspline")
        self.Surf_bspline.setChecked(False)
        self.Surf_bspline.setAutoExclusive(True)

        self.gridLayout_31.addWidget(self.Surf_bspline, 0, 2, 1, 1)

        self.Surf_bspline_surf = QCheckBox(self.groupBox_9)
        self.Surf_bspline_surf.setObjectName(u"Surf_bspline_surf")
        self.Surf_bspline_surf.setChecked(True)
        self.Surf_bspline_surf.setAutoExclusive(True)

        self.gridLayout_31.addWidget(self.Surf_bspline_surf, 1, 0, 1, 2)

        self.Surf_meshes = QCheckBox(self.groupBox_9)
        self.Surf_meshes.setObjectName(u"Surf_meshes")
        self.Surf_meshes.setEnabled(False)
        self.Surf_meshes.setChecked(False)
        self.Surf_meshes.setAutoExclusive(True)

        self.gridLayout_31.addWidget(self.Surf_meshes, 1, 2, 1, 1)


        self.gridLayout_43.addLayout(self.gridLayout_31, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_9, 3, 0, 1, 1)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.Surf_button_store = QPushButton(self.scrollAreaWidgetContents_7)
        self.Surf_button_store.setObjectName(u"Surf_button_store")
        self.Surf_button_store.setMinimumSize(QSize(40, 0))
        self.Surf_button_store.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_66.addWidget(self.Surf_button_store)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_15)

        self.Surf_button_apply = QPushButton(self.scrollAreaWidgetContents_7)
        self.Surf_button_apply.setObjectName(u"Surf_button_apply")
        self.Surf_button_apply.setMinimumSize(QSize(40, 0))
        self.Surf_button_apply.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_66.addWidget(self.Surf_button_apply)


        self.gridLayout_7.addLayout(self.horizontalLayout_66, 4, 0, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_40.addWidget(self.scrollArea_7, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.Surface_Tab1, "")

        self.gridLayout_38.addWidget(self.tabWidget_8, 0, 0, 1, 1)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.gridLayout_8.addWidget(self.scrollArea_8, 0, 0, 1, 1)

        self.tabWidget_6.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_45 = QGridLayout(self.tab_2)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_select_point = QPushButton(self.tab_2)
        self.button_select_point.setObjectName(u"button_select_point")

        self.verticalLayout_2.addWidget(self.button_select_point)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_x_6 = QLabel(self.tab_2)
        self.label_x_6.setObjectName(u"label_x_6")
        self.label_x_6.setMaximumSize(QSize(70, 16777215))
        self.label_x_6.setLayoutDirection(Qt.LeftToRight)
        self.label_x_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_x_6)

        self.Par_x_ref = QLineEdit(self.tab_2)
        self.Par_x_ref.setObjectName(u"Par_x_ref")
        sizePolicy2.setHeightForWidth(self.Par_x_ref.sizePolicy().hasHeightForWidth())
        self.Par_x_ref.setSizePolicy(sizePolicy2)
        self.Par_x_ref.setMinimumSize(QSize(40, 0))
        self.Par_x_ref.setMaximumSize(QSize(150, 16777215))
        self.Par_x_ref.setMaxLength(32769)

        self.horizontalLayout_35.addWidget(self.Par_x_ref)


        self.verticalLayout_3.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_y_6 = QLabel(self.tab_2)
        self.label_y_6.setObjectName(u"label_y_6")
        self.label_y_6.setMaximumSize(QSize(70, 16777215))
        self.label_y_6.setLayoutDirection(Qt.LeftToRight)
        self.label_y_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_y_6)

        self.Par_y_ref = QLineEdit(self.tab_2)
        self.Par_y_ref.setObjectName(u"Par_y_ref")
        sizePolicy2.setHeightForWidth(self.Par_y_ref.sizePolicy().hasHeightForWidth())
        self.Par_y_ref.setSizePolicy(sizePolicy2)
        self.Par_y_ref.setMinimumSize(QSize(40, 0))
        self.Par_y_ref.setMaximumSize(QSize(150, 16777215))
        self.Par_y_ref.setMaxLength(32769)

        self.horizontalLayout_36.addWidget(self.Par_y_ref)


        self.verticalLayout_3.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_z_6 = QLabel(self.tab_2)
        self.label_z_6.setObjectName(u"label_z_6")
        self.label_z_6.setMaximumSize(QSize(70, 16777215))
        self.label_z_6.setLayoutDirection(Qt.LeftToRight)
        self.label_z_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_z_6)

        self.Par_z_ref = QLineEdit(self.tab_2)
        self.Par_z_ref.setObjectName(u"Par_z_ref")
        sizePolicy2.setHeightForWidth(self.Par_z_ref.sizePolicy().hasHeightForWidth())
        self.Par_z_ref.setSizePolicy(sizePolicy2)
        self.Par_z_ref.setMinimumSize(QSize(40, 0))
        self.Par_z_ref.setMaximumSize(QSize(150, 16777215))
        self.Par_z_ref.setMaxLength(32769)

        self.horizontalLayout_37.addWidget(self.Par_z_ref)


        self.verticalLayout_3.addLayout(self.horizontalLayout_37)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout_45.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_45.addItem(self.horizontalSpacer_16, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 156, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_45.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout_45.addWidget(self.lineEdit, 0, 0, 1, 2)

        self.tabWidget_6.addTab(self.tab_2, "")
        self.lineEdit.raise_()

        self.gridLayout_41.addWidget(self.tabWidget_6, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_quit.setText(QCoreApplication.translate("Form", u"Close", None))
        self.label_release.setText(QCoreApplication.translate("Form", u"2024", None))
#if QT_CONFIG(tooltip)
        self.Reg2DCurve_button_select_points.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Select point(s) used for 2D regression.</p><p>- Select as much as Points as needed ;</p><p>- Then click on this button.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Reg2DCurve_button_select_points.setText(QCoreApplication.translate("Form", u"Select 2D Points", None))
        self.Reg2DCurve_input_textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Cantarell'; font-size:11pt;\"><br /></p></body></html>", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Input Data", None))
        self.Reg2DCurve_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Least squares Polynomial Regression", None))

        self.label.setText(QCoreApplication.translate("Form", u"Degree", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("Form", u"Type of 2D Curve :", None))
        self.checkBox_points_reg1.setText(QCoreApplication.translate("Form", u"Points", None))
        self.checkBox_polyline_reg1.setText(QCoreApplication.translate("Form", u"Polyline", None))
        self.checkBox_bezier_reg1.setText(QCoreApplication.translate("Form", u"Bezier", None))
        self.checkBox_bspline_reg1.setText(QCoreApplication.translate("Form", u"Bspline", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), QCoreApplication.translate("Form", u"Estimation by", None))
#if QT_CONFIG(tooltip)
        self.label_regmin_1.setToolTip(QCoreApplication.translate("Form", u"Minimum value of the Abscissa to plot", None))
#endif // QT_CONFIG(tooltip)
        self.label_regmin_1.setText(QCoreApplication.translate("Form", u"absc.  min", None))
        self.Reg2DCurve_min.setText("")
#if QT_CONFIG(tooltip)
        self.label_regmax_1.setToolTip(QCoreApplication.translate("Form", u"Maximum value of the Abscissa to plot", None))
#endif // QT_CONFIG(tooltip)
        self.label_regmax_1.setText(QCoreApplication.translate("Form", u"absc. max", None))
        self.Reg2DCurve_max.setText("")
        self.label_regstep_1.setText(QCoreApplication.translate("Form", u"step", None))
        self.Reg2DCurve_step.setText("")
        self.label_Reg2DCurve_z.setText(QCoreApplication.translate("Form", u"Z cst.", None))
#if QT_CONFIG(tooltip)
        self.Reg2DCurve_z.setToolTip(QCoreApplication.translate("Form", u"The constant coordinate value of the 2D curve", None))
#endif // QT_CONFIG(tooltip)
        self.Reg2DCurve_z.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), QCoreApplication.translate("Form", u"Function", None))
#if QT_CONFIG(tooltip)
        self.Reg2DCurve_button_apply.setToolTip(QCoreApplication.translate("Form", u"Click to visualize the curve.", None))
#endif // QT_CONFIG(tooltip)
        self.Reg2DCurve_button_apply.setText(QCoreApplication.translate("Form", u"Draw", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.Wire_Tab1_3), QCoreApplication.translate("Form", u"Regression 2D", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_comboBox_2.setToolTip(QCoreApplication.translate("Form", u"Choose another curve from the list.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ParCurve_button_edit_2.setToolTip(QCoreApplication.translate("Form", u"Click to access to a table where you can edit all parameters of all curves and \n"
"save your custom curves.", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_button_edit_2.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.label_name_2.setText(QCoreApplication.translate("Form", u"Name", None))
        self.ParCurve_name_2.setText(QCoreApplication.translate("Form", u"Circle", None))
        self.label_dim_2.setText(QCoreApplication.translate("Form", u"Select 2 axis", None))
        self.ParCurve_combo_dim_2D.setItemText(0, QCoreApplication.translate("Form", u"XY", None))
        self.ParCurve_combo_dim_2D.setItemText(1, QCoreApplication.translate("Form", u"YX", None))
        self.ParCurve_combo_dim_2D.setItemText(2, QCoreApplication.translate("Form", u"XZ", None))
        self.ParCurve_combo_dim_2D.setItemText(3, QCoreApplication.translate("Form", u"ZX", None))
        self.ParCurve_combo_dim_2D.setItemText(4, QCoreApplication.translate("Form", u"YZ", None))
        self.ParCurve_combo_dim_2D.setItemText(5, QCoreApplication.translate("Form", u"ZY", None))

        self.groupBox_16.setTitle(QCoreApplication.translate("Form", u"Type of 2D Curve :", None))
        self.checkBox_points_2.setText(QCoreApplication.translate("Form", u"Points", None))
        self.checkBox_polyline_2.setText(QCoreApplication.translate("Form", u"Polyline", None))
        self.checkBox_bezier_2.setText(QCoreApplication.translate("Form", u"Bezier", None))
        self.checkBox_bspline_2.setText(QCoreApplication.translate("Form", u"Bspline", None))
        self.checkBox_close_2.setText(QCoreApplication.translate("Form", u"Closed curve", None))
        self.checkBox_face_2.setText(QCoreApplication.translate("Form", u"Create Face", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_button_store_2.setToolTip(QCoreApplication.translate("Form", u"Click to store the current edited curve into the table.\n"
"To save your curve you need to go to \"Edit\".", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_button_store_2.setText(QCoreApplication.translate("Form", u"Store", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_button_apply_2.setToolTip(QCoreApplication.translate("Form", u"Click to visualize the curve.", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_button_apply_2.setText(QCoreApplication.translate("Form", u"Draw", None))
#if QT_CONFIG(tooltip)
        self.groupBox_14.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_14.setTitle("")
        self.label_a_3.setText(QCoreApplication.translate("Form", u"a (t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_a_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The function 'range' from Python and 'np.arange' from numpy module can be used here:</p><p>range([start,] stop[, step])</p><p>  start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>  stop : Generate numbers up to, but not including this number.</p><p>  step : Difference between each number in  the sequence. <span style=\" vertical-align:top;\">The default value is 1.</span></p><p><br/></p><p>np.arange([start,] stop[, step,]dtype=None)</p><p>Return evenly spaced values within a given interval.</p><p>  start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>  stop : <span style=\" vertical-align:top;\">End of interval. The interval does not include this value, except in some cases where </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is not an "
                        "integer and floating point round-off affects the length of </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">.</span></p><p>  step : Difference between each number in  the sequence. <span style=\" vertical-align:top;\">For any output </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">, this is the distance between two adjacent values. The default value is 1.</span></p><p><span style=\" vertical-align:top;\">If </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is specified, </span><span style=\" font-style:italic; vertical-align:top;\">start</span><span style=\" vertical-align:top;\"> must also be given.</span></p><p>  dtype : The type of the output array. if dtype <span style=\" vertical-align:top;\">is not given, infer the data type from the other input arguments.</span><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_a_2.setText(QCoreApplication.translate("Form", u"10    # Radius", None))
        self.label_b_3.setText(QCoreApplication.translate("Form", u"b (a, t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_b_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The function 'range' from Python and 'np.arange' from numpy module can be used here:</p><p>range([start,] stop[, step])</p><p>start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>stop : Generate numbers up to, but not including this number.</p><p>step : Difference between each number in the sequence. <span style=\" vertical-align:top;\">The default value is 1.</span></p><p><br/></p><p>np.arange([start,] stop[, step,]dtype=None)</p><p>Return evenly spaced values within a given interval.</p><p>start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>stop : <span style=\" vertical-align:top;\">End of interval. The interval does not include this value, except in some cases where </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is not an integer and"
                        " floating point round-off affects the length of </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">.</span></p><p>step : Difference between each number in the sequence. <span style=\" vertical-align:top;\">For any output </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">, this is the distance between two adjacent values. The default value is 1.</span></p><p><span style=\" vertical-align:top;\">If </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is specified, </span><span style=\" font-style:italic; vertical-align:top;\">start</span><span style=\" vertical-align:top;\"> must also be given.</span></p><p>dtype : The type of the output array. if dtype <span style=\" vertical-align:top;\">is not given, infer the data type from the other input arguments.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_b_2.setText(QCoreApplication.translate("Form", u"a", None))
#if QT_CONFIG(tooltip)
        self.checkBox_polar_2.setToolTip(QCoreApplication.translate("Form", u"Toggle for Polar coordinates:\n"
"then FIRST input field is interpreted as radius\n"
" and SECOND input field is interpreted as angle phi\n"
"\n"
"Polar coordinates (r, phi) as commonly used in physics: \n"
" If P(x, y) is the considered point in 3D space;\n"
"    Radial distance r ( > 0.0 ),  is the Euclidean distance from \n"
"    the origin O (0, 0) to P(x, y).The symbol rho is often used instead of r.\n"
"    The azimuthal angle phi (or azimuth) is the signed angle measured from the \n"
"    azimuth reference direction to the segment OP on the reference plane XY ( 0 <= phi <= pi radians (0 deg and 180 deg)).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_polar_2.setText(QCoreApplication.translate("Form", u" Polar coord.", None))
        self.label_x_2.setText(QCoreApplication.translate("Form", u"X (a,b,t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_x_2.setToolTip(QCoreApplication.translate("Form", u"The function from Python math module can be used here:\n"
"safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh',\n"
" 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp',\n"
" 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan',\n"
" 'tanh']", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_x_2.setText(QCoreApplication.translate("Form", u"a*cos(t)", None))
        self.label_y_2.setText(QCoreApplication.translate("Form", u"Y (a,b,t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_y_2.setToolTip(QCoreApplication.translate("Form", u"The function from Python math module can be used here:\n"
"safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh',\n"
" 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp',\n"
" 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan',\n"
" 'tanh']", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_y_2.setText(QCoreApplication.translate("Form", u"b*sin(t)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Equation_tab_2), QCoreApplication.translate("Form", u"Equation", None))
        self.groupBox_15.setTitle("")
        self.label_tmin_3.setText(QCoreApplication.translate("Form", u"t min", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_tmin_2.setToolTip(QCoreApplication.translate("Form", u"Minimum value of the t parameter", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_tmin_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_tmax_3.setText(QCoreApplication.translate("Form", u"t max", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_tmax_2.setToolTip(QCoreApplication.translate("Form", u"Maximum value of the t parameter", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_tmax_2.setText(QCoreApplication.translate("Form", u"2*pi", None))
        self.label_tstep_3.setText(QCoreApplication.translate("Form", u"step", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_tstep_2.setToolTip(QCoreApplication.translate("Form", u"Step between two consecutive values of the t parameter", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_tstep_2.setText(QCoreApplication.translate("Form", u"0.01", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Variables_tab_2), QCoreApplication.translate("Form", u"Variables", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.Wire_Tab2_3), QCoreApplication.translate("Form", u"Parametric 2D", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_comboBox_3.setToolTip(QCoreApplication.translate("Form", u"Choose another curve from the list.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ParCurve_button_edit_3.setToolTip(QCoreApplication.translate("Form", u"Click to access to a table where you can edit all parameters of all curves and \n"
"save your custom curves.", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_button_edit_3.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.label_name_3.setText(QCoreApplication.translate("Form", u"Name", None))
        self.ParCurve_name_3.setText(QCoreApplication.translate("Form", u"Cylindrical helix", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("Form", u"Type of 3D Curve :", None))
        self.checkBox_points_3.setText(QCoreApplication.translate("Form", u"Points", None))
        self.checkBox_polyline_3.setText(QCoreApplication.translate("Form", u"Polyline", None))
        self.checkBox_bspline_3.setText(QCoreApplication.translate("Form", u"Bspline", None))
        self.checkBox_bezier_3.setText(QCoreApplication.translate("Form", u"Bezier", None))
        self.checkBox_close_3.setText(QCoreApplication.translate("Form", u"Closed curve", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_button_store_3.setToolTip(QCoreApplication.translate("Form", u"Click to store the current edited curve into the table.\n"
"To save your curve you need to go to \"Edit\".", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_button_store_3.setText(QCoreApplication.translate("Form", u"Store", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_button_apply_3.setToolTip(QCoreApplication.translate("Form", u"Click to visualize the curve.", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_button_apply_3.setText(QCoreApplication.translate("Form", u"Draw", None))
        self.label_a_4.setText(QCoreApplication.translate("Form", u"a (t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_a_3.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The function 'range' from Python and 'np.arange' from numpy module can be used here:</p><p>range([start,] stop[, step])</p><p>start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>stop : Generate numbers up to, but not including this number.</p><p>step : Difference between each number in the sequence. <span style=\" vertical-align:top;\">The default value is 1.</span></p><p><br/></p><p>np.arange([start,] stop[, step,]dtype=None)</p><p>Return evenly spaced values within a given interval.</p><p>start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>stop : <span style=\" vertical-align:top;\">End of interval. The interval does not include this value, except in some cases where </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is not an integer and"
                        " floating point round-off affects the length of </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">.</span></p><p>step : Difference between each number in the sequence. <span style=\" vertical-align:top;\">For any output </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">, this is the distance between two adjacent values. The default value is 1.</span></p><p><span style=\" vertical-align:top;\">If </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is specified, </span><span style=\" font-style:italic; vertical-align:top;\">start</span><span style=\" vertical-align:top;\"> must also be given.</span></p><p>dtype : The type of the output array. if dtype <span style=\" vertical-align:top;\">is not given, infer the data type from the other input arguments.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_a_3.setText(QCoreApplication.translate("Form", u"10*0.05 #Vert. step", None))
        self.label_b_4.setText(QCoreApplication.translate("Form", u"b (a, t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_b_3.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The function 'range' from Python and 'np.arange' from numpy module can be used here:</p><p>range([start,] stop[, step])</p><p>start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>stop : Generate numbers up to, but not including this number.</p><p>step : Difference between each number in the sequence. <span style=\" vertical-align:top;\">The default value is 1.</span></p><p><br/></p><p>np.arange([start,] stop[, step,]dtype=None)</p><p>Return evenly spaced values within a given interval.</p><p>start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>stop : <span style=\" vertical-align:top;\">End of interval. The interval does not include this value, except in some cases where </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is not an integer and"
                        " floating point round-off affects the length of </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">.</span></p><p>step : Difference between each number in the sequence. <span style=\" vertical-align:top;\">For any output </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">, this is the distance between two adjacent values. The default value is 1.</span></p><p><span style=\" vertical-align:top;\">If </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is specified, </span><span style=\" font-style:italic; vertical-align:top;\">start</span><span style=\" vertical-align:top;\"> must also be given.</span></p><p>dtype : The type of the output array. if dtype <span style=\" vertical-align:top;\">is not given, infer the data type from the other input arguments.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_b_3.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_c_2.setText(QCoreApplication.translate("Form", u"c (a, b, t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_c_3.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The function 'range' from Python and 'np.arange' from numpy module can be used here:</p><p>range([start,] stop[, step])</p><p>start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>stop : Generate numbers up to, but not including this number.</p><p>step : Difference between each number in the sequence. <span style=\" vertical-align:top;\">The default value is 1.</span></p><p><br/></p><p>np.arange([start,] stop[, step,]dtype=None)</p><p>Return evenly spaced values within a given interval.</p><p>start : Starting number of the sequence. <span style=\" vertical-align:top;\">The interval includes this value. The default value is 0</span></p><p>stop : <span style=\" vertical-align:top;\">End of interval. The interval does not include this value, except in some cases where </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is not an integer and"
                        " floating point round-off affects the length of </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">.</span></p><p>step : Difference between each number in the sequence. <span style=\" vertical-align:top;\">For any output </span><span style=\" font-style:italic; vertical-align:top;\">out</span><span style=\" vertical-align:top;\">, this is the distance between two adjacent values. The default value is 1.</span></p><p><span style=\" vertical-align:top;\">If </span><span style=\" font-style:italic; vertical-align:top;\">step</span><span style=\" vertical-align:top;\"> is specified, </span><span style=\" font-style:italic; vertical-align:top;\">start</span><span style=\" vertical-align:top;\"> must also be given.</span></p><p>dtype : The type of the output array. if dtype <span style=\" vertical-align:top;\">is not given, infer the data type from the other input arguments.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_c_3.setText(QCoreApplication.translate("Form", u"10     # Radius", None))
#if QT_CONFIG(tooltip)
        self.checkBox_cylind_3.setToolTip(QCoreApplication.translate("Form", u"Toggle for Cylindrical coordinates:", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_cylind_3.setText(QCoreApplication.translate("Form", u" Cylindrical coord.", None))
#if QT_CONFIG(tooltip)
        self.checkBox_spheric_3.setToolTip(QCoreApplication.translate("Form", u"Toggle for Sperical coordinates:", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_spheric_3.setText(QCoreApplication.translate("Form", u"Spherical coord.", None))
        self.label_x_3.setText(QCoreApplication.translate("Form", u"X (a,b,c,t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_x_3.setToolTip(QCoreApplication.translate("Form", u"The function from Python math module can be used here:\n"
"safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh',\n"
" 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp',\n"
" 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan',\n"
" 'tanh']", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_x_3.setText(QCoreApplication.translate("Form", u"c*sin(t)", None))
        self.label_y_3.setText(QCoreApplication.translate("Form", u"Y (a,b,c,t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_y_3.setToolTip(QCoreApplication.translate("Form", u"The function from Python math module can be used here:\n"
"safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh',\n"
" 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp',\n"
" 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan',\n"
" 'tanh']", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_y_3.setText(QCoreApplication.translate("Form", u"c*cos(t)", None))
        self.label_z_3.setText(QCoreApplication.translate("Form", u"Z (a,b,c,t) ", None))
#if QT_CONFIG(tooltip)
        self.ParCurve_z_3.setToolTip(QCoreApplication.translate("Form", u"The function from Python math module can be used here:\n"
"safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh',\n"
" 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp',\n"
" 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan',\n"
" 'tanh']", None))
#endif // QT_CONFIG(tooltip)
        self.ParCurve_z_3.setText(QCoreApplication.translate("Form", u"a*t", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Equation_tab_3), QCoreApplication.translate("Form", u"Equation", None))
        self.label_tmin_4.setText(QCoreApplication.translate("Form", u"t min", None))
        self.ParCurve_tmin_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_tmax_4.setText(QCoreApplication.translate("Form", u"t max", None))
        self.ParCurve_tmax_3.setText(QCoreApplication.translate("Form", u"5*2*pi   #5 circles", None))
        self.label_tstep_4.setText(QCoreApplication.translate("Form", u"step", None))
        self.ParCurve_tstep_3.setText(QCoreApplication.translate("Form", u"0.01", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Variables_tab_3), QCoreApplication.translate("Form", u"Variables", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.Wire_Tab3_3), QCoreApplication.translate("Form", u"Parametric 3D", None))
#if QT_CONFIG(tooltip)
        self.Surf_comboBox.setToolTip(QCoreApplication.translate("Form", u"Choose another curve from the list.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Surf_button_edit.setToolTip(QCoreApplication.translate("Form", u"Click to access to a table where you can edit all parameters of all curves and \n"
"save your custom curves.", None))
#endif // QT_CONFIG(tooltip)
        self.Surf_button_edit.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.label_name_4.setText(QCoreApplication.translate("Form", u"Name", None))
        self.Surf_name.setText(QCoreApplication.translate("Form", u"Astroid", None))
        self.label_a_5.setText(QCoreApplication.translate("Form", u"a", None))
        self.Surf_a.setText(QCoreApplication.translate("Form", u"4", None))
        self.label_b_5.setText(QCoreApplication.translate("Form", u"b (a) ", None))
        self.Surf_b.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_c_3.setText(QCoreApplication.translate("Form", u"c (a, b) ", None))
        self.Surf_c.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_x_4.setText(QCoreApplication.translate("Form", u"X (a,b,c,u,v) ", None))
#if QT_CONFIG(tooltip)
        self.Surf_x.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The function from Python math module can be used here:</p><p>safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh',</p><p> 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp',</p><p> 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan',</p><p> 'tanh']</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Surf_x.setText(QCoreApplication.translate("Form", u"a*pow(cos(v),3)*pow(cos(u),3)", None))
        self.label_y_4.setText(QCoreApplication.translate("Form", u"Y (a,b,c,u,v) ", None))
#if QT_CONFIG(tooltip)
        self.Surf_y.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The function from Python math module can be used here:</p><p>safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh',</p><p> 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp',</p><p> 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan',</p><p> 'tanh']</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Surf_y.setText(QCoreApplication.translate("Form", u"b*pow(cos(v),3)*pow(sin(u),3)", None))
        self.label_z_2.setText(QCoreApplication.translate("Form", u"Z (a,b,c,u,v) ", None))
#if QT_CONFIG(tooltip)
        self.Surf_z.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The function from Python math module can be used here:</p><p>safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh',</p><p> 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp',</p><p> 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan',</p><p> 'tanh']</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Surf_z.setText(QCoreApplication.translate("Form", u"c*pow(sin(v),3)", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_8), QCoreApplication.translate("Form", u"Equation", None))
        self.label_umin.setText(QCoreApplication.translate("Form", u"u min", None))
        self.Surf_umin.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_umax.setText(QCoreApplication.translate("Form", u"u max", None))
        self.Surf_umax.setText(QCoreApplication.translate("Form", u"2*pi", None))
        self.label_ustep.setText(QCoreApplication.translate("Form", u"u step", None))
        self.Surf_ustep.setText(QCoreApplication.translate("Form", u"0.01", None))
        self.label_umin_2.setText(QCoreApplication.translate("Form", u"v min", None))
        self.Surf_vmin.setText(QCoreApplication.translate("Form", u"-2", None))
        self.label_umax_2.setText(QCoreApplication.translate("Form", u"v max", None))
        self.Surf_vmax.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_ustep_2.setText(QCoreApplication.translate("Form", u"v step", None))
        self.Surf_vstep.setText(QCoreApplication.translate("Form", u"0.01", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_9), QCoreApplication.translate("Form", u"Variables", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"Type of Surface", None))
        self.Surf_points.setText(QCoreApplication.translate("Form", u"Points", None))
        self.Surf_polyline.setText(QCoreApplication.translate("Form", u"Polyline", None))
        self.Surf_bspline.setText(QCoreApplication.translate("Form", u"Bspline", None))
        self.Surf_bspline_surf.setText(QCoreApplication.translate("Form", u"Surf Bspline (Nurbs)", None))
        self.Surf_meshes.setText(QCoreApplication.translate("Form", u"Meshes", None))
#if QT_CONFIG(tooltip)
        self.Surf_button_store.setToolTip(QCoreApplication.translate("Form", u"Click to store the current edited curve into the table.\n"
"To save your curve you need to go to \"Edit\".", None))
#endif // QT_CONFIG(tooltip)
        self.Surf_button_store.setText(QCoreApplication.translate("Form", u"Store", None))
#if QT_CONFIG(tooltip)
        self.Surf_button_apply.setToolTip(QCoreApplication.translate("Form", u"Click to visualize the curve.", None))
#endif // QT_CONFIG(tooltip)
        self.Surf_button_apply.setText(QCoreApplication.translate("Form", u"Draw", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.Surface_Tab1), QCoreApplication.translate("Form", u"Surface", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab), QCoreApplication.translate("Form", u"Curves and Surfaces", None))
#if QT_CONFIG(tooltip)
        self.button_select_point.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Select point(s) to define reference locations for parametric curves and surfaces.</p><p>- Select as much as Points as needed ;</p><p>- Then click on this button.<br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_select_point.setText(QCoreApplication.translate("Form", u"Select Point(s)", None))
        self.label_x_6.setText(QCoreApplication.translate("Form", u"X cst.", None))
#if QT_CONFIG(tooltip)
        self.Par_x_ref.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Reference point (X value) where to attach the 2D curve.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Par_x_ref.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_y_6.setText(QCoreApplication.translate("Form", u"Y cst.", None))
#if QT_CONFIG(tooltip)
        self.Par_y_ref.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Reference point (Y value) where to attach the 2D curve.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Par_y_ref.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_z_6.setText(QCoreApplication.translate("Form", u"Z cst.", None))
#if QT_CONFIG(tooltip)
        self.Par_z_ref.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Reference point (Z value) where to attach the 2D curve.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Par_z_ref.setText(QCoreApplication.translate("Form", u"0.0", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Examples </p><p>from http://www.mathcurve.com/ </p><p>and </p><p>https://en.wikipedia.org/wiki/List_of_curves</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setText(QCoreApplication.translate("Form", u"Examples from http://www.mathcurve.com/ and https://en.wikipedia.org/wiki/List_of_curves", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Origin", None))
    # retranslateUi

