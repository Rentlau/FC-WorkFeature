# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WFGui_2015.ui'
#
# Created by: PySide UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(396, 701)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_wf.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_13 = QtGui.QGridLayout(Form)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setFrameShape(QtGui.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 376, 643))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_128 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_128.setObjectName(_fromUtf8("gridLayout_128"))
        self.tabWidget_7 = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget_7.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget_7.setObjectName(_fromUtf8("tabWidget_7"))
        self.Origin_Tab_2 = QtGui.QWidget()
        self.Origin_Tab_2.setObjectName(_fromUtf8("Origin_Tab_2"))
        self.gridLayout_65 = QtGui.QGridLayout(self.Origin_Tab_2)
        self.gridLayout_65.setObjectName(_fromUtf8("gridLayout_65"))
        self.button_origin = QtGui.QPushButton(self.Origin_Tab_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_Axes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_origin.setIcon(icon1)
        self.button_origin.setIconSize(QtCore.QSize(32, 32))
        self.button_origin.setObjectName(_fromUtf8("button_origin"))
        self.gridLayout_65.addWidget(self.button_origin, 0, 0, 1, 1)
        self.frame_6 = QtGui.QFrame(self.Origin_Tab_2)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_66 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_66.setObjectName(_fromUtf8("gridLayout_66"))
        self.groupBox_13 = QtGui.QGroupBox(self.frame_6)
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.gridLayout_67 = QtGui.QGridLayout(self.groupBox_13)
        self.gridLayout_67.setObjectName(_fromUtf8("gridLayout_67"))
        self.radioButton_verbose = QtGui.QRadioButton(self.groupBox_13)
        self.radioButton_verbose.setChecked(False)
        self.radioButton_verbose.setAutoExclusive(False)
        self.radioButton_verbose.setObjectName(_fromUtf8("radioButton_verbose"))
        self.gridLayout_67.addWidget(self.radioButton_verbose, 0, 0, 1, 1)
        self.radioButton_biColor = QtGui.QRadioButton(self.groupBox_13)
        self.radioButton_biColor.setAutoExclusive(False)
        self.radioButton_biColor.setObjectName(_fromUtf8("radioButton_biColor"))
        self.gridLayout_67.addWidget(self.radioButton_biColor, 1, 0, 1, 1)
        self.radioButton_copy = QtGui.QRadioButton(self.groupBox_13)
        self.radioButton_copy.setObjectName(_fromUtf8("radioButton_copy"))
        self.gridLayout_67.addWidget(self.radioButton_copy, 2, 0, 1, 1)
        self.horizontalLayout_44 = QtGui.QHBoxLayout()
        self.horizontalLayout_44.setObjectName(_fromUtf8("horizontalLayout_44"))
        self.label_10 = QtGui.QLabel(self.groupBox_13)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_44.addWidget(self.label_10)
        self.tolerance_edit = QtGui.QLineEdit(self.groupBox_13)
        self.tolerance_edit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.tolerance_edit.setObjectName(_fromUtf8("tolerance_edit"))
        self.horizontalLayout_44.addWidget(self.tolerance_edit)
        self.gridLayout_67.addLayout(self.horizontalLayout_44, 3, 0, 1, 1)
        self.gridLayout_66.addWidget(self.groupBox_13, 0, 0, 1, 1)
        self.gridLayout_65.addWidget(self.frame_6, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_65.addItem(spacerItem, 2, 0, 1, 1)
        self.tabWidget_7.addTab(self.Origin_Tab_2, icon1, _fromUtf8(""))
        self.Point_Tab = QtGui.QWidget()
        self.Point_Tab.setObjectName(_fromUtf8("Point_Tab"))
        self.gridLayout_10 = QtGui.QGridLayout(self.Point_Tab)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.tabWidget = QtGui.QTabWidget(self.Point_Tab)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Point_Tab1_3 = QtGui.QWidget()
        self.Point_Tab1_3.setObjectName(_fromUtf8("Point_Tab1_3"))
        self.gridLayout_11 = QtGui.QGridLayout(self.Point_Tab1_3)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.horizontalLayout_46 = QtGui.QHBoxLayout()
        self.horizontalLayout_46.setObjectName(_fromUtf8("horizontalLayout_46"))
        self.button_object_center = QtGui.QPushButton(self.Point_Tab1_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerObjectsPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_center.setIcon(icon2)
        self.button_object_center.setIconSize(QtCore.QSize(32, 32))
        self.button_object_center.setObjectName(_fromUtf8("button_object_center"))
        self.horizontalLayout_46.addWidget(self.button_object_center)
        self.checkBox_object_center = QtGui.QCheckBox(self.Point_Tab1_3)
        self.checkBox_object_center.setObjectName(_fromUtf8("checkBox_object_center"))
        self.horizontalLayout_46.addWidget(self.checkBox_object_center)
        self.gridLayout_11.addLayout(self.horizontalLayout_46, 0, 0, 1, 1)
        self.button_Npoints_center = QtGui.QPushButton(self.Point_Tab1_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_NpointsPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_Npoints_center.setIcon(icon3)
        self.button_Npoints_center.setIconSize(QtCore.QSize(32, 32))
        self.button_Npoints_center.setObjectName(_fromUtf8("button_Npoints_center"))
        self.gridLayout_11.addWidget(self.button_Npoints_center, 1, 0, 1, 1)
        self.horizontalLayout_45 = QtGui.QHBoxLayout()
        self.horizontalLayout_45.setObjectName(_fromUtf8("horizontalLayout_45"))
        self.button_line_center = QtGui.QPushButton(self.Point_Tab1_3)
        self.button_line_center.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_center.setIcon(icon4)
        self.button_line_center.setIconSize(QtCore.QSize(32, 32))
        self.button_line_center.setObjectName(_fromUtf8("button_line_center"))
        self.horizontalLayout_45.addWidget(self.button_line_center)
        self.spin_line_center = QtGui.QSpinBox(self.Point_Tab1_3)
        self.spin_line_center.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_line_center.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_line_center.setMinimum(2)
        self.spin_line_center.setMaximum(100)
        self.spin_line_center.setSingleStep(1)
        self.spin_line_center.setObjectName(_fromUtf8("spin_line_center"))
        self.horizontalLayout_45.addWidget(self.spin_line_center)
        self.gridLayout_11.addLayout(self.horizontalLayout_45, 2, 0, 1, 1)
        self.button_line_extrema = QtGui.QPushButton(self.Point_Tab1_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_extremaLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_extrema.setIcon(icon5)
        self.button_line_extrema.setIconSize(QtCore.QSize(32, 32))
        self.button_line_extrema.setObjectName(_fromUtf8("button_line_extrema"))
        self.gridLayout_11.addWidget(self.button_line_extrema, 3, 0, 1, 1)
        self.button_circle_center = QtGui.QPushButton(self.Point_Tab1_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerCirclePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_circle_center.setIcon(icon6)
        self.button_circle_center.setIconSize(QtCore.QSize(32, 32))
        self.button_circle_center.setObjectName(_fromUtf8("button_circle_center"))
        self.gridLayout_11.addWidget(self.button_circle_center, 4, 0, 1, 1)
        self.button_face_center = QtGui.QPushButton(self.Point_Tab1_3)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerFacePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_face_center.setIcon(icon7)
        self.button_face_center.setIconSize(QtCore.QSize(32, 32))
        self.button_face_center.setObjectName(_fromUtf8("button_face_center"))
        self.gridLayout_11.addWidget(self.button_face_center, 5, 0, 1, 1)
        self.button_line_face_point = QtGui.QPushButton(self.Point_Tab1_3)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_lineFacePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_face_point.setIcon(icon8)
        self.button_line_face_point.setIconSize(QtCore.QSize(32, 32))
        self.button_line_face_point.setObjectName(_fromUtf8("button_line_face_point"))
        self.gridLayout_11.addWidget(self.button_line_face_point, 6, 0, 1, 1)
        self.button_point_face_point = QtGui.QPushButton(self.Point_Tab1_3)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointFacePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_face_point.setIcon(icon9)
        self.button_point_face_point.setIconSize(QtCore.QSize(32, 32))
        self.button_point_face_point.setObjectName(_fromUtf8("button_point_face_point"))
        self.gridLayout_11.addWidget(self.button_point_face_point, 7, 0, 1, 1)
        self.horizontalLayout_59 = QtGui.QHBoxLayout()
        self.horizontalLayout_59.setObjectName(_fromUtf8("horizontalLayout_59"))
        self.button_points_projection = QtGui.QPushButton(self.Point_Tab1_3)
        self.button_points_projection.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_projectedPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_points_projection.setIcon(icon10)
        self.button_points_projection.setIconSize(QtCore.QSize(32, 32))
        self.button_points_projection.setObjectName(_fromUtf8("button_points_projection"))
        self.horizontalLayout_59.addWidget(self.button_points_projection)
        self.point_proj_comboBox = QtGui.QComboBox(self.Point_Tab1_3)
        self.point_proj_comboBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.point_proj_comboBox.setObjectName(_fromUtf8("point_proj_comboBox"))
        self.point_proj_comboBox.addItem(_fromUtf8(""))
        self.point_proj_comboBox.addItem(_fromUtf8(""))
        self.point_proj_comboBox.addItem(_fromUtf8(""))
        self.point_proj_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_59.addWidget(self.point_proj_comboBox)
        self.gridLayout_11.addLayout(self.horizontalLayout_59, 8, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 252, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem1, 9, 0, 1, 1)
        self.tabWidget.addTab(self.Point_Tab1_3, _fromUtf8(""))
        self.Point_Tab2_3 = QtGui.QWidget()
        self.Point_Tab2_3.setObjectName(_fromUtf8("Point_Tab2_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Point_Tab2_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.button_point_line_point = QtGui.QPushButton(self.Point_Tab2_3)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_line_point.setIcon(icon11)
        self.button_point_line_point.setIconSize(QtCore.QSize(32, 32))
        self.button_point_line_point.setObjectName(_fromUtf8("button_point_line_point"))
        self.gridLayout_2.addWidget(self.button_point_line_point, 0, 0, 1, 1)
        self.button_twolines_point = QtGui.QPushButton(self.Point_Tab2_3)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_lineLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_twolines_point.setIcon(icon12)
        self.button_twolines_point.setIconSize(QtCore.QSize(32, 32))
        self.button_twolines_point.setObjectName(_fromUtf8("button_twolines_point"))
        self.gridLayout_2.addWidget(self.button_twolines_point, 1, 0, 1, 1)
        self.horizontalLayout_47 = QtGui.QHBoxLayout()
        self.horizontalLayout_47.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_47.setObjectName(_fromUtf8("horizontalLayout_47"))
        self.button_point_on_line = QtGui.QPushButton(self.Point_Tab2_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_point_on_line.sizePolicy().hasHeightForWidth())
        self.button_point_on_line.setSizePolicy(sizePolicy)
        self.button_point_on_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_alongLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_on_line.setIcon(icon13)
        self.button_point_on_line.setIconSize(QtCore.QSize(32, 32))
        self.button_point_on_line.setObjectName(_fromUtf8("button_point_on_line"))
        self.horizontalLayout_47.addWidget(self.button_point_on_line)
        self.distance_point_on_line = QtGui.QLineEdit(self.Point_Tab2_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distance_point_on_line.sizePolicy().hasHeightForWidth())
        self.distance_point_on_line.setSizePolicy(sizePolicy)
        self.distance_point_on_line.setMinimumSize(QtCore.QSize(50, 0))
        self.distance_point_on_line.setMaximumSize(QtCore.QSize(60, 16777215))
        self.distance_point_on_line.setObjectName(_fromUtf8("distance_point_on_line"))
        self.horizontalLayout_47.addWidget(self.distance_point_on_line)
        self.gridLayout_2.addLayout(self.horizontalLayout_47, 2, 0, 1, 1)
        self.horizontalLayout_48 = QtGui.QHBoxLayout()
        self.horizontalLayout_48.setObjectName(_fromUtf8("horizontalLayout_48"))
        self.button_distPoint = QtGui.QPushButton(self.Point_Tab2_3)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_distPointPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_distPoint.setIcon(icon14)
        self.button_distPoint.setIconSize(QtCore.QSize(32, 32))
        self.button_distPoint.setObjectName(_fromUtf8("button_distPoint"))
        self.horizontalLayout_48.addWidget(self.button_distPoint)
        self.dist_point = QtGui.QLineEdit(self.Point_Tab2_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dist_point.sizePolicy().hasHeightForWidth())
        self.dist_point.setSizePolicy(sizePolicy)
        self.dist_point.setMinimumSize(QtCore.QSize(40, 0))
        self.dist_point.setMaximumSize(QtCore.QSize(40, 16777215))
        self.dist_point.setObjectName(_fromUtf8("dist_point"))
        self.horizontalLayout_48.addWidget(self.dist_point)
        self.spin_dist_point = QtGui.QSpinBox(self.Point_Tab2_3)
        self.spin_dist_point.setMinimumSize(QtCore.QSize(30, 0))
        self.spin_dist_point.setMaximumSize(QtCore.QSize(30, 16777215))
        self.spin_dist_point.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spin_dist_point.setKeyboardTracking(False)
        self.spin_dist_point.setMinimum(1)
        self.spin_dist_point.setMaximum(100)
        self.spin_dist_point.setSingleStep(1)
        self.spin_dist_point.setProperty("value", 1)
        self.spin_dist_point.setObjectName(_fromUtf8("spin_dist_point"))
        self.horizontalLayout_48.addWidget(self.spin_dist_point)
        self.gridLayout_2.addLayout(self.horizontalLayout_48, 3, 0, 1, 1)
        self.horizontalLayout_49 = QtGui.QHBoxLayout()
        self.horizontalLayout_49.setObjectName(_fromUtf8("horizontalLayout_49"))
        self.button_cut_wire_point = QtGui.QPushButton(self.Point_Tab2_3)
        self.button_cut_wire_point.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cutWirePoints.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cut_wire_point.setIcon(icon15)
        self.button_cut_wire_point.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_wire_point.setObjectName(_fromUtf8("button_cut_wire_point"))
        self.horizontalLayout_49.addWidget(self.button_cut_wire_point)
        self.spin_wire_cut_point = QtGui.QSpinBox(self.Point_Tab2_3)
        self.spin_wire_cut_point.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_wire_cut_point.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_wire_cut_point.setMinimum(2)
        self.spin_wire_cut_point.setMaximum(100)
        self.spin_wire_cut_point.setSingleStep(1)
        self.spin_wire_cut_point.setObjectName(_fromUtf8("spin_wire_cut_point"))
        self.horizontalLayout_49.addWidget(self.spin_wire_cut_point)
        self.gridLayout_2.addLayout(self.horizontalLayout_49, 4, 0, 1, 1)
        self.button_click_for_point = QtGui.QRadioButton(self.Point_Tab2_3)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_clickPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_click_for_point.setIcon(icon16)
        self.button_click_for_point.setIconSize(QtCore.QSize(32, 32))
        self.button_click_for_point.setCheckable(True)
        self.button_click_for_point.setObjectName(_fromUtf8("button_click_for_point"))
        self.gridLayout_2.addWidget(self.button_click_for_point, 5, 0, 1, 1)
        self.button_object_base_point = QtGui.QPushButton(self.Point_Tab2_3)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectBasePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_base_point.setIcon(icon17)
        self.button_object_base_point.setIconSize(QtCore.QSize(32, 32))
        self.button_object_base_point.setObjectName(_fromUtf8("button_object_base_point"))
        self.gridLayout_2.addWidget(self.button_object_base_point, 6, 0, 1, 1)
        self.button_object_center_mass_point = QtGui.QPushButton(self.Point_Tab2_3)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectCenterMassPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_center_mass_point.setIcon(icon18)
        self.button_object_center_mass_point.setIconSize(QtCore.QSize(32, 32))
        self.button_object_center_mass_point.setObjectName(_fromUtf8("button_object_center_mass_point"))
        self.gridLayout_2.addWidget(self.button_object_center_mass_point, 7, 0, 1, 1)
        self.button_object_Npoint = QtGui.QPushButton(self.Point_Tab2_3)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectNPoints.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_Npoint.setIcon(icon19)
        self.button_object_Npoint.setIconSize(QtCore.QSize(32, 32))
        self.button_object_Npoint.setObjectName(_fromUtf8("button_object_Npoint"))
        self.gridLayout_2.addWidget(self.button_object_Npoint, 8, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 255, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 9, 0, 1, 1)
        self.tabWidget.addTab(self.Point_Tab2_3, _fromUtf8(""))
        self.Point_Tab3_3 = QtGui.QWidget()
        self.Point_Tab3_3.setObjectName(_fromUtf8("Point_Tab3_3"))
        self.gridLayout_22 = QtGui.QGridLayout(self.Point_Tab3_3)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        self.button_points_load = QtGui.QPushButton(self.Point_Tab3_3)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointsSetLoad.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_points_load.setIcon(icon20)
        self.button_points_load.setIconSize(QtCore.QSize(32, 32))
        self.button_points_load.setObjectName(_fromUtf8("button_points_load"))
        self.gridLayout_22.addWidget(self.button_points_load, 0, 0, 1, 1)
        self.button_points_save = QtGui.QPushButton(self.Point_Tab3_3)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointsSetSave.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_points_save.setIcon(icon21)
        self.button_points_save.setIconSize(QtCore.QSize(32, 32))
        self.button_points_save.setObjectName(_fromUtf8("button_points_save"))
        self.gridLayout_22.addWidget(self.button_points_save, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.button_points_random = QtGui.QPushButton(self.Point_Tab3_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_points_random.sizePolicy().hasHeightForWidth())
        self.button_points_random.setSizePolicy(sizePolicy)
        self.button_points_random.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointsRandom.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_points_random.setIcon(icon22)
        self.button_points_random.setIconSize(QtCore.QSize(32, 32))
        self.button_points_random.setObjectName(_fromUtf8("button_points_random"))
        self.horizontalLayout_5.addWidget(self.button_points_random)
        self.spin_random_points = QtGui.QSpinBox(self.Point_Tab3_3)
        self.spin_random_points.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_random_points.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_random_points.setMinimum(1)
        self.spin_random_points.setMaximum(100)
        self.spin_random_points.setSingleStep(1)
        self.spin_random_points.setProperty("value", 1)
        self.spin_random_points.setObjectName(_fromUtf8("spin_random_points"))
        self.horizontalLayout_5.addWidget(self.spin_random_points)
        self.distance_random_points = QtGui.QLineEdit(self.Point_Tab3_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distance_random_points.sizePolicy().hasHeightForWidth())
        self.distance_random_points.setSizePolicy(sizePolicy)
        self.distance_random_points.setMinimumSize(QtCore.QSize(50, 0))
        self.distance_random_points.setMaximumSize(QtCore.QSize(60, 16777215))
        self.distance_random_points.setObjectName(_fromUtf8("distance_random_points"))
        self.horizontalLayout_5.addWidget(self.distance_random_points)
        self.gridLayout_22.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.button_point_to_sketch = QtGui.QPushButton(self.Point_Tab3_3)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_2Sketch.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_to_sketch.setIcon(icon23)
        self.button_point_to_sketch.setIconSize(QtCore.QSize(32, 32))
        self.button_point_to_sketch.setObjectName(_fromUtf8("button_point_to_sketch"))
        self.gridLayout_22.addWidget(self.button_point_to_sketch, 3, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 579, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem3, 4, 0, 1, 1)
        self.tabWidget.addTab(self.Point_Tab3_3, _fromUtf8(""))
        self.gridLayout_10.addWidget(self.tabWidget, 0, 0, 1, 1)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_point.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_7.addTab(self.Point_Tab, icon24, _fromUtf8(""))
        self.Axis_Tab = QtGui.QWidget()
        self.Axis_Tab.setObjectName(_fromUtf8("Axis_Tab"))
        self.gridLayout_14 = QtGui.QGridLayout(self.Axis_Tab)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.tabWidget_2 = QtGui.QTabWidget(self.Axis_Tab)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.Axis_Tab1_3 = QtGui.QWidget()
        self.Axis_Tab1_3.setObjectName(_fromUtf8("Axis_Tab1_3"))
        self.gridLayout_15 = QtGui.QGridLayout(self.Axis_Tab1_3)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button_twopoints_axis = QtGui.QPushButton(self.Axis_Tab1_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_twopoints_axis.sizePolicy().hasHeightForWidth())
        self.button_twopoints_axis.setSizePolicy(sizePolicy)
        self.button_twopoints_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_2pointsLine.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_twopoints_axis.setIcon(icon25)
        self.button_twopoints_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_twopoints_axis.setObjectName(_fromUtf8("button_twopoints_axis"))
        self.horizontalLayout.addWidget(self.button_twopoints_axis)
        self.extension_twopoints_axis = QtGui.QLineEdit(self.Axis_Tab1_3)
        self.extension_twopoints_axis.setMaximumSize(QtCore.QSize(40, 16777215))
        self.extension_twopoints_axis.setObjectName(_fromUtf8("extension_twopoints_axis"))
        self.horizontalLayout.addWidget(self.extension_twopoints_axis)
        self.gridLayout_15.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 233, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem4, 7, 0, 1, 1)
        self.button_object_axis = QtGui.QPushButton(self.Axis_Tab1_3)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerObjectsAxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_axis.setIcon(icon26)
        self.button_object_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_object_axis.setObjectName(_fromUtf8("button_object_axis"))
        self.gridLayout_15.addWidget(self.button_object_axis, 0, 0, 1, 1)
        self.horizontalLayout_53 = QtGui.QHBoxLayout()
        self.horizontalLayout_53.setObjectName(_fromUtf8("horizontalLayout_53"))
        self.button_line_point_axis = QtGui.QPushButton(self.Axis_Tab1_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_line_point_axis.sizePolicy().hasHeightForWidth())
        self.button_line_point_axis.setSizePolicy(sizePolicy)
        self.button_line_point_axis.setMinimumSize(QtCore.QSize(0, 0))
        self.button_line_point_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePointAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_point_axis.setIcon(icon27)
        self.button_line_point_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_line_point_axis.setObjectName(_fromUtf8("button_line_point_axis"))
        self.horizontalLayout_53.addWidget(self.button_line_point_axis)
        self.extension_line_point_axis = QtGui.QLineEdit(self.Axis_Tab1_3)
        self.extension_line_point_axis.setMaximumSize(QtCore.QSize(40, 16777215))
        self.extension_line_point_axis.setObjectName(_fromUtf8("extension_line_point_axis"))
        self.horizontalLayout_53.addWidget(self.extension_line_point_axis)
        self.gridLayout_15.addLayout(self.horizontalLayout_53, 5, 0, 1, 1)
        self.button_Npoints_axis = QtGui.QPushButton(self.Axis_Tab1_3)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_NpointsLine.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_Npoints_axis.setIcon(icon28)
        self.button_Npoints_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_Npoints_axis.setObjectName(_fromUtf8("button_Npoints_axis"))
        self.gridLayout_15.addWidget(self.button_Npoints_axis, 2, 0, 1, 1)
        self.horizontalLayout_52 = QtGui.QHBoxLayout()
        self.horizontalLayout_52.setObjectName(_fromUtf8("horizontalLayout_52"))
        self.button_point_line_axis = QtGui.QPushButton(self.Axis_Tab1_3)
        self.button_point_line_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointLineAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_line_axis.setIcon(icon29)
        self.button_point_line_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_point_line_axis.setObjectName(_fromUtf8("button_point_line_axis"))
        self.horizontalLayout_52.addWidget(self.button_point_line_axis)
        self.extension_line = QtGui.QLineEdit(self.Axis_Tab1_3)
        self.extension_line.setMaximumSize(QtCore.QSize(40, 16777215))
        self.extension_line.setObjectName(_fromUtf8("extension_line"))
        self.horizontalLayout_52.addWidget(self.extension_line)
        self.point_loc_comboBox = QtGui.QComboBox(self.Axis_Tab1_3)
        self.point_loc_comboBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.point_loc_comboBox.setObjectName(_fromUtf8("point_loc_comboBox"))
        self.point_loc_comboBox.addItem(_fromUtf8(""))
        self.point_loc_comboBox.addItem(_fromUtf8(""))
        self.point_loc_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_52.addWidget(self.point_loc_comboBox)
        self.gridLayout_15.addLayout(self.horizontalLayout_52, 4, 0, 1, 1)
        self.horizontalLayout_51 = QtGui.QHBoxLayout()
        self.horizontalLayout_51.setObjectName(_fromUtf8("horizontalLayout_51"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.button_cylinder_axis = QtGui.QPushButton(self.Axis_Tab1_3)
        self.button_cylinder_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cylinderAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cylinder_axis.setIcon(icon30)
        self.button_cylinder_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_cylinder_axis.setObjectName(_fromUtf8("button_cylinder_axis"))
        self.verticalLayout_3.addWidget(self.button_cylinder_axis)
        self.button_plane_axis = QtGui.QPushButton(self.Axis_Tab1_3)
        self.button_plane_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_FaceAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_plane_axis.setIcon(icon31)
        self.button_plane_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_plane_axis.setObjectName(_fromUtf8("button_plane_axis"))
        self.verticalLayout_3.addWidget(self.button_plane_axis)
        self.button_face_normal = QtGui.QPushButton(self.Axis_Tab1_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_face_normal.sizePolicy().hasHeightForWidth())
        self.button_face_normal.setSizePolicy(sizePolicy)
        self.button_face_normal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_FaceNormal.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_face_normal.setIcon(icon32)
        self.button_face_normal.setIconSize(QtCore.QSize(32, 32))
        self.button_face_normal.setObjectName(_fromUtf8("button_face_normal"))
        self.verticalLayout_3.addWidget(self.button_face_normal)
        self.horizontalLayout_51.addLayout(self.verticalLayout_3)
        self.frame_8 = QtGui.QFrame(self.Axis_Tab1_3)
        self.frame_8.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.gridLayout_72 = QtGui.QGridLayout(self.frame_8)
        self.gridLayout_72.setObjectName(_fromUtf8("gridLayout_72"))
        self.extension_face_normal = QtGui.QLineEdit(self.frame_8)
        self.extension_face_normal.setMinimumSize(QtCore.QSize(40, 0))
        self.extension_face_normal.setMaximumSize(QtCore.QSize(40, 16777215))
        self.extension_face_normal.setObjectName(_fromUtf8("extension_face_normal"))
        self.gridLayout_72.addWidget(self.extension_face_normal, 0, 0, 1, 1)
        self.horizontalLayout_51.addWidget(self.frame_8)
        self.gridLayout_15.addLayout(self.horizontalLayout_51, 3, 0, 1, 1)
        self.button_twolines_axis = QtGui.QPushButton(self.Axis_Tab1_3)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_twoLinesAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_twolines_axis.setIcon(icon33)
        self.button_twolines_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_twolines_axis.setObjectName(_fromUtf8("button_twolines_axis"))
        self.gridLayout_15.addWidget(self.button_twolines_axis, 6, 0, 1, 1)
        self.tabWidget_2.addTab(self.Axis_Tab1_3, _fromUtf8(""))
        self.Axis_Tab31_3 = QtGui.QWidget()
        self.Axis_Tab31_3.setObjectName(_fromUtf8("Axis_Tab31_3"))
        self.gridLayout_16 = QtGui.QGridLayout(self.Axis_Tab31_3)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.button_object_base_axes = QtGui.QPushButton(self.Axis_Tab31_3)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_baseObjectsAxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_base_axes.setIcon(icon34)
        self.button_object_base_axes.setIconSize(QtCore.QSize(32, 32))
        self.button_object_base_axes.setObjectName(_fromUtf8("button_object_base_axes"))
        self.gridLayout_16.addWidget(self.button_object_base_axes, 0, 0, 1, 1)
        self.button_object_Naxes = QtGui.QPushButton(self.Axis_Tab31_3)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectNAxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_Naxes.setIcon(icon35)
        self.button_object_Naxes.setIconSize(QtCore.QSize(32, 32))
        self.button_object_Naxes.setObjectName(_fromUtf8("button_object_Naxes"))
        self.gridLayout_16.addWidget(self.button_object_Naxes, 1, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 483, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem5, 4, 0, 1, 1)
        self.button_line_to_sketch = QtGui.QPushButton(self.Axis_Tab31_3)
        self.button_line_to_sketch.setIcon(icon23)
        self.button_line_to_sketch.setIconSize(QtCore.QSize(32, 32))
        self.button_line_to_sketch.setObjectName(_fromUtf8("button_line_to_sketch"))
        self.gridLayout_16.addWidget(self.button_line_to_sketch, 3, 0, 1, 1)
        self.button_object_3axes = QtGui.QPushButton(self.Axis_Tab31_3)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_object3Axes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_3axes.setIcon(icon36)
        self.button_object_3axes.setIconSize(QtCore.QSize(32, 32))
        self.button_object_3axes.setObjectName(_fromUtf8("button_object_3axes"))
        self.gridLayout_16.addWidget(self.button_object_3axes, 2, 0, 1, 1)
        self.tabWidget_2.addTab(self.Axis_Tab31_3, _fromUtf8(""))
        self.Axis_Tab2_3 = QtGui.QWidget()
        self.Axis_Tab2_3.setObjectName(_fromUtf8("Axis_Tab2_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.Axis_Tab2_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.button_plane_point_line_axis = QtGui.QPushButton(self.Axis_Tab2_3)
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_planeLinePointAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_plane_point_line_axis.setIcon(icon37)
        self.button_plane_point_line_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_plane_point_line_axis.setObjectName(_fromUtf8("button_plane_point_line_axis"))
        self.gridLayout_4.addWidget(self.button_plane_point_line_axis, 0, 0, 1, 1)
        self.button_line_plane_axis = QtGui.QPushButton(self.Axis_Tab2_3)
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePlaneAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_plane_axis.setIcon(icon38)
        self.button_line_plane_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_line_plane_axis.setObjectName(_fromUtf8("button_line_plane_axis"))
        self.gridLayout_4.addWidget(self.button_line_plane_axis, 1, 0, 1, 1)
        self.button_twoplanes_axis = QtGui.QPushButton(self.Axis_Tab2_3)
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_2PlanesAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_twoplanes_axis.setIcon(icon39)
        self.button_twoplanes_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_twoplanes_axis.setObjectName(_fromUtf8("button_twoplanes_axis"))
        self.gridLayout_4.addWidget(self.button_twoplanes_axis, 2, 0, 1, 1)
        self.horizontalLayout_54 = QtGui.QHBoxLayout()
        self.horizontalLayout_54.setObjectName(_fromUtf8("horizontalLayout_54"))
        self.button_distLine = QtGui.QPushButton(self.Axis_Tab2_3)
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_distAxisAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_distLine.setIcon(icon40)
        self.button_distLine.setIconSize(QtCore.QSize(32, 32))
        self.button_distLine.setObjectName(_fromUtf8("button_distLine"))
        self.horizontalLayout_54.addWidget(self.button_distLine)
        self.dist_line = QtGui.QLineEdit(self.Axis_Tab2_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dist_line.sizePolicy().hasHeightForWidth())
        self.dist_line.setSizePolicy(sizePolicy)
        self.dist_line.setMinimumSize(QtCore.QSize(40, 0))
        self.dist_line.setMaximumSize(QtCore.QSize(40, 16777215))
        self.dist_line.setObjectName(_fromUtf8("dist_line"))
        self.horizontalLayout_54.addWidget(self.dist_line)
        self.spin_dist_line = QtGui.QSpinBox(self.Axis_Tab2_3)
        self.spin_dist_line.setMinimumSize(QtCore.QSize(30, 0))
        self.spin_dist_line.setMaximumSize(QtCore.QSize(30, 16777215))
        self.spin_dist_line.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spin_dist_line.setKeyboardTracking(False)
        self.spin_dist_line.setMinimum(1)
        self.spin_dist_line.setMaximum(100)
        self.spin_dist_line.setSingleStep(1)
        self.spin_dist_line.setProperty("value", 1)
        self.spin_dist_line.setObjectName(_fromUtf8("spin_dist_line"))
        self.horizontalLayout_54.addWidget(self.spin_dist_line)
        self.gridLayout_4.addLayout(self.horizontalLayout_54, 3, 0, 1, 1)
        self.horizontalLayout_55 = QtGui.QHBoxLayout()
        self.horizontalLayout_55.setObjectName(_fromUtf8("horizontalLayout_55"))
        self.button_angleLine = QtGui.QPushButton(self.Axis_Tab2_3)
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_angleAxisAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_angleLine.setIcon(icon41)
        self.button_angleLine.setIconSize(QtCore.QSize(32, 32))
        self.button_angleLine.setObjectName(_fromUtf8("button_angleLine"))
        self.horizontalLayout_55.addWidget(self.button_angleLine)
        self.angle_line = QtGui.QLineEdit(self.Axis_Tab2_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_line.sizePolicy().hasHeightForWidth())
        self.angle_line.setSizePolicy(sizePolicy)
        self.angle_line.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_line.setMaximumSize(QtCore.QSize(40, 16777215))
        self.angle_line.setObjectName(_fromUtf8("angle_line"))
        self.horizontalLayout_55.addWidget(self.angle_line)
        self.spin_angle_line = QtGui.QSpinBox(self.Axis_Tab2_3)
        self.spin_angle_line.setMinimumSize(QtCore.QSize(30, 0))
        self.spin_angle_line.setMaximumSize(QtCore.QSize(30, 16777215))
        self.spin_angle_line.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spin_angle_line.setKeyboardTracking(False)
        self.spin_angle_line.setMinimum(1)
        self.spin_angle_line.setMaximum(100)
        self.spin_angle_line.setSingleStep(1)
        self.spin_angle_line.setProperty("value", 1)
        self.spin_angle_line.setObjectName(_fromUtf8("spin_angle_line"))
        self.horizontalLayout_55.addWidget(self.spin_angle_line)
        self.gridLayout_4.addLayout(self.horizontalLayout_55, 4, 0, 1, 1)
        self.horizontalLayout_56 = QtGui.QHBoxLayout()
        self.horizontalLayout_56.setObjectName(_fromUtf8("horizontalLayout_56"))
        self.button_cut_wire_axis = QtGui.QPushButton(self.Axis_Tab2_3)
        self.button_cut_wire_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cutWireAxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cut_wire_axis.setIcon(icon42)
        self.button_cut_wire_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_wire_axis.setObjectName(_fromUtf8("button_cut_wire_axis"))
        self.horizontalLayout_56.addWidget(self.button_cut_wire_axis)
        self.spin_wire_cut_axis = QtGui.QSpinBox(self.Axis_Tab2_3)
        self.spin_wire_cut_axis.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_wire_cut_axis.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_wire_cut_axis.setMinimum(2)
        self.spin_wire_cut_axis.setMaximum(100)
        self.spin_wire_cut_axis.setSingleStep(1)
        self.spin_wire_cut_axis.setObjectName(_fromUtf8("spin_wire_cut_axis"))
        self.horizontalLayout_56.addWidget(self.spin_wire_cut_axis)
        self.gridLayout_4.addLayout(self.horizontalLayout_56, 5, 0, 1, 1)
        self.horizontalLayout_57 = QtGui.QHBoxLayout()
        self.horizontalLayout_57.setObjectName(_fromUtf8("horizontalLayout_57"))
        self.button_cut_axis = QtGui.QPushButton(self.Axis_Tab2_3)
        self.button_cut_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cutAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cut_axis.setIcon(icon43)
        self.button_cut_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_axis.setObjectName(_fromUtf8("button_cut_axis"))
        self.horizontalLayout_57.addWidget(self.button_cut_axis)
        self.spin_axis_cut = QtGui.QSpinBox(self.Axis_Tab2_3)
        self.spin_axis_cut.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_axis_cut.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_axis_cut.setMinimum(2)
        self.spin_axis_cut.setMaximum(100)
        self.spin_axis_cut.setSingleStep(1)
        self.spin_axis_cut.setObjectName(_fromUtf8("spin_axis_cut"))
        self.horizontalLayout_57.addWidget(self.spin_axis_cut)
        self.gridLayout_4.addLayout(self.horizontalLayout_57, 6, 0, 1, 1)
        self.horizontalLayout_58 = QtGui.QHBoxLayout()
        self.horizontalLayout_58.setObjectName(_fromUtf8("horizontalLayout_58"))
        self.button_extension_axis = QtGui.QPushButton(self.Axis_Tab2_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_extension_axis.sizePolicy().hasHeightForWidth())
        self.button_extension_axis.setSizePolicy(sizePolicy)
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_enlargeLine.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_extension_axis.setIcon(icon44)
        self.button_extension_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_extension_axis.setObjectName(_fromUtf8("button_extension_axis"))
        self.horizontalLayout_58.addWidget(self.button_extension_axis)
        self.extension_axis = QtGui.QLineEdit(self.Axis_Tab2_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extension_axis.sizePolicy().hasHeightForWidth())
        self.extension_axis.setSizePolicy(sizePolicy)
        self.extension_axis.setMinimumSize(QtCore.QSize(40, 0))
        self.extension_axis.setMaximumSize(QtCore.QSize(50, 16777215))
        self.extension_axis.setObjectName(_fromUtf8("extension_axis"))
        self.horizontalLayout_58.addWidget(self.extension_axis)
        self.gridLayout_4.addLayout(self.horizontalLayout_58, 7, 0, 1, 1)
        self.button_click_for_axis = QtGui.QRadioButton(self.Axis_Tab2_3)
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_clickLine.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_click_for_axis.setIcon(icon45)
        self.button_click_for_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_click_for_axis.setObjectName(_fromUtf8("button_click_for_axis"))
        self.gridLayout_4.addWidget(self.button_click_for_axis, 8, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 238, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 9, 0, 1, 1)
        self.tabWidget_2.addTab(self.Axis_Tab2_3, _fromUtf8(""))
        self.gridLayout_14.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_axis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_7.addTab(self.Axis_Tab, icon46, _fromUtf8(""))
        self.Wire_Tab = QtGui.QWidget()
        self.Wire_Tab.setObjectName(_fromUtf8("Wire_Tab"))
        self.gridLayout_74 = QtGui.QGridLayout(self.Wire_Tab)
        self.gridLayout_74.setObjectName(_fromUtf8("gridLayout_74"))
        self.tabWidget_8 = QtGui.QTabWidget(self.Wire_Tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_8.sizePolicy().hasHeightForWidth())
        self.tabWidget_8.setSizePolicy(sizePolicy)
        self.tabWidget_8.setObjectName(_fromUtf8("tabWidget_8"))
        self.Wire_Tab1_3 = QtGui.QWidget()
        self.Wire_Tab1_3.setObjectName(_fromUtf8("Wire_Tab1_3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.Wire_Tab1_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.button_points_to_polygon = QtGui.QPushButton(self.Wire_Tab1_3)
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_makePolygon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_points_to_polygon.setIcon(icon47)
        self.button_points_to_polygon.setIconSize(QtCore.QSize(32, 32))
        self.button_points_to_polygon.setObjectName(_fromUtf8("button_points_to_polygon"))
        self.gridLayout_7.addWidget(self.button_points_to_polygon, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.button_points_to_convex_2Dpolygon = QtGui.QPushButton(self.Wire_Tab1_3)
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_convexPolygon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_points_to_convex_2Dpolygon.setIcon(icon48)
        self.button_points_to_convex_2Dpolygon.setIconSize(QtCore.QSize(32, 32))
        self.button_points_to_convex_2Dpolygon.setObjectName(_fromUtf8("button_points_to_convex_2Dpolygon"))
        self.horizontalLayout_6.addWidget(self.button_points_to_convex_2Dpolygon)
        self.point_proj_comboBox_2 = QtGui.QComboBox(self.Wire_Tab1_3)
        self.point_proj_comboBox_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.point_proj_comboBox_2.setObjectName(_fromUtf8("point_proj_comboBox_2"))
        self.point_proj_comboBox_2.addItem(_fromUtf8(""))
        self.point_proj_comboBox_2.addItem(_fromUtf8(""))
        self.point_proj_comboBox_2.addItem(_fromUtf8(""))
        self.point_proj_comboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.point_proj_comboBox_2)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.button_4points_bezier = QtGui.QPushButton(self.Wire_Tab1_3)
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_bezierCubic2nodes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_4points_bezier.setIcon(icon49)
        self.button_4points_bezier.setIconSize(QtCore.QSize(32, 32))
        self.button_4points_bezier.setObjectName(_fromUtf8("button_4points_bezier"))
        self.gridLayout_7.addWidget(self.button_4points_bezier, 2, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 588, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem7, 3, 0, 1, 1)
        self.tabWidget_8.addTab(self.Wire_Tab1_3, _fromUtf8(""))
        self.Wire_Tab1_4 = QtGui.QWidget()
        self.Wire_Tab1_4.setObjectName(_fromUtf8("Wire_Tab1_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Wire_Tab1_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.button_curves_and_surfaces = QtGui.QToolButton(self.Wire_Tab1_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_curves_and_surfaces.sizePolicy().hasHeightForWidth())
        self.button_curves_and_surfaces.setSizePolicy(sizePolicy)
        self.button_curves_and_surfaces.setObjectName(_fromUtf8("button_curves_and_surfaces"))
        self.gridLayout_3.addWidget(self.button_curves_and_surfaces, 0, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 1, 0, 1, 1)
        self.tabWidget_8.addTab(self.Wire_Tab1_4, _fromUtf8(""))
        self.gridLayout_74.addWidget(self.tabWidget_8, 0, 0, 1, 1)
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_wire.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_7.addTab(self.Wire_Tab, icon50, _fromUtf8(""))
        self.Circle_Tab = QtGui.QWidget()
        self.Circle_Tab.setObjectName(_fromUtf8("Circle_Tab"))
        self.gridLayout = QtGui.QGridLayout(self.Circle_Tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_66 = QtGui.QHBoxLayout()
        self.horizontalLayout_66.setObjectName(_fromUtf8("horizontalLayout_66"))
        self.button_linecenter_circle = QtGui.QPushButton(self.Circle_Tab)
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_lineCenterCircle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_linecenter_circle.setIcon(icon51)
        self.button_linecenter_circle.setIconSize(QtCore.QSize(32, 32))
        self.button_linecenter_circle.setObjectName(_fromUtf8("button_linecenter_circle"))
        self.horizontalLayout_66.addWidget(self.button_linecenter_circle)
        self.radius_circle = QtGui.QLineEdit(self.Circle_Tab)
        self.radius_circle.setMinimumSize(QtCore.QSize(40, 0))
        self.radius_circle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.radius_circle.setObjectName(_fromUtf8("radius_circle"))
        self.horizontalLayout_66.addWidget(self.radius_circle)
        self.gridLayout.addLayout(self.horizontalLayout_66, 0, 0, 1, 1)
        self.button_linepoint_circle = QtGui.QPushButton(self.Circle_Tab)
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePointCircle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_linepoint_circle.setIcon(icon52)
        self.button_linepoint_circle.setIconSize(QtCore.QSize(32, 32))
        self.button_linepoint_circle.setObjectName(_fromUtf8("button_linepoint_circle"))
        self.gridLayout.addWidget(self.button_linepoint_circle, 1, 0, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 7, 0, 1, 1)
        self.button_3points_ellipse = QtGui.QPushButton(self.Circle_Tab)
        icon53 = QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_3pointsEllipse.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_3points_ellipse.setIcon(icon53)
        self.button_3points_ellipse.setIconSize(QtCore.QSize(32, 32))
        self.button_3points_ellipse.setObjectName(_fromUtf8("button_3points_ellipse"))
        self.gridLayout.addWidget(self.button_3points_ellipse, 4, 0, 1, 1)
        self.button_circle_to_sketch = QtGui.QPushButton(self.Circle_Tab)
        self.button_circle_to_sketch.setIcon(icon23)
        self.button_circle_to_sketch.setIconSize(QtCore.QSize(32, 32))
        self.button_circle_to_sketch.setObjectName(_fromUtf8("button_circle_to_sketch"))
        self.gridLayout.addWidget(self.button_circle_to_sketch, 8, 0, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 121, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 9, 0, 1, 1)
        self.button_3points_arc = QtGui.QPushButton(self.Circle_Tab)
        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_3pointsArc.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_3points_arc.setIcon(icon54)
        self.button_3points_arc.setIconSize(QtCore.QSize(32, 32))
        self.button_3points_arc.setObjectName(_fromUtf8("button_3points_arc"))
        self.gridLayout.addWidget(self.button_3points_arc, 5, 0, 1, 1)
        self.button_3points_circle = QtGui.QPushButton(self.Circle_Tab)
        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_3pointsCircle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_3points_circle.setIcon(icon55)
        self.button_3points_circle.setIconSize(QtCore.QSize(32, 32))
        self.button_3points_circle.setObjectName(_fromUtf8("button_3points_circle"))
        self.gridLayout.addWidget(self.button_3points_circle, 2, 0, 1, 1)
        self.horizontalLayout_67 = QtGui.QHBoxLayout()
        self.horizontalLayout_67.setObjectName(_fromUtf8("horizontalLayout_67"))
        self.button_cut_circle = QtGui.QPushButton(self.Circle_Tab)
        icon56 = QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cutCircle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cut_circle.setIcon(icon56)
        self.button_cut_circle.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_circle.setObjectName(_fromUtf8("button_cut_circle"))
        self.horizontalLayout_67.addWidget(self.button_cut_circle)
        self.spin_circle_cut = QtGui.QSpinBox(self.Circle_Tab)
        self.spin_circle_cut.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_circle_cut.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_circle_cut.setMinimum(2)
        self.spin_circle_cut.setMaximum(100)
        self.spin_circle_cut.setSingleStep(1)
        self.spin_circle_cut.setObjectName(_fromUtf8("spin_circle_cut"))
        self.horizontalLayout_67.addWidget(self.spin_circle_cut)
        self.gridLayout.addLayout(self.horizontalLayout_67, 6, 0, 1, 1)
        icon57 = QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_circle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_7.addTab(self.Circle_Tab, icon57, _fromUtf8(""))
        self.Plane_Tab = QtGui.QWidget()
        self.Plane_Tab.setObjectName(_fromUtf8("Plane_Tab"))
        self.gridLayout_17 = QtGui.QGridLayout(self.Plane_Tab)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.tabWidget_3 = QtGui.QTabWidget(self.Plane_Tab)
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.Plane_Tab1_2 = QtGui.QWidget()
        self.Plane_Tab1_2.setObjectName(_fromUtf8("Plane_Tab1_2"))
        self.gridLayout_18 = QtGui.QGridLayout(self.Plane_Tab1_2)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.button_threepoints_plane = QtGui.QPushButton(self.Plane_Tab1_2)
        icon58 = QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_threePointsPlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_threepoints_plane.setIcon(icon58)
        self.button_threepoints_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_threepoints_plane.setObjectName(_fromUtf8("button_threepoints_plane"))
        self.gridLayout_18.addWidget(self.button_threepoints_plane, 0, 0, 1, 1)
        self.button_twopoints_plane = QtGui.QPushButton(self.Plane_Tab1_2)
        icon59 = QtGui.QIcon()
        icon59.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_twoPointsPlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_twopoints_plane.setIcon(icon59)
        self.button_twopoints_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_twopoints_plane.setObjectName(_fromUtf8("button_twopoints_plane"))
        self.gridLayout_18.addWidget(self.button_twopoints_plane, 1, 0, 1, 1)
        self.button_Npoints_plane = QtGui.QPushButton(self.Plane_Tab1_2)
        icon60 = QtGui.QIcon()
        icon60.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_NpointsPlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_Npoints_plane.setIcon(icon60)
        self.button_Npoints_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_Npoints_plane.setObjectName(_fromUtf8("button_Npoints_plane"))
        self.gridLayout_18.addWidget(self.button_Npoints_plane, 2, 0, 1, 1)
        self.button_axisandpoint_plane = QtGui.QPushButton(self.Plane_Tab1_2)
        icon61 = QtGui.QIcon()
        icon61.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePointPlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_axisandpoint_plane.setIcon(icon61)
        self.button_axisandpoint_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_axisandpoint_plane.setObjectName(_fromUtf8("button_axisandpoint_plane"))
        self.gridLayout_18.addWidget(self.button_axisandpoint_plane, 3, 0, 1, 1)
        self.button_axis_point_plane = QtGui.QPushButton(self.Plane_Tab1_2)
        icon62 = QtGui.QIcon()
        icon62.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePointPlane2.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_axis_point_plane.setIcon(icon62)
        self.button_axis_point_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_axis_point_plane.setObjectName(_fromUtf8("button_axis_point_plane"))
        self.gridLayout_18.addWidget(self.button_axis_point_plane, 4, 0, 1, 1)
        self.gridLayout_90 = QtGui.QGridLayout()
        self.gridLayout_90.setObjectName(_fromUtf8("gridLayout_90"))
        self.button_planeandpoint_plane = QtGui.QPushButton(self.Plane_Tab1_2)
        icon63 = QtGui.QIcon()
        icon63.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointPlanePlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_planeandpoint_plane.setIcon(icon63)
        self.button_planeandpoint_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_planeandpoint_plane.setObjectName(_fromUtf8("button_planeandpoint_plane"))
        self.gridLayout_90.addWidget(self.button_planeandpoint_plane, 0, 0, 1, 1)
        self.extension_planePointPlane = QtGui.QLineEdit(self.Plane_Tab1_2)
        self.extension_planePointPlane.setMinimumSize(QtCore.QSize(40, 0))
        self.extension_planePointPlane.setMaximumSize(QtCore.QSize(60, 16777215))
        self.extension_planePointPlane.setObjectName(_fromUtf8("extension_planePointPlane"))
        self.gridLayout_90.addWidget(self.extension_planePointPlane, 0, 1, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_90, 5, 0, 1, 1)
        self.gridLayout_89 = QtGui.QGridLayout()
        self.gridLayout_89.setObjectName(_fromUtf8("gridLayout_89"))
        self.button_planeandaxis_plane = QtGui.QPushButton(self.Plane_Tab1_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_planeandaxis_plane.sizePolicy().hasHeightForWidth())
        self.button_planeandaxis_plane.setSizePolicy(sizePolicy)
        icon64 = QtGui.QIcon()
        icon64.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_planeLinePlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_planeandaxis_plane.setIcon(icon64)
        self.button_planeandaxis_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_planeandaxis_plane.setObjectName(_fromUtf8("button_planeandaxis_plane"))
        self.gridLayout_89.addWidget(self.button_planeandaxis_plane, 0, 0, 1, 1)
        self.angle_planeandaxis_plane = QtGui.QLineEdit(self.Plane_Tab1_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_planeandaxis_plane.sizePolicy().hasHeightForWidth())
        self.angle_planeandaxis_plane.setSizePolicy(sizePolicy)
        self.angle_planeandaxis_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_planeandaxis_plane.setMaximumSize(QtCore.QSize(60, 16777215))
        self.angle_planeandaxis_plane.setObjectName(_fromUtf8("angle_planeandaxis_plane"))
        self.gridLayout_89.addWidget(self.angle_planeandaxis_plane, 0, 1, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_89, 6, 0, 1, 1)
        self.horizontalLayout_70 = QtGui.QHBoxLayout()
        self.horizontalLayout_70.setObjectName(_fromUtf8("horizontalLayout_70"))
        self.button_distPlane = QtGui.QPushButton(self.Plane_Tab1_2)
        icon65 = QtGui.QIcon()
        icon65.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_distPlanePlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_distPlane.setIcon(icon65)
        self.button_distPlane.setIconSize(QtCore.QSize(32, 32))
        self.button_distPlane.setObjectName(_fromUtf8("button_distPlane"))
        self.horizontalLayout_70.addWidget(self.button_distPlane)
        self.dist_plane = QtGui.QLineEdit(self.Plane_Tab1_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dist_plane.sizePolicy().hasHeightForWidth())
        self.dist_plane.setSizePolicy(sizePolicy)
        self.dist_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.dist_plane.setMaximumSize(QtCore.QSize(40, 16777215))
        self.dist_plane.setObjectName(_fromUtf8("dist_plane"))
        self.horizontalLayout_70.addWidget(self.dist_plane)
        self.spin_dist_plane = QtGui.QSpinBox(self.Plane_Tab1_2)
        self.spin_dist_plane.setMinimumSize(QtCore.QSize(30, 0))
        self.spin_dist_plane.setMaximumSize(QtCore.QSize(30, 16777215))
        self.spin_dist_plane.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spin_dist_plane.setKeyboardTracking(False)
        self.spin_dist_plane.setMinimum(1)
        self.spin_dist_plane.setMaximum(100)
        self.spin_dist_plane.setSingleStep(1)
        self.spin_dist_plane.setProperty("value", 1)
        self.spin_dist_plane.setObjectName(_fromUtf8("spin_dist_plane"))
        self.horizontalLayout_70.addWidget(self.spin_dist_plane)
        self.gridLayout_18.addLayout(self.horizontalLayout_70, 7, 0, 1, 1)
        self.horizontalLayout_69 = QtGui.QHBoxLayout()
        self.horizontalLayout_69.setObjectName(_fromUtf8("horizontalLayout_69"))
        self.button_face_tangent = QtGui.QPushButton(self.Plane_Tab1_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_face_tangent.sizePolicy().hasHeightForWidth())
        self.button_face_tangent.setSizePolicy(sizePolicy)
        icon66 = QtGui.QIcon()
        icon66.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_FaceTangent.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_face_tangent.setIcon(icon66)
        self.button_face_tangent.setIconSize(QtCore.QSize(32, 32))
        self.button_face_tangent.setObjectName(_fromUtf8("button_face_tangent"))
        self.horizontalLayout_69.addWidget(self.button_face_tangent)
        self.length_plane_2 = QtGui.QLineEdit(self.Plane_Tab1_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length_plane_2.sizePolicy().hasHeightForWidth())
        self.length_plane_2.setSizePolicy(sizePolicy)
        self.length_plane_2.setMinimumSize(QtCore.QSize(40, 0))
        self.length_plane_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.length_plane_2.setObjectName(_fromUtf8("length_plane_2"))
        self.horizontalLayout_69.addWidget(self.length_plane_2)
        self.width_plane_2 = QtGui.QLineEdit(self.Plane_Tab1_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_plane_2.sizePolicy().hasHeightForWidth())
        self.width_plane_2.setSizePolicy(sizePolicy)
        self.width_plane_2.setMinimumSize(QtCore.QSize(40, 0))
        self.width_plane_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.width_plane_2.setObjectName(_fromUtf8("width_plane_2"))
        self.horizontalLayout_69.addWidget(self.width_plane_2)
        self.gridLayout_18.addLayout(self.horizontalLayout_69, 8, 0, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 235, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_18.addItem(spacerItem11, 9, 0, 1, 1)
        self.tabWidget_3.addTab(self.Plane_Tab1_2, _fromUtf8(""))
        self.Plane_Tab2_2 = QtGui.QWidget()
        self.Plane_Tab2_2.setObjectName(_fromUtf8("Plane_Tab2_2"))
        self.gridLayout_36 = QtGui.QGridLayout(self.Plane_Tab2_2)
        self.gridLayout_36.setObjectName(_fromUtf8("gridLayout_36"))
        self.horizontalLayout_68 = QtGui.QHBoxLayout()
        self.horizontalLayout_68.setObjectName(_fromUtf8("horizontalLayout_68"))
        self.button_click_for_plane = QtGui.QPushButton(self.Plane_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_click_for_plane.sizePolicy().hasHeightForWidth())
        self.button_click_for_plane.setSizePolicy(sizePolicy)
        icon67 = QtGui.QIcon()
        icon67.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_clickPlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_click_for_plane.setIcon(icon67)
        self.button_click_for_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_click_for_plane.setObjectName(_fromUtf8("button_click_for_plane"))
        self.horizontalLayout_68.addWidget(self.button_click_for_plane)
        self.length_plane = QtGui.QLineEdit(self.Plane_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length_plane.sizePolicy().hasHeightForWidth())
        self.length_plane.setSizePolicy(sizePolicy)
        self.length_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.length_plane.setMaximumSize(QtCore.QSize(50, 16777215))
        self.length_plane.setObjectName(_fromUtf8("length_plane"))
        self.horizontalLayout_68.addWidget(self.length_plane)
        self.width_plane = QtGui.QLineEdit(self.Plane_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_plane.sizePolicy().hasHeightForWidth())
        self.width_plane.setSizePolicy(sizePolicy)
        self.width_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.width_plane.setMaximumSize(QtCore.QSize(50, 16777215))
        self.width_plane.setObjectName(_fromUtf8("width_plane"))
        self.horizontalLayout_68.addWidget(self.width_plane)
        self.gridLayout_36.addLayout(self.horizontalLayout_68, 0, 0, 1, 1)
        self.horizontalLayout_71 = QtGui.QHBoxLayout()
        self.horizontalLayout_71.setObjectName(_fromUtf8("horizontalLayout_71"))
        self.button_extension_plane = QtGui.QPushButton(self.Plane_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_extension_plane.sizePolicy().hasHeightForWidth())
        self.button_extension_plane.setSizePolicy(sizePolicy)
        icon68 = QtGui.QIcon()
        icon68.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_enlargePlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_extension_plane.setIcon(icon68)
        self.button_extension_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_extension_plane.setObjectName(_fromUtf8("button_extension_plane"))
        self.horizontalLayout_71.addWidget(self.button_extension_plane)
        self.extension_plane = QtGui.QLineEdit(self.Plane_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extension_plane.sizePolicy().hasHeightForWidth())
        self.extension_plane.setSizePolicy(sizePolicy)
        self.extension_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.extension_plane.setMaximumSize(QtCore.QSize(50, 16777215))
        self.extension_plane.setObjectName(_fromUtf8("extension_plane"))
        self.horizontalLayout_71.addWidget(self.extension_plane)
        self.gridLayout_36.addLayout(self.horizontalLayout_71, 1, 0, 1, 1)
        self.button_object_center_planes = QtGui.QPushButton(self.Plane_Tab2_2)
        icon69 = QtGui.QIcon()
        icon69.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerObjectsPlanes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_center_planes.setIcon(icon69)
        self.button_object_center_planes.setIconSize(QtCore.QSize(32, 32))
        self.button_object_center_planes.setObjectName(_fromUtf8("button_object_center_planes"))
        self.gridLayout_36.addWidget(self.button_object_center_planes, 2, 0, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(20, 527, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_36.addItem(spacerItem12, 3, 0, 1, 1)
        self.tabWidget_3.addTab(self.Plane_Tab2_2, _fromUtf8(""))
        self.gridLayout_17.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        icon70 = QtGui.QIcon()
        icon70.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_plane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_7.addTab(self.Plane_Tab, icon70, _fromUtf8(""))
        self.Sweep_Tab = QtGui.QWidget()
        self.Sweep_Tab.setObjectName(_fromUtf8("Sweep_Tab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.Sweep_Tab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.frame_9 = QtGui.QFrame(self.Sweep_Tab)
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setLineWidth(3)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.gridLayout_86 = QtGui.QGridLayout(self.frame_9)
        self.gridLayout_86.setObjectName(_fromUtf8("gridLayout_86"))
        self.gridLayout_87 = QtGui.QGridLayout()
        self.gridLayout_87.setObjectName(_fromUtf8("gridLayout_87"))
        self.checkBox_allsubselect = QtGui.QCheckBox(self.frame_9)
        self.checkBox_allsubselect.setChecked(True)
        self.checkBox_allsubselect.setObjectName(_fromUtf8("checkBox_allsubselect"))
        self.gridLayout_87.addWidget(self.checkBox_allsubselect, 2, 0, 1, 1)
        self.transition_comboBox = QtGui.QComboBox(self.frame_9)
        self.transition_comboBox.setObjectName(_fromUtf8("transition_comboBox"))
        self.transition_comboBox.addItem(_fromUtf8(""))
        self.transition_comboBox.addItem(_fromUtf8(""))
        self.transition_comboBox.addItem(_fromUtf8(""))
        self.gridLayout_87.addWidget(self.transition_comboBox, 2, 1, 1, 1)
        self.checkBox_solid = QtGui.QCheckBox(self.frame_9)
        self.checkBox_solid.setMinimumSize(QtCore.QSize(9, 0))
        self.checkBox_solid.setMaximumSize(QtCore.QSize(60, 16777215))
        self.checkBox_solid.setChecked(True)
        self.checkBox_solid.setObjectName(_fromUtf8("checkBox_solid"))
        self.gridLayout_87.addWidget(self.checkBox_solid, 1, 0, 1, 1)
        self.radioButton_Frenet = QtGui.QRadioButton(self.frame_9)
        self.radioButton_Frenet.setChecked(True)
        self.radioButton_Frenet.setAutoExclusive(False)
        self.radioButton_Frenet.setObjectName(_fromUtf8("radioButton_Frenet"))
        self.gridLayout_87.addWidget(self.radioButton_Frenet, 1, 1, 1, 1)
        self.gridLayout_86.addLayout(self.gridLayout_87, 0, 0, 1, 1)
        self.button_sweep = QtGui.QPushButton(self.frame_9)
        icon71 = QtGui.QIcon()
        icon71.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_Sweep.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sweep.setIcon(icon71)
        self.button_sweep.setIconSize(QtCore.QSize(32, 32))
        self.button_sweep.setObjectName(_fromUtf8("button_sweep"))
        self.gridLayout_86.addWidget(self.button_sweep, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_9, 0, 0, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem13, 3, 0, 1, 1)
        self.button_beam = QtGui.QPushButton(self.Sweep_Tab)
        icon72 = QtGui.QIcon()
        icon72.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_Beam.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_beam.setIcon(icon72)
        self.button_beam.setIconSize(QtCore.QSize(32, 32))
        self.button_beam.setObjectName(_fromUtf8("button_beam"))
        self.gridLayout_6.addWidget(self.button_beam, 1, 0, 1, 1)
        self.button_beam_cut_miter = QtGui.QPushButton(self.Sweep_Tab)
        icon73 = QtGui.QIcon()
        icon73.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_BeamMiterCut.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_beam_cut_miter.setIcon(icon73)
        self.button_beam_cut_miter.setIconSize(QtCore.QSize(32, 32))
        self.button_beam_cut_miter.setObjectName(_fromUtf8("button_beam_cut_miter"))
        self.gridLayout_6.addWidget(self.button_beam_cut_miter, 2, 0, 1, 1)
        self.tabWidget_7.addTab(self.Sweep_Tab, icon72, _fromUtf8(""))
        self.Objects_Tab2_2 = QtGui.QWidget()
        self.Objects_Tab2_2.setEnabled(True)
        self.Objects_Tab2_2.setMinimumSize(QtCore.QSize(0, 0))
        self.Objects_Tab2_2.setObjectName(_fromUtf8("Objects_Tab2_2"))
        self.gridLayout_23 = QtGui.QGridLayout(self.Objects_Tab2_2)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.button_boundingboxes = QtGui.QPushButton(self.Objects_Tab2_2)
        self.button_boundingboxes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon74 = QtGui.QIcon()
        icon74.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_boundingBoxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_boundingboxes.setIcon(icon74)
        self.button_boundingboxes.setIconSize(QtCore.QSize(32, 32))
        self.button_boundingboxes.setObjectName(_fromUtf8("button_boundingboxes"))
        self.verticalLayout_4.addWidget(self.button_boundingboxes)
        self.button_boundingbox = QtGui.QPushButton(self.Objects_Tab2_2)
        self.button_boundingbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon75 = QtGui.QIcon()
        icon75.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_boundingBox.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_boundingbox.setIcon(icon75)
        self.button_boundingbox.setIconSize(QtCore.QSize(32, 32))
        self.button_boundingbox.setObjectName(_fromUtf8("button_boundingbox"))
        self.verticalLayout_4.addWidget(self.button_boundingbox)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox_volumBB = QtGui.QCheckBox(self.Objects_Tab2_2)
        self.checkBox_volumBB.setMaximumSize(QtCore.QSize(60, 16777215))
        self.checkBox_volumBB.setObjectName(_fromUtf8("checkBox_volumBB"))
        self.verticalLayout_2.addWidget(self.checkBox_volumBB)
        self.checkBox_infoBB = QtGui.QCheckBox(self.Objects_Tab2_2)
        self.checkBox_infoBB.setMaximumSize(QtCore.QSize(60, 16777215))
        self.checkBox_infoBB.setObjectName(_fromUtf8("checkBox_infoBB"))
        self.verticalLayout_2.addWidget(self.checkBox_infoBB)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.Objects_Tab2_2)
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setLineWidth(4)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_23.addWidget(self.line_2, 1, 0, 1, 1)
        self.gridLayout_93 = QtGui.QGridLayout()
        self.gridLayout_93.setObjectName(_fromUtf8("gridLayout_93"))
        self.button_cylinder_create = QtGui.QPushButton(self.Objects_Tab2_2)
        icon76 = QtGui.QIcon()
        icon76.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cylinder.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cylinder_create.setIcon(icon76)
        self.button_cylinder_create.setIconSize(QtCore.QSize(32, 32))
        self.button_cylinder_create.setObjectName(_fromUtf8("button_cylinder_create"))
        self.gridLayout_93.addWidget(self.button_cylinder_create, 0, 0, 1, 1)
        self.diameter_cylinder = QtGui.QLineEdit(self.Objects_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter_cylinder.sizePolicy().hasHeightForWidth())
        self.diameter_cylinder.setSizePolicy(sizePolicy)
        self.diameter_cylinder.setMinimumSize(QtCore.QSize(50, 0))
        self.diameter_cylinder.setMaximumSize(QtCore.QSize(60, 16777215))
        self.diameter_cylinder.setObjectName(_fromUtf8("diameter_cylinder"))
        self.gridLayout_93.addWidget(self.diameter_cylinder, 0, 1, 1, 1)
        self.length_cylinder = QtGui.QLineEdit(self.Objects_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length_cylinder.sizePolicy().hasHeightForWidth())
        self.length_cylinder.setSizePolicy(sizePolicy)
        self.length_cylinder.setMinimumSize(QtCore.QSize(50, 0))
        self.length_cylinder.setMaximumSize(QtCore.QSize(60, 16777215))
        self.length_cylinder.setObjectName(_fromUtf8("length_cylinder"))
        self.gridLayout_93.addWidget(self.length_cylinder, 0, 2, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_93, 2, 0, 1, 1)
        self.horizontalLayout_73 = QtGui.QHBoxLayout()
        self.horizontalLayout_73.setObjectName(_fromUtf8("horizontalLayout_73"))
        self.button_cube_create = QtGui.QPushButton(self.Objects_Tab2_2)
        icon77 = QtGui.QIcon()
        icon77.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cube.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cube_create.setIcon(icon77)
        self.button_cube_create.setIconSize(QtCore.QSize(32, 32))
        self.button_cube_create.setObjectName(_fromUtf8("button_cube_create"))
        self.horizontalLayout_73.addWidget(self.button_cube_create)
        self.section_cube = QtGui.QLineEdit(self.Objects_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.section_cube.sizePolicy().hasHeightForWidth())
        self.section_cube.setSizePolicy(sizePolicy)
        self.section_cube.setMinimumSize(QtCore.QSize(50, 0))
        self.section_cube.setMaximumSize(QtCore.QSize(60, 16777215))
        self.section_cube.setObjectName(_fromUtf8("section_cube"))
        self.horizontalLayout_73.addWidget(self.section_cube)
        self.height_cube = QtGui.QLineEdit(self.Objects_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_cube.sizePolicy().hasHeightForWidth())
        self.height_cube.setSizePolicy(sizePolicy)
        self.height_cube.setMinimumSize(QtCore.QSize(50, 0))
        self.height_cube.setMaximumSize(QtCore.QSize(60, 16777215))
        self.height_cube.setObjectName(_fromUtf8("height_cube"))
        self.horizontalLayout_73.addWidget(self.height_cube)
        self.gridLayout_23.addLayout(self.horizontalLayout_73, 3, 0, 1, 1)
        self.horizontalLayout_74 = QtGui.QHBoxLayout()
        self.horizontalLayout_74.setObjectName(_fromUtf8("horizontalLayout_74"))
        self.button_sphere_create = QtGui.QPushButton(self.Objects_Tab2_2)
        icon78 = QtGui.QIcon()
        icon78.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_sphere.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sphere_create.setIcon(icon78)
        self.button_sphere_create.setIconSize(QtCore.QSize(32, 32))
        self.button_sphere_create.setObjectName(_fromUtf8("button_sphere_create"))
        self.horizontalLayout_74.addWidget(self.button_sphere_create)
        self.diameter_sphere = QtGui.QLineEdit(self.Objects_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter_sphere.sizePolicy().hasHeightForWidth())
        self.diameter_sphere.setSizePolicy(sizePolicy)
        self.diameter_sphere.setMinimumSize(QtCore.QSize(50, 0))
        self.diameter_sphere.setMaximumSize(QtCore.QSize(60, 16777215))
        self.diameter_sphere.setObjectName(_fromUtf8("diameter_sphere"))
        self.horizontalLayout_74.addWidget(self.diameter_sphere)
        self.gridLayout_23.addLayout(self.horizontalLayout_74, 4, 0, 1, 1)
        self.horizontalLayout_77 = QtGui.QHBoxLayout()
        self.horizontalLayout_77.setObjectName(_fromUtf8("horizontalLayout_77"))
        self.button_dome_create = QtGui.QPushButton(self.Objects_Tab2_2)
        icon79 = QtGui.QIcon()
        icon79.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_dome.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_dome_create.setIcon(icon79)
        self.button_dome_create.setIconSize(QtCore.QSize(32, 32))
        self.button_dome_create.setObjectName(_fromUtf8("button_dome_create"))
        self.horizontalLayout_77.addWidget(self.button_dome_create)
        self.spin_frequency_dome = QtGui.QSpinBox(self.Objects_Tab2_2)
        self.spin_frequency_dome.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_frequency_dome.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_frequency_dome.setMinimum(1)
        self.spin_frequency_dome.setMaximum(20)
        self.spin_frequency_dome.setSingleStep(1)
        self.spin_frequency_dome.setProperty("value", 2)
        self.spin_frequency_dome.setObjectName(_fromUtf8("spin_frequency_dome"))
        self.horizontalLayout_77.addWidget(self.spin_frequency_dome)
        self.diameter_dome = QtGui.QLineEdit(self.Objects_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter_dome.sizePolicy().hasHeightForWidth())
        self.diameter_dome.setSizePolicy(sizePolicy)
        self.diameter_dome.setMinimumSize(QtCore.QSize(50, 0))
        self.diameter_dome.setMaximumSize(QtCore.QSize(60, 16777215))
        self.diameter_dome.setObjectName(_fromUtf8("diameter_dome"))
        self.horizontalLayout_77.addWidget(self.diameter_dome)
        self.gridLayout_23.addLayout(self.horizontalLayout_77, 5, 0, 1, 1)
        self.horizontalLayout_75 = QtGui.QHBoxLayout()
        self.horizontalLayout_75.setObjectName(_fromUtf8("horizontalLayout_75"))
        self.button_letter = QtGui.QPushButton(self.Objects_Tab2_2)
        icon80 = QtGui.QIcon()
        icon80.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointText.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_letter.setIcon(icon80)
        self.button_letter.setIconSize(QtCore.QSize(32, 32))
        self.button_letter.setObjectName(_fromUtf8("button_letter"))
        self.horizontalLayout_75.addWidget(self.button_letter)
        self.letter = QtGui.QLineEdit(self.Objects_Tab2_2)
        self.letter.setMaximumSize(QtCore.QSize(70, 16777215))
        self.letter.setObjectName(_fromUtf8("letter"))
        self.horizontalLayout_75.addWidget(self.letter)
        self.size_letter = QtGui.QLineEdit(self.Objects_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.size_letter.sizePolicy().hasHeightForWidth())
        self.size_letter.setSizePolicy(sizePolicy)
        self.size_letter.setMinimumSize(QtCore.QSize(50, 0))
        self.size_letter.setMaximumSize(QtCore.QSize(50, 16777215))
        self.size_letter.setObjectName(_fromUtf8("size_letter"))
        self.horizontalLayout_75.addWidget(self.size_letter)
        self.gridLayout_23.addLayout(self.horizontalLayout_75, 6, 0, 1, 1)
        self.horizontalLayout_76 = QtGui.QHBoxLayout()
        self.horizontalLayout_76.setObjectName(_fromUtf8("horizontalLayout_76"))
        self.button_revolve = QtGui.QPushButton(self.Objects_Tab2_2)
        icon81 = QtGui.QIcon()
        icon81.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_Revolve.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_revolve.setIcon(icon81)
        self.button_revolve.setIconSize(QtCore.QSize(32, 32))
        self.button_revolve.setObjectName(_fromUtf8("button_revolve"))
        self.horizontalLayout_76.addWidget(self.button_revolve)
        self.angle_revolve = QtGui.QLineEdit(self.Objects_Tab2_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_revolve.sizePolicy().hasHeightForWidth())
        self.angle_revolve.setSizePolicy(sizePolicy)
        self.angle_revolve.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_revolve.setMaximumSize(QtCore.QSize(40, 16777215))
        self.angle_revolve.setObjectName(_fromUtf8("angle_revolve"))
        self.horizontalLayout_76.addWidget(self.angle_revolve)
        self.gridLayout_23.addLayout(self.horizontalLayout_76, 7, 0, 1, 1)
        self.button_copy_objects = QtGui.QPushButton(self.Objects_Tab2_2)
        icon82 = QtGui.QIcon()
        icon82.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectCopy.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_copy_objects.setIcon(icon82)
        self.button_copy_objects.setIconSize(QtCore.QSize(32, 32))
        self.button_copy_objects.setObjectName(_fromUtf8("button_copy_objects"))
        self.gridLayout_23.addWidget(self.button_copy_objects, 8, 0, 1, 1)
        self.button_common = QtGui.QPushButton(self.Objects_Tab2_2)
        icon83 = QtGui.QIcon()
        icon83.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_Common.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_common.setIcon(icon83)
        self.button_common.setIconSize(QtCore.QSize(32, 32))
        self.button_common.setObjectName(_fromUtf8("button_common"))
        self.gridLayout_23.addWidget(self.button_common, 9, 0, 1, 1)
        self.button_difference = QtGui.QPushButton(self.Objects_Tab2_2)
        icon84 = QtGui.QIcon()
        icon84.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_Difference.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_difference.setIcon(icon84)
        self.button_difference.setIconSize(QtCore.QSize(32, 32))
        self.button_difference.setObjectName(_fromUtf8("button_difference"))
        self.gridLayout_23.addWidget(self.button_difference, 10, 0, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(17, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem14, 11, 0, 1, 1)
        icon85 = QtGui.QIcon()
        icon85.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_box.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_7.addTab(self.Objects_Tab2_2, icon85, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.button_rotate_image = QtGui.QPushButton(self.tab_2)
        self.button_rotate_image.setObjectName(_fromUtf8("button_rotate_image"))
        self.horizontalLayout_3.addWidget(self.button_rotate_image)
        self.Image_comboBox_axis_rotate = QtGui.QComboBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_comboBox_axis_rotate.sizePolicy().hasHeightForWidth())
        self.Image_comboBox_axis_rotate.setSizePolicy(sizePolicy)
        self.Image_comboBox_axis_rotate.setMinimumSize(QtCore.QSize(40, 0))
        self.Image_comboBox_axis_rotate.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Image_comboBox_axis_rotate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Image_comboBox_axis_rotate.setObjectName(_fromUtf8("Image_comboBox_axis_rotate"))
        self.Image_comboBox_axis_rotate.addItem(_fromUtf8(""))
        self.Image_comboBox_axis_rotate.addItem(_fromUtf8(""))
        self.Image_comboBox_axis_rotate.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.Image_comboBox_axis_rotate)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.button_scale_image = QtGui.QPushButton(self.tab_2)
        icon86 = QtGui.QIcon()
        icon86.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_ImageScale.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_scale_image.setIcon(icon86)
        self.button_scale_image.setIconSize(QtCore.QSize(32, 32))
        self.button_scale_image.setObjectName(_fromUtf8("button_scale_image"))
        self.horizontalLayout_4.addWidget(self.button_scale_image)
        self.Image_comboBox_axis_scale = QtGui.QComboBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_comboBox_axis_scale.sizePolicy().hasHeightForWidth())
        self.Image_comboBox_axis_scale.setSizePolicy(sizePolicy)
        self.Image_comboBox_axis_scale.setMinimumSize(QtCore.QSize(40, 0))
        self.Image_comboBox_axis_scale.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Image_comboBox_axis_scale.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Image_comboBox_axis_scale.setObjectName(_fromUtf8("Image_comboBox_axis_scale"))
        self.Image_comboBox_axis_scale.addItem(_fromUtf8(""))
        self.Image_comboBox_axis_scale.addItem(_fromUtf8(""))
        self.Image_comboBox_axis_scale.addItem(_fromUtf8(""))
        self.Image_comboBox_axis_scale.addItem(_fromUtf8(""))
        self.Image_comboBox_axis_scale.addItem(_fromUtf8(""))
        self.Image_comboBox_axis_scale.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.Image_comboBox_axis_scale)
        self.length_image = QtGui.QLineEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length_image.sizePolicy().hasHeightForWidth())
        self.length_image.setSizePolicy(sizePolicy)
        self.length_image.setMinimumSize(QtCore.QSize(60, 0))
        self.length_image.setMaximumSize(QtCore.QSize(50, 16777215))
        self.length_image.setObjectName(_fromUtf8("length_image"))
        self.horizontalLayout_4.addWidget(self.length_image)
        self.gridLayout_8.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(20, 650, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem15, 2, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_2, _fromUtf8(""))
        self.Modif_Tab_2 = QtGui.QWidget()
        self.Modif_Tab_2.setObjectName(_fromUtf8("Modif_Tab_2"))
        self.gridLayout_94 = QtGui.QGridLayout(self.Modif_Tab_2)
        self.gridLayout_94.setObjectName(_fromUtf8("gridLayout_94"))
        self.tabWidget_9 = QtGui.QTabWidget(self.Modif_Tab_2)
        self.tabWidget_9.setObjectName(_fromUtf8("tabWidget_9"))
        self.align_tab_2 = QtGui.QWidget()
        self.align_tab_2.setObjectName(_fromUtf8("align_tab_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.align_tab_2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.button_alignface2view = QtGui.QPushButton(self.align_tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_alignface2view.sizePolicy().hasHeightForWidth())
        self.button_alignface2view.setSizePolicy(sizePolicy)
        self.button_alignface2view.setMaximumSize(QtCore.QSize(220, 16777215))
        icon87 = QtGui.QIcon()
        icon87.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_viewAlignFace.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_alignface2view.setIcon(icon87)
        self.button_alignface2view.setIconSize(QtCore.QSize(32, 32))
        self.button_alignface2view.setObjectName(_fromUtf8("button_alignface2view"))
        self.gridLayout_9.addWidget(self.button_alignface2view, 0, 0, 1, 1)
        self.horizontalLayout_78 = QtGui.QHBoxLayout()
        self.horizontalLayout_78.setObjectName(_fromUtf8("horizontalLayout_78"))
        self.button_align_faces = QtGui.QPushButton(self.align_tab_2)
        self.button_align_faces.setMaximumSize(QtCore.QSize(220, 16777215))
        icon88 = QtGui.QIcon()
        icon88.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectAlignFaces.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_align_faces.setIcon(icon88)
        self.button_align_faces.setIconSize(QtCore.QSize(32, 32))
        self.button_align_faces.setObjectName(_fromUtf8("button_align_faces"))
        self.horizontalLayout_78.addWidget(self.button_align_faces)
        self.angle_align_faces = QtGui.QLineEdit(self.align_tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_align_faces.sizePolicy().hasHeightForWidth())
        self.angle_align_faces.setSizePolicy(sizePolicy)
        self.angle_align_faces.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_align_faces.setMaximumSize(QtCore.QSize(50, 16777215))
        self.angle_align_faces.setObjectName(_fromUtf8("angle_align_faces"))
        self.horizontalLayout_78.addWidget(self.angle_align_faces)
        self.gridLayout_9.addLayout(self.horizontalLayout_78, 1, 0, 1, 1)
        self.horizontalLayout_79 = QtGui.QHBoxLayout()
        self.horizontalLayout_79.setObjectName(_fromUtf8("horizontalLayout_79"))
        self.button_align_edges = QtGui.QPushButton(self.align_tab_2)
        self.button_align_edges.setMaximumSize(QtCore.QSize(220, 16777215))
        icon89 = QtGui.QIcon()
        icon89.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectAlignAxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_align_edges.setIcon(icon89)
        self.button_align_edges.setIconSize(QtCore.QSize(32, 32))
        self.button_align_edges.setObjectName(_fromUtf8("button_align_edges"))
        self.horizontalLayout_79.addWidget(self.button_align_edges)
        self.angle_align_edges = QtGui.QLineEdit(self.align_tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_align_edges.sizePolicy().hasHeightForWidth())
        self.angle_align_edges.setSizePolicy(sizePolicy)
        self.angle_align_edges.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_align_edges.setMaximumSize(QtCore.QSize(50, 16777215))
        self.angle_align_edges.setObjectName(_fromUtf8("angle_align_edges"))
        self.horizontalLayout_79.addWidget(self.angle_align_edges)
        self.gridLayout_9.addLayout(self.horizontalLayout_79, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.button_align_main_axis = QtGui.QPushButton(self.align_tab_2)
        icon90 = QtGui.QIcon()
        icon90.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectAlignMainAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_align_main_axis.setIcon(icon90)
        self.button_align_main_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_align_main_axis.setObjectName(_fromUtf8("button_align_main_axis"))
        self.horizontalLayout_2.addWidget(self.button_align_main_axis)
        self.angle_align_main_axis = QtGui.QLineEdit(self.align_tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_align_main_axis.sizePolicy().hasHeightForWidth())
        self.angle_align_main_axis.setSizePolicy(sizePolicy)
        self.angle_align_main_axis.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_align_main_axis.setMaximumSize(QtCore.QSize(50, 16777215))
        self.angle_align_main_axis.setObjectName(_fromUtf8("angle_align_main_axis"))
        self.horizontalLayout_2.addWidget(self.angle_align_main_axis)
        self.gridLayout_9.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.button_joint_points = QtGui.QPushButton(self.align_tab_2)
        icon91 = QtGui.QIcon()
        icon91.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectJointPoints.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_joint_points.setIcon(icon91)
        self.button_joint_points.setIconSize(QtCore.QSize(32, 32))
        self.button_joint_points.setObjectName(_fromUtf8("button_joint_points"))
        self.gridLayout_9.addWidget(self.button_joint_points, 4, 0, 1, 1)
        self.button_joint_faces = QtGui.QPushButton(self.align_tab_2)
        icon92 = QtGui.QIcon()
        icon92.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectJointFaces.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_joint_faces.setIcon(icon92)
        self.button_joint_faces.setIconSize(QtCore.QSize(32, 32))
        self.button_joint_faces.setObjectName(_fromUtf8("button_joint_faces"))
        self.gridLayout_9.addWidget(self.button_joint_faces, 5, 0, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem16, 6, 0, 1, 1)
        self.tabWidget_9.addTab(self.align_tab_2, _fromUtf8(""))
        self.cut_tab_2 = QtGui.QWidget()
        self.cut_tab_2.setObjectName(_fromUtf8("cut_tab_2"))
        self.gridLayout_96 = QtGui.QGridLayout(self.cut_tab_2)
        self.gridLayout_96.setObjectName(_fromUtf8("gridLayout_96"))
        self.frame_10 = QtGui.QFrame(self.cut_tab_2)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.gridLayout_97 = QtGui.QGridLayout(self.frame_10)
        self.gridLayout_97.setObjectName(_fromUtf8("gridLayout_97"))
        self.groupBox_20 = QtGui.QGroupBox(self.frame_10)
        self.groupBox_20.setObjectName(_fromUtf8("groupBox_20"))
        self.gridLayout_98 = QtGui.QGridLayout(self.groupBox_20)
        self.gridLayout_98.setObjectName(_fromUtf8("gridLayout_98"))
        self.gridLayout_99 = QtGui.QGridLayout()
        self.gridLayout_99.setObjectName(_fromUtf8("gridLayout_99"))
        self.button_cut_select_object = QtGui.QPushButton(self.groupBox_20)
        self.button_cut_select_object.setMinimumSize(QtCore.QSize(130, 31))
        self.button_cut_select_object.setMaximumSize(QtCore.QSize(250, 40))
        self.button_cut_select_object.setObjectName(_fromUtf8("button_cut_select_object"))
        self.gridLayout_99.addWidget(self.button_cut_select_object, 0, 0, 1, 1)
        self.info_cut_select_object = QtGui.QLineEdit(self.groupBox_20)
        self.info_cut_select_object.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_cut_select_object.sizePolicy().hasHeightForWidth())
        self.info_cut_select_object.setSizePolicy(sizePolicy)
        self.info_cut_select_object.setReadOnly(True)
        self.info_cut_select_object.setObjectName(_fromUtf8("info_cut_select_object"))
        self.gridLayout_99.addWidget(self.info_cut_select_object, 1, 0, 1, 1)
        self.button_cut_select_line = QtGui.QPushButton(self.groupBox_20)
        self.button_cut_select_line.setEnabled(False)
        self.button_cut_select_line.setMinimumSize(QtCore.QSize(130, 31))
        self.button_cut_select_line.setMaximumSize(QtCore.QSize(250, 40))
        self.button_cut_select_line.setObjectName(_fromUtf8("button_cut_select_line"))
        self.gridLayout_99.addWidget(self.button_cut_select_line, 2, 0, 1, 1)
        self.info_cut_select_axis = QtGui.QLineEdit(self.groupBox_20)
        self.info_cut_select_axis.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_cut_select_axis.sizePolicy().hasHeightForWidth())
        self.info_cut_select_axis.setSizePolicy(sizePolicy)
        self.info_cut_select_axis.setReadOnly(True)
        self.info_cut_select_axis.setObjectName(_fromUtf8("info_cut_select_axis"))
        self.gridLayout_99.addWidget(self.info_cut_select_axis, 3, 0, 1, 1)
        self.button_cut_select_plane = QtGui.QPushButton(self.groupBox_20)
        self.button_cut_select_plane.setEnabled(False)
        self.button_cut_select_plane.setMinimumSize(QtCore.QSize(130, 31))
        self.button_cut_select_plane.setMaximumSize(QtCore.QSize(250, 40))
        self.button_cut_select_plane.setObjectName(_fromUtf8("button_cut_select_plane"))
        self.gridLayout_99.addWidget(self.button_cut_select_plane, 4, 0, 1, 1)
        self.info_cut_select_plane = QtGui.QLineEdit(self.groupBox_20)
        self.info_cut_select_plane.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_cut_select_plane.sizePolicy().hasHeightForWidth())
        self.info_cut_select_plane.setSizePolicy(sizePolicy)
        self.info_cut_select_plane.setReadOnly(True)
        self.info_cut_select_plane.setObjectName(_fromUtf8("info_cut_select_plane"))
        self.gridLayout_99.addWidget(self.info_cut_select_plane, 5, 0, 1, 1)
        self.gridLayout_98.addLayout(self.gridLayout_99, 0, 0, 1, 1)
        self.gridLayout_100 = QtGui.QGridLayout()
        self.gridLayout_100.setObjectName(_fromUtf8("gridLayout_100"))
        self.gridLayout_101 = QtGui.QGridLayout()
        self.gridLayout_101.setObjectName(_fromUtf8("gridLayout_101"))
        self.label_angle_3 = QtGui.QLabel(self.groupBox_20)
        self.label_angle_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_angle_3.setObjectName(_fromUtf8("label_angle_3"))
        self.gridLayout_101.addWidget(self.label_angle_3, 0, 0, 1, 1)
        self.angle_cut_object = QtGui.QLineEdit(self.groupBox_20)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_cut_object.sizePolicy().hasHeightForWidth())
        self.angle_cut_object.setSizePolicy(sizePolicy)
        self.angle_cut_object.setMinimumSize(QtCore.QSize(0, 0))
        self.angle_cut_object.setMaximumSize(QtCore.QSize(50, 16777215))
        self.angle_cut_object.setObjectName(_fromUtf8("angle_cut_object"))
        self.gridLayout_101.addWidget(self.angle_cut_object, 0, 1, 1, 1)
        self.gridLayout_100.addLayout(self.gridLayout_101, 0, 0, 1, 1)
        self.gridLayout_102 = QtGui.QGridLayout()
        self.gridLayout_102.setObjectName(_fromUtf8("gridLayout_102"))
        self.label_thickness_2 = QtGui.QLabel(self.groupBox_20)
        self.label_thickness_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_thickness_2.setObjectName(_fromUtf8("label_thickness_2"))
        self.gridLayout_102.addWidget(self.label_thickness_2, 0, 0, 1, 1)
        self.thickness_cut_object = QtGui.QLineEdit(self.groupBox_20)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thickness_cut_object.sizePolicy().hasHeightForWidth())
        self.thickness_cut_object.setSizePolicy(sizePolicy)
        self.thickness_cut_object.setMaximumSize(QtCore.QSize(50, 16777215))
        self.thickness_cut_object.setObjectName(_fromUtf8("thickness_cut_object"))
        self.gridLayout_102.addWidget(self.thickness_cut_object, 0, 1, 1, 1)
        self.gridLayout_100.addLayout(self.gridLayout_102, 1, 0, 1, 1)
        self.horizontalLayout_80 = QtGui.QHBoxLayout()
        self.horizontalLayout_80.setObjectName(_fromUtf8("horizontalLayout_80"))
        self.button_cut_reset = QtGui.QPushButton(self.groupBox_20)
        self.button_cut_reset.setMinimumSize(QtCore.QSize(40, 0))
        self.button_cut_reset.setMaximumSize(QtCore.QSize(60, 16777215))
        self.button_cut_reset.setObjectName(_fromUtf8("button_cut_reset"))
        self.horizontalLayout_80.addWidget(self.button_cut_reset)
        spacerItem17 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_80.addItem(spacerItem17)
        self.button_cut_apply = QtGui.QPushButton(self.groupBox_20)
        self.button_cut_apply.setEnabled(False)
        self.button_cut_apply.setMaximumSize(QtCore.QSize(50, 16777215))
        self.button_cut_apply.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_apply.setObjectName(_fromUtf8("button_cut_apply"))
        self.horizontalLayout_80.addWidget(self.button_cut_apply)
        self.gridLayout_100.addLayout(self.horizontalLayout_80, 2, 0, 1, 1)
        self.gridLayout_98.addLayout(self.gridLayout_100, 1, 0, 1, 1)
        self.gridLayout_97.addWidget(self.groupBox_20, 0, 0, 1, 1)
        self.gridLayout_96.addWidget(self.frame_10, 0, 0, 1, 1)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_96.addItem(spacerItem18, 1, 0, 1, 1)
        self.tabWidget_9.addTab(self.cut_tab_2, _fromUtf8(""))
        self.rotate_tab_2 = QtGui.QWidget()
        self.rotate_tab_2.setObjectName(_fromUtf8("rotate_tab_2"))
        self.gridLayout_103 = QtGui.QGridLayout(self.rotate_tab_2)
        self.gridLayout_103.setObjectName(_fromUtf8("gridLayout_103"))
        self.frame_11 = QtGui.QFrame(self.rotate_tab_2)
        self.frame_11.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.gridLayout_104 = QtGui.QGridLayout(self.frame_11)
        self.gridLayout_104.setObjectName(_fromUtf8("gridLayout_104"))
        self.ObjRot_button_select = QtGui.QPushButton(self.frame_11)
        self.ObjRot_button_select.setObjectName(_fromUtf8("ObjRot_button_select"))
        self.gridLayout_104.addWidget(self.ObjRot_button_select, 0, 0, 1, 1)
        self.tabWidget_10 = QtGui.QTabWidget(self.frame_11)
        self.tabWidget_10.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget_10.setObjectName(_fromUtf8("tabWidget_10"))
        self.tab_18 = QtGui.QWidget()
        self.tab_18.setObjectName(_fromUtf8("tab_18"))
        self.gridLayout_105 = QtGui.QGridLayout(self.tab_18)
        self.gridLayout_105.setObjectName(_fromUtf8("gridLayout_105"))
        self.ObjRot_comboBox_axis = QtGui.QComboBox(self.tab_18)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ObjRot_comboBox_axis.sizePolicy().hasHeightForWidth())
        self.ObjRot_comboBox_axis.setSizePolicy(sizePolicy)
        self.ObjRot_comboBox_axis.setMinimumSize(QtCore.QSize(80, 0))
        self.ObjRot_comboBox_axis.setMaximumSize(QtCore.QSize(130, 16777215))
        self.ObjRot_comboBox_axis.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ObjRot_comboBox_axis.setObjectName(_fromUtf8("ObjRot_comboBox_axis"))
        self.ObjRot_comboBox_axis.addItem(_fromUtf8(""))
        self.ObjRot_comboBox_axis.addItem(_fromUtf8(""))
        self.ObjRot_comboBox_axis.addItem(_fromUtf8(""))
        self.ObjRot_comboBox_axis.addItem(_fromUtf8(""))
        self.gridLayout_105.addWidget(self.ObjRot_comboBox_axis, 0, 0, 1, 1)
        self.ObjRot_button_select_axis = QtGui.QPushButton(self.tab_18)
        self.ObjRot_button_select_axis.setEnabled(False)
        self.ObjRot_button_select_axis.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_select_axis.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ObjRot_button_select_axis.setObjectName(_fromUtf8("ObjRot_button_select_axis"))
        self.gridLayout_105.addWidget(self.ObjRot_button_select_axis, 1, 0, 1, 1)
        icon93 = QtGui.QIcon()
        icon93.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_rotationAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_10.addTab(self.tab_18, icon93, _fromUtf8(""))
        self.tab_19 = QtGui.QWidget()
        self.tab_19.setObjectName(_fromUtf8("tab_19"))
        self.gridLayout_106 = QtGui.QGridLayout(self.tab_19)
        self.gridLayout_106.setObjectName(_fromUtf8("gridLayout_106"))
        self.ObjRot_comboBox_center = QtGui.QComboBox(self.tab_19)
        self.ObjRot_comboBox_center.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ObjRot_comboBox_center.sizePolicy().hasHeightForWidth())
        self.ObjRot_comboBox_center.setSizePolicy(sizePolicy)
        self.ObjRot_comboBox_center.setMinimumSize(QtCore.QSize(120, 0))
        self.ObjRot_comboBox_center.setMaximumSize(QtCore.QSize(130, 16777215))
        self.ObjRot_comboBox_center.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.ObjRot_comboBox_center.setObjectName(_fromUtf8("ObjRot_comboBox_center"))
        self.ObjRot_comboBox_center.addItem(_fromUtf8(""))
        self.ObjRot_comboBox_center.addItem(_fromUtf8(""))
        self.ObjRot_comboBox_center.addItem(_fromUtf8(""))
        self.ObjRot_comboBox_center.addItem(_fromUtf8(""))
        self.gridLayout_106.addWidget(self.ObjRot_comboBox_center, 0, 0, 1, 1)
        self.ObjRot_button_select_center = QtGui.QPushButton(self.tab_19)
        self.ObjRot_button_select_center.setEnabled(False)
        self.ObjRot_button_select_center.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_select_center.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ObjRot_button_select_center.setObjectName(_fromUtf8("ObjRot_button_select_center"))
        self.gridLayout_106.addWidget(self.ObjRot_button_select_center, 1, 0, 1, 1)
        icon94 = QtGui.QIcon()
        icon94.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_rotationPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_10.addTab(self.tab_19, icon94, _fromUtf8(""))
        self.gridLayout_104.addWidget(self.tabWidget_10, 1, 0, 1, 1)
        self.groupBox_21 = QtGui.QGroupBox(self.frame_11)
        self.groupBox_21.setMinimumSize(QtCore.QSize(150, 67))
        self.groupBox_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_21.setFlat(False)
        self.groupBox_21.setObjectName(_fromUtf8("groupBox_21"))
        self.gridLayout_107 = QtGui.QGridLayout(self.groupBox_21)
        self.gridLayout_107.setObjectName(_fromUtf8("gridLayout_107"))
        self.tabWidget_11 = QtGui.QTabWidget(self.groupBox_21)
        self.tabWidget_11.setObjectName(_fromUtf8("tabWidget_11"))
        self.tab_20 = QtGui.QWidget()
        self.tab_20.setObjectName(_fromUtf8("tab_20"))
        self.gridLayout_108 = QtGui.QGridLayout(self.tab_20)
        self.gridLayout_108.setObjectName(_fromUtf8("gridLayout_108"))
        self.ObjRot_horizontalSlider = QtGui.QSlider(self.tab_20)
        self.ObjRot_horizontalSlider.setMinimumSize(QtCore.QSize(0, 39))
        self.ObjRot_horizontalSlider.setMaximumSize(QtCore.QSize(120, 16777215))
        self.ObjRot_horizontalSlider.setMinimum(-180)
        self.ObjRot_horizontalSlider.setMaximum(180)
        self.ObjRot_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ObjRot_horizontalSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.ObjRot_horizontalSlider.setTickInterval(20)
        self.ObjRot_horizontalSlider.setObjectName(_fromUtf8("ObjRot_horizontalSlider"))
        self.gridLayout_108.addWidget(self.ObjRot_horizontalSlider, 0, 0, 1, 1)
        self.tabWidget_11.addTab(self.tab_20, _fromUtf8(""))
        self.tab_21 = QtGui.QWidget()
        self.tab_21.setObjectName(_fromUtf8("tab_21"))
        self.gridLayout_109 = QtGui.QGridLayout(self.tab_21)
        self.gridLayout_109.setObjectName(_fromUtf8("gridLayout_109"))
        self.ObjRot_button_select_angle = QtGui.QPushButton(self.tab_21)
        self.ObjRot_button_select_angle.setEnabled(True)
        self.ObjRot_button_select_angle.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_select_angle.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ObjRot_button_select_angle.setObjectName(_fromUtf8("ObjRot_button_select_angle"))
        self.gridLayout_109.addWidget(self.ObjRot_button_select_angle, 0, 0, 1, 1)
        icon95 = QtGui.QIcon()
        icon95.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_click.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_11.addTab(self.tab_21, icon95, _fromUtf8(""))
        self.gridLayout_107.addWidget(self.tabWidget_11, 0, 0, 1, 1)
        self.horizontalLayout_81 = QtGui.QHBoxLayout()
        self.horizontalLayout_81.setObjectName(_fromUtf8("horizontalLayout_81"))
        self.ObjRot_lineEdit_angle = QtGui.QLineEdit(self.groupBox_21)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ObjRot_lineEdit_angle.sizePolicy().hasHeightForWidth())
        self.ObjRot_lineEdit_angle.setSizePolicy(sizePolicy)
        self.ObjRot_lineEdit_angle.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_lineEdit_angle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjRot_lineEdit_angle.setMaxLength(32769)
        self.ObjRot_lineEdit_angle.setObjectName(_fromUtf8("ObjRot_lineEdit_angle"))
        self.horizontalLayout_81.addWidget(self.ObjRot_lineEdit_angle)
        self.label_angle_4 = QtGui.QLabel(self.groupBox_21)
        self.label_angle_4.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_angle_4.setObjectName(_fromUtf8("label_angle_4"))
        self.horizontalLayout_81.addWidget(self.label_angle_4)
        self.gridLayout_107.addLayout(self.horizontalLayout_81, 1, 0, 1, 1)
        self.gridLayout_104.addWidget(self.groupBox_21, 2, 0, 1, 1)
        self.horizontalLayout_82 = QtGui.QHBoxLayout()
        self.horizontalLayout_82.setObjectName(_fromUtf8("horizontalLayout_82"))
        self.ObjRot_button_reset = QtGui.QPushButton(self.frame_11)
        self.ObjRot_button_reset.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_reset.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjRot_button_reset.setObjectName(_fromUtf8("ObjRot_button_reset"))
        self.horizontalLayout_82.addWidget(self.ObjRot_button_reset)
        spacerItem19 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem19)
        self.ObjRot_button_apply = QtGui.QPushButton(self.frame_11)
        self.ObjRot_button_apply.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_apply.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjRot_button_apply.setObjectName(_fromUtf8("ObjRot_button_apply"))
        self.horizontalLayout_82.addWidget(self.ObjRot_button_apply)
        self.gridLayout_104.addLayout(self.horizontalLayout_82, 3, 0, 1, 1)
        self.gridLayout_103.addWidget(self.frame_11, 0, 0, 1, 1)
        spacerItem20 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_103.addItem(spacerItem20, 1, 0, 1, 1)
        self.tabWidget_9.addTab(self.rotate_tab_2, _fromUtf8(""))
        self.translate_tab_2 = QtGui.QWidget()
        self.translate_tab_2.setObjectName(_fromUtf8("translate_tab_2"))
        self.gridLayout_20 = QtGui.QGridLayout(self.translate_tab_2)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.frame_12 = QtGui.QFrame(self.translate_tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName(_fromUtf8("frame_12"))
        self.gridLayout_111 = QtGui.QGridLayout(self.frame_12)
        self.gridLayout_111.setObjectName(_fromUtf8("gridLayout_111"))
        self.ObjTrans_button_select = QtGui.QPushButton(self.frame_12)
        self.ObjTrans_button_select.setObjectName(_fromUtf8("ObjTrans_button_select"))
        self.gridLayout_111.addWidget(self.ObjTrans_button_select, 0, 0, 1, 1)
        self.horizontalLayout_83 = QtGui.QHBoxLayout()
        self.horizontalLayout_83.setObjectName(_fromUtf8("horizontalLayout_83"))
        self.ObjTrans_duplicate = QtGui.QCheckBox(self.frame_12)
        self.ObjTrans_duplicate.setObjectName(_fromUtf8("ObjTrans_duplicate"))
        self.horizontalLayout_83.addWidget(self.ObjTrans_duplicate)
        self.ObjTrans_spin = QtGui.QSpinBox(self.frame_12)
        self.ObjTrans_spin.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjTrans_spin.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ObjTrans_spin.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.ObjTrans_spin.setKeyboardTracking(False)
        self.ObjTrans_spin.setMinimum(1)
        self.ObjTrans_spin.setMaximum(20)
        self.ObjTrans_spin.setSingleStep(1)
        self.ObjTrans_spin.setProperty("value", 1)
        self.ObjTrans_spin.setObjectName(_fromUtf8("ObjTrans_spin"))
        self.horizontalLayout_83.addWidget(self.ObjTrans_spin)
        self.ObjTrans_deepCopy = QtGui.QCheckBox(self.frame_12)
        self.ObjTrans_deepCopy.setObjectName(_fromUtf8("ObjTrans_deepCopy"))
        self.horizontalLayout_83.addWidget(self.ObjTrans_deepCopy)
        self.gridLayout_111.addLayout(self.horizontalLayout_83, 1, 0, 1, 1)
        self.horizontalLayout_84 = QtGui.QHBoxLayout()
        self.horizontalLayout_84.setObjectName(_fromUtf8("horizontalLayout_84"))
        self.ObjTrans_button_reset = QtGui.QPushButton(self.frame_12)
        self.ObjTrans_button_reset.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjTrans_button_reset.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjTrans_button_reset.setObjectName(_fromUtf8("ObjTrans_button_reset"))
        self.horizontalLayout_84.addWidget(self.ObjTrans_button_reset)
        spacerItem21 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_84.addItem(spacerItem21)
        self.ObjTrans_button_apply = QtGui.QPushButton(self.frame_12)
        self.ObjTrans_button_apply.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjTrans_button_apply.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjTrans_button_apply.setObjectName(_fromUtf8("ObjTrans_button_apply"))
        self.horizontalLayout_84.addWidget(self.ObjTrans_button_apply)
        self.gridLayout_111.addLayout(self.horizontalLayout_84, 3, 0, 1, 1)
        self.tabWidget_12 = QtGui.QTabWidget(self.frame_12)
        self.tabWidget_12.setEnabled(True)
        self.tabWidget_12.setObjectName(_fromUtf8("tabWidget_12"))
        self.tab_22 = QtGui.QWidget()
        self.tab_22.setObjectName(_fromUtf8("tab_22"))
        self.gridLayout_112 = QtGui.QGridLayout(self.tab_22)
        self.gridLayout_112.setObjectName(_fromUtf8("gridLayout_112"))
        self.groupBox_22 = QtGui.QGroupBox(self.tab_22)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_22.sizePolicy().hasHeightForWidth())
        self.groupBox_22.setSizePolicy(sizePolicy)
        self.groupBox_22.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_22.setFlat(False)
        self.groupBox_22.setObjectName(_fromUtf8("groupBox_22"))
        self.gridLayout_19 = QtGui.QGridLayout(self.groupBox_22)
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.ObjTrans_comboBox_start = QtGui.QComboBox(self.groupBox_22)
        self.ObjTrans_comboBox_start.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ObjTrans_comboBox_start.sizePolicy().hasHeightForWidth())
        self.ObjTrans_comboBox_start.setSizePolicy(sizePolicy)
        self.ObjTrans_comboBox_start.setMinimumSize(QtCore.QSize(100, 0))
        self.ObjTrans_comboBox_start.setMaximumSize(QtCore.QSize(120, 16777215))
        self.ObjTrans_comboBox_start.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.ObjTrans_comboBox_start.setObjectName(_fromUtf8("ObjTrans_comboBox_start"))
        self.ObjTrans_comboBox_start.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_start.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_start.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_start.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_start.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_start.addItem(_fromUtf8(""))
        self.gridLayout_19.addWidget(self.ObjTrans_comboBox_start, 0, 0, 1, 1)
        self.ObjTrans_button_select_start = QtGui.QPushButton(self.groupBox_22)
        self.ObjTrans_button_select_start.setEnabled(True)
        self.ObjTrans_button_select_start.setMinimumSize(QtCore.QSize(0, 0))
        self.ObjTrans_button_select_start.setMaximumSize(QtCore.QSize(100, 29))
        self.ObjTrans_button_select_start.setObjectName(_fromUtf8("ObjTrans_button_select_start"))
        self.gridLayout_19.addWidget(self.ObjTrans_button_select_start, 1, 0, 1, 1)
        self.gridLayout_114 = QtGui.QGridLayout()
        self.gridLayout_114.setObjectName(_fromUtf8("gridLayout_114"))
        self.gridLayout_115 = QtGui.QGridLayout()
        self.gridLayout_115.setObjectName(_fromUtf8("gridLayout_115"))
        self.label_11 = QtGui.QLabel(self.groupBox_22)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_115.addWidget(self.label_11, 0, 0, 1, 1)
        self.ObjTrans_start_x = QtGui.QLineEdit(self.groupBox_22)
        self.ObjTrans_start_x.setEnabled(False)
        self.ObjTrans_start_x.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_start_x.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_start_x.setObjectName(_fromUtf8("ObjTrans_start_x"))
        self.gridLayout_115.addWidget(self.ObjTrans_start_x, 0, 1, 1, 1)
        self.gridLayout_114.addLayout(self.gridLayout_115, 0, 0, 1, 1)
        self.gridLayout_116 = QtGui.QGridLayout()
        self.gridLayout_116.setObjectName(_fromUtf8("gridLayout_116"))
        self.label_12 = QtGui.QLabel(self.groupBox_22)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_116.addWidget(self.label_12, 0, 0, 1, 1)
        self.ObjTrans_start_y = QtGui.QLineEdit(self.groupBox_22)
        self.ObjTrans_start_y.setEnabled(False)
        self.ObjTrans_start_y.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_start_y.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_start_y.setObjectName(_fromUtf8("ObjTrans_start_y"))
        self.gridLayout_116.addWidget(self.ObjTrans_start_y, 0, 1, 1, 1)
        self.gridLayout_114.addLayout(self.gridLayout_116, 1, 0, 1, 1)
        self.gridLayout_117 = QtGui.QGridLayout()
        self.gridLayout_117.setObjectName(_fromUtf8("gridLayout_117"))
        self.label_13 = QtGui.QLabel(self.groupBox_22)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_117.addWidget(self.label_13, 0, 0, 1, 1)
        self.ObjTrans_start_z = QtGui.QLineEdit(self.groupBox_22)
        self.ObjTrans_start_z.setEnabled(False)
        self.ObjTrans_start_z.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_start_z.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_start_z.setObjectName(_fromUtf8("ObjTrans_start_z"))
        self.gridLayout_117.addWidget(self.ObjTrans_start_z, 0, 1, 1, 1)
        self.gridLayout_114.addLayout(self.gridLayout_117, 2, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_114, 2, 0, 1, 1)
        self.gridLayout_112.addWidget(self.groupBox_22, 0, 0, 1, 1)
        icon96 = QtGui.QIcon()
        icon96.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_startPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_12.addTab(self.tab_22, icon96, _fromUtf8(""))
        self.tab_23 = QtGui.QWidget()
        self.tab_23.setObjectName(_fromUtf8("tab_23"))
        self.groupBox_23 = QtGui.QGroupBox(self.tab_23)
        self.groupBox_23.setGeometry(QtCore.QRect(9, 9, 183, 225))
        self.groupBox_23.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_23.setFlat(False)
        self.groupBox_23.setObjectName(_fromUtf8("groupBox_23"))
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox_23)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.ObjTrans_comboBox_end = QtGui.QComboBox(self.groupBox_23)
        self.ObjTrans_comboBox_end.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ObjTrans_comboBox_end.sizePolicy().hasHeightForWidth())
        self.ObjTrans_comboBox_end.setSizePolicy(sizePolicy)
        self.ObjTrans_comboBox_end.setMinimumSize(QtCore.QSize(100, 0))
        self.ObjTrans_comboBox_end.setMaximumSize(QtCore.QSize(120, 16777215))
        self.ObjTrans_comboBox_end.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.ObjTrans_comboBox_end.setObjectName(_fromUtf8("ObjTrans_comboBox_end"))
        self.ObjTrans_comboBox_end.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_end.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_end.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_end.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_end.addItem(_fromUtf8(""))
        self.ObjTrans_comboBox_end.addItem(_fromUtf8(""))
        self.gridLayout_12.addWidget(self.ObjTrans_comboBox_end, 0, 0, 1, 1)
        self.ObjTrans_button_select_end = QtGui.QPushButton(self.groupBox_23)
        self.ObjTrans_button_select_end.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ObjTrans_button_select_end.sizePolicy().hasHeightForWidth())
        self.ObjTrans_button_select_end.setSizePolicy(sizePolicy)
        self.ObjTrans_button_select_end.setMinimumSize(QtCore.QSize(0, 0))
        self.ObjTrans_button_select_end.setMaximumSize(QtCore.QSize(100, 29))
        self.ObjTrans_button_select_end.setObjectName(_fromUtf8("ObjTrans_button_select_end"))
        self.gridLayout_12.addWidget(self.ObjTrans_button_select_end, 1, 0, 1, 1)
        self.gridLayout_120 = QtGui.QGridLayout()
        self.gridLayout_120.setObjectName(_fromUtf8("gridLayout_120"))
        self.gridLayout_121 = QtGui.QGridLayout()
        self.gridLayout_121.setObjectName(_fromUtf8("gridLayout_121"))
        self.label_14 = QtGui.QLabel(self.groupBox_23)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_121.addWidget(self.label_14, 0, 0, 1, 1)
        self.ObjTrans_end_z = QtGui.QLineEdit(self.groupBox_23)
        self.ObjTrans_end_z.setEnabled(False)
        self.ObjTrans_end_z.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_end_z.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_end_z.setObjectName(_fromUtf8("ObjTrans_end_z"))
        self.gridLayout_121.addWidget(self.ObjTrans_end_z, 0, 1, 1, 1)
        self.gridLayout_120.addLayout(self.gridLayout_121, 2, 0, 1, 1)
        self.gridLayout_122 = QtGui.QGridLayout()
        self.gridLayout_122.setObjectName(_fromUtf8("gridLayout_122"))
        self.label_15 = QtGui.QLabel(self.groupBox_23)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_122.addWidget(self.label_15, 0, 0, 1, 1)
        self.ObjTrans_end_y = QtGui.QLineEdit(self.groupBox_23)
        self.ObjTrans_end_y.setEnabled(False)
        self.ObjTrans_end_y.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_end_y.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_end_y.setObjectName(_fromUtf8("ObjTrans_end_y"))
        self.gridLayout_122.addWidget(self.ObjTrans_end_y, 0, 1, 1, 1)
        self.gridLayout_120.addLayout(self.gridLayout_122, 1, 0, 1, 1)
        self.gridLayout_123 = QtGui.QGridLayout()
        self.gridLayout_123.setObjectName(_fromUtf8("gridLayout_123"))
        self.label_16 = QtGui.QLabel(self.groupBox_23)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_123.addWidget(self.label_16, 0, 0, 1, 1)
        self.ObjTrans_end_x = QtGui.QLineEdit(self.groupBox_23)
        self.ObjTrans_end_x.setEnabled(False)
        self.ObjTrans_end_x.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_end_x.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_end_x.setObjectName(_fromUtf8("ObjTrans_end_x"))
        self.gridLayout_123.addWidget(self.ObjTrans_end_x, 0, 1, 1, 1)
        self.gridLayout_120.addLayout(self.gridLayout_123, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_120, 2, 0, 1, 1)
        icon97 = QtGui.QIcon()
        icon97.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_endPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_12.addTab(self.tab_23, icon97, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_21 = QtGui.QGridLayout(self.tab)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ObjTrans_horizontalSlider = QtGui.QSlider(self.tab)
        self.ObjTrans_horizontalSlider.setEnabled(False)
        self.ObjTrans_horizontalSlider.setMinimumSize(QtCore.QSize(0, 39))
        self.ObjTrans_horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ObjTrans_horizontalSlider.setMinimum(-1000)
        self.ObjTrans_horizontalSlider.setMaximum(1000)
        self.ObjTrans_horizontalSlider.setProperty("value", 100)
        self.ObjTrans_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ObjTrans_horizontalSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.ObjTrans_horizontalSlider.setTickInterval(20)
        self.ObjTrans_horizontalSlider.setObjectName(_fromUtf8("ObjTrans_horizontalSlider"))
        self.verticalLayout.addWidget(self.ObjTrans_horizontalSlider)
        self.horizontalLayout_85 = QtGui.QHBoxLayout()
        self.horizontalLayout_85.setObjectName(_fromUtf8("horizontalLayout_85"))
        self.ObjTrans_lineEdit_length_seg = QtGui.QLineEdit(self.tab)
        self.ObjTrans_lineEdit_length_seg.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ObjTrans_lineEdit_length_seg.sizePolicy().hasHeightForWidth())
        self.ObjTrans_lineEdit_length_seg.setSizePolicy(sizePolicy)
        self.ObjTrans_lineEdit_length_seg.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjTrans_lineEdit_length_seg.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjTrans_lineEdit_length_seg.setMaxLength(32769)
        self.ObjTrans_lineEdit_length_seg.setObjectName(_fromUtf8("ObjTrans_lineEdit_length_seg"))
        self.horizontalLayout_85.addWidget(self.ObjTrans_lineEdit_length_seg)
        self.label_length_segment = QtGui.QLabel(self.tab)
        self.label_length_segment.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_length_segment.setObjectName(_fromUtf8("label_length_segment"))
        self.horizontalLayout_85.addWidget(self.label_length_segment)
        self.verticalLayout.addLayout(self.horizontalLayout_85)
        self.gridLayout_21.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem22 = QtGui.QSpacerItem(20, 138, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_21.addItem(spacerItem22, 1, 0, 1, 1)
        self.tabWidget_12.addTab(self.tab, _fromUtf8(""))
        self.gridLayout_111.addWidget(self.tabWidget_12, 2, 0, 1, 1)
        self.gridLayout_20.addWidget(self.frame_12, 0, 0, 1, 1)
        spacerItem23 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_20.addItem(spacerItem23, 1, 0, 1, 1)
        self.tabWidget_9.addTab(self.translate_tab_2, _fromUtf8(""))
        self.gridLayout_94.addWidget(self.tabWidget_9, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.Modif_Tab_2, _fromUtf8(""))
        self.View_Tab_2 = QtGui.QWidget()
        self.View_Tab_2.setObjectName(_fromUtf8("View_Tab_2"))
        self.gridLayout_124 = QtGui.QGridLayout(self.View_Tab_2)
        self.gridLayout_124.setObjectName(_fromUtf8("gridLayout_124"))
        self.button_alignview = QtGui.QPushButton(self.View_Tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_alignview.sizePolicy().hasHeightForWidth())
        self.button_alignview.setSizePolicy(sizePolicy)
        self.button_alignview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon98 = QtGui.QIcon()
        icon98.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_viewAlign.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_alignview.setIcon(icon98)
        self.button_alignview.setIconSize(QtCore.QSize(32, 32))
        self.button_alignview.setObjectName(_fromUtf8("button_alignview"))
        self.gridLayout_124.addWidget(self.button_alignview, 0, 0, 1, 1)
        spacerItem24 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_124.addItem(spacerItem24, 2, 0, 1, 1)
        self.button_trackcamera = QtGui.QPushButton(self.View_Tab_2)
        icon99 = QtGui.QIcon()
        icon99.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_trackCamera.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_trackcamera.setIcon(icon99)
        self.button_trackcamera.setIconSize(QtCore.QSize(32, 32))
        self.button_trackcamera.setObjectName(_fromUtf8("button_trackcamera"))
        self.gridLayout_124.addWidget(self.button_trackcamera, 1, 0, 1, 1)
        icon100 = QtGui.QIcon()
        icon100.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_view.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_7.addTab(self.View_Tab_2, icon100, _fromUtf8(""))
        self.tab_24 = QtGui.QWidget()
        self.tab_24.setObjectName(_fromUtf8("tab_24"))
        self.gridLayout_125 = QtGui.QGridLayout(self.tab_24)
        self.gridLayout_125.setObjectName(_fromUtf8("gridLayout_125"))
        self.button_isView = QtGui.QPushButton(self.tab_24)
        icon101 = QtGui.QIcon()
        icon101.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_FCCamera_02.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isView.setIcon(icon101)
        self.button_isView.setIconSize(QtCore.QSize(32, 32))
        self.button_isView.setObjectName(_fromUtf8("button_isView"))
        self.gridLayout_125.addWidget(self.button_isView, 9, 0, 1, 1)
        spacerItem25 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_125.addItem(spacerItem25, 10, 0, 1, 1)
        self.button_isParallel = QtGui.QPushButton(self.tab_24)
        icon102 = QtGui.QIcon()
        icon102.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isParallel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isParallel.setIcon(icon102)
        self.button_isParallel.setIconSize(QtCore.QSize(32, 32))
        self.button_isParallel.setObjectName(_fromUtf8("button_isParallel"))
        self.gridLayout_125.addWidget(self.button_isParallel, 0, 0, 1, 1)
        self.button_isAngle = QtGui.QPushButton(self.tab_24)
        icon103 = QtGui.QIcon()
        icon103.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_angleBetween.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isAngle.setIcon(icon103)
        self.button_isAngle.setIconSize(QtCore.QSize(32, 32))
        self.button_isAngle.setObjectName(_fromUtf8("button_isAngle"))
        self.gridLayout_125.addWidget(self.button_isAngle, 4, 0, 1, 1)
        self.button_isLength = QtGui.QPushButton(self.tab_24)
        icon104 = QtGui.QIcon()
        icon104.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isLength.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isLength.setIcon(icon104)
        self.button_isLength.setIconSize(QtCore.QSize(32, 32))
        self.button_isLength.setObjectName(_fromUtf8("button_isLength"))
        self.gridLayout_125.addWidget(self.button_isLength, 6, 0, 1, 1)
        self.button_isDistance = QtGui.QPushButton(self.tab_24)
        icon105 = QtGui.QIcon()
        icon105.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_distanceBetween.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isDistance.setIcon(icon105)
        self.button_isDistance.setIconSize(QtCore.QSize(32, 32))
        self.button_isDistance.setObjectName(_fromUtf8("button_isDistance"))
        self.gridLayout_125.addWidget(self.button_isDistance, 5, 0, 1, 1)
        self.button_isCoplanar = QtGui.QPushButton(self.tab_24)
        icon106 = QtGui.QIcon()
        icon106.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isCoplanar.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isCoplanar.setIcon(icon106)
        self.button_isCoplanar.setIconSize(QtCore.QSize(32, 32))
        self.button_isCoplanar.setObjectName(_fromUtf8("button_isCoplanar"))
        self.gridLayout_125.addWidget(self.button_isCoplanar, 2, 0, 1, 1)
        self.button_isArea = QtGui.QPushButton(self.tab_24)
        icon107 = QtGui.QIcon()
        icon107.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isArea.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isArea.setIcon(icon107)
        self.button_isArea.setIconSize(QtCore.QSize(32, 32))
        self.button_isArea.setObjectName(_fromUtf8("button_isArea"))
        self.gridLayout_125.addWidget(self.button_isArea, 7, 0, 1, 1)
        self.button_isPerpendicular = QtGui.QPushButton(self.tab_24)
        icon108 = QtGui.QIcon()
        icon108.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isPerpendicular.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isPerpendicular.setIcon(icon108)
        self.button_isPerpendicular.setIconSize(QtCore.QSize(32, 32))
        self.button_isPerpendicular.setObjectName(_fromUtf8("button_isPerpendicular"))
        self.gridLayout_125.addWidget(self.button_isPerpendicular, 1, 0, 1, 1)
        self.button_isClearance = QtGui.QPushButton(self.tab_24)
        icon109 = QtGui.QIcon()
        icon109.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isClearance.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isClearance.setIcon(icon109)
        self.button_isClearance.setIconSize(QtCore.QSize(32, 32))
        self.button_isClearance.setObjectName(_fromUtf8("button_isClearance"))
        self.gridLayout_125.addWidget(self.button_isClearance, 3, 0, 1, 1)
        self.button_isRadius = QtGui.QPushButton(self.tab_24)
        icon110 = QtGui.QIcon()
        icon110.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isRadius.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isRadius.setIcon(icon110)
        self.button_isRadius.setIconSize(QtCore.QSize(32, 32))
        self.button_isRadius.setObjectName(_fromUtf8("button_isRadius"))
        self.gridLayout_125.addWidget(self.button_isRadius, 8, 0, 1, 1)
        icon111 = QtGui.QIcon()
        icon111.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_check.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_7.addTab(self.tab_24, icon111, _fromUtf8(""))
        self.gridLayout_128.addWidget(self.tabWidget_7, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_13.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayout_43 = QtGui.QHBoxLayout()
        self.horizontalLayout_43.setObjectName(_fromUtf8("horizontalLayout_43"))
        self.button_WF_quit = QtGui.QPushButton(Form)
        self.button_WF_quit.setObjectName(_fromUtf8("button_WF_quit"))
        self.horizontalLayout_43.addWidget(self.button_WF_quit)
        spacerItem26 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem26)
        self.label_release = QtGui.QLabel(Form)
        self.label_release.setObjectName(_fromUtf8("label_release"))
        self.horizontalLayout_43.addWidget(self.label_release)
        self.gridLayout_13.addLayout(self.horizontalLayout_43, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.point_proj_comboBox.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.point_loc_comboBox.setCurrentIndex(1)
        self.tabWidget_8.setCurrentIndex(0)
        self.point_proj_comboBox_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.transition_comboBox.setCurrentIndex(2)
        self.Image_comboBox_axis_rotate.setCurrentIndex(0)
        self.Image_comboBox_axis_scale.setCurrentIndex(0)
        self.tabWidget_9.setCurrentIndex(0)
        self.tabWidget_10.setCurrentIndex(0)
        self.ObjRot_comboBox_axis.setCurrentIndex(0)
        self.ObjRot_comboBox_center.setCurrentIndex(2)
        self.tabWidget_11.setCurrentIndex(0)
        self.tabWidget_12.setCurrentIndex(0)
        self.ObjTrans_comboBox_start.setCurrentIndex(0)
        self.ObjTrans_comboBox_end.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "WorkFeature", None))
        self.button_origin.setToolTip(_translate("Form", "Create at origin of the document: \n"
"  a point,\n"
"  X, Y, Z axis, \n"
"  XZ, XY, YZ planes.", None))
        self.button_origin.setText(_translate("Form", "Origin", None))
        self.groupBox_13.setTitle(_translate("Form", "Preferences :", None))
        self.radioButton_verbose.setToolTip(_translate("Form", "Toggle here if you want a lot of information printed into report View.", None))
        self.radioButton_verbose.setText(_translate("Form", "Verbose", None))
        self.radioButton_biColor.setToolTip(_translate("Form", "Change the successive lines to be bicolor (red and white) for the following functions:\n"
"  - in \"Axis 1/2\" TAB:\n"
"    Axes=Cut(Wire)\n"
"  - in \"Circle\" TAB:\n"
"    Arcs=Cut(Circle)  \n"
"", None))
        self.radioButton_biColor.setText(_translate("Form", "Bi Color", None))
        self.radioButton_copy.setToolTip(_translate("Form", "Force the duplication of the Parent Object for the following functions:\n"
"  - in \"Axis 2/2\" TAB:\n"
"    Axes=(Axis,Pt,dist)\n"
"    If an Edge of a Cube is selected the Cube is duplicate \n"
"    with the corresponding\n"
"    Edge at the defined distance from the original.\n"
"  - in \"Plane\" TAB:\n"
"    Plane=(Plane,dist)  ", None))
        self.radioButton_copy.setText(_translate("Form", "Object copy", None))
        self.label_10.setToolTip(_translate("Form", "Change the tolerance for the following functions:\n"
"  - in \"Check\" TAB:\n"
"    are Parallel?\n"
"    are Perpendicular?\n"
"    are Coplanar?", None))
        self.label_10.setText(_translate("Form", "Tolerance", None))
        self.tolerance_edit.setToolTip(_translate("Form", "Change the tolerance for the following functions:\n"
"  - in \"Check\" TAB:\n"
"    are Parallel?\n"
"    are Perpendicular?\n"
"    are Coplanar?", None))
        self.tolerance_edit.setText(_translate("Form", "1e-10", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Origin_Tab_2), _translate("Form", "Ori. Pref.", None))
        self.button_object_center.setToolTip(_translate("Form", "Create a Point at center location of all selected Object(s).\n"
"if BBox is not toggled :\n"
"  This point is the MEAN location of all center of Mass (if exist) of all objects.\n"
"  All  center of Mass of al selected object(s) will be created too.\n"
"    \n"
"if BBox check box is toggled :\n"
"  This point is the center of the Global X,Y,Z bounding box of all objects.\n"
"  This global bounding box always exists (especially for draft objects).\n"
"  Be aware this point is not necessary the center of Mass of all Objects!\n"
"\n"
"- First select one or several Object(s)\n"
"- Then push this button", None))
        self.button_object_center.setText(_translate("Form", "Object(s) Center", None))
        self.checkBox_object_center.setToolTip(_translate("Form", "if BBox check box is toggled\n"
"        This point is the center of the Global X,Y,Z bounding box of all objects.\n"
"        This bounding box always exists (especially for draft objects).\n"
"        Be aware this point is not necessary the center of Mass of all Objects!", None))
        self.checkBox_object_center.setText(_translate("Form", "BBox", None))
        self.button_Npoints_center.setToolTip(_translate("Form", "Point=(N Points):\n"
"Create a Point at MEAN location of all selected points.\n"
"- First select several Points (at least 2)\n"
"- Then push this button", None))
        self.button_Npoints_center.setText(_translate("Form", "Points Center", None))
        self.button_line_center.setToolTip(_translate("Form", "Create Point(s) :\n"
"Cut each selected Line(s) in 2 (n) parts and\n"
"create a (n-1) Point(s) along selected edge(s) except at extrema.\n"
"The number indicates how many parts to consider.\n"
"\n"
"- First define the number of Parts, then\n"
"- Select at least 2 Points and/or\n"
"- Select one or several Line/Edge(s) and/or\n"
"- Select one Plane/Face to process all (4) Edges and/or\n"
"- Select one Object to process all Edges at once\n"
"- Then Click on the button ", None))
        self.button_line_center.setText(_translate("Form", "Line(s) Center", None))
        self.spin_line_center.setToolTip(_translate("Form", "The number indicates in how many parts each selected Lines(s) will be cut  (Max 100).", None))
        self.button_line_extrema.setToolTip(_translate("Form", "Create Points at start and end location of each selected Line(s).\n"
"\n"
"- Select one or several Line/Edge(s) and/or\n"
"- Select one Plane/Face to process all (4) Edges and/or\n"
"- Select one Object to process all Edges at once\n"
"- Then Click on the button ", None))
        self.button_line_extrema.setText(_translate("Form", "Line(s) Extrema", None))
        self.button_circle_center.setToolTip(_translate("Form", "Create a Point at center location of each selected Circle(s), Arc(s) or Ellipse(s).\n"
"\n"
"- Select one or several Circle(s), Arc(s) or Ellipse(s)\n"
"- Then Click on the button", None))
        self.button_circle_center.setText(_translate("Form", "Circle(s) Center", None))
        self.button_face_center.setToolTip(_translate("Form", "Create a Point at center location of each selected Face(s).\n"
"\n"
"- Select one or several Plane/Face(s) to process and/or\n"
"- Select one or several Object(s) to process all Faces at once\n"
"- Then Click on the button ", None))
        self.button_face_center.setText(_translate("Form", "Face(s) Center", None))
        self.button_line_face_point.setToolTip(_translate("Form", "Create a point at the intersection of the Line(s) and Plane(s) selected.\n"
" \n"
"First\n"
"- Select at least 2 Points and/or\n"
"- Select one or several Line/Edge(s) \n"
"and Second\n"
"- Select one or several Plane/Face(s) to process and/or\n"
"- Select one or several Object(s) to process all Faces at once\n"
"- Then Click on the button\n"
"\n"
"Be aware that if the plane is not extended enough the intersection Point is still created (as if). ", None))
        self.button_line_face_point.setText(_translate("Form", "Point=(Line,Face) ", None))
        self.button_point_face_point.setToolTip(_translate("Form", "Point(s)=(Point(s),Face(s)):\n"
"Create projection(s) of Point(s) onto Face(s).\n"
"\n"
"First\n"
"- Select one (or several) Point(s) and/or\n"
"- Select one or several Line/Edge(s) \n"
"and Second\n"
"- Select one or several Plane/Face(s) to process and/or\n"
"- Select one or several Object(s) to process all Faces at once\n"
"- Then Click on the button\n"
"\n"
"Plot the intersection point T on a Plane given one Plane and One Point C.\n"
"The Vector TC is perpendicular to the plane.\n"
"\n"
"Be aware that if the plane is not extended enough the intersection Point is still created (as if). ", None))
        self.button_point_face_point.setText(_translate("Form", "Point(s)=(Pt(s),Face(s))", None))
        self.button_points_projection.setToolTip(_translate("Form", "<html><head/><body><p>Create projected point(s) on the chosen main planes.</p><p>- Select one (or several) Point(s) and/or one (or several) Axis.</p><p>Define the projection plane if needed.</p><p>It can be either</p><p>XY plane,</p><p>YZ plane,</p><p>XZ plane or</p><p>All 3 planes</p></body></html>", None))
        self.button_points_projection.setText(_translate("Form", "Projected Points", None))
        self.point_proj_comboBox.setToolTip(_translate("Form", "<html><head/><body><p>The projection plane(s)</p></body></html>", None))
        self.point_proj_comboBox.setItemText(0, _translate("Form", "All", None))
        self.point_proj_comboBox.setItemText(1, _translate("Form", "XY plane", None))
        self.point_proj_comboBox.setItemText(2, _translate("Form", "YZ plane", None))
        self.point_proj_comboBox.setItemText(3, _translate("Form", "XZ plane", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Point_Tab1_3), _translate("Form", "Point 1/3", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.Point_Tab1_3), _translate("Form", "Create Point(s)", None))
        self.button_point_line_point.setToolTip(_translate("Form", "Point(s)=(Point(s),Line(s)):\n"
"    Create projection(s) of Point(s) onto Line(s).\n"
"\n"
"    First\n"
"    - Select one (or several) Point(s)\n"
"    and Second\n"
"    - Select one or several Line/Edge(s) and/or\n"
"    - Select one or several Plane/Face(s) to process and/or\n"
"    - Select one or several Object(s) to process all Faces at once\n"
"    - Then Click on the button\n"
"    \n"
"    Plot the intersection point T on a Line given one Linee and One Point C.\n"
"    The Vector TC is perpendicular to the Line.\n"
"    The symmetric point Cprime is also created as TC=TCprime.\n"
"    \n"
"    Be aware that if the line is not extended enough the intersection Point is still created (as if).", None))
        self.button_point_line_point.setText(_translate("Form", "Point(s)=(Pt(s),Line(s)) ", None))
        self.button_twolines_point.setToolTip(_translate("Form", "Point(s)=(Line(s),Line(s)):\n"
"Plot one or two Point(s) at minimum distance of two Lines\n"
"Create a unique Point at intersection of 2 crossing Lines.\n"
"\n"
"First\n"
"  - Select two or more Line/Edge(s) and\n"
"  - Then Click on the button\n"
"    \n"
"Plot the point A on the first Line given and the point  B on the second Line.\n"
"The Vector AB perpendicular to the first and second Line.\n"
"    ", None))
        self.button_twolines_point.setText(_translate("Form", "Point=(Line,Line) ", None))
        self.button_point_on_line.setToolTip(_translate("Form", "Create a Point at a certain distance along the line \n"
"respecting to the chosen reference starting point.", None))
        self.button_point_on_line.setText(_translate("Form", "Point along Line", None))
        self.distance_point_on_line.setToolTip(_translate("Form", "Distance from the extremity", None))
        self.distance_point_on_line.setText(_translate("Form", "0.0", None))
        self.button_distPoint.setToolTip(_translate("Form", "Point=(Point,Ax,dist):\n"
"Create a Point along the given Axis,  at a given distance of the selected Point.\n"
"The Axis indicate the direction along where the Point is duplicate.\n"
"(you can also select several axes to define different directions)\n"
"- First select a Point (you can select several points) and one or several Axis \n"
"- Second push this button\n"
"\n"
"NB: \n"
" - The distance between points can be defined first.\n"
"Positive number in one direction and negative in the other one.\n"
"The second number indicates the number of Points to create.\n"
"", None))
        self.button_distPoint.setText(_translate("Form", "Point=(Pt,Ax,dist)", None))
        self.dist_point.setToolTip(_translate("Form", "Distance to the new Axis.\n"
"Can be negative for the reverse direction!", None))
        self.dist_point.setText(_translate("Form", "10.0", None))
        self.spin_dist_point.setToolTip(_translate("Form", "The number of copies  (Max 100).", None))
        self.button_cut_wire_point.setToolTip(_translate("Form", "Create Points by Partition:\n"
"Cut the selected wire(s) in 2(n) parts and create 2(n) Points with function discretize.\n"
"The number indicates in how many parts to cut.\n"
"Wires can be:\n"
"    Line\n"
"    Circle\n"
"    Arc\n"
"    Ellipse\n"
"An object must also be selected but before any Wire to cut all his edges!    ", None))
        self.button_cut_wire_point.setText(_translate("Form", "Points=Cut(Wire)", None))
        self.spin_wire_cut_point.setToolTip(_translate("Form", "The number indicates in how many parts the selected Line will be cut  (Max 100).", None))
        self.button_click_for_point.setToolTip(_translate("Form", "Create a set of Points on a Plane perpendicular to the view at location of mouse clicks.\n"
"- Click first on the Button then click  on the View (with no object in background).\n"
"- Click first on the Button then click on the View (with an object in background), it will attach the points to the surface of the object.\n"
"\n"
"Use left mouse button (MB1) to generate Points. \n"
"MB2 and MB3 can still be used for view zoom and view rotation.\n"
"", None))
        self.button_click_for_point.setText(_translate("Form", "Click", None))
        self.button_object_base_point.setToolTip(_translate("Form", "Create Base Point of all selected Object(s).", None))
        self.button_object_base_point.setText(_translate("Form", "Object(s) Base Point", None))
        self.button_object_center_mass_point.setToolTip(_translate("Form", "Create Center of Mass Point of all selected Object(s).", None))
        self.button_object_center_mass_point.setText(_translate("Form", "Object(s) Mass Center Point", None))
        self.button_object_Npoint.setToolTip(_translate("Form", "Create a set of points from selected Objects:\n"
"- Select object(s)\n"
"    to create points from these object(s) !\n"
"    If you select an Edge : 2 points will be created;\n"
"    if you select a Plane : 4 points will be created;\n"
"    if you select an Object : many points will be created.\n"
"- Then click on this button.", None))
        self.button_object_Npoint.setText(_translate("Form", "Object(s) N Point(s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Point_Tab2_3), _translate("Form", "Point 2/3", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.Point_Tab2_3), _translate("Form", "Create Point(s)", None))
        self.button_points_load.setToolTip(_translate("Form", "Load a set of points from an ASCII file:\n"
"  ASCII format is 3 values by line separated by blank as :  \n"
"        15.3f  15.3f  15.3f\n"
"  Values are read as float.\n"
"        \n"
"  Lines starting with characeter : # or / are considered as comment lines\n"
"     ", None))
        self.button_points_load.setText(_translate("Form", "Load Points", None))
        self.button_points_save.setToolTip(_translate("Form", "Save a point or a set of points into an ASCII file:\n"
"One (x, y, z) triplet per line separated by blank.\n"
"\n"
"- Select as much as Points as needed and/or select object(s)\n"
"    to save points from these object(s) !\n"
"    If you select an Edge : 2 points will be saved;\n"
"    if you select a Plane : 4 points will be saved;\n"
"    if you select an Object : many points will be saved.\n"
"- Then click on this button.", None))
        self.button_points_save.setText(_translate("Form", "Save Points", None))
        self.button_points_random.setToolTip(_translate("Form", "<html><head/><body><p>Create random Point(s).</p><p>Define first the number of points to create and the coordinates limits.</p><p>- Then push the button, </p><p>or</p><p>- Select first one point to the center desired location;</p><p>- Then push the button.</p></body></html>", None))
        self.button_points_random.setText(_translate("Form", "Random Points", None))
        self.spin_random_points.setToolTip(_translate("Form", "<html><head/><body><p>The number indicates in how many point(s) will be generated  (Max 100).</p></body></html>", None))
        self.distance_random_points.setToolTip(_translate("Form", "<html><head/><body><p>If set to 10.0 return random floats coordinates in the half-open interval [-10.0, 10.0).</p></body></html>", None))
        self.distance_random_points.setText(_translate("Form", "10.0", None))
        self.button_point_to_sketch.setToolTip(_translate("Form", "Transform Point(s) in Sketch\'s Point(s) by projection onto the Sketch\'s Plane:\n"
"- First select an existing Sketch;\n"
"- Select as much as Points needed;\n"
"Then click on this button.", None))
        self.button_point_to_sketch.setText(_translate("Form", "Point(s) to Sketch", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Point_Tab3_3), _translate("Form", "Point 3/3", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Point_Tab), _translate("Form", "Point", None))
        self.tabWidget_7.setTabToolTip(self.tabWidget_7.indexOf(self.Point_Tab), _translate("Form", "Create Point(s)", None))
        self.button_twopoints_axis.setToolTip(_translate("Form", "Create an Axis crossing 2 Points.", None))
        self.button_twopoints_axis.setText(_translate("Form", "Two Points Axis", None))
        self.extension_twopoints_axis.setToolTip(_translate("Form", "Distance for the extensions on extrema.\n"
"Positive values will enlarge the Axis.\n"
"Negative values will start to shrink it (then reverse when middle reached). ", None))
        self.extension_twopoints_axis.setText(_translate("Form", "0.0", None))
        self.button_object_axis.setToolTip(_translate("Form", "Create 3 Axes at center location of all selected Object(s).", None))
        self.button_object_axis.setText(_translate("Form", "Object(s) X, Y, Z Axes", None))
        self.button_line_point_axis.setToolTip(_translate("Form", "Create an Axis Perpendicular to an Axis and crossing a Point\n"
"-Select one Axis and one (or several) Point(s) NOT on the previous Axis.", None))
        self.button_line_point_axis.setText(_translate("Form", "Axis=(Axis,Point)", None))
        self.extension_line_point_axis.setToolTip(_translate("Form", "Distance for the extensions on extrema.\n"
"Positive values will enlarge the Axis.\n"
"Negative values will start to shrink it (then reverse when middle reached). ", None))
        self.extension_line_point_axis.setText(_translate("Form", "0.0", None))
        self.button_Npoints_axis.setToolTip(_translate("Form", "Axis=(N Points):\n"
"Create a \"best fit\" Line from a set of points using Singular Value Decomposition.\n"
"- First select several Points (at least 2);\n"
"- Then push this button\n"
"\n"
"The 3 eigenvectors are generated.\n"
"Orange one is the best fit line.\n"
"", None))
        self.button_Npoints_axis.setText(_translate("Form", "Axis from Point(s)", None))
        self.button_point_line_axis.setToolTip(_translate("Form", "Create an Axis Parallel to an Axis (as Direction) and crossing a Point.\n"
"- Select one Axis and one (or several) Point(s) NOT on the previous Axis.\n"
"Define the length and the attach point if needed.\n"
"A Length of Zero means the length of already selected Axis will be used.", None))
        self.button_point_line_axis.setText(_translate("Form", "Axis=(Pt,Dir)", None))
        self.extension_line.setToolTip(_translate("Form", "Define the length of the Axis to create.\n"
"A Length of Zero means the length of already selected Axis will be used.", None))
        self.extension_line.setText(_translate("Form", "0.0", None))
        self.point_loc_comboBox.setToolTip(_translate("Form", "The Attach Point will be at :\n"
"Start of the Axis;\n"
"Mid of the Axis;\n"
"End of the Axis.", None))
        self.point_loc_comboBox.setItemText(0, _translate("Form", "Start", None))
        self.point_loc_comboBox.setItemText(1, _translate("Form", "Mid", None))
        self.point_loc_comboBox.setItemText(2, _translate("Form", "End", None))
        self.button_cylinder_axis.setToolTip(_translate("Form", "Create the Axis of a Cylinder.", None))
        self.button_cylinder_axis.setText(_translate("Form", "Cylinder(s) Axis", None))
        self.button_plane_axis.setToolTip(_translate("Form", "Plane(s) Axes:\n"
"Create Perpendicular Axes at the center location of a Plane.\n"
" - First select one (or several) Plane(s);\n"
" - Then press the button\n"
"\n"
"or \n"
"Create Perpendicular Axes of a Plane at selected locations.\n"
" - First select one Plane;\n"
" - Second select Point(s) for locations\n"
" - Press the button\n"
"\n"
"NB: Axes are created on both sides of the Plane\n"
"The extension is 10 units by default but must be changed if needed.", None))
        self.button_plane_axis.setText(_translate("Form", "Plane(s) Axes", None))
        self.button_face_normal.setToolTip(_translate("Form", "Create a normal Axis of a Face.\n"
"To create a Normal at click location on a Face:\n"
"- Click first in the view to select and object,\n"
"- then push the button, \n"
"- then click on a location on the selected Face.\n"
"or\n"
"To create several Normal of the face:\n"
"- Click first in the view to select and object,\n"
"- then select one or several points of the face\n"
"- then push the button.\n"
"(These selections can also be done into the Combined View)", None))
        self.button_face_normal.setText(_translate("Form", "Face Normal", None))
        self.extension_face_normal.setToolTip(_translate("Form", "Length of external part of the (Normal) Axis.\n"
"  If zero In case of cylinder axis the extension will be a percentage (10%) of the object length.\n"
"  If zero and plane of face Normal, the extension will be 10 units.\n"
"\n"
"For \"Cylinder Axis\", \"Planes Axes\" and \"Face Normal\"\n"
"  Positive values will enlarge the Axis toward OUTSIDE of the Face Object;\n"
"  Negative values will  enlarge the Axis toward INSIDE of the Face Object.", None))
        self.extension_face_normal.setText(_translate("Form", "0.0", None))
        self.button_twolines_axis.setToolTip(_translate("Form", "Create an Axis between two Axes.\n"
"-Select two Axes.", None))
        self.button_twolines_axis.setText(_translate("Form", "Axis=(Line,Line)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Axis_Tab1_3), _translate("Form", "Axis 1/3", None))
        self.button_object_base_axes.setToolTip(_translate("Form", "Create 3 Axes at Base location of all selected Object(s).", None))
        self.button_object_base_axes.setText(_translate("Form", "Object(s) Base Axes", None))
        self.button_object_Naxes.setToolTip(_translate("Form", "Create a set of axes from selected Objects:\n"
"- Select object(s)\n"
"    to create axes from these object(s) !\n"
"    if you select a Plane : 4 axes will be created;\n"
"    if you select an Object : many axes will be created.\n"
"- Then click on this button.", None))
        self.button_object_Naxes.setText(_translate("Form", "Object(s) N Axes(s)", None))
        self.button_line_to_sketch.setToolTip(_translate("Form", "Transform Line(s) in Sketch\'s Line(s) by projection onto the Sketch\'s Plane:\n"
"- First select an existing Skecth;\n"
"- Select as much as Lines needed;\n"
"Then click on this button.", None))
        self.button_line_to_sketch.setText(_translate("Form", "Axis(es) to Sketch", None))
        self.button_object_3axes.setToolTip(_translate("Form", "Create a set of 2 or 3 main axes from selected Objects:\n"
"The most representative axes will be selected from all axis.\n"
"The length of main axes will be the cumulative length of all axes with the same direction.\n"
"- Select object(s)\n"
"    to create axes from these object(s) !\n"
"    if you select a Plane : 2 axes will be created;\n"
"    if you select an Object : 3 axes will be created.\n"
"- Then click on this button.", None))
        self.button_object_3axes.setText(_translate("Form", "Object(s) 3 Axes(s)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Axis_Tab31_3), _translate("Form", "Axis 3/3", None))
        self.button_plane_point_line_axis.setToolTip(_translate("Form", "Create an Axis Perpendicular to an Axis, crossing a Point and Parallel to a Plane.\n"
"-Select one Plane, one Axis and one Point ON the previous Axis.", None))
        self.button_plane_point_line_axis.setText(_translate("Form", "Axis=(Plane,Point,Axis)", None))
        self.button_line_plane_axis.setToolTip(_translate("Form", "Axes=(Pl(s),Axes):\n"
"Create projection(s) of Axes onto Plane(s).\n"
"- First select one (or several) Line(s)\n"
"- Second select one or several) Plane(s)\n"
"- Then push this button", None))
        self.button_line_plane_axis.setText(_translate("Form", "Axes=(Pl(s),Axes)", None))
        self.button_twoplanes_axis.setToolTip(_translate("Form", "Create an Axis by intersect of 2 Planes.", None))
        self.button_twoplanes_axis.setText(_translate("Form", "Axis=(Plane,Plane)", None))
        self.button_distLine.setToolTip(_translate("Form", "Axes=(Axis,Pt,dist):\n"
"Create an Axis parallel to a given Axis, Point at a given distance.\n"
"The Axis is created along the Plane defined by the given Axis and Point.\n"
"- First select an Axis (or several Axes) and a Point\n"
"(you can also select several points to define different Planes)\n"
"- Second push this button\n"
"\n"
"NB: \n"
" - The distance to the Axis created can be defined first.\n"
"Positive number in one direction and negative in the other one.\n"
"The second number indicates the number of Axes to create.\n"
"With option \"Object copy\" in \"Ori. Pref.\"  TAB\n"
"  - If an Edge of a Cube is selected the Cube is duplicate with the corresponding\n"
"Edge at the defined distance from the original.\n"
"Several Edges of the cube can be selected.\n"
"", None))
        self.button_distLine.setText(_translate("Form", "Axes=(Axis,Pt,dist)", None))
        self.dist_line.setToolTip(_translate("Form", "Distance to the new Axis.\n"
"Can be negative for the reverse direction!", None))
        self.dist_line.setText(_translate("Form", "10.0", None))
        self.spin_dist_line.setToolTip(_translate("Form", "The number of copies  (Max 100).", None))
        self.button_angleLine.setToolTip(_translate("Form", "Axes=(Axis,Pt,Pl,a):\n"
"Create an Axis with an Angle to a origin Axis.\n"
"- First select an Axis to rotate, then a Plane and a rotation Point\n"
"- Second push this button\n"
"or\n"
"- First select an Axis to rotate, then a rotation Axis and a rotation Point\n"
"- Second push this button\n"
"\n"
"NB:\n"
"The Axis is created by rotation using :\n"
"  The Normal of the selected Plane as rotation Axis \n"
"and selected Point as rotation Point. \n"
"or\n"
"  The second selected Axis as rotation Axis \n"
"and selected Point as rotation Point. \n"
"\n"
" - The angle (in degrees) of rotation can be defined first.\n"
"Positive number in one direction and negative in the other one.\n"
" - The second number indicates the number of Axes to create.\n"
"\n"
"", None))
        self.button_angleLine.setText(_translate("Form", "Axes=(Axis,Pt,Pl,a)", None))
        self.angle_line.setToolTip(_translate("Form", "Angle to the new Axis.\n"
"Can be negative for the reverse direction!\n"
"(in degrees)", None))
        self.angle_line.setText(_translate("Form", "45.0", None))
        self.spin_angle_line.setToolTip(_translate("Form", "The number of copies (Max 100).", None))
        self.button_cut_wire_axis.setToolTip(_translate("Form", "Create Axes by Partition:\n"
"Cut the selected wire(s) in 2(n) parts and create 2(n) Axes with function discretize.\n"
"The number indicates in how many parts to cut.\n"
"Wires can be:\n"
"    Line\n"
"    Circle\n"
"    Arc\n"
"    Ellipse\n"
"An object must also be selected but before any Wire to cut all his Edges!\n"
"NB: You can change the successive lines to be bicolor (red and white)  \n"
"in \"Ori. Pref.\"  TAB    \n"
"", None))
        self.button_cut_wire_axis.setText(_translate("Form", "Axes=Cut(Wire)", None))
        self.spin_wire_cut_axis.setToolTip(_translate("Form", "The number indicates in how many parts the selected Line will be cut  (Max 100).", None))
        self.button_cut_axis.setToolTip(_translate("Form", "Create Axes:\n"
"Cut the selected Line in 2(n) parts and create 2(n) Axes.\n"
"The number indicates in how many parts to cut.\n"
"\n"
"NB: You can change the successive lines to be bicolor (red and white)  \n"
"in \"Ori. Pref.\"  TAB", None))
        self.button_cut_axis.setText(_translate("Form", "Axes=Cut(Axis)", None))
        self.spin_axis_cut.setToolTip(_translate("Form", "The number indicates in how many parts the selected Line will be cut  (Max 100).", None))
        self.button_extension_axis.setToolTip(_translate("Form", "Enlarge(Axis):\n"
"Extend an Axis at two extrema.\n"
"- First select an Axis (or several Axes) \n"
"- Second push this button\n"
"\n"
"NB: \n"
" - The percentage of  the extension can be defined first.\n"
" - Negative percentage will shrink the Axis", None))
        self.button_extension_axis.setText(_translate("Form", "Enlarge(Axis)", None))
        self.extension_axis.setToolTip(_translate("Form", "Extension of the Line in percentage of original length of the Line.\n"
"If the extension is 50% it means that each side is extended with 25% length.\n"
"\n"
"Positive values will enlarge the Axis.\n"
"Negative values will start to shrink it. ", None))
        self.extension_axis.setText(_translate("Form", "50.0", None))
        self.button_click_for_axis.setToolTip(_translate("Form", "Create a set of Lines on a Plane perpendicular to the view at location of 2 mouse clicks.\n"
"- Click first on the Button then at least twice click on the View (with no object in background).\n"
"- Click first on the Button then at least twice click on the View (with an object in background), it will attach the lines to the surface of the object.\n"
"\n"
"\n"
"Use left mouse button (MB1) to generate Lines. \n"
"MB2 and MB3 can still be used for view zoom and view rotation.", None))
        self.button_click_for_axis.setText(_translate("Form", "Click", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Axis_Tab2_3), _translate("Form", "Axis 2/3", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Axis_Tab), _translate("Form", "Axis", None))
        self.button_points_to_polygon.setToolTip(_translate("Form", "<html><head/><body><p>Wire=(N Points):</p><p>Create a Polygon (wire) from a set of points.</p><p>- First select several Points (at least 2);</p><p>- Then push this button</p><p><br/></p></body></html>", None))
        self.button_points_to_polygon.setText(_translate("Form", "Make Polygon", None))
        self.button_points_to_convex_2Dpolygon.setToolTip(_translate("Form", "<html><head/><body><p>Wire=(N Points):</p><p>Create a Convex 2D Polygon (wire) from a set of points.</p><p>The Convex Polygon is the outer limit of all selected Points.</p><p> - First select several Points (at least 3);</p><p>    Define the projection plane if needed.</p><p>    It can be either</p><p>    XY plane,</p><p>    YZ plane,</p><p>    XZ plane or</p><p>    All 3 planes</p><p>- Then push the button.</p></body></html>", None))
        self.button_points_to_convex_2Dpolygon.setText(_translate("Form", "Convex 2D Polygon", None))
        self.point_proj_comboBox_2.setToolTip(_translate("Form", "<html><head/><body><p>The projection plane(s)</p></body></html>", None))
        self.point_proj_comboBox_2.setItemText(0, _translate("Form", "All", None))
        self.point_proj_comboBox_2.setItemText(1, _translate("Form", "XY plane", None))
        self.point_proj_comboBox_2.setItemText(2, _translate("Form", "YZ plane", None))
        self.point_proj_comboBox_2.setItemText(3, _translate("Form", "XZ plane", None))
        self.button_4points_bezier.setToolTip(_translate("Form", "Bezier Cubic=(4 Points):\n"
"Create a Wire (Bezier Cubic) from 4 selected points.\n"
"- First 4 Points\n"
"- Then push this button", None))
        self.button_4points_bezier.setText(_translate("Form", "4 Points Bezier Cubic", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.Wire_Tab1_3), _translate("Form", "Wire", None))
        self.button_curves_and_surfaces.setText(_translate("Form", "Launch Curves and Surfaces Menu...", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.Wire_Tab1_4), _translate("Form", "Curves And Surfaces", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Wire_Tab), _translate("Form", "Wire", None))
        self.button_linecenter_circle.setToolTip(_translate("Form", "Select an Axis and a Point to create a Circle\n"
"centered on the Point, perpendicular to the Axis \n"
"with the given radius.", None))
        self.button_linecenter_circle.setText(_translate("Form", "Circle=(Axis, center)", None))
        self.radius_circle.setToolTip(_translate("Form", "Radius of the Circle.", None))
        self.radius_circle.setText(_translate("Form", "10.0", None))
        self.button_linepoint_circle.setToolTip(_translate("Form", "Select an Axis and a Point  to create a Circle\n"
"centered on the Axis and tangenting the Point.", None))
        self.button_linepoint_circle.setText(_translate("Form", "Circle=(Axis, point)", None))
        self.button_3points_ellipse.setToolTip(_translate("Form", "Select a center and 2 Points to create an Ellipse.", None))
        self.button_3points_ellipse.setText(_translate("Form", "Ellipse=(3 points)", None))
        self.button_circle_to_sketch.setToolTip(_translate("Form", "Transform Circle(s) and Arc(s) in Sketch\'s object(s) by projection onto the Sketch\'s Plane:\n"
"- First select an existing Skecth;\n"
"- Select as much as Circles and arcs needed;\n"
"Then click on this button.", None))
        self.button_circle_to_sketch.setText(_translate("Form", "Circle(s) to Sketch", None))
        self.button_3points_arc.setToolTip(_translate("Form", "Arc=(3 Points):\n"
"Create one Arc depending on 3 points.\n"
"\n"
"- First select 3 Points\n"
"- Then Click on the button", None))
        self.button_3points_arc.setText(_translate("Form", "Arc=(3 points)", None))
        self.button_3points_circle.setToolTip(_translate("Form", "Select 3 Points  to create a Circle.", None))
        self.button_3points_circle.setText(_translate("Form", "Circle=(3 points)", None))
        self.button_cut_circle.setToolTip(_translate("Form", "Create Arcs:\n"
"Cut the selected Circle(s) or Arc(s) in 2(n) parts and create 2(n) Arcs.\n"
"The number indicates in how many parts to cut.\n"
"- First select as many Circles and Arcs you want\n"
"- Second set the number of parts\n"
"- Third push this button\n"
"\n"
"NB: You can change the successive lines to be bicolor (red and white)  \n"
"in \"Ori. Pref.\"  TAB", None))
        self.button_cut_circle.setText(_translate("Form", "Arcs=Cut(Circle)", None))
        self.spin_circle_cut.setToolTip(_translate("Form", "The number indicates in how many parts the selected Circle will be cut  (Max 100).", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Circle_Tab), _translate("Form", "Circle", None))
        self.button_threepoints_plane.setToolTip(_translate("Form", "<html><head/><body><p>Plane=(3 Points):</p><p>Create a Plane crossing 3 Points.</p><p> - Select at least 3 Points and/or</p><p>    Select at least 2 Line/Edge(s)</p><p>- Second push this button</p></body></html>", None))
        self.button_threepoints_plane.setText(_translate("Form", "Plane=(3 Points)", None))
        self.button_twopoints_plane.setToolTip(_translate("Form", "Plane=(2 Points):\n"
"Create a Plane in the middle of 2 points.\n"
"PLANE is perpendicular to line (P1 P2) and contains the midpoint of P1 and P2.\n"
"The direction of the normal of PLANE is the same as the vector from P1 to P2.\n"
"- First select 2 different points\n"
"- Second push this button", None))
        self.button_twopoints_plane.setText(_translate("Form", "Plane=(2 Points)", None))
        self.button_Npoints_plane.setToolTip(_translate("Form", "Plane=(N Points):\n"
"Create a \"best fit\" Plane from a set of points using Singular Value Decomposition.\n"
"- First select several Points (at least 3);\n"
"- Then push this button", None))
        self.button_Npoints_plane.setText(_translate("Form", "Plane=(N Points)", None))
        self.button_axisandpoint_plane.setToolTip(_translate("Form", "Plane=(Point, Axis):\n"
"Create a plane crossing a Line and a Point.\n"
"- First select a line and a point NOT on the previous line\n"
"- Second push this button", None))
        self.button_axisandpoint_plane.setText(_translate("Form", "Plane=(Point, Axis)", None))
        self.button_axis_point_plane.setToolTip(_translate("Form", "Plane=(Point, _|Axis):\n"
"Create a plane perpendicular to a Line and crossing a Point.\n"
"- First select a line and a point NOT on the previous line\n"
"- Second push this button", None))
        self.button_axis_point_plane.setText(_translate("Form", "Plane=(Point, _|Axis)", None))
        self.button_planeandpoint_plane.setToolTip(_translate("Form", "Plane=(Point, Plane):\n"
"Create a plane crossing a Point and parallel to a Plane.\n"
"- First select a plane and a point NOT on the previous plane\n"
"- Second push this button\n"
"\n"
"NB: you can enlarge the created new plane by setting first an extension length.", None))
        self.button_planeandpoint_plane.setText(_translate("Form", "Plane=(Point, Plane)", None))
        self.extension_planePointPlane.setToolTip(_translate("Form", "Length for the extensions of the new Plane compared to initial one.", None))
        self.extension_planePointPlane.setText(_translate("Form", "0.0", None))
        self.button_planeandaxis_plane.setToolTip(_translate("Form", "Plane=(Plane, Axis):\n"
"Create a Plane crossing a Line and perpendicular to a Plane.\n"
"- First select a plane and a line NOT on the previous plane\n"
"- Second push this button\n"
"\n"
"NB: The plane created can be rotated if a none null angle is defined first.", None))
        self.button_planeandaxis_plane.setText(_translate("Form", "Plane=(Plane, Axis)", None))
        self.angle_planeandaxis_plane.setToolTip(_translate("Form", "Angle of rotation of the created Plane (in degrees).", None))
        self.angle_planeandaxis_plane.setText(_translate("Form", "0.0", None))
        self.button_distPlane.setToolTip(_translate("Form", "Plane=(Plane,dist):\n"
"Create a Plane parallel to a Plane at a given distance.\n"
"- First select a plane or several Planes\n"
"- Second push this button\n"
"\n"
"NB: \n"
"  - The distance to the plane created can be defined first.\n"
"Positive number in one direction and negative in the other one.\n"
"The second number indicates the number of planes to create.\n"
"With option \"Object copy\" in \"Ori. Pref.\"  TAB\n"
"  - If a Face of a Cube is selected the Cube is duplicate with the \n"
"corresponding Face at the defined distance from the original.\n"
"Several Faces of the cube can be selected.", None))
        self.button_distPlane.setText(_translate("Form", "Plane=(Plane,dist)", None))
        self.dist_plane.setToolTip(_translate("Form", "Distance to the new plane.\n"
"Can be negative for the reverse direction!", None))
        self.dist_plane.setText(_translate("Form", "10.0", None))
        self.spin_dist_plane.setToolTip(_translate("Form", "The number of copies  (Max 100).", None))
        self.button_face_tangent.setToolTip(_translate("Form", "Face Tangent:\n"
"Create a tangent Plane at click location of a Face.\n"
"- First click in the view to select and object,\n"
"- Second push this button\n"
"-Third click on a location on the selected object.\n"
"\n"
"NB: The plane width and length can be defined first.", None))
        self.button_face_tangent.setText(_translate("Form", "Face Tangent", None))
        self.length_plane_2.setToolTip(_translate("Form", "Length of the Plane.", None))
        self.length_plane_2.setText(_translate("Form", "10.0", None))
        self.width_plane_2.setToolTip(_translate("Form", "Width of the Plane.", None))
        self.width_plane_2.setText(_translate("Form", "10.0", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Plane_Tab1_2), _translate("Form", "Plane 1/2", None))
        self.button_click_for_plane.setToolTip(_translate("Form", "Click:\n"
"Create a rectangular Plane perpendicular to the view at location of one mouse click.\n"
"Define the width and the length of the Plane if needed.\n"
"- Click first on the Button then click once on the View.\n"
"- Click first on the Button then click once on top of one object of the View\n"
" to attach the plane at this object.\n"
"- You can also select an already existing point first and click the button to attach the plane.\n"
"\n"
"NB: The plane width and length can be defined first.\n"
"\n"
"Use left mouse button (MB1) to generate Planes. \n"
"MB2 and MB3 can still be used for view zoom and view rotation.\n"
"", None))
        self.button_click_for_plane.setText(_translate("Form", "Click", None))
        self.length_plane.setToolTip(_translate("Form", "Length of the Plane.", None))
        self.length_plane.setText(_translate("Form", "10.0", None))
        self.width_plane.setToolTip(_translate("Form", "Width of the Plane.", None))
        self.width_plane.setText(_translate("Form", "10.0", None))
        self.button_extension_plane.setToolTip(_translate("Form", "Enlarge(Plane):\n"
"Extend a Plane in each dimension.\n"
"- First select a  Plane (or several Planes) \n"
"- Second push this button\n"
"\n"
"NB: \n"
" - The percentage of  the extension can be defined first.", None))
        self.button_extension_plane.setText(_translate("Form", "Enlarge(Plane)", None))
        self.extension_plane.setToolTip(_translate("Form", "Extension of the Plane in each dimension in percentage.", None))
        self.extension_plane.setText(_translate("Form", "50.0", None))
        self.button_object_center_planes.setToolTip(_translate("Form", "Object(s) Center Planes:\n"
"Create 3 Planes (XY, XZ and YZ) at center location of all selected Object(s).\n"
"- First select one or severl objects\n"
"- Second push this button", None))
        self.button_object_center_planes.setText(_translate("Form", "Object(s) Center Planes", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Plane_Tab2_2), _translate("Form", "Plane 1/2", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Plane_Tab), _translate("Form", "Plane", None))
        self.checkBox_allsubselect.setToolTip(_translate("Form", "if \"All\" is toggled:\n"
"  All the wires of the Trajectory  selected will be considered.\n"
"\n"
"Untoggled if you select a Skecth with several curves and you want to process\n"
"only the one subselected.", None))
        self.checkBox_allsubselect.setText(_translate("Form", "All", None))
        self.transition_comboBox.setToolTip(_translate("Form", "For the function :\n"
"makePipeShell(shapeList,[isSolid,isFrenet,transition])\n"
"Select a Transition option in case of trajectory with several wires; Transition can be:\n"
"#     0 (default), 1 (right corners) or 2 (rounded corners).", None))
        self.transition_comboBox.setItemText(0, _translate("Form", "No Transition", None))
        self.transition_comboBox.setItemText(1, _translate("Form", "Right corners", None))
        self.transition_comboBox.setItemText(2, _translate("Form", "Rounded corners", None))
        self.checkBox_solid.setToolTip(_translate("Form", "if \"Solid\" is toggled:\n"
"  The Beam sweep will generate a solid with a closed selected wire as Section.\n"
"If this check box is toggle off:\n"
"  Or if the Section wire is not closed, only a shell will be created.", None))
        self.checkBox_solid.setText(_translate("Form", "Solid", None))
        self.radioButton_Frenet.setToolTip(_translate("Form", "Force the \"isFrenet\" parameter to True for the function :\n"
"makePipeShell(shapeList,[isSolid,isFrenet,transition])\n"
"", None))
        self.radioButton_Frenet.setText(_translate("Form", "isFrenet", None))
        self.button_sweep.setToolTip(_translate("Form", "Section Sweep:\n"
"#  Make a loft defined by a list of profiles along a wire.\n"
"Will extrude/sweep a Section along a Trajectory like sweep from Part Workbench but:\n"
"- the Section center (of Mass) is move at the first point of the Trajectory and;\n"
"- the \"plane\" of the Section is rotate to be perpendicular to the Trajectory.\n"
"\n"
"- Select first one Section wire (Closed wire will generate volumes by default)\n"
"(This Section can be a compound from sketch to realize \"tube\")\n"
"- Select one or several wire(s) as Trajectory(ies)\n"
"- Then push this button\n"
"\n"
"NB: You can change first:\n"
"- Solid option (if toggled will generate a solid for Closed wire Section only) \n"
"- isFrenet option\n"
"- All option (means if the trajectory selected is a compound, all sub wires will be used for the sweep)\n"
"- Transition Option (Select a Transition option in case of trajectory with several wires; Transition can be:\n"
"#     0 (default), 1 (right corners) or 2 (rounded corners).)\n"
"", None))
        self.button_sweep.setText(_translate("Form", "Section Sweep", None))
        self.button_beam.setToolTip(_translate("Form", "Beam:\n"
"Will extrude a Section along a Linear Trajectory.\n"
"- Select first one Section wire (Closed wire will generate volumes by default)\n"
"(This Section can be a compound from sketch to realize \"tube\")\n"
"- Select one or several wire(s) as Trajectory(ies)\n"
"- Then push this button\n"
"", None))
        self.button_beam.setText(_translate("Form", "Beam", None))
        self.button_beam_cut_miter.setText(_translate("Form", "Beam Cut Miter", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Sweep_Tab), _translate("Form", "Sweep", None))
        self.button_boundingboxes.setToolTip(_translate("Form", "Create bounding boxes around each of selected object(s).\n"
"6 rectangles at the limits of each bounding boxes will be created.", None))
        self.button_boundingboxes.setText(_translate("Form", "Bounding Box(es)", None))
        self.button_boundingbox.setToolTip(_translate("Form", "Create one bounding box around all of selected object(s).\n"
"6 rectangles at the limits of the bounding box will be created.", None))
        self.button_boundingbox.setText(_translate("Form", "Bounding Box", None))
        self.checkBox_volumBB.setToolTip(_translate("Form", "<html><head/><body><p>if &quot;Vol.&quot; is toggled:</p><p>   In Addition of Rectangles creation,  Bounding box(es) will be also created as a Volume(s).</p></body></html>", None))
        self.checkBox_volumBB.setText(_translate("Form", "Vol.", None))
        self.checkBox_infoBB.setToolTip(_translate("Form", "<html><head/><body><p>if &quot;Info&quot; is toggled:</p><p> In Addition of Rectangles creation,  Annotations regarding lengths of edges will be added.</p></body></html>", None))
        self.checkBox_infoBB.setText(_translate("Form", "Info", None))
        self.button_cylinder_create.setToolTip(_translate("Form", "Create a Cylinder aligned on Axes:\n"
"- First select one or several couple of ( Axis and a Ref. Point). \n"
"- Define Diameter and Length if needed.\n"
"Then Click the button...\n"
"It will create a Cylinder aligned on the selected axis \n"
"with one of the extremities at the Ref. point,\n"
"for all couple selected.", None))
        self.button_cylinder_create.setText(_translate("Form", "Cylinder", None))
        self.diameter_cylinder.setToolTip(_translate("Form", "Radius of the Cylinder.", None))
        self.diameter_cylinder.setText(_translate("Form", "2.0", None))
        self.length_cylinder.setToolTip(_translate("Form", "Length of the Cylinder.\n"
"Negative value will reverse the direction from Ref. Point", None))
        self.length_cylinder.setText(_translate("Form", "20.0", None))
        self.button_cube_create.setToolTip(_translate("Form", "Create a Cuboid aligned on Axes:\n"
"- First select one or several couple of ( Axis and a Ref. Point). \n"
"- Define Dimensions if needed.\n"
"Then Click the button...\n"
"It will create a Cube aligned on the selected axis \n"
"with one of the extremities at Ref. point,\n"
"for all couple selected.", None))
        self.button_cube_create.setText(_translate("Form", "Cube", None))
        self.section_cube.setToolTip(_translate("Form", "Section (Length, Width) of the Cube.", None))
        self.section_cube.setText(_translate("Form", "2.0,2.0", None))
        self.height_cube.setToolTip(_translate("Form", "Height of the Cube.\n"
"Negative value will reverse the direction from Ref. Point", None))
        self.height_cube.setText(_translate("Form", "20.0", None))
        self.button_sphere_create.setToolTip(_translate("Form", "Create a Sphere shell:\n"
"- First select one or several Center Point(s). \n"
"- Define Diameter if needed.\n"
"Then Click the button...\n"
"It will create Sphere shell(s) centered\n"
"at the selected point(s).", None))
        self.button_sphere_create.setText(_translate("Form", "Sphere", None))
        self.diameter_sphere.setToolTip(_translate("Form", "Diameter of the Sphere.", None))
        self.diameter_sphere.setText(_translate("Form", "10.0", None))
        self.button_dome_create.setToolTip(_translate("Form", "Create a full geodesic dome shell:\n"
"- First select one or several Center Point(s). \n"
"- Define Diameter and Frequency Parameter (Integer between 1 to 10) if needed.\n"
"Then Click the button...\n"
"It will create full geodesic dome shell(s) with a X-Y-symmetry plane   \n"
"for even frequencies and centered\n"
"at the selected point(s).\n"
"\n"
"If Frequency Parameter = 1, the code create an icosahedron. \n"
"An icosahedron is a polyhedron with 20 faces.\n"
"\n"
"Original code from : Ulrich Brammer", None))
        self.button_dome_create.setText(_translate("Form", "Dome", None))
        self.spin_frequency_dome.setToolTip(_translate("Form", "Frequency Parameter (Integer between 1 to 20).", None))
        self.diameter_dome.setToolTip(_translate("Form", "Diameter of the Dome.", None))
        self.diameter_dome.setText(_translate("Form", "10.0", None))
        self.button_letter.setToolTip(_translate("Form", "AB:\n"
"Create 3D Text attached to a Point. \n"
"- First select a  Plane\n"
"- Then push this button\n"
"in this case the center of the text is attached to center of the Plane;\n"
"or\n"
"- First select a  Plane and a Point on the Plane\n"
"- Then push this button\n"
"NB:\n"
" Change the text and his size if needed", None))
        self.button_letter.setText(_translate("Form", "AB", None))
        self.letter.setToolTip(_translate("Form", "Put the desired text here", None))
        self.letter.setText(_translate("Form", "A", None))
        self.size_letter.setToolTip(_translate("Form", "Size of the font.", None))
        self.size_letter.setText(_translate("Form", "2.0", None))
        self.button_revolve.setToolTip(_translate("Form", "Revolve:\n"
"Make the revolution of Edge(s) or Wire(s) around an Axis:\n"
"- Select one or several wire(s)\n"
"- Then push this button\n"
"or\n"
"- Select FIRST one Point as center of rotation and one Axis as rotation axis !\n"
"- Select one or several wire(s)\n"
"- Then push this button\n"
"\n"
"NB:\n"
"  You can also define the angle of revolution if needed\n"
"   If no Axis is selected the Z axis is considered as Axis of rotation !\n"
"   If no Point is selected the Origin is considered as Center of rotation !", None))
        self.button_revolve.setText(_translate("Form", "Revolve", None))
        self.angle_revolve.setToolTip(_translate("Form", "Angle of the revolution in degrees.", None))
        self.angle_revolve.setText(_translate("Form", "360", None))
        self.button_copy_objects.setToolTip(_translate("Form", "Duplicate:\n"
"Make a copy of an object or a selected subObject part:\n"
"- Select one or several object(s) or subobject(s)\n"
"- Then push this button", None))
        self.button_copy_objects.setText(_translate("Form", "Duplicate", None))
        self.button_common.setToolTip(_translate("Form", "Compute the common parts between selected shapes.\n"
"- Select at least two objects and click.\n"
"\n"
"Highlight common parts by showing the common shape in red and setting half-transparency on original parts (the original objects are not modified).\n"
"Original code from HighlightCommon.FCMacro\n"
"    https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/HighlightCommon.FCMacro\n"
"    Authors = 2015 Javier Martinez Garcia\n"
"", None))
        self.button_common.setText(_translate("Form", "Common", None))
        self.button_difference.setToolTip(_translate("Form", "Compute the difference parts between selected shapes.\n"
"- Select two objects and click.\n"
"\n"
"Compute the difference between two shapes. Additions are marked red, removals are marked green. Both original parts will be half transparent. The volume of the additions and removals are printed in the console. \n"
"Original code from HighlightDifference.FCMacro\n"
"    https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/HighlightDifference.FCMacro\n"
"    Authors = 2015 Gaël Ecorchard (Galou)", None))
        self.button_difference.setText(_translate("Form", "Difference", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Objects_Tab2_2), _translate("Form", "Object", None))
        self.button_rotate_image.setText(_translate("Form", "Rotate", None))
        self.Image_comboBox_axis_rotate.setItemText(0, _translate("Form", "X", None))
        self.Image_comboBox_axis_rotate.setItemText(1, _translate("Form", "Y", None))
        self.Image_comboBox_axis_rotate.setItemText(2, _translate("Form", "Z", None))
        self.button_scale_image.setToolTip(_translate("Form", "Copy and Scale Image(s) :\n"
"Scale an image along desired direction(s) (make a copy first of the original Image).\n"
"- First define the direction(s) on the right combo (default is XY):\n"
"  if X is selected then only X direction will be scaled\n"
"  if XY is selected then the scale will be squared in X and Y directions together\n"
"- Select one or several Images (in combo view)\n"
"- Select one Line (or 2 Points) (close to the Image) you want to define new dimension.\n"
"(better to select a Line strictly in X direction if you want to enlarge/squize the Image in X direction)\n"
"- Then give the target dimension of the Line (on the last right LineEdit).\n"
"Then push the button\n"
"", None))
        self.button_scale_image.setText(_translate("Form", "Scale", None))
        self.Image_comboBox_axis_scale.setToolTip(_translate("Form", "Axis of Scaling for image.\n"
"Options :\n"
"    XY\n"
"    XZ\n"
"    YZ\n"
"    X\n"
"    Y\n"
"    Z\n"
"i.e.: if  XY is selected then the X and Y dimensions will be scaled together.\n"
"if only X is selected the only X dimension will be scaled.\n"
"\n"
"Note that some options are invalid regarding the image\'s plane.", None))
        self.Image_comboBox_axis_scale.setItemText(0, _translate("Form", "XY", None))
        self.Image_comboBox_axis_scale.setItemText(1, _translate("Form", "XZ", None))
        self.Image_comboBox_axis_scale.setItemText(2, _translate("Form", "YZ", None))
        self.Image_comboBox_axis_scale.setItemText(3, _translate("Form", "X", None))
        self.Image_comboBox_axis_scale.setItemText(4, _translate("Form", "Y", None))
        self.Image_comboBox_axis_scale.setItemText(5, _translate("Form", "Z", None))
        self.length_image.setToolTip(_translate("Form", "Desired length(s).", None))
        self.length_image.setText(_translate("Form", "100.0", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_2), _translate("Form", "Image", None))
        self.button_alignface2view.setToolTip(_translate("Form", "Align the face of selected object(s)  to the actual view Plane.\n"
" - Click first to select a Face of one or several objects.\n"
"These objects will be moved not the point of view.\n"
"Then Click the button.\n"
"\n"
"NB:\n"
"  The center of rotation is the center of the bounbing box if possible or \n"
"  the center of the Face.\n"
" \n"
"  if the Face of the object selected is already aligned to the  view Plane,\n"
"  a rotation of 180 deg is applied to the object.\n"
"  In this case the Axis of rotation is Z vector : Base.Vector(0, 0, 1)\n"
"\n"
"  Two clicks will rotate by 180 deg the moving objects.\n"
"\n"
"", None))
        self.button_alignface2view.setText(_translate("Form", "Align Face to View", None))
        self.button_align_faces.setToolTip(_translate("Form", "Align the Face(s) from selected object(s) to the last Face selected.\n"
" - Click first to select a Face of an object or several Faces from several objects. \n"
"These objects will be moved.\n"
" - Click second to select a Face to align to (the last object is fixed and will never move).\n"
"Then Click the button.\n"
"\n"
"NB:\n"
"  The center of rotation is the center of the bounbing box if possible or \n"
"  the center of the Face.\n"
" \n"
"  if the Face of the object selected is already aligned to the last one,\n"
"  a rotation of 180 deg is applied to the object.\n"
"  In this case the Axis of rotation is Z vector : Base.Vector(0, 0, 1)\n"
"\n"
"  Two clicks will rotate by 180 deg the moving objects.\n"
"", None))
        self.button_align_faces.setText(_translate("Form", "Align Faces", None))
        self.angle_align_faces.setToolTip(_translate("Form", "This Angle  (in degrees) will be added to the angle needed to align Faces.", None))
        self.angle_align_faces.setText(_translate("Form", "0.0", None))
        self.button_align_edges.setToolTip(_translate("Form", "Align the Edge(s) from selected object(s) to the last Edge selected.\n"
" - Click first to select an Edge of an object or several Edges from several objects. \n"
"These objects will be moved.\n"
" - Click second to select an Edge to align to  (the last object is fixed and will never move).\n"
"Then Click the button.\n"
"\n"
"NB:\n"
"  The center of rotation is the center of the bounbing box if possible or \n"
"  the center of the Edge.\n"
" \n"
"  if the Edge of the object selected is already aligned to the last one,\n"
"  a rotation of 180 deg is applied to the object.\n"
"  In this case the Axis of rotation is Z vector : Base.Vector(0, 0, 1)\n"
"\n"
"  Two clicks will rotate by 180 deg the moving objects.\n"
"", None))
        self.button_align_edges.setText(_translate("Form", "Align Edges", None))
        self.angle_align_edges.setToolTip(_translate("Form", "This Angle  (in degrees) will be added to the angle needed to align Edges.", None))
        self.angle_align_edges.setText(_translate("Form", "0.0", None))
        self.button_align_main_axis.setToolTip(_translate("Form", "Align the main Axis (first of the 2 axis set) from selected object(s) to the last Edge (or 2 main Axis from an object) selected.\n"
" - Click first to select at least one object! \n"
"This or These first object(s) will be rotated.\n"
" - Click last to select an Edge (or an Object) to align to (this last object is fixed and will never move).\n"
"Then Click the button.\n"
"\n"
"NB:\n"
"  The 2 main first axis are calculated using scan and sort from all axis of the object.\n"
"  The center of rotation is at center mass location of each selected object.\n"
"\n"
"  In case of several objects selection : \n"
"    The 2 main Axis of the first object(s) will be aligned on the 2 main Axis of the last one.\n"
"  In case of several objects selection plus one Edge :\n"
"     The first main Axis of the object(s) will be aligned on the Edge.\n"
" \n"
" -  One click will align first main Axes.\n"
" -  Second click will also align the second main Axes if exists on last object or\n"
"  will rotate by 180 deg the moving objects on first main axes.\n"
" -  Third and following clicks will rotate by 180 deg the moving objects on first main axes.", None))
        self.button_align_main_axis.setText(_translate("Form", "Align Main Axis", None))
        self.angle_align_main_axis.setToolTip(_translate("Form", "This Angle  (in degrees) will be added to the angle needed to align Edges.", None))
        self.angle_align_main_axis.setText(_translate("Form", "0.0", None))
        self.button_joint_points.setToolTip(_translate("Form", "Joint Point(s) from selected object(s) to the last Point selected.\n"
" - Click first to select a Point of an object or several Points from several objects.\n"
"These objects will be moved. \n"
" - Click second to select an Point to joint to (the last object is fixed and will never move).\n"
"Then Click the button.\n"
"\n"
"", None))
        self.button_joint_points.setText(_translate("Form", "Joint Points", None))
        self.button_joint_faces.setToolTip(_translate("Form", "Joint Face(s) from selected object(s) to the last Face selected.\n"
" - Click first to select a Face of an object or several Faces from several objects. \n"
"These objects will be moved.\n"
" - Click second to select a Face to joint to (the last object is fixed and will never move).\n"
"Then Click the button.\n"
"\n"
"  Two clicks will rotate by 180 deg the moving objects.\n"
"", None))
        self.button_joint_faces.setText(_translate("Form", "Joint Faces", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.align_tab_2), _translate("Form", "Align", None))
        self.groupBox_20.setTitle(_translate("Form", "Object", None))
        self.button_cut_select_object.setToolTip(_translate("Form", "Select the Object to cut:\n"
"First Click on the object in the view \n"
"and push this button to accept...", None))
        self.button_cut_select_object.setText(_translate("Form", "Select Object", None))
        self.button_cut_select_line.setToolTip(_translate("Form", "Select the Line to cut the Object along:\n"
"First Click on the line/edge in the view \n"
"and push this button to accept...", None))
        self.button_cut_select_line.setText(_translate("Form", "Select Cut Line", None))
        self.button_cut_select_plane.setToolTip(_translate("Form", "Select the Reference Plane to cut the Object from:\n"
"First Click on the plane in the view \n"
"and push this button to accept...\n"
"\n"
"The Reference Plane is the Plane you pose the object on before to use a saw! \n"
"(Note that the Angle is calculated from the Normal at this Plane)", None))
        self.button_cut_select_plane.setText(_translate("Form", "Select Ref. Plane", None))
        self.label_angle_3.setToolTip(_translate("Form", "Angle of cutting  relative to the Normal of the Reference Plane (in degrees).\n"
"\n"
"  0.0 means that the Plane of cutting is along the Cut Line with \n"
"a 90 deg angle with Reference Plane.", None))
        self.label_angle_3.setText(_translate("Form", "Angle", None))
        self.angle_cut_object.setToolTip(_translate("Form", "Angle of cutting  relative to the Normal of the Reference Plane (in degrees).\n"
"\n"
"  0.0 means that the Plane of cutting is along the Cut Line with \n"
"a 90 deg angle with Reference Plane.", None))
        self.angle_cut_object.setText(_translate("Form", "0.0", None))
        self.label_thickness_2.setToolTip(_translate("Form", "Thickness of the Cut.\n"
"\n"
"i.e. the thickness of a saw.", None))
        self.label_thickness_2.setText(_translate("Form", "Thickness", None))
        self.thickness_cut_object.setToolTip(_translate("Form", "Thickness of the Cut.\n"
"\n"
"i.e. the thickness of a saw.", None))
        self.thickness_cut_object.setText(_translate("Form", "0.0", None))
        self.button_cut_reset.setText(_translate("Form", "Reset", None))
        self.button_cut_apply.setToolTip(_translate("Form", "Cut an object by selecting a Line cut, a Plane and an Angle regarding the Plane.", None))
        self.button_cut_apply.setText(_translate("Form", "Apply", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.cut_tab_2), _translate("Form", "Cut", None))
        self.ObjRot_button_select.setToolTip(_translate("Form", "- Select one or several object(s) in the view and \n"
"- Click on this button.\n"
"\n"
"NB\n"
"Once object(s) are selected an other Click will unselect them !\n"
"Selected Object(s) will be displayed with 75% of transparency.", None))
        self.ObjRot_button_select.setText(_translate("Form", "Select Object(s)", None))
        self.ObjRot_comboBox_axis.setItemText(0, _translate("Form", "X", None))
        self.ObjRot_comboBox_axis.setItemText(1, _translate("Form", "Y", None))
        self.ObjRot_comboBox_axis.setItemText(2, _translate("Form", "Z", None))
        self.ObjRot_comboBox_axis.setItemText(3, _translate("Form", "To select", None))
        self.ObjRot_button_select_axis.setText(_translate("Form", "Select", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_18), _translate("Form", "Axis", None))
        self.ObjRot_comboBox_center.setItemText(0, _translate("Form", "Origin", None))
        self.ObjRot_comboBox_center.setItemText(1, _translate("Form", "Base Obj.", None))
        self.ObjRot_comboBox_center.setItemText(2, _translate("Form", "Center Obj.(s)", None))
        self.ObjRot_comboBox_center.setItemText(3, _translate("Form", "To select", None))
        self.ObjRot_button_select_center.setText(_translate("Form", "Select", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_19), _translate("Form", "Center", None))
        self.groupBox_21.setTitle(_translate("Form", "Angle of rotation :", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_20), _translate("Form", "Define", None))
        self.ObjRot_button_select_angle.setToolTip(_translate("Form", "Calculate angle from 2 objects.\n"
"Angle measurement between two Edges or two Planes\n"
"- Select the 2 Edges and\n"
"- Click this button\n"
"or\n"
"- Select the 2 Planes and\n"
"- Click this button\n"
"or\n"
"- Select one Edge and one Plane and\n"
"- Click this button\n"
"\n"
"NB:\n"
"  Normals of Planes will be used.    ", None))
        self.ObjRot_button_select_angle.setText(_translate("Form", "Select", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_21), _translate("Form", "Select", None))
        self.ObjRot_lineEdit_angle.setText(_translate("Form", "0.0", None))
        self.label_angle_4.setText(_translate("Form", " (deg)", None))
        self.ObjRot_button_reset.setText(_translate("Form", "Reset", None))
        self.ObjRot_button_apply.setText(_translate("Form", "Apply", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.rotate_tab_2), _translate("Form", "Rotate", None))
        self.ObjTrans_button_select.setToolTip(_translate("Form", "- Select one or several object(s) in the view and \n"
"- Click on this button.\n"
"\n"
"NB\n"
"Once object(s) are selected an other Click will unselect them !\n"
"Selected Object(s) will be displayed with 75% of transparency.", None))
        self.ObjTrans_button_select.setText(_translate("Form", "Select Object(s)", None))
        self.ObjTrans_duplicate.setToolTip(_translate("Form", "Toggle this check box to generate copies the object during the Translation.\n"
"Copy means that the original Object will be left in his original location.\n"
"NB:\n"
"\n"
"1 copy requested : \n"
" - If one starting point and one ending point are selected.\n"
"   Only one copy is done!\n"
"\n"
" - If one starting point and several ending points are selected.\n"
"   One copy is done at each ending points selected!\n"
"\n"
"N copies requested :\n"
" - If one starting point and one ending point are selected.\n"
"   Only one copy is done at the ending point then at double distance\n"
"  of the ending point along the line defined by starting and ending point,\n"
"  and so on!\n"
" - If one starting point and several ending points are selected.\n"
"  One copy is done at each ending points selected, then at double distance\n"
"  of each ending points along the line defined by starting and the current \n"
"  ending point,  and so on!", None))
        self.ObjTrans_duplicate.setText(_translate("Form", "Copy", None))
        self.ObjTrans_spin.setToolTip(_translate("Form", "The number of copies.", None))
        self.ObjTrans_deepCopy.setToolTip(_translate("Form", "Toggle this check box to realize \"deep\" copies. \n"
"Means that all children and parents of selected Object(s) will be copied too! \n"
"\n"
"If the object selected is Pad and his link is on Sketch, and Skecth parent is Box\n"
"Box \n"
"Pad \n"
"   |_Sketch\n"
"\n"
"if the current check box is toggle the result will be : \n"
"Box \n"
"Pad\n"
"   |_Sketch \n"
"Box001 \n"
"Pad001 \n"
"   |_Sketch001 \n"
"\n"
"if not the result will be : \n"
"Box \n"
"Pad \n"
"Pad001 \n"
"   |_Sketch \n"
"\n"
"On the last result the same Sketch is both link to Pad001 but also still to Pad.", None))
        self.ObjTrans_deepCopy.setText(_translate("Form", "Deep", None))
        self.ObjTrans_button_reset.setText(_translate("Form", "Reset", None))
        self.ObjTrans_button_apply.setText(_translate("Form", "Apply", None))
        self.groupBox_22.setTitle(_translate("Form", "Starting Point :", None))
        self.ObjTrans_comboBox_start.setToolTip(_translate("Form", "<html><head/><body><p>Choose here your starting Point(s)</p><p>it can be either:</p><p>  - The Origin point (0,0,0),</p><p>  - The Base point of the selected object(s),</p><p>  - The Center point of the selected object(s),</p><p>  - One selected Point by mouse</p><p>  - One of the extrema of One Segment/Edge</p><p>  - A user defined Points<br/></p></body></html>", None))
        self.ObjTrans_comboBox_start.setItemText(0, _translate("Form", "Origin", None))
        self.ObjTrans_comboBox_start.setItemText(1, _translate("Form", "Base Obj.", None))
        self.ObjTrans_comboBox_start.setItemText(2, _translate("Form", "Center Obj.(s)", None))
        self.ObjTrans_comboBox_start.setItemText(3, _translate("Form", "To select", None))
        self.ObjTrans_comboBox_start.setItemText(4, _translate("Form", "From Segment", None))
        self.ObjTrans_comboBox_start.setItemText(5, _translate("Form", "To define", None))
        self.ObjTrans_button_select_start.setToolTip(_translate("Form", "<html><head/><body><p>Once Point(s) or one Segment selected;</p><p>Click this button to activate the selection !</p></body></html>", None))
        self.ObjTrans_button_select_start.setText(_translate("Form", "Select", None))
        self.label_11.setText(_translate("Form", "X :", None))
        self.ObjTrans_start_x.setToolTip(_translate("Form", "Please Enter a new coordinate and type RETURN to validate!", None))
        self.ObjTrans_start_x.setText(_translate("Form", "0.0", None))
        self.label_12.setText(_translate("Form", "Y :", None))
        self.ObjTrans_start_y.setToolTip(_translate("Form", "Please Enter a new coordinate and type RETURN to validate!", None))
        self.ObjTrans_start_y.setText(_translate("Form", "0.0", None))
        self.label_13.setText(_translate("Form", "Z :", None))
        self.ObjTrans_start_z.setToolTip(_translate("Form", "Please Enter a new coordinate and type RETURN to validate!", None))
        self.ObjTrans_start_z.setText(_translate("Form", "0.0", None))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_22), _translate("Form", "Start", None))
        self.groupBox_23.setTitle(_translate("Form", "Ending Point :", None))
        self.ObjTrans_comboBox_end.setItemText(0, _translate("Form", "Origin", None))
        self.ObjTrans_comboBox_end.setItemText(1, _translate("Form", "Base Obj.", None))
        self.ObjTrans_comboBox_end.setItemText(2, _translate("Form", "Center Obj.(s)", None))
        self.ObjTrans_comboBox_end.setItemText(3, _translate("Form", "To select", None))
        self.ObjTrans_comboBox_end.setItemText(4, _translate("Form", "To define", None))
        self.ObjTrans_comboBox_end.setItemText(5, _translate("Form", "Relative", None))
        self.ObjTrans_button_select_end.setToolTip(_translate("Form", "<html><head/><body><p>Once Point(s) selected;</p><p>Click this button to activate the selection !</p></body></html>", None))
        self.ObjTrans_button_select_end.setText(_translate("Form", "Select", None))
        self.label_14.setText(_translate("Form", "Z :", None))
        self.ObjTrans_end_z.setToolTip(_translate("Form", "Please Enter a new coordinate and type RETURN to validate!", None))
        self.ObjTrans_end_z.setText(_translate("Form", "0.0", None))
        self.label_15.setText(_translate("Form", "Y :", None))
        self.ObjTrans_end_y.setToolTip(_translate("Form", "Please Enter a new coordinate and type RETURN to validate!", None))
        self.ObjTrans_end_y.setText(_translate("Form", "0.0", None))
        self.label_16.setText(_translate("Form", "X :", None))
        self.ObjTrans_end_x.setToolTip(_translate("Form", "Please Enter a new coordinate and type RETURN to validate!", None))
        self.ObjTrans_end_x.setText(_translate("Form", "0.0", None))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_23), _translate("Form", "End", None))
        self.ObjTrans_horizontalSlider.setToolTip(_translate("Form", "<html><head/><body><p>Once a Segment(s) is selected as starting Point(s),</p><p>This slider define the ending Point(s) by defining the relative distance from the starting Point(s).</p><p>Slider values are : -1000% to 1000%</p><p>100% mean full length of the Segment(s) with one ends as starting point(s)</p><p>-100% mean full length of the Segment(s) by reversing the starting Point(s)</p><p>0% means you do not Translate your selected Object(s)</p><p><br/></p></body></html>", None))
        self.ObjTrans_lineEdit_length_seg.setToolTip(_translate("Form", "<html><head/><body><p>Enter here a more precise value :</p><p>100% mean full length of the Segment(s) with one ends as starting point(s)</p><p>-100% mean full length of the Segment(s) by reversing the starting Point(s)</p><p>Maximum values allowed [-1000, 1000]</p></body></html>", None))
        self.ObjTrans_lineEdit_length_seg.setText(_translate("Form", "100.0", None))
        self.label_length_segment.setText(_translate("Form", " (%)", None))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab), _translate("Form", "Seg.", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.translate_tab_2), _translate("Form", "Translate", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.Modif_Tab_2), _translate("Form", "Modif.", None))
        self.button_alignview.setToolTip(_translate("Form", "Set the current view perpendicular to the selected Face, \n"
"or aligned to the selected Axis, \n"
"or aligned on 2 Points.\n"
"ReClick with same selection, will reverse the direction.", None))
        self.button_alignview.setText(_translate("Form", "Align View to ...", None))
        self.button_trackcamera.setText(_translate("Form", "Camera Track", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.View_Tab_2), _translate("Form", "View", None))
        self.button_isView.setToolTip(_translate("Form", "Detect the position of the camera.\n"
"The returned value is the value provided \n"
"by the function getCameraOrientation().", None))
        self.button_isView.setText(_translate("Form", "View ?", None))
        self.button_isParallel.setToolTip(_translate("Form", "Check if two faces or two Edges are Parallel:\n"
"- Select the 2 faces/planes or 2 Edges/Lines and\n"
"Click this button\n"
"\n"
"NB: You can change the tolerance in \"Ori. Pref.\"  TAB", None))
        self.button_isParallel.setText(_translate("Form", "are Parallel ?", None))
        self.button_isAngle.setToolTip(_translate("Form", "Check for two Edges/Planes angle:\n"
"Angle measurement between two Edges or two Planes\n"
"- Select the 2 Edges and\n"
"- Click this button\n"
"or\n"
"- Select the 2 Planes and\n"
"- Click this button\n"
"or\n"
"- Select one Edge and one Plane and\n"
"- Click this button\n"
"\n"
"NB:\n"
"  Normals of Planes will be used.     ", None))
        self.button_isAngle.setText(_translate("Form", "Angle ?", None))
        self.button_isLength.setToolTip(_translate("Form", "Check for Line Length:\n"
"Length measurement and Delta values (on main Axes) for a Line\n"
"- Select the Line and\n"
"Click this button\n"
" ", None))
        self.button_isLength.setText(_translate("Form", "Length ?", None))
        self.button_isDistance.setToolTip(_translate("Form", "Check for two Points distance:\n"
"Distances measurement and Delta values (on main Axes) between two Points\n"
"- Select the 2 Points and\n"
"Click this button\n"
" ", None))
        self.button_isDistance.setText(_translate("Form", "Distance ?", None))
        self.button_isCoplanar.setToolTip(_translate("Form", "Check if two faces or two Edges are Coplanar:\n"
"- Select the 2 faces/planes or 2 Edges/Lines and\n"
"Click this button\n"
"\n"
"NB: You can change the tolerance in \"Ori. Pref.\"  TAB", None))
        self.button_isCoplanar.setText(_translate("Form", "are Coplanar ?", None))
        self.button_isArea.setToolTip(_translate("Form", "Check for surface Area:\n"
"Area measurement for a Plane or a set of Planes.\n"
"- Select One or several Planes and\n"
"- Then click this button", None))
        self.button_isArea.setText(_translate("Form", "Area ?", None))
        self.button_isPerpendicular.setToolTip(_translate("Form", "Check if two faces or two Edges are Perpendicular:\n"
"- Select the 2 faces/planes or 2 Edges/Lines and\n"
"Click this button\n"
"\n"
"NB: You can change the tolerance in \"Ori. Pref.\"  TAB", None))
        self.button_isPerpendicular.setText(_translate("Form", "are Perpendicular ?", None))
        self.button_isClearance.setToolTip(_translate("Form", "Check for two Objects Clearance distance:\n"
"Quick measurements between parallel faces and similarly placed objects\n"
"- Select the 2 Objects and\n"
"Click this button", None))
        self.button_isClearance.setText(_translate("Form", "Distance Clearance ?", None))
        self.button_isRadius.setToolTip(_translate("Form", "Check for Radius:\n"
"Radius measurement for a Circle or an Arc.\n"
"- Select One Circle or Arc\n"
"- Then click this button", None))
        self.button_isRadius.setText(_translate("Form", "Radius ?", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_24), _translate("Form", "Check", None))
        self.button_WF_quit.setText(_translate("Form", "Close", None))
        self.label_release.setText(_translate("Form", "2015", None))

