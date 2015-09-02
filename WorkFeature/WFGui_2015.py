# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WFGui_2015_08_31.ui'
#
# Created: Mon Aug 31 22:01:38 2015
#      by: PySide UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(364, 693)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_Axes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_34 = QtGui.QGridLayout(Form)
        self.gridLayout_34.setObjectName(_fromUtf8("gridLayout_34"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 344, 638))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.tabWidget_0 = QtGui.QTabWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget_0.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget_0.setObjectName(_fromUtf8("tabWidget_0"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_30 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_30.setObjectName(_fromUtf8("gridLayout_30"))
        self.tabWidget = QtGui.QTabWidget(self.tab_2)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Origin_Tab = QtGui.QWidget()
        self.Origin_Tab.setObjectName(_fromUtf8("Origin_Tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.Origin_Tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.button_origin = QtGui.QPushButton(self.Origin_Tab)
        self.button_origin.setIcon(icon)
        self.button_origin.setIconSize(QtCore.QSize(32, 32))
        self.button_origin.setObjectName(_fromUtf8("button_origin"))
        self.gridLayout_5.addWidget(self.button_origin, 0, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.Origin_Tab)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_14 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.groupBox_5 = QtGui.QGroupBox(self.frame_3)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.radioButton_verbose = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_verbose.setChecked(False)
        self.radioButton_verbose.setAutoExclusive(False)
        self.radioButton_verbose.setObjectName(_fromUtf8("radioButton_verbose"))
        self.gridLayout_3.addWidget(self.radioButton_verbose, 0, 0, 1, 1)
        self.radioButton_biColor = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_biColor.setAutoExclusive(False)
        self.radioButton_biColor.setObjectName(_fromUtf8("radioButton_biColor"))
        self.gridLayout_3.addWidget(self.radioButton_biColor, 1, 0, 1, 1)
        self.radioButton_copy = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_copy.setObjectName(_fromUtf8("radioButton_copy"))
        self.gridLayout_3.addWidget(self.radioButton_copy, 2, 0, 1, 1)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_25.addWidget(self.label_5)
        self.tolerance_edit = QtGui.QLineEdit(self.groupBox_5)
        self.tolerance_edit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.tolerance_edit.setObjectName(_fromUtf8("tolerance_edit"))
        self.horizontalLayout_25.addWidget(self.tolerance_edit)
        self.gridLayout_3.addLayout(self.horizontalLayout_25, 3, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_3, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 2, 0, 1, 1)
        self.tabWidget.addTab(self.Origin_Tab, icon, _fromUtf8(""))
        self.Point_Tab1 = QtGui.QWidget()
        self.Point_Tab1.setObjectName(_fromUtf8("Point_Tab1"))
        self.gridLayout_7 = QtGui.QGridLayout(self.Point_Tab1)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.button_point_line_point = QtGui.QPushButton(self.Point_Tab1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_line_point.setIcon(icon1)
        self.button_point_line_point.setIconSize(QtCore.QSize(32, 32))
        self.button_point_line_point.setObjectName(_fromUtf8("button_point_line_point"))
        self.gridLayout_7.addWidget(self.button_point_line_point, 8, 0, 1, 1)
        self.button_face_center = QtGui.QPushButton(self.Point_Tab1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerFacePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_face_center.setIcon(icon2)
        self.button_face_center.setIconSize(QtCore.QSize(32, 32))
        self.button_face_center.setObjectName(_fromUtf8("button_face_center"))
        self.gridLayout_7.addWidget(self.button_face_center, 5, 0, 1, 1)
        self.button_circle_center = QtGui.QPushButton(self.Point_Tab1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerCirclePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_circle_center.setIcon(icon3)
        self.button_circle_center.setIconSize(QtCore.QSize(32, 32))
        self.button_circle_center.setObjectName(_fromUtf8("button_circle_center"))
        self.gridLayout_7.addWidget(self.button_circle_center, 4, 0, 1, 1)
        self.button_Npoints_center = QtGui.QPushButton(self.Point_Tab1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_NpointsPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_Npoints_center.setIcon(icon4)
        self.button_Npoints_center.setIconSize(QtCore.QSize(32, 32))
        self.button_Npoints_center.setObjectName(_fromUtf8("button_Npoints_center"))
        self.gridLayout_7.addWidget(self.button_Npoints_center, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.button_line_center = QtGui.QPushButton(self.Point_Tab1)
        self.button_line_center.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_center.setIcon(icon5)
        self.button_line_center.setIconSize(QtCore.QSize(32, 32))
        self.button_line_center.setObjectName(_fromUtf8("button_line_center"))
        self.horizontalLayout_6.addWidget(self.button_line_center)
        self.spin_line_center = QtGui.QSpinBox(self.Point_Tab1)
        self.spin_line_center.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_line_center.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_line_center.setMinimum(2)
        self.spin_line_center.setMaximum(100)
        self.spin_line_center.setSingleStep(1)
        self.spin_line_center.setObjectName(_fromUtf8("spin_line_center"))
        self.horizontalLayout_6.addWidget(self.spin_line_center)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.button_line_face_point = QtGui.QPushButton(self.Point_Tab1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_lineFacePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_face_point.setIcon(icon6)
        self.button_line_face_point.setIconSize(QtCore.QSize(32, 32))
        self.button_line_face_point.setObjectName(_fromUtf8("button_line_face_point"))
        self.gridLayout_7.addWidget(self.button_line_face_point, 6, 0, 1, 1)
        self.button_line_extrema = QtGui.QPushButton(self.Point_Tab1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_extremaLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_extrema.setIcon(icon7)
        self.button_line_extrema.setIconSize(QtCore.QSize(32, 32))
        self.button_line_extrema.setObjectName(_fromUtf8("button_line_extrema"))
        self.gridLayout_7.addWidget(self.button_line_extrema, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem1, 9, 0, 1, 1)
        self.button_point_face_point = QtGui.QPushButton(self.Point_Tab1)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointFacePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_face_point.setIcon(icon8)
        self.button_point_face_point.setIconSize(QtCore.QSize(32, 32))
        self.button_point_face_point.setObjectName(_fromUtf8("button_point_face_point"))
        self.gridLayout_7.addWidget(self.button_point_face_point, 7, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.button_object_center = QtGui.QPushButton(self.Point_Tab1)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerObjectsPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_center.setIcon(icon9)
        self.button_object_center.setIconSize(QtCore.QSize(32, 32))
        self.button_object_center.setObjectName(_fromUtf8("button_object_center"))
        self.horizontalLayout_10.addWidget(self.button_object_center)
        self.checkBox_object_center = QtGui.QCheckBox(self.Point_Tab1)
        self.checkBox_object_center.setObjectName(_fromUtf8("checkBox_object_center"))
        self.horizontalLayout_10.addWidget(self.checkBox_object_center)
        self.gridLayout_7.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_point.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Point_Tab1, icon10, _fromUtf8(""))
        self.Point_Tab2 = QtGui.QWidget()
        self.Point_Tab2.setObjectName(_fromUtf8("Point_Tab2"))
        self.gridLayout_31 = QtGui.QGridLayout(self.Point_Tab2)
        self.gridLayout_31.setObjectName(_fromUtf8("gridLayout_31"))
        self.button_twolines_point = QtGui.QPushButton(self.Point_Tab2)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_lineLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_twolines_point.setIcon(icon11)
        self.button_twolines_point.setIconSize(QtCore.QSize(32, 32))
        self.button_twolines_point.setObjectName(_fromUtf8("button_twolines_point"))
        self.gridLayout_31.addWidget(self.button_twolines_point, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button_point_on_line = QtGui.QPushButton(self.Point_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_point_on_line.sizePolicy().hasHeightForWidth())
        self.button_point_on_line.setSizePolicy(sizePolicy)
        self.button_point_on_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_alongLinePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_on_line.setIcon(icon12)
        self.button_point_on_line.setIconSize(QtCore.QSize(32, 32))
        self.button_point_on_line.setObjectName(_fromUtf8("button_point_on_line"))
        self.horizontalLayout.addWidget(self.button_point_on_line)
        self.distance_point_on_line = QtGui.QLineEdit(self.Point_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distance_point_on_line.sizePolicy().hasHeightForWidth())
        self.distance_point_on_line.setSizePolicy(sizePolicy)
        self.distance_point_on_line.setMinimumSize(QtCore.QSize(50, 0))
        self.distance_point_on_line.setMaximumSize(QtCore.QSize(60, 16777215))
        self.distance_point_on_line.setObjectName(_fromUtf8("distance_point_on_line"))
        self.horizontalLayout.addWidget(self.distance_point_on_line)
        self.gridLayout_31.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.button_distPoint = QtGui.QPushButton(self.Point_Tab2)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_distPointPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_distPoint.setIcon(icon13)
        self.button_distPoint.setIconSize(QtCore.QSize(32, 32))
        self.button_distPoint.setObjectName(_fromUtf8("button_distPoint"))
        self.horizontalLayout_30.addWidget(self.button_distPoint)
        self.dist_point = QtGui.QLineEdit(self.Point_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dist_point.sizePolicy().hasHeightForWidth())
        self.dist_point.setSizePolicy(sizePolicy)
        self.dist_point.setMinimumSize(QtCore.QSize(40, 0))
        self.dist_point.setMaximumSize(QtCore.QSize(40, 16777215))
        self.dist_point.setObjectName(_fromUtf8("dist_point"))
        self.horizontalLayout_30.addWidget(self.dist_point)
        self.spin_dist_point = QtGui.QSpinBox(self.Point_Tab2)
        self.spin_dist_point.setMinimumSize(QtCore.QSize(30, 0))
        self.spin_dist_point.setMaximumSize(QtCore.QSize(30, 16777215))
        self.spin_dist_point.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spin_dist_point.setKeyboardTracking(False)
        self.spin_dist_point.setMinimum(1)
        self.spin_dist_point.setMaximum(100)
        self.spin_dist_point.setSingleStep(1)
        self.spin_dist_point.setProperty("value", 1)
        self.spin_dist_point.setObjectName(_fromUtf8("spin_dist_point"))
        self.horizontalLayout_30.addWidget(self.spin_dist_point)
        self.gridLayout_31.addLayout(self.horizontalLayout_30, 2, 0, 1, 1)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.button_cut_wire_point = QtGui.QPushButton(self.Point_Tab2)
        self.button_cut_wire_point.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cutWirePoints.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cut_wire_point.setIcon(icon14)
        self.button_cut_wire_point.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_wire_point.setObjectName(_fromUtf8("button_cut_wire_point"))
        self.horizontalLayout_27.addWidget(self.button_cut_wire_point)
        self.spin_wire_cut_point = QtGui.QSpinBox(self.Point_Tab2)
        self.spin_wire_cut_point.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_wire_cut_point.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_wire_cut_point.setMinimum(2)
        self.spin_wire_cut_point.setMaximum(100)
        self.spin_wire_cut_point.setSingleStep(1)
        self.spin_wire_cut_point.setObjectName(_fromUtf8("spin_wire_cut_point"))
        self.horizontalLayout_27.addWidget(self.spin_wire_cut_point)
        self.gridLayout_31.addLayout(self.horizontalLayout_27, 3, 0, 1, 1)
        self.button_click_for_point = QtGui.QRadioButton(self.Point_Tab2)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_clickPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_click_for_point.setIcon(icon15)
        self.button_click_for_point.setIconSize(QtCore.QSize(32, 32))
        self.button_click_for_point.setCheckable(True)
        self.button_click_for_point.setObjectName(_fromUtf8("button_click_for_point"))
        self.gridLayout_31.addWidget(self.button_click_for_point, 4, 0, 1, 1)
        self.button_object_base_point = QtGui.QPushButton(self.Point_Tab2)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectBasePoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_base_point.setIcon(icon16)
        self.button_object_base_point.setIconSize(QtCore.QSize(32, 32))
        self.button_object_base_point.setObjectName(_fromUtf8("button_object_base_point"))
        self.gridLayout_31.addWidget(self.button_object_base_point, 5, 0, 1, 1)
        self.button_point_to_sketch = QtGui.QPushButton(self.Point_Tab2)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_2Sketch.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_to_sketch.setIcon(icon17)
        self.button_point_to_sketch.setIconSize(QtCore.QSize(32, 32))
        self.button_point_to_sketch.setObjectName(_fromUtf8("button_point_to_sketch"))
        self.gridLayout_31.addWidget(self.button_point_to_sketch, 6, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_31.addItem(spacerItem2, 7, 0, 1, 1)
        self.tabWidget.addTab(self.Point_Tab2, icon10, _fromUtf8(""))
        self.Axis_Tab1 = QtGui.QWidget()
        self.Axis_Tab1.setObjectName(_fromUtf8("Axis_Tab1"))
        self.gridLayout_32 = QtGui.QGridLayout(self.Axis_Tab1)
        self.gridLayout_32.setObjectName(_fromUtf8("gridLayout_32"))
        self.button_object_axis = QtGui.QPushButton(self.Axis_Tab1)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerObjectsAxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_axis.setIcon(icon18)
        self.button_object_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_object_axis.setObjectName(_fromUtf8("button_object_axis"))
        self.gridLayout_32.addWidget(self.button_object_axis, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.button_twopoints_axis = QtGui.QPushButton(self.Axis_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_twopoints_axis.sizePolicy().hasHeightForWidth())
        self.button_twopoints_axis.setSizePolicy(sizePolicy)
        self.button_twopoints_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_2pointsLine.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_twopoints_axis.setIcon(icon19)
        self.button_twopoints_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_twopoints_axis.setObjectName(_fromUtf8("button_twopoints_axis"))
        self.horizontalLayout_2.addWidget(self.button_twopoints_axis)
        self.extension_twopoints_axis = QtGui.QLineEdit(self.Axis_Tab1)
        self.extension_twopoints_axis.setMaximumSize(QtCore.QSize(40, 16777215))
        self.extension_twopoints_axis.setObjectName(_fromUtf8("extension_twopoints_axis"))
        self.horizontalLayout_2.addWidget(self.extension_twopoints_axis)
        self.gridLayout_32.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.button_cylinder_axis = QtGui.QPushButton(self.Axis_Tab1)
        self.button_cylinder_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cylinderAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cylinder_axis.setIcon(icon20)
        self.button_cylinder_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_cylinder_axis.setObjectName(_fromUtf8("button_cylinder_axis"))
        self.verticalLayout.addWidget(self.button_cylinder_axis)
        self.button_plane_axis = QtGui.QPushButton(self.Axis_Tab1)
        self.button_plane_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_FaceAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_plane_axis.setIcon(icon21)
        self.button_plane_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_plane_axis.setObjectName(_fromUtf8("button_plane_axis"))
        self.verticalLayout.addWidget(self.button_plane_axis)
        self.button_face_normal = QtGui.QPushButton(self.Axis_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_face_normal.sizePolicy().hasHeightForWidth())
        self.button_face_normal.setSizePolicy(sizePolicy)
        self.button_face_normal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_FaceNormal.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_face_normal.setIcon(icon22)
        self.button_face_normal.setIconSize(QtCore.QSize(32, 32))
        self.button_face_normal.setObjectName(_fromUtf8("button_face_normal"))
        self.verticalLayout.addWidget(self.button_face_normal)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.frame_4 = QtGui.QFrame(self.Axis_Tab1)
        self.frame_4.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout = QtGui.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.extension_face_normal = QtGui.QLineEdit(self.frame_4)
        self.extension_face_normal.setMinimumSize(QtCore.QSize(40, 0))
        self.extension_face_normal.setMaximumSize(QtCore.QSize(40, 16777215))
        self.extension_face_normal.setObjectName(_fromUtf8("extension_face_normal"))
        self.gridLayout.addWidget(self.extension_face_normal, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_4)
        self.gridLayout_32.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.button_point_line_axis = QtGui.QPushButton(self.Axis_Tab1)
        self.button_point_line_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointLineAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_point_line_axis.setIcon(icon23)
        self.button_point_line_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_point_line_axis.setObjectName(_fromUtf8("button_point_line_axis"))
        self.horizontalLayout_18.addWidget(self.button_point_line_axis)
        self.extension_line = QtGui.QLineEdit(self.Axis_Tab1)
        self.extension_line.setMaximumSize(QtCore.QSize(40, 16777215))
        self.extension_line.setObjectName(_fromUtf8("extension_line"))
        self.horizontalLayout_18.addWidget(self.extension_line)
        self.point_loc_comboBox = QtGui.QComboBox(self.Axis_Tab1)
        self.point_loc_comboBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.point_loc_comboBox.setObjectName(_fromUtf8("point_loc_comboBox"))
        self.point_loc_comboBox.addItem(_fromUtf8(""))
        self.point_loc_comboBox.addItem(_fromUtf8(""))
        self.point_loc_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_18.addWidget(self.point_loc_comboBox)
        self.gridLayout_32.addLayout(self.horizontalLayout_18, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.button_line_point_axis = QtGui.QPushButton(self.Axis_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_line_point_axis.sizePolicy().hasHeightForWidth())
        self.button_line_point_axis.setSizePolicy(sizePolicy)
        self.button_line_point_axis.setMinimumSize(QtCore.QSize(0, 0))
        self.button_line_point_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePointAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_point_axis.setIcon(icon24)
        self.button_line_point_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_line_point_axis.setObjectName(_fromUtf8("button_line_point_axis"))
        self.horizontalLayout_7.addWidget(self.button_line_point_axis)
        self.extension_line_point_axis = QtGui.QLineEdit(self.Axis_Tab1)
        self.extension_line_point_axis.setMaximumSize(QtCore.QSize(40, 16777215))
        self.extension_line_point_axis.setObjectName(_fromUtf8("extension_line_point_axis"))
        self.horizontalLayout_7.addWidget(self.extension_line_point_axis)
        self.gridLayout_32.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        self.button_twolines_axis = QtGui.QPushButton(self.Axis_Tab1)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_twoLinesAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_twolines_axis.setIcon(icon25)
        self.button_twolines_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_twolines_axis.setObjectName(_fromUtf8("button_twolines_axis"))
        self.gridLayout_32.addWidget(self.button_twolines_axis, 5, 0, 1, 1)
        self.button_plane_point_line_axis = QtGui.QPushButton(self.Axis_Tab1)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_planeLinePointAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_plane_point_line_axis.setIcon(icon26)
        self.button_plane_point_line_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_plane_point_line_axis.setObjectName(_fromUtf8("button_plane_point_line_axis"))
        self.gridLayout_32.addWidget(self.button_plane_point_line_axis, 6, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_32.addItem(spacerItem3, 7, 0, 1, 1)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_axis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Axis_Tab1, icon27, _fromUtf8(""))
        self.Axis_Tab2 = QtGui.QWidget()
        self.Axis_Tab2.setObjectName(_fromUtf8("Axis_Tab2"))
        self.gridLayout_33 = QtGui.QGridLayout(self.Axis_Tab2)
        self.gridLayout_33.setObjectName(_fromUtf8("gridLayout_33"))
        self.button_line_plane_axis = QtGui.QPushButton(self.Axis_Tab2)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePlaneAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_line_plane_axis.setIcon(icon28)
        self.button_line_plane_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_line_plane_axis.setObjectName(_fromUtf8("button_line_plane_axis"))
        self.gridLayout_33.addWidget(self.button_line_plane_axis, 0, 0, 1, 1)
        self.button_twoplanes_axis = QtGui.QPushButton(self.Axis_Tab2)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_2PlanesAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_twoplanes_axis.setIcon(icon29)
        self.button_twoplanes_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_twoplanes_axis.setObjectName(_fromUtf8("button_twoplanes_axis"))
        self.gridLayout_33.addWidget(self.button_twoplanes_axis, 1, 0, 1, 1)
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.button_distLine = QtGui.QPushButton(self.Axis_Tab2)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_distAxisAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_distLine.setIcon(icon30)
        self.button_distLine.setIconSize(QtCore.QSize(32, 32))
        self.button_distLine.setObjectName(_fromUtf8("button_distLine"))
        self.horizontalLayout_29.addWidget(self.button_distLine)
        self.dist_line = QtGui.QLineEdit(self.Axis_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dist_line.sizePolicy().hasHeightForWidth())
        self.dist_line.setSizePolicy(sizePolicy)
        self.dist_line.setMinimumSize(QtCore.QSize(40, 0))
        self.dist_line.setMaximumSize(QtCore.QSize(40, 16777215))
        self.dist_line.setObjectName(_fromUtf8("dist_line"))
        self.horizontalLayout_29.addWidget(self.dist_line)
        self.spin_dist_line = QtGui.QSpinBox(self.Axis_Tab2)
        self.spin_dist_line.setMinimumSize(QtCore.QSize(30, 0))
        self.spin_dist_line.setMaximumSize(QtCore.QSize(30, 16777215))
        self.spin_dist_line.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spin_dist_line.setKeyboardTracking(False)
        self.spin_dist_line.setMinimum(1)
        self.spin_dist_line.setMaximum(100)
        self.spin_dist_line.setSingleStep(1)
        self.spin_dist_line.setProperty("value", 1)
        self.spin_dist_line.setObjectName(_fromUtf8("spin_dist_line"))
        self.horizontalLayout_29.addWidget(self.spin_dist_line)
        self.gridLayout_33.addLayout(self.horizontalLayout_29, 2, 0, 1, 1)
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.button_angleLine = QtGui.QPushButton(self.Axis_Tab2)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_angleAxisAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_angleLine.setIcon(icon31)
        self.button_angleLine.setIconSize(QtCore.QSize(32, 32))
        self.button_angleLine.setObjectName(_fromUtf8("button_angleLine"))
        self.horizontalLayout_31.addWidget(self.button_angleLine)
        self.angle_line = QtGui.QLineEdit(self.Axis_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_line.sizePolicy().hasHeightForWidth())
        self.angle_line.setSizePolicy(sizePolicy)
        self.angle_line.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_line.setMaximumSize(QtCore.QSize(40, 16777215))
        self.angle_line.setObjectName(_fromUtf8("angle_line"))
        self.horizontalLayout_31.addWidget(self.angle_line)
        self.spin_angle_line = QtGui.QSpinBox(self.Axis_Tab2)
        self.spin_angle_line.setMinimumSize(QtCore.QSize(30, 0))
        self.spin_angle_line.setMaximumSize(QtCore.QSize(30, 16777215))
        self.spin_angle_line.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spin_angle_line.setKeyboardTracking(False)
        self.spin_angle_line.setMinimum(1)
        self.spin_angle_line.setMaximum(100)
        self.spin_angle_line.setSingleStep(1)
        self.spin_angle_line.setProperty("value", 1)
        self.spin_angle_line.setObjectName(_fromUtf8("spin_angle_line"))
        self.horizontalLayout_31.addWidget(self.spin_angle_line)
        self.gridLayout_33.addLayout(self.horizontalLayout_31, 3, 0, 1, 1)
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.button_cut_wire_axis = QtGui.QPushButton(self.Axis_Tab2)
        self.button_cut_wire_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cutWireAxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cut_wire_axis.setIcon(icon32)
        self.button_cut_wire_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_wire_axis.setObjectName(_fromUtf8("button_cut_wire_axis"))
        self.horizontalLayout_26.addWidget(self.button_cut_wire_axis)
        self.spin_wire_cut_axis = QtGui.QSpinBox(self.Axis_Tab2)
        self.spin_wire_cut_axis.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_wire_cut_axis.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_wire_cut_axis.setMinimum(2)
        self.spin_wire_cut_axis.setMaximum(100)
        self.spin_wire_cut_axis.setSingleStep(1)
        self.spin_wire_cut_axis.setObjectName(_fromUtf8("spin_wire_cut_axis"))
        self.horizontalLayout_26.addWidget(self.spin_wire_cut_axis)
        self.gridLayout_33.addLayout(self.horizontalLayout_26, 4, 0, 1, 1)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.button_cut_axis = QtGui.QPushButton(self.Axis_Tab2)
        self.button_cut_axis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cutAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cut_axis.setIcon(icon33)
        self.button_cut_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_axis.setObjectName(_fromUtf8("button_cut_axis"))
        self.horizontalLayout_21.addWidget(self.button_cut_axis)
        self.spin_axis_cut = QtGui.QSpinBox(self.Axis_Tab2)
        self.spin_axis_cut.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_axis_cut.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_axis_cut.setMinimum(2)
        self.spin_axis_cut.setMaximum(100)
        self.spin_axis_cut.setSingleStep(1)
        self.spin_axis_cut.setObjectName(_fromUtf8("spin_axis_cut"))
        self.horizontalLayout_21.addWidget(self.spin_axis_cut)
        self.gridLayout_33.addLayout(self.horizontalLayout_21, 5, 0, 1, 1)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.button_extension_axis = QtGui.QPushButton(self.Axis_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_extension_axis.sizePolicy().hasHeightForWidth())
        self.button_extension_axis.setSizePolicy(sizePolicy)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_enlargeLine.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_extension_axis.setIcon(icon34)
        self.button_extension_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_extension_axis.setObjectName(_fromUtf8("button_extension_axis"))
        self.horizontalLayout_22.addWidget(self.button_extension_axis)
        self.extension_axis = QtGui.QLineEdit(self.Axis_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extension_axis.sizePolicy().hasHeightForWidth())
        self.extension_axis.setSizePolicy(sizePolicy)
        self.extension_axis.setMinimumSize(QtCore.QSize(40, 0))
        self.extension_axis.setMaximumSize(QtCore.QSize(50, 16777215))
        self.extension_axis.setObjectName(_fromUtf8("extension_axis"))
        self.horizontalLayout_22.addWidget(self.extension_axis)
        self.gridLayout_33.addLayout(self.horizontalLayout_22, 6, 0, 1, 1)
        self.button_click_for_axis = QtGui.QRadioButton(self.Axis_Tab2)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_clickLine.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_click_for_axis.setIcon(icon35)
        self.button_click_for_axis.setIconSize(QtCore.QSize(32, 32))
        self.button_click_for_axis.setObjectName(_fromUtf8("button_click_for_axis"))
        self.gridLayout_33.addWidget(self.button_click_for_axis, 7, 0, 1, 1)
        self.button_object_base_axes = QtGui.QPushButton(self.Axis_Tab2)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_baseObjectsAxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_base_axes.setIcon(icon36)
        self.button_object_base_axes.setIconSize(QtCore.QSize(32, 32))
        self.button_object_base_axes.setObjectName(_fromUtf8("button_object_base_axes"))
        self.gridLayout_33.addWidget(self.button_object_base_axes, 8, 0, 1, 1)
        self.button_line_to_sketch = QtGui.QPushButton(self.Axis_Tab2)
        self.button_line_to_sketch.setIcon(icon17)
        self.button_line_to_sketch.setIconSize(QtCore.QSize(32, 32))
        self.button_line_to_sketch.setObjectName(_fromUtf8("button_line_to_sketch"))
        self.gridLayout_33.addWidget(self.button_line_to_sketch, 9, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_33.addItem(spacerItem4, 10, 0, 1, 1)
        self.tabWidget.addTab(self.Axis_Tab2, icon27, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_22 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.button_linecenter_circle = QtGui.QPushButton(self.tab_4)
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_lineCenterCircle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_linecenter_circle.setIcon(icon37)
        self.button_linecenter_circle.setIconSize(QtCore.QSize(32, 32))
        self.button_linecenter_circle.setObjectName(_fromUtf8("button_linecenter_circle"))
        self.horizontalLayout_11.addWidget(self.button_linecenter_circle)
        self.radius_circle = QtGui.QLineEdit(self.tab_4)
        self.radius_circle.setMinimumSize(QtCore.QSize(40, 0))
        self.radius_circle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.radius_circle.setObjectName(_fromUtf8("radius_circle"))
        self.horizontalLayout_11.addWidget(self.radius_circle)
        self.gridLayout_22.addLayout(self.horizontalLayout_11, 0, 0, 1, 2)
        self.button_linepoint_circle = QtGui.QPushButton(self.tab_4)
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePointCircle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_linepoint_circle.setIcon(icon38)
        self.button_linepoint_circle.setIconSize(QtCore.QSize(32, 32))
        self.button_linepoint_circle.setObjectName(_fromUtf8("button_linepoint_circle"))
        self.gridLayout_22.addWidget(self.button_linepoint_circle, 1, 0, 1, 2)
        self.button_3points_circle = QtGui.QPushButton(self.tab_4)
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_3pointsCircle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_3points_circle.setIcon(icon39)
        self.button_3points_circle.setIconSize(QtCore.QSize(32, 32))
        self.button_3points_circle.setObjectName(_fromUtf8("button_3points_circle"))
        self.gridLayout_22.addWidget(self.button_3points_circle, 2, 0, 1, 2)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.button_cut_circle = QtGui.QPushButton(self.tab_4)
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cutCircle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cut_circle.setIcon(icon40)
        self.button_cut_circle.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_circle.setObjectName(_fromUtf8("button_cut_circle"))
        self.horizontalLayout_24.addWidget(self.button_cut_circle)
        self.spin_circle_cut = QtGui.QSpinBox(self.tab_4)
        self.spin_circle_cut.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_circle_cut.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_circle_cut.setMinimum(2)
        self.spin_circle_cut.setMaximum(100)
        self.spin_circle_cut.setSingleStep(1)
        self.spin_circle_cut.setObjectName(_fromUtf8("spin_circle_cut"))
        self.horizontalLayout_24.addWidget(self.spin_circle_cut)
        self.gridLayout_22.addLayout(self.horizontalLayout_24, 3, 0, 1, 2)
        self.button_3points_ellipse = QtGui.QPushButton(self.tab_4)
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_3pointsEllipse.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_3points_ellipse.setIcon(icon41)
        self.button_3points_ellipse.setIconSize(QtCore.QSize(32, 32))
        self.button_3points_ellipse.setObjectName(_fromUtf8("button_3points_ellipse"))
        self.gridLayout_22.addWidget(self.button_3points_ellipse, 4, 0, 1, 2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem5, 5, 0, 1, 1)
        self.button_circle_to_sketch = QtGui.QPushButton(self.tab_4)
        self.button_circle_to_sketch.setIcon(icon17)
        self.button_circle_to_sketch.setIconSize(QtCore.QSize(32, 32))
        self.button_circle_to_sketch.setObjectName(_fromUtf8("button_circle_to_sketch"))
        self.gridLayout_22.addWidget(self.button_circle_to_sketch, 6, 0, 1, 2)
        spacerItem6 = QtGui.QSpacerItem(20, 121, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem6, 7, 1, 1, 1)
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_circle.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon42, _fromUtf8(""))
        self.Plane_Tab1 = QtGui.QWidget()
        self.Plane_Tab1.setObjectName(_fromUtf8("Plane_Tab1"))
        self.gridLayout_4 = QtGui.QGridLayout(self.Plane_Tab1)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 9, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.button_click_for_plane = QtGui.QPushButton(self.Plane_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_click_for_plane.sizePolicy().hasHeightForWidth())
        self.button_click_for_plane.setSizePolicy(sizePolicy)
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_clickPlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_click_for_plane.setIcon(icon43)
        self.button_click_for_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_click_for_plane.setObjectName(_fromUtf8("button_click_for_plane"))
        self.horizontalLayout_3.addWidget(self.button_click_for_plane)
        self.length_plane = QtGui.QLineEdit(self.Plane_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length_plane.sizePolicy().hasHeightForWidth())
        self.length_plane.setSizePolicy(sizePolicy)
        self.length_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.length_plane.setMaximumSize(QtCore.QSize(50, 16777215))
        self.length_plane.setObjectName(_fromUtf8("length_plane"))
        self.horizontalLayout_3.addWidget(self.length_plane)
        self.width_plane = QtGui.QLineEdit(self.Plane_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_plane.sizePolicy().hasHeightForWidth())
        self.width_plane.setSizePolicy(sizePolicy)
        self.width_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.width_plane.setMaximumSize(QtCore.QSize(50, 16777215))
        self.width_plane.setObjectName(_fromUtf8("width_plane"))
        self.horizontalLayout_3.addWidget(self.width_plane)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.button_planeandaxis_plane = QtGui.QPushButton(self.Plane_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_planeandaxis_plane.sizePolicy().hasHeightForWidth())
        self.button_planeandaxis_plane.setSizePolicy(sizePolicy)
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_planeLinePlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_planeandaxis_plane.setIcon(icon44)
        self.button_planeandaxis_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_planeandaxis_plane.setObjectName(_fromUtf8("button_planeandaxis_plane"))
        self.gridLayout_8.addWidget(self.button_planeandaxis_plane, 0, 0, 1, 1)
        self.angle_planeandaxis_plane = QtGui.QLineEdit(self.Plane_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_planeandaxis_plane.sizePolicy().hasHeightForWidth())
        self.angle_planeandaxis_plane.setSizePolicy(sizePolicy)
        self.angle_planeandaxis_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_planeandaxis_plane.setMaximumSize(QtCore.QSize(60, 16777215))
        self.angle_planeandaxis_plane.setObjectName(_fromUtf8("angle_planeandaxis_plane"))
        self.gridLayout_8.addWidget(self.angle_planeandaxis_plane, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_8, 4, 0, 1, 1)
        self.button_axisandpoint_plane = QtGui.QPushButton(self.Plane_Tab1)
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePointPlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_axisandpoint_plane.setIcon(icon45)
        self.button_axisandpoint_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_axisandpoint_plane.setObjectName(_fromUtf8("button_axisandpoint_plane"))
        self.gridLayout_4.addWidget(self.button_axisandpoint_plane, 1, 0, 1, 1)
        self.button_axis_point_plane = QtGui.QPushButton(self.Plane_Tab1)
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_linePointPlane2.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_axis_point_plane.setIcon(icon46)
        self.button_axis_point_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_axis_point_plane.setObjectName(_fromUtf8("button_axis_point_plane"))
        self.gridLayout_4.addWidget(self.button_axis_point_plane, 2, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.button_face_tangent = QtGui.QPushButton(self.Plane_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_face_tangent.sizePolicy().hasHeightForWidth())
        self.button_face_tangent.setSizePolicy(sizePolicy)
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_FaceTangent.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_face_tangent.setIcon(icon47)
        self.button_face_tangent.setIconSize(QtCore.QSize(32, 32))
        self.button_face_tangent.setObjectName(_fromUtf8("button_face_tangent"))
        self.horizontalLayout_12.addWidget(self.button_face_tangent)
        self.length_plane_2 = QtGui.QLineEdit(self.Plane_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length_plane_2.sizePolicy().hasHeightForWidth())
        self.length_plane_2.setSizePolicy(sizePolicy)
        self.length_plane_2.setMinimumSize(QtCore.QSize(40, 0))
        self.length_plane_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.length_plane_2.setObjectName(_fromUtf8("length_plane_2"))
        self.horizontalLayout_12.addWidget(self.length_plane_2)
        self.width_plane_2 = QtGui.QLineEdit(self.Plane_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_plane_2.sizePolicy().hasHeightForWidth())
        self.width_plane_2.setSizePolicy(sizePolicy)
        self.width_plane_2.setMinimumSize(QtCore.QSize(40, 0))
        self.width_plane_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.width_plane_2.setObjectName(_fromUtf8("width_plane_2"))
        self.horizontalLayout_12.addWidget(self.width_plane_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_12, 6, 0, 1, 1)
        self.button_threepoints_plane = QtGui.QPushButton(self.Plane_Tab1)
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_threePointsPlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_threepoints_plane.setIcon(icon48)
        self.button_threepoints_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_threepoints_plane.setObjectName(_fromUtf8("button_threepoints_plane"))
        self.gridLayout_4.addWidget(self.button_threepoints_plane, 0, 0, 1, 1)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.button_distPlane = QtGui.QPushButton(self.Plane_Tab1)
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_distPlanePlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_distPlane.setIcon(icon49)
        self.button_distPlane.setIconSize(QtCore.QSize(32, 32))
        self.button_distPlane.setObjectName(_fromUtf8("button_distPlane"))
        self.horizontalLayout_28.addWidget(self.button_distPlane)
        self.dist_plane = QtGui.QLineEdit(self.Plane_Tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dist_plane.sizePolicy().hasHeightForWidth())
        self.dist_plane.setSizePolicy(sizePolicy)
        self.dist_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.dist_plane.setMaximumSize(QtCore.QSize(40, 16777215))
        self.dist_plane.setObjectName(_fromUtf8("dist_plane"))
        self.horizontalLayout_28.addWidget(self.dist_plane)
        self.spin_dist_plane = QtGui.QSpinBox(self.Plane_Tab1)
        self.spin_dist_plane.setMinimumSize(QtCore.QSize(30, 0))
        self.spin_dist_plane.setMaximumSize(QtCore.QSize(30, 16777215))
        self.spin_dist_plane.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spin_dist_plane.setKeyboardTracking(False)
        self.spin_dist_plane.setMinimum(1)
        self.spin_dist_plane.setMaximum(100)
        self.spin_dist_plane.setSingleStep(1)
        self.spin_dist_plane.setProperty("value", 1)
        self.spin_dist_plane.setObjectName(_fromUtf8("spin_dist_plane"))
        self.horizontalLayout_28.addWidget(self.spin_dist_plane)
        self.gridLayout_4.addLayout(self.horizontalLayout_28, 5, 0, 1, 1)
        self.gridLayout_16 = QtGui.QGridLayout()
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.button_planeandpoint_plane = QtGui.QPushButton(self.Plane_Tab1)
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointPlanePlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_planeandpoint_plane.setIcon(icon50)
        self.button_planeandpoint_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_planeandpoint_plane.setObjectName(_fromUtf8("button_planeandpoint_plane"))
        self.gridLayout_16.addWidget(self.button_planeandpoint_plane, 0, 0, 1, 1)
        self.extension_planePointPlane = QtGui.QLineEdit(self.Plane_Tab1)
        self.extension_planePointPlane.setMinimumSize(QtCore.QSize(40, 0))
        self.extension_planePointPlane.setMaximumSize(QtCore.QSize(60, 16777215))
        self.extension_planePointPlane.setObjectName(_fromUtf8("extension_planePointPlane"))
        self.gridLayout_16.addWidget(self.extension_planePointPlane, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_16, 3, 0, 1, 1)
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_plane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Plane_Tab1, icon51, _fromUtf8(""))
        self.Plane_Tab11 = QtGui.QWidget()
        self.Plane_Tab11.setObjectName(_fromUtf8("Plane_Tab11"))
        self.gridLayout_37 = QtGui.QGridLayout(self.Plane_Tab11)
        self.gridLayout_37.setObjectName(_fromUtf8("gridLayout_37"))
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_37.addItem(spacerItem8, 2, 0, 1, 1)
        self.button_object_center_planes = QtGui.QPushButton(self.Plane_Tab11)
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_centerObjectsPlanes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object_center_planes.setIcon(icon52)
        self.button_object_center_planes.setIconSize(QtCore.QSize(32, 32))
        self.button_object_center_planes.setObjectName(_fromUtf8("button_object_center_planes"))
        self.gridLayout_37.addWidget(self.button_object_center_planes, 1, 0, 1, 1)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.button_extension_plane = QtGui.QPushButton(self.Plane_Tab11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_extension_plane.sizePolicy().hasHeightForWidth())
        self.button_extension_plane.setSizePolicy(sizePolicy)
        icon53 = QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_enlargePlane.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_extension_plane.setIcon(icon53)
        self.button_extension_plane.setIconSize(QtCore.QSize(32, 32))
        self.button_extension_plane.setObjectName(_fromUtf8("button_extension_plane"))
        self.horizontalLayout_17.addWidget(self.button_extension_plane)
        self.extension_plane = QtGui.QLineEdit(self.Plane_Tab11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extension_plane.sizePolicy().hasHeightForWidth())
        self.extension_plane.setSizePolicy(sizePolicy)
        self.extension_plane.setMinimumSize(QtCore.QSize(40, 0))
        self.extension_plane.setMaximumSize(QtCore.QSize(50, 16777215))
        self.extension_plane.setObjectName(_fromUtf8("extension_plane"))
        self.horizontalLayout_17.addWidget(self.extension_plane)
        self.gridLayout_37.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Plane_Tab11, icon51, _fromUtf8(""))
        self.Objects_Tab2 = QtGui.QWidget()
        self.Objects_Tab2.setEnabled(True)
        self.Objects_Tab2.setMinimumSize(QtCore.QSize(0, 0))
        self.Objects_Tab2.setObjectName(_fromUtf8("Objects_Tab2"))
        self.gridLayout_54 = QtGui.QGridLayout(self.Objects_Tab2)
        self.gridLayout_54.setObjectName(_fromUtf8("gridLayout_54"))
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setObjectName(_fromUtf8("horizontalLayout_35"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.button_boundingboxes = QtGui.QPushButton(self.Objects_Tab2)
        self.button_boundingboxes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_boundingBoxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_boundingboxes.setIcon(icon54)
        self.button_boundingboxes.setIconSize(QtCore.QSize(32, 32))
        self.button_boundingboxes.setObjectName(_fromUtf8("button_boundingboxes"))
        self.verticalLayout_2.addWidget(self.button_boundingboxes)
        self.button_boundingbox = QtGui.QPushButton(self.Objects_Tab2)
        self.button_boundingbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_boundingBox.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_boundingbox.setIcon(icon55)
        self.button_boundingbox.setIconSize(QtCore.QSize(32, 32))
        self.button_boundingbox.setObjectName(_fromUtf8("button_boundingbox"))
        self.verticalLayout_2.addWidget(self.button_boundingbox)
        self.horizontalLayout_35.addLayout(self.verticalLayout_2)
        self.checkBox_volumBB = QtGui.QCheckBox(self.Objects_Tab2)
        self.checkBox_volumBB.setMaximumSize(QtCore.QSize(60, 16777215))
        self.checkBox_volumBB.setObjectName(_fromUtf8("checkBox_volumBB"))
        self.horizontalLayout_35.addWidget(self.checkBox_volumBB)
        self.gridLayout_54.addLayout(self.horizontalLayout_35, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.Objects_Tab2)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_54.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.button_cylinder_create = QtGui.QPushButton(self.Objects_Tab2)
        icon56 = QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cylinder.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cylinder_create.setIcon(icon56)
        self.button_cylinder_create.setIconSize(QtCore.QSize(32, 32))
        self.button_cylinder_create.setObjectName(_fromUtf8("button_cylinder_create"))
        self.gridLayout_6.addWidget(self.button_cylinder_create, 0, 0, 1, 1)
        self.diameter_cylinder = QtGui.QLineEdit(self.Objects_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter_cylinder.sizePolicy().hasHeightForWidth())
        self.diameter_cylinder.setSizePolicy(sizePolicy)
        self.diameter_cylinder.setMinimumSize(QtCore.QSize(50, 0))
        self.diameter_cylinder.setMaximumSize(QtCore.QSize(60, 16777215))
        self.diameter_cylinder.setObjectName(_fromUtf8("diameter_cylinder"))
        self.gridLayout_6.addWidget(self.diameter_cylinder, 0, 1, 1, 1)
        self.length_cylinder = QtGui.QLineEdit(self.Objects_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length_cylinder.sizePolicy().hasHeightForWidth())
        self.length_cylinder.setSizePolicy(sizePolicy)
        self.length_cylinder.setMinimumSize(QtCore.QSize(50, 0))
        self.length_cylinder.setMaximumSize(QtCore.QSize(60, 16777215))
        self.length_cylinder.setObjectName(_fromUtf8("length_cylinder"))
        self.gridLayout_6.addWidget(self.length_cylinder, 0, 2, 1, 1)
        self.gridLayout_54.addLayout(self.gridLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.button_cube_create = QtGui.QPushButton(self.Objects_Tab2)
        icon57 = QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_cube.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cube_create.setIcon(icon57)
        self.button_cube_create.setIconSize(QtCore.QSize(32, 32))
        self.button_cube_create.setObjectName(_fromUtf8("button_cube_create"))
        self.horizontalLayout_4.addWidget(self.button_cube_create)
        self.section_cube = QtGui.QLineEdit(self.Objects_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.section_cube.sizePolicy().hasHeightForWidth())
        self.section_cube.setSizePolicy(sizePolicy)
        self.section_cube.setMinimumSize(QtCore.QSize(50, 0))
        self.section_cube.setMaximumSize(QtCore.QSize(60, 16777215))
        self.section_cube.setObjectName(_fromUtf8("section_cube"))
        self.horizontalLayout_4.addWidget(self.section_cube)
        self.height_cube = QtGui.QLineEdit(self.Objects_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_cube.sizePolicy().hasHeightForWidth())
        self.height_cube.setSizePolicy(sizePolicy)
        self.height_cube.setMinimumSize(QtCore.QSize(50, 0))
        self.height_cube.setMaximumSize(QtCore.QSize(60, 16777215))
        self.height_cube.setObjectName(_fromUtf8("height_cube"))
        self.horizontalLayout_4.addWidget(self.height_cube)
        self.gridLayout_54.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.button_sphere_create = QtGui.QPushButton(self.Objects_Tab2)
        icon58 = QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_sphere.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sphere_create.setIcon(icon58)
        self.button_sphere_create.setIconSize(QtCore.QSize(32, 32))
        self.button_sphere_create.setObjectName(_fromUtf8("button_sphere_create"))
        self.horizontalLayout_19.addWidget(self.button_sphere_create)
        self.diameter_sphere = QtGui.QLineEdit(self.Objects_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter_sphere.sizePolicy().hasHeightForWidth())
        self.diameter_sphere.setSizePolicy(sizePolicy)
        self.diameter_sphere.setMinimumSize(QtCore.QSize(50, 0))
        self.diameter_sphere.setMaximumSize(QtCore.QSize(60, 16777215))
        self.diameter_sphere.setObjectName(_fromUtf8("diameter_sphere"))
        self.horizontalLayout_19.addWidget(self.diameter_sphere)
        self.gridLayout_54.addLayout(self.horizontalLayout_19, 4, 0, 1, 1)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.button_dome_create = QtGui.QPushButton(self.Objects_Tab2)
        icon59 = QtGui.QIcon()
        icon59.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_dome.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_dome_create.setIcon(icon59)
        self.button_dome_create.setIconSize(QtCore.QSize(32, 32))
        self.button_dome_create.setObjectName(_fromUtf8("button_dome_create"))
        self.horizontalLayout_20.addWidget(self.button_dome_create)
        self.spin_frequency_dome = QtGui.QSpinBox(self.Objects_Tab2)
        self.spin_frequency_dome.setMinimumSize(QtCore.QSize(40, 0))
        self.spin_frequency_dome.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_frequency_dome.setMinimum(1)
        self.spin_frequency_dome.setMaximum(20)
        self.spin_frequency_dome.setSingleStep(1)
        self.spin_frequency_dome.setProperty("value", 2)
        self.spin_frequency_dome.setObjectName(_fromUtf8("spin_frequency_dome"))
        self.horizontalLayout_20.addWidget(self.spin_frequency_dome)
        self.diameter_dome = QtGui.QLineEdit(self.Objects_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter_dome.sizePolicy().hasHeightForWidth())
        self.diameter_dome.setSizePolicy(sizePolicy)
        self.diameter_dome.setMinimumSize(QtCore.QSize(50, 0))
        self.diameter_dome.setMaximumSize(QtCore.QSize(60, 16777215))
        self.diameter_dome.setObjectName(_fromUtf8("diameter_dome"))
        self.horizontalLayout_20.addWidget(self.diameter_dome)
        self.gridLayout_54.addLayout(self.horizontalLayout_20, 5, 0, 1, 1)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.button_letter = QtGui.QPushButton(self.Objects_Tab2)
        icon60 = QtGui.QIcon()
        icon60.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_pointText.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_letter.setIcon(icon60)
        self.button_letter.setIconSize(QtCore.QSize(32, 32))
        self.button_letter.setObjectName(_fromUtf8("button_letter"))
        self.horizontalLayout_23.addWidget(self.button_letter)
        self.letter = QtGui.QLineEdit(self.Objects_Tab2)
        self.letter.setMaximumSize(QtCore.QSize(70, 16777215))
        self.letter.setObjectName(_fromUtf8("letter"))
        self.horizontalLayout_23.addWidget(self.letter)
        self.size_letter = QtGui.QLineEdit(self.Objects_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.size_letter.sizePolicy().hasHeightForWidth())
        self.size_letter.setSizePolicy(sizePolicy)
        self.size_letter.setMinimumSize(QtCore.QSize(50, 0))
        self.size_letter.setMaximumSize(QtCore.QSize(50, 16777215))
        self.size_letter.setObjectName(_fromUtf8("size_letter"))
        self.horizontalLayout_23.addWidget(self.size_letter)
        self.gridLayout_54.addLayout(self.horizontalLayout_23, 6, 0, 1, 1)
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setObjectName(_fromUtf8("horizontalLayout_34"))
        self.button_revolve = QtGui.QPushButton(self.Objects_Tab2)
        icon61 = QtGui.QIcon()
        icon61.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_Revolve.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_revolve.setIcon(icon61)
        self.button_revolve.setIconSize(QtCore.QSize(32, 32))
        self.button_revolve.setObjectName(_fromUtf8("button_revolve"))
        self.horizontalLayout_34.addWidget(self.button_revolve)
        self.angle_revolve = QtGui.QLineEdit(self.Objects_Tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_revolve.sizePolicy().hasHeightForWidth())
        self.angle_revolve.setSizePolicy(sizePolicy)
        self.angle_revolve.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_revolve.setMaximumSize(QtCore.QSize(40, 16777215))
        self.angle_revolve.setObjectName(_fromUtf8("angle_revolve"))
        self.horizontalLayout_34.addWidget(self.angle_revolve)
        self.gridLayout_54.addLayout(self.horizontalLayout_34, 7, 0, 1, 1)
        self.frame_5 = QtGui.QFrame(self.Objects_Tab2)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setLineWidth(3)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_53 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_53.setObjectName(_fromUtf8("gridLayout_53"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.checkBox_allsubselect = QtGui.QCheckBox(self.frame_5)
        self.checkBox_allsubselect.setChecked(True)
        self.checkBox_allsubselect.setObjectName(_fromUtf8("checkBox_allsubselect"))
        self.gridLayout_12.addWidget(self.checkBox_allsubselect, 2, 0, 1, 1)
        self.transition_comboBox = QtGui.QComboBox(self.frame_5)
        self.transition_comboBox.setObjectName(_fromUtf8("transition_comboBox"))
        self.transition_comboBox.addItem(_fromUtf8(""))
        self.transition_comboBox.addItem(_fromUtf8(""))
        self.transition_comboBox.addItem(_fromUtf8(""))
        self.gridLayout_12.addWidget(self.transition_comboBox, 2, 1, 1, 1)
        self.checkBox_solid = QtGui.QCheckBox(self.frame_5)
        self.checkBox_solid.setMinimumSize(QtCore.QSize(9, 0))
        self.checkBox_solid.setMaximumSize(QtCore.QSize(60, 16777215))
        self.checkBox_solid.setChecked(True)
        self.checkBox_solid.setObjectName(_fromUtf8("checkBox_solid"))
        self.gridLayout_12.addWidget(self.checkBox_solid, 1, 0, 1, 1)
        self.radioButton_Frenet = QtGui.QRadioButton(self.frame_5)
        self.radioButton_Frenet.setChecked(True)
        self.radioButton_Frenet.setAutoExclusive(False)
        self.radioButton_Frenet.setObjectName(_fromUtf8("radioButton_Frenet"))
        self.gridLayout_12.addWidget(self.radioButton_Frenet, 1, 1, 1, 1)
        self.gridLayout_53.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.button_sweep = QtGui.QPushButton(self.frame_5)
        icon62 = QtGui.QIcon()
        icon62.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_Beam.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sweep.setIcon(icon62)
        self.button_sweep.setIconSize(QtCore.QSize(32, 32))
        self.button_sweep.setObjectName(_fromUtf8("button_sweep"))
        self.gridLayout_53.addWidget(self.button_sweep, 1, 0, 1, 1)
        self.gridLayout_54.addWidget(self.frame_5, 8, 0, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(17, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_54.addItem(spacerItem9, 9, 0, 1, 1)
        icon63 = QtGui.QIcon()
        icon63.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_box.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Objects_Tab2, icon63, _fromUtf8(""))
        self.Modif_Tab = QtGui.QWidget()
        self.Modif_Tab.setObjectName(_fromUtf8("Modif_Tab"))
        self.gridLayout_11 = QtGui.QGridLayout(self.Modif_Tab)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.tabWidget_2 = QtGui.QTabWidget(self.Modif_Tab)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.align_tab = QtGui.QWidget()
        self.align_tab.setObjectName(_fromUtf8("align_tab"))
        self.gridLayout_51 = QtGui.QGridLayout(self.align_tab)
        self.gridLayout_51.setObjectName(_fromUtf8("gridLayout_51"))
        self.button_alignface2view = QtGui.QPushButton(self.align_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_alignface2view.sizePolicy().hasHeightForWidth())
        self.button_alignface2view.setSizePolicy(sizePolicy)
        self.button_alignface2view.setMaximumSize(QtCore.QSize(220, 16777215))
        icon64 = QtGui.QIcon()
        icon64.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_viewAlignFace.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_alignface2view.setIcon(icon64)
        self.button_alignface2view.setIconSize(QtCore.QSize(32, 32))
        self.button_alignface2view.setObjectName(_fromUtf8("button_alignface2view"))
        self.gridLayout_51.addWidget(self.button_alignface2view, 0, 0, 1, 1)
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.button_align_faces = QtGui.QPushButton(self.align_tab)
        self.button_align_faces.setMaximumSize(QtCore.QSize(220, 16777215))
        icon65 = QtGui.QIcon()
        icon65.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectAlignFaces.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_align_faces.setIcon(icon65)
        self.button_align_faces.setIconSize(QtCore.QSize(32, 32))
        self.button_align_faces.setObjectName(_fromUtf8("button_align_faces"))
        self.horizontalLayout_32.addWidget(self.button_align_faces)
        self.angle_align_faces = QtGui.QLineEdit(self.align_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_align_faces.sizePolicy().hasHeightForWidth())
        self.angle_align_faces.setSizePolicy(sizePolicy)
        self.angle_align_faces.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_align_faces.setMaximumSize(QtCore.QSize(50, 16777215))
        self.angle_align_faces.setObjectName(_fromUtf8("angle_align_faces"))
        self.horizontalLayout_32.addWidget(self.angle_align_faces)
        self.gridLayout_51.addLayout(self.horizontalLayout_32, 1, 0, 1, 1)
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setObjectName(_fromUtf8("horizontalLayout_33"))
        self.button_align_edges = QtGui.QPushButton(self.align_tab)
        self.button_align_edges.setMaximumSize(QtCore.QSize(220, 16777215))
        icon66 = QtGui.QIcon()
        icon66.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectAlignAxes.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_align_edges.setIcon(icon66)
        self.button_align_edges.setIconSize(QtCore.QSize(32, 32))
        self.button_align_edges.setObjectName(_fromUtf8("button_align_edges"))
        self.horizontalLayout_33.addWidget(self.button_align_edges)
        self.angle_align_edges = QtGui.QLineEdit(self.align_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_align_edges.sizePolicy().hasHeightForWidth())
        self.angle_align_edges.setSizePolicy(sizePolicy)
        self.angle_align_edges.setMinimumSize(QtCore.QSize(40, 0))
        self.angle_align_edges.setMaximumSize(QtCore.QSize(50, 16777215))
        self.angle_align_edges.setObjectName(_fromUtf8("angle_align_edges"))
        self.horizontalLayout_33.addWidget(self.angle_align_edges)
        self.gridLayout_51.addLayout(self.horizontalLayout_33, 2, 0, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_51.addItem(spacerItem10, 5, 0, 1, 1)
        self.button_joint_points = QtGui.QPushButton(self.align_tab)
        icon67 = QtGui.QIcon()
        icon67.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectJointPoints.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_joint_points.setIcon(icon67)
        self.button_joint_points.setIconSize(QtCore.QSize(32, 32))
        self.button_joint_points.setObjectName(_fromUtf8("button_joint_points"))
        self.gridLayout_51.addWidget(self.button_joint_points, 3, 0, 1, 1)
        self.button_joint_faces = QtGui.QPushButton(self.align_tab)
        icon68 = QtGui.QIcon()
        icon68.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_objectJointFaces.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_joint_faces.setIcon(icon68)
        self.button_joint_faces.setIconSize(QtCore.QSize(32, 32))
        self.button_joint_faces.setObjectName(_fromUtf8("button_joint_faces"))
        self.gridLayout_51.addWidget(self.button_joint_faces, 4, 0, 1, 1)
        self.tabWidget_2.addTab(self.align_tab, _fromUtf8(""))
        self.cut_tab = QtGui.QWidget()
        self.cut_tab.setObjectName(_fromUtf8("cut_tab"))
        self.gridLayout_38 = QtGui.QGridLayout(self.cut_tab)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.frame_7 = QtGui.QFrame(self.cut_tab)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout_36 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_36.setObjectName(_fromUtf8("gridLayout_36"))
        self.groupBox_6 = QtGui.QGroupBox(self.frame_7)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_18 = QtGui.QGridLayout()
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.button_cut_select_object = QtGui.QPushButton(self.groupBox_6)
        self.button_cut_select_object.setMinimumSize(QtCore.QSize(130, 31))
        self.button_cut_select_object.setMaximumSize(QtCore.QSize(250, 40))
        self.button_cut_select_object.setObjectName(_fromUtf8("button_cut_select_object"))
        self.gridLayout_18.addWidget(self.button_cut_select_object, 0, 0, 1, 1)
        self.info_cut_select_object = QtGui.QLineEdit(self.groupBox_6)
        self.info_cut_select_object.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_cut_select_object.sizePolicy().hasHeightForWidth())
        self.info_cut_select_object.setSizePolicy(sizePolicy)
        self.info_cut_select_object.setReadOnly(True)
        self.info_cut_select_object.setObjectName(_fromUtf8("info_cut_select_object"))
        self.gridLayout_18.addWidget(self.info_cut_select_object, 1, 0, 1, 1)
        self.button_cut_select_line = QtGui.QPushButton(self.groupBox_6)
        self.button_cut_select_line.setEnabled(False)
        self.button_cut_select_line.setMinimumSize(QtCore.QSize(130, 31))
        self.button_cut_select_line.setMaximumSize(QtCore.QSize(250, 40))
        self.button_cut_select_line.setObjectName(_fromUtf8("button_cut_select_line"))
        self.gridLayout_18.addWidget(self.button_cut_select_line, 2, 0, 1, 1)
        self.info_cut_select_axis = QtGui.QLineEdit(self.groupBox_6)
        self.info_cut_select_axis.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_cut_select_axis.sizePolicy().hasHeightForWidth())
        self.info_cut_select_axis.setSizePolicy(sizePolicy)
        self.info_cut_select_axis.setReadOnly(True)
        self.info_cut_select_axis.setObjectName(_fromUtf8("info_cut_select_axis"))
        self.gridLayout_18.addWidget(self.info_cut_select_axis, 3, 0, 1, 1)
        self.button_cut_select_plane = QtGui.QPushButton(self.groupBox_6)
        self.button_cut_select_plane.setEnabled(False)
        self.button_cut_select_plane.setMinimumSize(QtCore.QSize(130, 31))
        self.button_cut_select_plane.setMaximumSize(QtCore.QSize(250, 40))
        self.button_cut_select_plane.setObjectName(_fromUtf8("button_cut_select_plane"))
        self.gridLayout_18.addWidget(self.button_cut_select_plane, 4, 0, 1, 1)
        self.info_cut_select_plane = QtGui.QLineEdit(self.groupBox_6)
        self.info_cut_select_plane.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_cut_select_plane.sizePolicy().hasHeightForWidth())
        self.info_cut_select_plane.setSizePolicy(sizePolicy)
        self.info_cut_select_plane.setReadOnly(True)
        self.info_cut_select_plane.setObjectName(_fromUtf8("info_cut_select_plane"))
        self.gridLayout_18.addWidget(self.info_cut_select_plane, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.gridLayout_17 = QtGui.QGridLayout()
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.gridLayout_19 = QtGui.QGridLayout()
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.label_angle = QtGui.QLabel(self.groupBox_6)
        self.label_angle.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_angle.setObjectName(_fromUtf8("label_angle"))
        self.gridLayout_19.addWidget(self.label_angle, 0, 0, 1, 1)
        self.angle_cut_object = QtGui.QLineEdit(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_cut_object.sizePolicy().hasHeightForWidth())
        self.angle_cut_object.setSizePolicy(sizePolicy)
        self.angle_cut_object.setMinimumSize(QtCore.QSize(0, 0))
        self.angle_cut_object.setMaximumSize(QtCore.QSize(50, 16777215))
        self.angle_cut_object.setObjectName(_fromUtf8("angle_cut_object"))
        self.gridLayout_19.addWidget(self.angle_cut_object, 0, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_19, 0, 0, 1, 1)
        self.gridLayout_20 = QtGui.QGridLayout()
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.label_thickness = QtGui.QLabel(self.groupBox_6)
        self.label_thickness.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_thickness.setObjectName(_fromUtf8("label_thickness"))
        self.gridLayout_20.addWidget(self.label_thickness, 0, 0, 1, 1)
        self.thickness_cut_object = QtGui.QLineEdit(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thickness_cut_object.sizePolicy().hasHeightForWidth())
        self.thickness_cut_object.setSizePolicy(sizePolicy)
        self.thickness_cut_object.setMaximumSize(QtCore.QSize(50, 16777215))
        self.thickness_cut_object.setObjectName(_fromUtf8("thickness_cut_object"))
        self.gridLayout_20.addWidget(self.thickness_cut_object, 0, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_20, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.button_cut_reset = QtGui.QPushButton(self.groupBox_6)
        self.button_cut_reset.setMinimumSize(QtCore.QSize(40, 0))
        self.button_cut_reset.setMaximumSize(QtCore.QSize(60, 16777215))
        self.button_cut_reset.setObjectName(_fromUtf8("button_cut_reset"))
        self.horizontalLayout_8.addWidget(self.button_cut_reset)
        spacerItem11 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.button_cut_apply = QtGui.QPushButton(self.groupBox_6)
        self.button_cut_apply.setEnabled(False)
        self.button_cut_apply.setMaximumSize(QtCore.QSize(50, 16777215))
        self.button_cut_apply.setIconSize(QtCore.QSize(32, 32))
        self.button_cut_apply.setObjectName(_fromUtf8("button_cut_apply"))
        self.horizontalLayout_8.addWidget(self.button_cut_apply)
        self.gridLayout_17.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_17, 1, 0, 1, 1)
        self.gridLayout_36.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.gridLayout_38.addWidget(self.frame_7, 0, 0, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_38.addItem(spacerItem12, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.cut_tab, _fromUtf8(""))
        self.rotate_tab = QtGui.QWidget()
        self.rotate_tab.setObjectName(_fromUtf8("rotate_tab"))
        self.gridLayout_52 = QtGui.QGridLayout(self.rotate_tab)
        self.gridLayout_52.setObjectName(_fromUtf8("gridLayout_52"))
        self.frame = QtGui.QFrame(self.rotate_tab)
        self.frame.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_50 = QtGui.QGridLayout(self.frame)
        self.gridLayout_50.setObjectName(_fromUtf8("gridLayout_50"))
        self.ObjRot_button_select = QtGui.QPushButton(self.frame)
        self.ObjRot_button_select.setObjectName(_fromUtf8("ObjRot_button_select"))
        self.gridLayout_50.addWidget(self.ObjRot_button_select, 0, 0, 1, 1)
        self.tabWidget_3 = QtGui.QTabWidget(self.frame)
        self.tabWidget_3.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.gridLayout_21 = QtGui.QGridLayout(self.tab_8)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.ObjRot_comboBox_axis = QtGui.QComboBox(self.tab_8)
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
        self.gridLayout_21.addWidget(self.ObjRot_comboBox_axis, 0, 0, 1, 1)
        self.ObjRot_button_select_axis = QtGui.QPushButton(self.tab_8)
        self.ObjRot_button_select_axis.setEnabled(False)
        self.ObjRot_button_select_axis.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_select_axis.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ObjRot_button_select_axis.setObjectName(_fromUtf8("ObjRot_button_select_axis"))
        self.gridLayout_21.addWidget(self.ObjRot_button_select_axis, 1, 0, 1, 1)
        icon69 = QtGui.QIcon()
        icon69.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_rotationAxis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_3.addTab(self.tab_8, icon69, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.gridLayout_23 = QtGui.QGridLayout(self.tab_9)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.ObjRot_comboBox_center = QtGui.QComboBox(self.tab_9)
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
        self.gridLayout_23.addWidget(self.ObjRot_comboBox_center, 0, 0, 1, 1)
        self.ObjRot_button_select_center = QtGui.QPushButton(self.tab_9)
        self.ObjRot_button_select_center.setEnabled(False)
        self.ObjRot_button_select_center.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_select_center.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ObjRot_button_select_center.setObjectName(_fromUtf8("ObjRot_button_select_center"))
        self.gridLayout_23.addWidget(self.ObjRot_button_select_center, 1, 0, 1, 1)
        icon70 = QtGui.QIcon()
        icon70.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_rotationPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_3.addTab(self.tab_9, icon70, _fromUtf8(""))
        self.gridLayout_50.addWidget(self.tabWidget_3, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setMinimumSize(QtCore.QSize(150, 67))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_29 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_29.setObjectName(_fromUtf8("gridLayout_29"))
        self.tabWidget_5 = QtGui.QTabWidget(self.groupBox_2)
        self.tabWidget_5.setObjectName(_fromUtf8("tabWidget_5"))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.gridLayout_25 = QtGui.QGridLayout(self.tab_7)
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        self.ObjRot_horizontalSlider = QtGui.QSlider(self.tab_7)
        self.ObjRot_horizontalSlider.setMinimumSize(QtCore.QSize(0, 39))
        self.ObjRot_horizontalSlider.setMaximumSize(QtCore.QSize(120, 16777215))
        self.ObjRot_horizontalSlider.setMinimum(-180)
        self.ObjRot_horizontalSlider.setMaximum(180)
        self.ObjRot_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ObjRot_horizontalSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.ObjRot_horizontalSlider.setTickInterval(20)
        self.ObjRot_horizontalSlider.setObjectName(_fromUtf8("ObjRot_horizontalSlider"))
        self.gridLayout_25.addWidget(self.ObjRot_horizontalSlider, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_7, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.gridLayout_24 = QtGui.QGridLayout(self.tab_10)
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.ObjRot_button_select_angle = QtGui.QPushButton(self.tab_10)
        self.ObjRot_button_select_angle.setEnabled(True)
        self.ObjRot_button_select_angle.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_select_angle.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ObjRot_button_select_angle.setObjectName(_fromUtf8("ObjRot_button_select_angle"))
        self.gridLayout_24.addWidget(self.ObjRot_button_select_angle, 0, 0, 1, 1)
        icon71 = QtGui.QIcon()
        icon71.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_click.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_5.addTab(self.tab_10, icon71, _fromUtf8(""))
        self.gridLayout_29.addWidget(self.tabWidget_5, 0, 0, 1, 1)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.ObjRot_lineEdit_angle = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ObjRot_lineEdit_angle.sizePolicy().hasHeightForWidth())
        self.ObjRot_lineEdit_angle.setSizePolicy(sizePolicy)
        self.ObjRot_lineEdit_angle.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_lineEdit_angle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjRot_lineEdit_angle.setMaxLength(32769)
        self.ObjRot_lineEdit_angle.setObjectName(_fromUtf8("ObjRot_lineEdit_angle"))
        self.horizontalLayout_13.addWidget(self.ObjRot_lineEdit_angle)
        self.label_angle_2 = QtGui.QLabel(self.groupBox_2)
        self.label_angle_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_angle_2.setObjectName(_fromUtf8("label_angle_2"))
        self.horizontalLayout_13.addWidget(self.label_angle_2)
        self.gridLayout_29.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)
        self.gridLayout_50.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.ObjRot_button_reset = QtGui.QPushButton(self.frame)
        self.ObjRot_button_reset.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_reset.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjRot_button_reset.setObjectName(_fromUtf8("ObjRot_button_reset"))
        self.horizontalLayout_14.addWidget(self.ObjRot_button_reset)
        spacerItem13 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.ObjRot_button_apply = QtGui.QPushButton(self.frame)
        self.ObjRot_button_apply.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjRot_button_apply.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjRot_button_apply.setObjectName(_fromUtf8("ObjRot_button_apply"))
        self.horizontalLayout_14.addWidget(self.ObjRot_button_apply)
        self.gridLayout_50.addLayout(self.horizontalLayout_14, 3, 0, 1, 1)
        self.gridLayout_52.addWidget(self.frame, 0, 0, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_52.addItem(spacerItem14, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.rotate_tab, _fromUtf8(""))
        self.translate_tab = QtGui.QWidget()
        self.translate_tab.setObjectName(_fromUtf8("translate_tab"))
        self.gridLayout_49 = QtGui.QGridLayout(self.translate_tab)
        self.gridLayout_49.setObjectName(_fromUtf8("gridLayout_49"))
        self.frame_2 = QtGui.QFrame(self.translate_tab)
        self.frame_2.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_48 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_48.setObjectName(_fromUtf8("gridLayout_48"))
        self.ObjTrans_button_select = QtGui.QPushButton(self.frame_2)
        self.ObjTrans_button_select.setObjectName(_fromUtf8("ObjTrans_button_select"))
        self.gridLayout_48.addWidget(self.ObjTrans_button_select, 0, 0, 1, 1)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.ObjTrans_duplicate = QtGui.QCheckBox(self.frame_2)
        self.ObjTrans_duplicate.setObjectName(_fromUtf8("ObjTrans_duplicate"))
        self.horizontalLayout_15.addWidget(self.ObjTrans_duplicate)
        self.ObjTrans_spin = QtGui.QSpinBox(self.frame_2)
        self.ObjTrans_spin.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjTrans_spin.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ObjTrans_spin.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.ObjTrans_spin.setKeyboardTracking(False)
        self.ObjTrans_spin.setMinimum(1)
        self.ObjTrans_spin.setMaximum(20)
        self.ObjTrans_spin.setSingleStep(1)
        self.ObjTrans_spin.setProperty("value", 1)
        self.ObjTrans_spin.setObjectName(_fromUtf8("ObjTrans_spin"))
        self.horizontalLayout_15.addWidget(self.ObjTrans_spin)
        self.ObjTrans_deepCopy = QtGui.QCheckBox(self.frame_2)
        self.ObjTrans_deepCopy.setObjectName(_fromUtf8("ObjTrans_deepCopy"))
        self.horizontalLayout_15.addWidget(self.ObjTrans_deepCopy)
        self.gridLayout_48.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)
        self.tabWidget_4 = QtGui.QTabWidget(self.frame_2)
        self.tabWidget_4.setObjectName(_fromUtf8("tabWidget_4"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_15 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_3.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_26 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_26.setObjectName(_fromUtf8("gridLayout_26"))
        self.ObjTrans_comboBox_start = QtGui.QComboBox(self.groupBox_3)
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
        self.gridLayout_26.addWidget(self.ObjTrans_comboBox_start, 0, 0, 1, 1)
        self.ObjTrans_button_select_start = QtGui.QPushButton(self.groupBox_3)
        self.ObjTrans_button_select_start.setEnabled(True)
        self.ObjTrans_button_select_start.setMinimumSize(QtCore.QSize(50, 0))
        self.ObjTrans_button_select_start.setMaximumSize(QtCore.QSize(120, 16777215))
        self.ObjTrans_button_select_start.setObjectName(_fromUtf8("ObjTrans_button_select_start"))
        self.gridLayout_26.addWidget(self.ObjTrans_button_select_start, 1, 0, 1, 1)
        self.gridLayout_27 = QtGui.QGridLayout()
        self.gridLayout_27.setObjectName(_fromUtf8("gridLayout_27"))
        self.gridLayout_28 = QtGui.QGridLayout()
        self.gridLayout_28.setObjectName(_fromUtf8("gridLayout_28"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_28.addWidget(self.label_3, 0, 0, 1, 1)
        self.ObjTrans_start_x = QtGui.QLineEdit(self.groupBox_3)
        self.ObjTrans_start_x.setEnabled(False)
        self.ObjTrans_start_x.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_start_x.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_start_x.setObjectName(_fromUtf8("ObjTrans_start_x"))
        self.gridLayout_28.addWidget(self.ObjTrans_start_x, 0, 1, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_28, 0, 0, 1, 1)
        self.gridLayout_40 = QtGui.QGridLayout()
        self.gridLayout_40.setObjectName(_fromUtf8("gridLayout_40"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_40.addWidget(self.label_4, 0, 0, 1, 1)
        self.ObjTrans_start_y = QtGui.QLineEdit(self.groupBox_3)
        self.ObjTrans_start_y.setEnabled(False)
        self.ObjTrans_start_y.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_start_y.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_start_y.setObjectName(_fromUtf8("ObjTrans_start_y"))
        self.gridLayout_40.addWidget(self.ObjTrans_start_y, 0, 1, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_40, 1, 0, 1, 1)
        self.gridLayout_41 = QtGui.QGridLayout()
        self.gridLayout_41.setObjectName(_fromUtf8("gridLayout_41"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_41.addWidget(self.label_6, 0, 0, 1, 1)
        self.ObjTrans_start_z = QtGui.QLineEdit(self.groupBox_3)
        self.ObjTrans_start_z.setEnabled(False)
        self.ObjTrans_start_z.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_start_z.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_start_z.setObjectName(_fromUtf8("ObjTrans_start_z"))
        self.gridLayout_41.addWidget(self.ObjTrans_start_z, 0, 1, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_41, 2, 0, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_27, 2, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_3, 0, 0, 1, 1)
        icon72 = QtGui.QIcon()
        icon72.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_startPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_4.addTab(self.tab_5, icon72, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridLayout_42 = QtGui.QGridLayout(self.tab_6)
        self.gridLayout_42.setObjectName(_fromUtf8("gridLayout_42"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_4.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_43 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_43.setObjectName(_fromUtf8("gridLayout_43"))
        self.ObjTrans_comboBox_end = QtGui.QComboBox(self.groupBox_4)
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
        self.gridLayout_43.addWidget(self.ObjTrans_comboBox_end, 0, 0, 1, 1)
        self.ObjTrans_button_select_end = QtGui.QPushButton(self.groupBox_4)
        self.ObjTrans_button_select_end.setEnabled(True)
        self.ObjTrans_button_select_end.setMinimumSize(QtCore.QSize(100, 0))
        self.ObjTrans_button_select_end.setMaximumSize(QtCore.QSize(120, 16777215))
        self.ObjTrans_button_select_end.setObjectName(_fromUtf8("ObjTrans_button_select_end"))
        self.gridLayout_43.addWidget(self.ObjTrans_button_select_end, 1, 0, 1, 1)
        self.gridLayout_44 = QtGui.QGridLayout()
        self.gridLayout_44.setObjectName(_fromUtf8("gridLayout_44"))
        self.gridLayout_45 = QtGui.QGridLayout()
        self.gridLayout_45.setObjectName(_fromUtf8("gridLayout_45"))
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_45.addWidget(self.label_7, 0, 0, 1, 1)
        self.ObjTrans_end_z = QtGui.QLineEdit(self.groupBox_4)
        self.ObjTrans_end_z.setEnabled(False)
        self.ObjTrans_end_z.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_end_z.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_end_z.setObjectName(_fromUtf8("ObjTrans_end_z"))
        self.gridLayout_45.addWidget(self.ObjTrans_end_z, 0, 1, 1, 1)
        self.gridLayout_44.addLayout(self.gridLayout_45, 2, 0, 1, 1)
        self.gridLayout_46 = QtGui.QGridLayout()
        self.gridLayout_46.setObjectName(_fromUtf8("gridLayout_46"))
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_46.addWidget(self.label_8, 0, 0, 1, 1)
        self.ObjTrans_end_y = QtGui.QLineEdit(self.groupBox_4)
        self.ObjTrans_end_y.setEnabled(False)
        self.ObjTrans_end_y.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_end_y.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_end_y.setObjectName(_fromUtf8("ObjTrans_end_y"))
        self.gridLayout_46.addWidget(self.ObjTrans_end_y, 0, 1, 1, 1)
        self.gridLayout_44.addLayout(self.gridLayout_46, 1, 0, 1, 1)
        self.gridLayout_47 = QtGui.QGridLayout()
        self.gridLayout_47.setObjectName(_fromUtf8("gridLayout_47"))
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_47.addWidget(self.label_9, 0, 0, 1, 1)
        self.ObjTrans_end_x = QtGui.QLineEdit(self.groupBox_4)
        self.ObjTrans_end_x.setEnabled(False)
        self.ObjTrans_end_x.setMinimumSize(QtCore.QSize(90, 0))
        self.ObjTrans_end_x.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ObjTrans_end_x.setObjectName(_fromUtf8("ObjTrans_end_x"))
        self.gridLayout_47.addWidget(self.ObjTrans_end_x, 0, 1, 1, 1)
        self.gridLayout_44.addLayout(self.gridLayout_47, 0, 0, 1, 1)
        self.gridLayout_43.addLayout(self.gridLayout_44, 2, 0, 1, 1)
        self.gridLayout_42.addWidget(self.groupBox_4, 0, 0, 1, 1)
        icon73 = QtGui.QIcon()
        icon73.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_endPoint.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_4.addTab(self.tab_6, icon73, _fromUtf8(""))
        self.gridLayout_48.addWidget(self.tabWidget_4, 2, 0, 1, 1)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.ObjTrans_button_reset = QtGui.QPushButton(self.frame_2)
        self.ObjTrans_button_reset.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjTrans_button_reset.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjTrans_button_reset.setObjectName(_fromUtf8("ObjTrans_button_reset"))
        self.horizontalLayout_16.addWidget(self.ObjTrans_button_reset)
        spacerItem15 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem15)
        self.ObjTrans_button_apply = QtGui.QPushButton(self.frame_2)
        self.ObjTrans_button_apply.setMinimumSize(QtCore.QSize(40, 0))
        self.ObjTrans_button_apply.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ObjTrans_button_apply.setObjectName(_fromUtf8("ObjTrans_button_apply"))
        self.horizontalLayout_16.addWidget(self.ObjTrans_button_apply)
        self.gridLayout_48.addLayout(self.horizontalLayout_16, 3, 0, 1, 1)
        self.gridLayout_49.addWidget(self.frame_2, 0, 0, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_49.addItem(spacerItem16, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.translate_tab, _fromUtf8(""))
        self.gridLayout_11.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Modif_Tab, _fromUtf8(""))
        self.View_Tab = QtGui.QWidget()
        self.View_Tab.setObjectName(_fromUtf8("View_Tab"))
        self.gridLayout_13 = QtGui.QGridLayout(self.View_Tab)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.button_alignview = QtGui.QPushButton(self.View_Tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_alignview.sizePolicy().hasHeightForWidth())
        self.button_alignview.setSizePolicy(sizePolicy)
        self.button_alignview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon74 = QtGui.QIcon()
        icon74.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_viewAlign.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_alignview.setIcon(icon74)
        self.button_alignview.setIconSize(QtCore.QSize(32, 32))
        self.button_alignview.setObjectName(_fromUtf8("button_alignview"))
        self.gridLayout_13.addWidget(self.button_alignview, 0, 0, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem17, 2, 0, 1, 1)
        self.button_trackcamera = QtGui.QPushButton(self.View_Tab)
        icon75 = QtGui.QIcon()
        icon75.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_trackCamera.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_trackcamera.setIcon(icon75)
        self.button_trackcamera.setIconSize(QtCore.QSize(32, 32))
        self.button_trackcamera.setObjectName(_fromUtf8("button_trackcamera"))
        self.gridLayout_13.addWidget(self.button_trackcamera, 1, 0, 1, 1)
        icon76 = QtGui.QIcon()
        icon76.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_view.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.View_Tab, icon76, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_35 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_35.setObjectName(_fromUtf8("gridLayout_35"))
        self.button_isView = QtGui.QPushButton(self.tab_3)
        icon77 = QtGui.QIcon()
        icon77.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_FCCamera_02.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isView.setIcon(icon77)
        self.button_isView.setIconSize(QtCore.QSize(32, 32))
        self.button_isView.setObjectName(_fromUtf8("button_isView"))
        self.gridLayout_35.addWidget(self.button_isView, 8, 0, 1, 1)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_35.addItem(spacerItem18, 9, 0, 1, 1)
        self.button_isCoplanar = QtGui.QPushButton(self.tab_3)
        icon78 = QtGui.QIcon()
        icon78.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isCoplanar.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isCoplanar.setIcon(icon78)
        self.button_isCoplanar.setIconSize(QtCore.QSize(32, 32))
        self.button_isCoplanar.setObjectName(_fromUtf8("button_isCoplanar"))
        self.gridLayout_35.addWidget(self.button_isCoplanar, 2, 0, 1, 1)
        self.button_isParallel = QtGui.QPushButton(self.tab_3)
        icon79 = QtGui.QIcon()
        icon79.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isParallel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isParallel.setIcon(icon79)
        self.button_isParallel.setIconSize(QtCore.QSize(32, 32))
        self.button_isParallel.setObjectName(_fromUtf8("button_isParallel"))
        self.gridLayout_35.addWidget(self.button_isParallel, 0, 0, 1, 1)
        self.button_isAngle = QtGui.QPushButton(self.tab_3)
        icon80 = QtGui.QIcon()
        icon80.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_angleBetween.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isAngle.setIcon(icon80)
        self.button_isAngle.setIconSize(QtCore.QSize(32, 32))
        self.button_isAngle.setObjectName(_fromUtf8("button_isAngle"))
        self.gridLayout_35.addWidget(self.button_isAngle, 4, 0, 1, 1)
        self.button_isLength = QtGui.QPushButton(self.tab_3)
        icon81 = QtGui.QIcon()
        icon81.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isLength.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isLength.setIcon(icon81)
        self.button_isLength.setIconSize(QtCore.QSize(32, 32))
        self.button_isLength.setObjectName(_fromUtf8("button_isLength"))
        self.gridLayout_35.addWidget(self.button_isLength, 6, 0, 1, 1)
        self.button_isDistance = QtGui.QPushButton(self.tab_3)
        icon82 = QtGui.QIcon()
        icon82.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_distanceBetween.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isDistance.setIcon(icon82)
        self.button_isDistance.setIconSize(QtCore.QSize(32, 32))
        self.button_isDistance.setObjectName(_fromUtf8("button_isDistance"))
        self.gridLayout_35.addWidget(self.button_isDistance, 5, 0, 1, 1)
        self.button_isPerpendicular = QtGui.QPushButton(self.tab_3)
        icon83 = QtGui.QIcon()
        icon83.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isPerpendicular.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isPerpendicular.setIcon(icon83)
        self.button_isPerpendicular.setIconSize(QtCore.QSize(32, 32))
        self.button_isPerpendicular.setObjectName(_fromUtf8("button_isPerpendicular"))
        self.gridLayout_35.addWidget(self.button_isPerpendicular, 1, 0, 1, 1)
        self.button_isClearance = QtGui.QPushButton(self.tab_3)
        icon84 = QtGui.QIcon()
        icon84.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isClearance.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isClearance.setIcon(icon84)
        self.button_isClearance.setIconSize(QtCore.QSize(32, 32))
        self.button_isClearance.setObjectName(_fromUtf8("button_isClearance"))
        self.gridLayout_35.addWidget(self.button_isClearance, 3, 0, 1, 1)
        self.button_isArea = QtGui.QPushButton(self.tab_3)
        icon85 = QtGui.QIcon()
        icon85.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_isArea.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_isArea.setIcon(icon85)
        self.button_isArea.setIconSize(QtCore.QSize(32, 32))
        self.button_isArea.setObjectName(_fromUtf8("button_isArea"))
        self.gridLayout_35.addWidget(self.button_isArea, 7, 0, 1, 1)
        icon86 = QtGui.QIcon()
        icon86.addPixmap(QtGui.QPixmap(_fromUtf8("icons:WF_check.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon86, _fromUtf8(""))
        self.gridLayout_30.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.tabWidget_0.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_9.addWidget(self.tabWidget_0, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_34.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.button_WF_quit = QtGui.QPushButton(Form)
        self.button_WF_quit.setObjectName(_fromUtf8("button_WF_quit"))
        self.horizontalLayout_9.addWidget(self.button_WF_quit)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.label_release = QtGui.QLabel(Form)
        self.label_release.setObjectName(_fromUtf8("label_release"))
        self.horizontalLayout_9.addWidget(self.label_release)
        self.gridLayout_34.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget_0.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.point_loc_comboBox.setCurrentIndex(1)
        self.transition_comboBox.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.ObjRot_comboBox_axis.setCurrentIndex(0)
        self.ObjRot_comboBox_center.setCurrentIndex(2)
        self.tabWidget_5.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(1)
        self.ObjTrans_comboBox_start.setCurrentIndex(3)
        self.ObjTrans_comboBox_end.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "WorkFeature", None, QtGui.QApplication.UnicodeUTF8))
        self.button_origin.setToolTip(QtGui.QApplication.translate("Form", "Create at origin: a point and X,Y and Z axis and XZ,XY  and YZ planes", None, QtGui.QApplication.UnicodeUTF8))
        self.button_origin.setText(QtGui.QApplication.translate("Form", "Origin", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Preferences :", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_verbose.setToolTip(QtGui.QApplication.translate("Form", "Toggle here if you want a lot of information printed into report View.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_verbose.setText(QtGui.QApplication.translate("Form", "Verbose", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_biColor.setToolTip(QtGui.QApplication.translate("Form", "Change the successive lines to be bicolor (red and white) for the following functions:\n"
"  - in \"Axis 1/2\" TAB:\n"
"    Axes=Cut(Wire)\n"
"  - in \"Circle\" TAB:\n"
"    Arcs=Cut(Circle)  \n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_biColor.setText(QtGui.QApplication.translate("Form", "Bi Color", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_copy.setToolTip(QtGui.QApplication.translate("Form", "Force the duplication of the Parent Object for the following functions:\n"
"  - in \"Axis 2/2\" TAB:\n"
"    Axes=(Axis,Pt,dist)\n"
"    If an Edge of a Cube is selected the Cube is duplicate \n"
"    with the corresponding\n"
"    Edge at the defined distance from the original.\n"
"  - in \"Plane\" TAB:\n"
"    Plane=(Plane,dist)  ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_copy.setText(QtGui.QApplication.translate("Form", "Object copy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setToolTip(QtGui.QApplication.translate("Form", "Change the tolerance for the following functions:\n"
"  - in \"Check\" TAB:\n"
"    are Parallel?\n"
"    are Perpendicular?\n"
"    are Coplanar?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Tolerance", None, QtGui.QApplication.UnicodeUTF8))
        self.tolerance_edit.setToolTip(QtGui.QApplication.translate("Form", "Change the tolerance for the following functions:\n"
"  - in \"Check\" TAB:\n"
"    are Parallel?\n"
"    are Perpendicular?\n"
"    are Coplanar?", None, QtGui.QApplication.UnicodeUTF8))
        self.tolerance_edit.setText(QtGui.QApplication.translate("Form", "1e-10", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Origin_Tab), QtGui.QApplication.translate("Form", "Ori. Pref.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_line_point.setToolTip(QtGui.QApplication.translate("Form", "Point(s)=(Point(s),Line(s)):\n"
"Create projection(s) of Point(s) onto Line(s).\n"
"- First select one (or several) Point(s)\n"
"- Second select one or several) Line(s)\n"
"- Then push this button\n"
"\n"
"Plot the intersection point T on a Line given one Line and One Point C.\n"
"The Vector TC is perpendicular to the Line.\n"
"The symetric point Cprime is also created as TC=TCprime.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_line_point.setText(QtGui.QApplication.translate("Form", "Point(s)=(Pt(s),Line(s)) ", None, QtGui.QApplication.UnicodeUTF8))
        self.button_face_center.setToolTip(QtGui.QApplication.translate("Form", "Create a Point at center location of each selected Face(s).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_face_center.setText(QtGui.QApplication.translate("Form", "Face(s) Center", None, QtGui.QApplication.UnicodeUTF8))
        self.button_circle_center.setToolTip(QtGui.QApplication.translate("Form", "Create a Point at center location of each selected Circle(s) or Arc(s).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_circle_center.setText(QtGui.QApplication.translate("Form", "Circle(s) Center", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Npoints_center.setToolTip(QtGui.QApplication.translate("Form", "Create a Point at mean location of all selected points.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Npoints_center.setText(QtGui.QApplication.translate("Form", "Points Center", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_center.setToolTip(QtGui.QApplication.translate("Form", "Create Point(s):\n"
"Cut each selected Line(s) in 2 (n) parts and create a (n-1) Point(s) at ends of edge(s).\n"
"The number indicates how many parts to consider.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_center.setText(QtGui.QApplication.translate("Form", "Line(s) Center", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_line_center.setToolTip(QtGui.QApplication.translate("Form", "The number indicates in how many parts each selected Lines(s) will be cut  (Max 100).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_face_point.setToolTip(QtGui.QApplication.translate("Form", "Create a point at the intersection of the Line and Plane selected.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_face_point.setText(QtGui.QApplication.translate("Form", "Point=(Line,Face) ", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_extrema.setToolTip(QtGui.QApplication.translate("Form", "Create Points at start and end location of each selected Line(s).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_extrema.setText(QtGui.QApplication.translate("Form", "Line(s) Extrema", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_face_point.setToolTip(QtGui.QApplication.translate("Form", "Point(s)=(Point(s),Face(s)):\n"
"Create projection(s) of Point(s) onto Face(s).\n"
"- First select one (or several) Point(s)\n"
"- Second select one or several) Plane(s)\n"
"- Then push this button\n"
"\n"
"Plot the intersection point T on a Plane given one Plane and One Point C.\n"
"The Vector TC is perpendicular to the plane.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_face_point.setText(QtGui.QApplication.translate("Form", "Point(s)=(Pt(s),Face(s))", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_center.setToolTip(QtGui.QApplication.translate("Form", "Create a Point at center location of all selected Object(s).\n"
"    if BBox is not toggled\n"
"        This point is the MEAN location of all center of Mass (if exist) of all objects.\n"
"        All  center of Mass will be created too.\n"
"    \n"
"if BBox check box is toggled\n"
"        This point is the center of the Global X,Y,Z bounding box of all objects.\n"
"        This bounding box alway exists (especially for draft objects).\n"
"        Be aware this point is not necessary the center of Mass of all Objects!", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_center.setText(QtGui.QApplication.translate("Form", "Object(s) Center", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_object_center.setToolTip(QtGui.QApplication.translate("Form", "if BBox check box is toggled\n"
"        This point is the center of the Global X,Y,Z bounding box of all objects.\n"
"        This bounding box alway exists (especially for draft objects).\n"
"        Be aware this point is not necessary the center of Mass of all Objects!", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_object_center.setText(QtGui.QApplication.translate("Form", "BBox", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Point_Tab1), QtGui.QApplication.translate("Form", "Point 1/2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.Point_Tab1), QtGui.QApplication.translate("Form", "Point", None, QtGui.QApplication.UnicodeUTF8))
        self.button_twolines_point.setToolTip(QtGui.QApplication.translate("Form", "Plot one or two Point(s) at minimum distance of two Lines\n"
"Create a Point at intersection of 2 crossing Lines.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_twolines_point.setText(QtGui.QApplication.translate("Form", "Point=(Line,Line) ", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_on_line.setToolTip(QtGui.QApplication.translate("Form", "Create a Point at a certain distance along the line \n"
"respecting to the choosen reference starting point.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_on_line.setText(QtGui.QApplication.translate("Form", "Point along Line", None, QtGui.QApplication.UnicodeUTF8))
        self.distance_point_on_line.setToolTip(QtGui.QApplication.translate("Form", "Distance from the extremity", None, QtGui.QApplication.UnicodeUTF8))
        self.distance_point_on_line.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_distPoint.setToolTip(QtGui.QApplication.translate("Form", "Point=(Point,Ax,dist):\n"
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
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_distPoint.setText(QtGui.QApplication.translate("Form", "Point=(Pt,Ax,dist)", None, QtGui.QApplication.UnicodeUTF8))
        self.dist_point.setToolTip(QtGui.QApplication.translate("Form", "Distance to the new Axis.\n"
"Can be negative for the reverse direction!", None, QtGui.QApplication.UnicodeUTF8))
        self.dist_point.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_dist_point.setToolTip(QtGui.QApplication.translate("Form", "The number of copies  (Max 100).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_wire_point.setToolTip(QtGui.QApplication.translate("Form", "Create Points by Partition:\n"
"Cut the selected wire(s) in 2(n) parts and create 2(n) Points with function discretize.\n"
"The number indicates in how many parts to cut.\n"
"Wires can be:\n"
"    Line\n"
"    Circle\n"
"    Arc\n"
"    Ellipse\n"
"An object must also be seleted but before any Wire to cut all his edges!    ", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_wire_point.setText(QtGui.QApplication.translate("Form", "Points=Cut(Wire)", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_wire_cut_point.setToolTip(QtGui.QApplication.translate("Form", "The number indicates in how many parts the selected Line will be cut  (Max 100).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_click_for_point.setToolTip(QtGui.QApplication.translate("Form", "Create a set of Points on a Plane perpendicular to the view at location of mouse clicks.\n"
"- Click first on the Button then click  on the View (with no object in background).\n"
"- Click first on the Button then click on the View (with an object in background), it will attach the points to the surface of the object.\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_click_for_point.setText(QtGui.QApplication.translate("Form", "Click", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_base_point.setToolTip(QtGui.QApplication.translate("Form", "Create Base Point of all selected Object(s).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_base_point.setText(QtGui.QApplication.translate("Form", "Object(s) Base Point", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_to_sketch.setToolTip(QtGui.QApplication.translate("Form", "Transform Point(s) in Sketch\'s Point(s) by projection onto the Sketch\'s Plane:\n"
"- First select an existing Skecth;\n"
"- Select as much as Points needed;\n"
"Then click on this button.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_to_sketch.setText(QtGui.QApplication.translate("Form", "Point(s) to Sketch", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Point_Tab2), QtGui.QApplication.translate("Form", "Point 2/2", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_axis.setToolTip(QtGui.QApplication.translate("Form", "Create 3 Axes at center location of all selected Object(s).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_axis.setText(QtGui.QApplication.translate("Form", "Object(s) X, Y, Z Axes", None, QtGui.QApplication.UnicodeUTF8))
        self.button_twopoints_axis.setToolTip(QtGui.QApplication.translate("Form", "Create an Axis crossing 2 Points.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_twopoints_axis.setText(QtGui.QApplication.translate("Form", "Two Points Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_twopoints_axis.setToolTip(QtGui.QApplication.translate("Form", "Distance for the extensions on extrema", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_twopoints_axis.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cylinder_axis.setToolTip(QtGui.QApplication.translate("Form", "Create the Axis of a Cylinder.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cylinder_axis.setText(QtGui.QApplication.translate("Form", "Cylinder(s) Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.button_plane_axis.setToolTip(QtGui.QApplication.translate("Form", "Plane(s) Axes:\n"
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
"The extension is 10 units by defaut but must be changed if needed.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_plane_axis.setText(QtGui.QApplication.translate("Form", "Plane(s) Axes", None, QtGui.QApplication.UnicodeUTF8))
        self.button_face_normal.setToolTip(QtGui.QApplication.translate("Form", "Create a normal Axis of a Face.\n"
"To create a Normal at click location on a Face:\n"
"- Click first in the view to select and object,\n"
"- then push the button, \n"
"- then click on a location on the selected Face.\n"
"or\n"
"To create several Normal of the face:\n"
"- Click first in the view to select and object,\n"
"- then select one or several points of the face\n"
"- then push the button.\n"
"(These selections can also be done into the Combined View)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_face_normal.setText(QtGui.QApplication.translate("Form", "Face Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_face_normal.setToolTip(QtGui.QApplication.translate("Form", "Length of external part of the (Normal) Axis.\n"
"  If zero In case of cylinder axis the extension will be a percentage of the object length.\n"
"  If zero and plane of face Normal, the extension will be 10 units.", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_face_normal.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_line_axis.setToolTip(QtGui.QApplication.translate("Form", "Create an Axis Parallel to an Axis (as Direction) and crossing a Point.\n"
"- Select one Axis and one (or several) Point(s) NOT on the previous Axis.\n"
"Define the length and the attach point if needed.\n"
"A Length of Zero means the length of already selected Axis will be used.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_point_line_axis.setText(QtGui.QApplication.translate("Form", "Axis=(Pt,Dir)", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_line.setToolTip(QtGui.QApplication.translate("Form", "Define the length of the Axis to create.\n"
"A Length of Zero means the length of already selected Axis will be used.", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_line.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.point_loc_comboBox.setToolTip(QtGui.QApplication.translate("Form", "The Attach Point will be at :\n"
"Start of the Axis;\n"
"Mid of the Axis;\n"
"End of the Axis.", None, QtGui.QApplication.UnicodeUTF8))
        self.point_loc_comboBox.setItemText(0, QtGui.QApplication.translate("Form", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.point_loc_comboBox.setItemText(1, QtGui.QApplication.translate("Form", "Mid", None, QtGui.QApplication.UnicodeUTF8))
        self.point_loc_comboBox.setItemText(2, QtGui.QApplication.translate("Form", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_point_axis.setToolTip(QtGui.QApplication.translate("Form", "Create an Axis Perpendicular to an Axis and crossing a Point\n"
"-Select one Axis and one (or several) Point(s) NOT on the previous Axis.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_point_axis.setText(QtGui.QApplication.translate("Form", "Axis=(Axis,Point)", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_line_point_axis.setToolTip(QtGui.QApplication.translate("Form", "Distance for the extensions on extrema.", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_line_point_axis.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_twolines_axis.setToolTip(QtGui.QApplication.translate("Form", "Create an Axis between two Axes.\n"
"-Select two Axes.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_twolines_axis.setText(QtGui.QApplication.translate("Form", "Axis=(Line,Line)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_plane_point_line_axis.setToolTip(QtGui.QApplication.translate("Form", "Create an Axis Perpendicular to an Axis, crossing a Point and Parallel to a Plane.\n"
"-Select one Plane, one Axis and one Point ON the previous Axis.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_plane_point_line_axis.setText(QtGui.QApplication.translate("Form", "Axis=(Plane,Point,Axis)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Axis_Tab1), QtGui.QApplication.translate("Form", "Axis 1/2", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_plane_axis.setToolTip(QtGui.QApplication.translate("Form", "Axes=(Pl(s),Axes):\n"
"Create projection(s) of Axes onto Plane(s).\n"
"- First select one (or several) Line(s)\n"
"- Second select one or several) Plane(s)\n"
"- Then push this button", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_plane_axis.setText(QtGui.QApplication.translate("Form", "Axes=(Pl(s),Axes)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_twoplanes_axis.setToolTip(QtGui.QApplication.translate("Form", "Create an Axis by intersect of 2 Planes.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_twoplanes_axis.setText(QtGui.QApplication.translate("Form", "Axis=(Plane,Plane)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_distLine.setToolTip(QtGui.QApplication.translate("Form", "Axes=(Axis,Pt,dist):\n"
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
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_distLine.setText(QtGui.QApplication.translate("Form", "Axes=(Axis,Pt,dist)", None, QtGui.QApplication.UnicodeUTF8))
        self.dist_line.setToolTip(QtGui.QApplication.translate("Form", "Distance to the new Axis.\n"
"Can be negative for the reverse direction!", None, QtGui.QApplication.UnicodeUTF8))
        self.dist_line.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_dist_line.setToolTip(QtGui.QApplication.translate("Form", "The number of copies  (Max 100).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_angleLine.setToolTip(QtGui.QApplication.translate("Form", "Axes=(Axis,Pt,Pl,a):\n"
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
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_angleLine.setText(QtGui.QApplication.translate("Form", "Axes=(Axis,Pt,Pl,a)", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_line.setToolTip(QtGui.QApplication.translate("Form", "Angle to the new Axis.\n"
"Can be negative for the reverse direction!\n"
"(in degrees)", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_line.setText(QtGui.QApplication.translate("Form", "45.0", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_angle_line.setToolTip(QtGui.QApplication.translate("Form", "The number of copies (Max 100).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_wire_axis.setToolTip(QtGui.QApplication.translate("Form", "Create Axes by Partition:\n"
"Cut the selected wire(s) in 2(n) parts and create 2(n) Axes with function discretize.\n"
"The number indicates in how many parts to cut.\n"
"Wires can be:\n"
"    Line\n"
"    Circle\n"
"    Arc\n"
"    Ellipse\n"
"An object must also be seleted but before any Wire to cut all his Edges!\n"
"NB: You can change the successive lines to be bicolor (red and white)  \n"
"in \"Ori. Pref.\"  TAB    \n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_wire_axis.setText(QtGui.QApplication.translate("Form", "Axes=Cut(Wire)", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_wire_cut_axis.setToolTip(QtGui.QApplication.translate("Form", "The number indicates in how many parts the selected Line will be cut  (Max 100).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_axis.setToolTip(QtGui.QApplication.translate("Form", "Create Axes:\n"
"Cut the selected Line in 2(n) parts and create 2(n) Axes.\n"
"The number indicates in how many parts to cut.\n"
"\n"
"NB: You can change the successive lines to be bicolor (red and white)  \n"
"in \"Ori. Pref.\"  TAB", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_axis.setText(QtGui.QApplication.translate("Form", "Axes=Cut(Axis)", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_axis_cut.setToolTip(QtGui.QApplication.translate("Form", "The number indicates in how many parts the selected Line will be cut  (Max 100).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_extension_axis.setToolTip(QtGui.QApplication.translate("Form", "Enlarge(Axis):\n"
"Extend an Axis at two extrema.\n"
"- First select an Axis (or several Axes) \n"
"- Second push this button\n"
"\n"
"NB: \n"
" - The percentage of  the extension can be defined first.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_extension_axis.setText(QtGui.QApplication.translate("Form", "Enlarge(Axis)", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_axis.setToolTip(QtGui.QApplication.translate("Form", "Extension of the Line in  percentage.", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_axis.setText(QtGui.QApplication.translate("Form", "50.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_click_for_axis.setToolTip(QtGui.QApplication.translate("Form", "Create a set of Lines on a Plane perpendicular to the view at location of 2 mouse clicks.\n"
"- Click first on the Button then at least twice click on the View (with no object in background).\n"
"- Click first on the Button then at least twice click on the View (with an object in background), it will attach the lines to the surface of the object.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_click_for_axis.setText(QtGui.QApplication.translate("Form", "Click", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_base_axes.setToolTip(QtGui.QApplication.translate("Form", "Create 3 Axes at Base location of all selected Object(s).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_base_axes.setText(QtGui.QApplication.translate("Form", "Object(s) Base Axes", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_to_sketch.setToolTip(QtGui.QApplication.translate("Form", "Transform Line(s) in Sketch\'s Line(s) by projection onto the Sketch\'s Plane:\n"
"- First select an existing Skecth;\n"
"- Select as much as Lines needed;\n"
"Then click on this button.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_line_to_sketch.setText(QtGui.QApplication.translate("Form", "Axis(es) to Sketch", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Axis_Tab2), QtGui.QApplication.translate("Form", "Axis 2/2", None, QtGui.QApplication.UnicodeUTF8))
        self.button_linecenter_circle.setToolTip(QtGui.QApplication.translate("Form", "Select an Axis and a Point to create a Circle\n"
"centered on the Point, perpendicular to the Axis \n"
"with the given radius.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_linecenter_circle.setText(QtGui.QApplication.translate("Form", "Circle=(Axis, center)", None, QtGui.QApplication.UnicodeUTF8))
        self.radius_circle.setToolTip(QtGui.QApplication.translate("Form", "Radius of the Circle.", None, QtGui.QApplication.UnicodeUTF8))
        self.radius_circle.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_linepoint_circle.setToolTip(QtGui.QApplication.translate("Form", "Select an Axis and a Point  to create a Circle\n"
"centered on the Axis and tangenting the Point.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_linepoint_circle.setText(QtGui.QApplication.translate("Form", "Circle=(Axis, point)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_3points_circle.setToolTip(QtGui.QApplication.translate("Form", "Select 3 Points  to create a Circle.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_3points_circle.setText(QtGui.QApplication.translate("Form", "Circle=(3 points)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_circle.setToolTip(QtGui.QApplication.translate("Form", "Create Arcs:\n"
"Cut the selected Circle(s) or Arc(s) in 2(n) parts and create 2(n) Arcs.\n"
"The number indicates in how many parts to cut.\n"
"- First select as many Circles and Arcs you want\n"
"- Second set the number of parts\n"
"- Third push this button\n"
"\n"
"NB: You can change the successive lines to be bicolor (red and white)  \n"
"in \"Ori. Pref.\"  TAB", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_circle.setText(QtGui.QApplication.translate("Form", "Arcs=Cut(Circle)", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_circle_cut.setToolTip(QtGui.QApplication.translate("Form", "The number indicates in how many parts the selected Circle will be cut  (Max 100).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_3points_ellipse.setToolTip(QtGui.QApplication.translate("Form", "Select a center and 2 Points to create an Ellipse.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_3points_ellipse.setText(QtGui.QApplication.translate("Form", "Ellipse=(3 points)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_circle_to_sketch.setToolTip(QtGui.QApplication.translate("Form", "Transform Circle(s) and Arc(s) in Sketch\'s object(s) by projection onto the Sketch\'s Plane:\n"
"- First select an existing Skecth;\n"
"- Select as much as Circles and arcs needed;\n"
"Then click on this button.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_circle_to_sketch.setText(QtGui.QApplication.translate("Form", "Circle(s) to Sketch", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Form", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.button_click_for_plane.setToolTip(QtGui.QApplication.translate("Form", "Click:\n"
"Create a rectangular Plane perpendicular to the view at location of one mouse click.\n"
"Define the width and the length of the Plane if needed.\n"
"- Click first on the Button then click once on the View.\n"
"- Click first on the Button then click once on top of one object of the View\n"
" to attach the plane at this object.\n"
"- You can also select an already existing point first and click the button to attach the plane.\n"
"\n"
"NB: The plane width and length can be defined first.\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_click_for_plane.setText(QtGui.QApplication.translate("Form", "Click", None, QtGui.QApplication.UnicodeUTF8))
        self.length_plane.setToolTip(QtGui.QApplication.translate("Form", "Length of the Plane.", None, QtGui.QApplication.UnicodeUTF8))
        self.length_plane.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.width_plane.setToolTip(QtGui.QApplication.translate("Form", "Width of the Plane.", None, QtGui.QApplication.UnicodeUTF8))
        self.width_plane.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_planeandaxis_plane.setToolTip(QtGui.QApplication.translate("Form", "Plane=(Plane, Axis):\n"
"Create a Plane crossing a Line and perpendicular to a Plane.\n"
"- First select a plane and a line NOT on the previous plane\n"
"- Second push this button\n"
"\n"
"NB: The plane created can be rotated if a none null angle is defined first.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_planeandaxis_plane.setText(QtGui.QApplication.translate("Form", "Plane=(Plane, Axis)", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_planeandaxis_plane.setToolTip(QtGui.QApplication.translate("Form", "Angle of rotation of the created Plane (in degrees).", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_planeandaxis_plane.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_axisandpoint_plane.setToolTip(QtGui.QApplication.translate("Form", "Plane=(Point, Axis):\n"
"Create a plane crossing a Line and a Point.\n"
"- First select a line and a point NOT on the previous line\n"
"- Second push this button", None, QtGui.QApplication.UnicodeUTF8))
        self.button_axisandpoint_plane.setText(QtGui.QApplication.translate("Form", "Plane=(Point, Axis)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_axis_point_plane.setToolTip(QtGui.QApplication.translate("Form", "Plane=(Point, _|Axis):\n"
"Create a plane perpendicular to a Line and crossing a Point.\n"
"- First select a line and a point NOT on the previous line\n"
"- Second push this button", None, QtGui.QApplication.UnicodeUTF8))
        self.button_axis_point_plane.setText(QtGui.QApplication.translate("Form", "Plane=(Point, _|Axis)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_face_tangent.setToolTip(QtGui.QApplication.translate("Form", "Face Tangent:\n"
"Create a tanget Plane at click location of a Face.\n"
"- First click in the view to select and object,\n"
"- Second push this button\n"
"-Third click on a location on the selected object.\n"
"\n"
"NB: The plane width and length can be defined first.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_face_tangent.setText(QtGui.QApplication.translate("Form", "Face Tangent", None, QtGui.QApplication.UnicodeUTF8))
        self.length_plane_2.setToolTip(QtGui.QApplication.translate("Form", "Length of the Plane.", None, QtGui.QApplication.UnicodeUTF8))
        self.length_plane_2.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.width_plane_2.setToolTip(QtGui.QApplication.translate("Form", "Width of the Plane.", None, QtGui.QApplication.UnicodeUTF8))
        self.width_plane_2.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_threepoints_plane.setToolTip(QtGui.QApplication.translate("Form", "Plane=(3 Points):\n"
"Create a Plane crossing 3 Points.\n"
"- First select 3 different points\n"
"- Second push this button", None, QtGui.QApplication.UnicodeUTF8))
        self.button_threepoints_plane.setText(QtGui.QApplication.translate("Form", "Plane=(3 Points)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_distPlane.setToolTip(QtGui.QApplication.translate("Form", "Plane=(Plane,dist):\n"
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
"Several Faces of the cube can be selected.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_distPlane.setText(QtGui.QApplication.translate("Form", "Plane=(Plane,dist)", None, QtGui.QApplication.UnicodeUTF8))
        self.dist_plane.setToolTip(QtGui.QApplication.translate("Form", "Distance to the new plane.\n"
"Can be negative for the reverse direction!", None, QtGui.QApplication.UnicodeUTF8))
        self.dist_plane.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_dist_plane.setToolTip(QtGui.QApplication.translate("Form", "The number of copies  (Max 100).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_planeandpoint_plane.setToolTip(QtGui.QApplication.translate("Form", "Plane=(Point, Plane):\n"
"Create a plane crossing a Point and parallel to a Plane.\n"
"- First select a plane and a point NOT on the previous plane\n"
"- Second push this button\n"
"\n"
"NB: you can enlarge the created new plane by setting first an extension length.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_planeandpoint_plane.setText(QtGui.QApplication.translate("Form", "Plane=(Point, Plane)", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_planePointPlane.setToolTip(QtGui.QApplication.translate("Form", "Length for the extensions of the new Plane compared to initial one.", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_planePointPlane.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Plane_Tab1), QtGui.QApplication.translate("Form", "Plane 1/2", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_center_planes.setToolTip(QtGui.QApplication.translate("Form", "Object(s) Center Planes:\n"
"Create 3 Planes (XY, XZ and YZ) at center location of all selected Object(s).\n"
"- First select one or severl objects\n"
"- Second push this button", None, QtGui.QApplication.UnicodeUTF8))
        self.button_object_center_planes.setText(QtGui.QApplication.translate("Form", "Object(s) Center Planes", None, QtGui.QApplication.UnicodeUTF8))
        self.button_extension_plane.setToolTip(QtGui.QApplication.translate("Form", "Enlarge(Plane):\n"
"Extend a Plane in each dimension.\n"
"- First select a  Plane (or several Planes) \n"
"- Second push this button\n"
"\n"
"NB: \n"
" - The percentage of  the extension can be defined first.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_extension_plane.setText(QtGui.QApplication.translate("Form", "Enlarge(Plane)", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_plane.setToolTip(QtGui.QApplication.translate("Form", "Extension of the Plane in each dimension in percentage.", None, QtGui.QApplication.UnicodeUTF8))
        self.extension_plane.setText(QtGui.QApplication.translate("Form", "50.0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Plane_Tab11), QtGui.QApplication.translate("Form", "Plane 2/2", None, QtGui.QApplication.UnicodeUTF8))
        self.button_boundingboxes.setToolTip(QtGui.QApplication.translate("Form", "Create bounding boxes around each of selected object(s).\n"
"6 rectangles at the limits of each bounding boxes will be created.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_boundingboxes.setText(QtGui.QApplication.translate("Form", "Bounding Box(es)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_boundingbox.setToolTip(QtGui.QApplication.translate("Form", "Create one bounding box around all of selected object(s).\n"
"6 rectangles at the limits of the bounding box will be created.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_boundingbox.setText(QtGui.QApplication.translate("Form", "Bounding Box", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_volumBB.setToolTip(QtGui.QApplication.translate("Form", "if \"Vol.\" is toggled:\n"
"  In Addition of rectangles, the Bounding box will be also created as a Volume.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_volumBB.setText(QtGui.QApplication.translate("Form", "Vol.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cylinder_create.setToolTip(QtGui.QApplication.translate("Form", "Create a Cylinder aligned on Axes:\n"
"- First select one or several couple of ( Axis and a Ref. Point). \n"
"- Define Diameter and Length if needed.\n"
"Then Click the button...\n"
"It will create a Cylinder aligned on the selected axis \n"
"with one of the extremities at the Ref. point,\n"
"for all couple selected.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cylinder_create.setText(QtGui.QApplication.translate("Form", "Cylinder", None, QtGui.QApplication.UnicodeUTF8))
        self.diameter_cylinder.setToolTip(QtGui.QApplication.translate("Form", "Radius of the Cylinder.", None, QtGui.QApplication.UnicodeUTF8))
        self.diameter_cylinder.setText(QtGui.QApplication.translate("Form", "2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.length_cylinder.setToolTip(QtGui.QApplication.translate("Form", "Length of the Cylinder.\n"
"Negative value will reverse the direction from Ref. Point", None, QtGui.QApplication.UnicodeUTF8))
        self.length_cylinder.setText(QtGui.QApplication.translate("Form", "20.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cube_create.setToolTip(QtGui.QApplication.translate("Form", "Create a Cuboid aligned on Axes:\n"
"- First select one or several couple of ( Axis and a Ref. Point). \n"
"- Define Dimensions if needed.\n"
"Then Click the button...\n"
"It will create a Cube aligned on the selected axis \n"
"with one of the extremities at Ref. point,\n"
"for all couple selected.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cube_create.setText(QtGui.QApplication.translate("Form", "Cube", None, QtGui.QApplication.UnicodeUTF8))
        self.section_cube.setToolTip(QtGui.QApplication.translate("Form", "Section (Length, Width) of the Cube.", None, QtGui.QApplication.UnicodeUTF8))
        self.section_cube.setText(QtGui.QApplication.translate("Form", "2.0,2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.height_cube.setToolTip(QtGui.QApplication.translate("Form", "Heigth of the Cube.\n"
"Negative value will reverse the direction from Ref. Point", None, QtGui.QApplication.UnicodeUTF8))
        self.height_cube.setText(QtGui.QApplication.translate("Form", "20.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sphere_create.setToolTip(QtGui.QApplication.translate("Form", "Create a Sphere shell:\n"
"- First select one or several Center Point(s). \n"
"- Define Diameter if needed.\n"
"Then Click the button...\n"
"It will create Sphere shell(s) centered\n"
"at the selected point(s).", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sphere_create.setText(QtGui.QApplication.translate("Form", "Sphere", None, QtGui.QApplication.UnicodeUTF8))
        self.diameter_sphere.setToolTip(QtGui.QApplication.translate("Form", "Diameter of the Sphere.", None, QtGui.QApplication.UnicodeUTF8))
        self.diameter_sphere.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_dome_create.setToolTip(QtGui.QApplication.translate("Form", "Create a full geodesic dome shell:\n"
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
"Original code from : Ulrich Brammer", None, QtGui.QApplication.UnicodeUTF8))
        self.button_dome_create.setText(QtGui.QApplication.translate("Form", "Dome", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_frequency_dome.setToolTip(QtGui.QApplication.translate("Form", "Frequency Parameter (Integer between 1 to 20).", None, QtGui.QApplication.UnicodeUTF8))
        self.diameter_dome.setToolTip(QtGui.QApplication.translate("Form", "Diameter of the Dome.", None, QtGui.QApplication.UnicodeUTF8))
        self.diameter_dome.setText(QtGui.QApplication.translate("Form", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_letter.setToolTip(QtGui.QApplication.translate("Form", "AB:\n"
"Create 3D Text attached to a Point. \n"
"- First select a  Plane\n"
"- Then push this button\n"
"in this case the center of the text is attached to center of the Plane;\n"
"or\n"
"- First select a  Plane and a Point on the Plane\n"
"- Then push this button\n"
"NB:\n"
" Change the text and his size if needed", None, QtGui.QApplication.UnicodeUTF8))
        self.button_letter.setText(QtGui.QApplication.translate("Form", "AB", None, QtGui.QApplication.UnicodeUTF8))
        self.letter.setToolTip(QtGui.QApplication.translate("Form", "Put the desired text here", None, QtGui.QApplication.UnicodeUTF8))
        self.letter.setText(QtGui.QApplication.translate("Form", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.size_letter.setToolTip(QtGui.QApplication.translate("Form", "Size of the font.", None, QtGui.QApplication.UnicodeUTF8))
        self.size_letter.setText(QtGui.QApplication.translate("Form", "2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_revolve.setToolTip(QtGui.QApplication.translate("Form", "Revolve:\n"
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
"   If no Point is selected the Origin is considered as Center of rotation !", None, QtGui.QApplication.UnicodeUTF8))
        self.button_revolve.setText(QtGui.QApplication.translate("Form", "Revolve", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_revolve.setToolTip(QtGui.QApplication.translate("Form", "Angle of the revolution in degrees.", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_revolve.setText(QtGui.QApplication.translate("Form", "360", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_allsubselect.setToolTip(QtGui.QApplication.translate("Form", "if \"All\" is toggled:\n"
"  All the wires of the Trajectory  selected will be considered.\n"
"\n"
"Untoggled if you select a Skecth with several curves and you want to process\n"
"only the one subselected.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_allsubselect.setText(QtGui.QApplication.translate("Form", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.transition_comboBox.setToolTip(QtGui.QApplication.translate("Form", "For the function :\n"
"makePipeShell(shapeList,[isSolid,isFrenet,transition])\n"
"Select a Transition option in case of trajectory with several wires; Transition can be:\n"
"#     0 (default), 1 (right corners) or 2 (rounded corners).", None, QtGui.QApplication.UnicodeUTF8))
        self.transition_comboBox.setItemText(0, QtGui.QApplication.translate("Form", "No Transition", None, QtGui.QApplication.UnicodeUTF8))
        self.transition_comboBox.setItemText(1, QtGui.QApplication.translate("Form", "Right corners", None, QtGui.QApplication.UnicodeUTF8))
        self.transition_comboBox.setItemText(2, QtGui.QApplication.translate("Form", "Rounded corners", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_solid.setToolTip(QtGui.QApplication.translate("Form", "if \"Solid\" is toggled:\n"
"  The Beam sweep will generate a solid with a closed selected wire as Section.\n"
"If this check box is toggle off:\n"
"  Or if the Section wire is not closed, only a shell will be created.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_solid.setText(QtGui.QApplication.translate("Form", "Solid", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_Frenet.setToolTip(QtGui.QApplication.translate("Form", "Force the \"isFrenet\" parameter to True for the function :\n"
"makePipeShell(shapeList,[isSolid,isFrenet,transition])\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_Frenet.setText(QtGui.QApplication.translate("Form", "isFrenet", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sweep.setToolTip(QtGui.QApplication.translate("Form", "Section Sweep:\n"
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
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sweep.setText(QtGui.QApplication.translate("Form", "Section Sweep", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Objects_Tab2), QtGui.QApplication.translate("Form", "Object", None, QtGui.QApplication.UnicodeUTF8))
        self.button_alignface2view.setToolTip(QtGui.QApplication.translate("Form", "Align the face of selected object(s)  to the actual view Plane.\n"
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
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_alignface2view.setText(QtGui.QApplication.translate("Form", "Align Face to View", None, QtGui.QApplication.UnicodeUTF8))
        self.button_align_faces.setToolTip(QtGui.QApplication.translate("Form", "Align the Face(s) from selected object(s) to the last Face selected.\n"
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
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_align_faces.setText(QtGui.QApplication.translate("Form", "Align Faces", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_align_faces.setToolTip(QtGui.QApplication.translate("Form", "This Angle  (in degrees) will be added to the angle needed to align Faces.", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_align_faces.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_align_edges.setToolTip(QtGui.QApplication.translate("Form", "Align the Edge(s) from selected object(s) to the last Edge selected.\n"
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
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_align_edges.setText(QtGui.QApplication.translate("Form", "Align Edges", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_align_edges.setToolTip(QtGui.QApplication.translate("Form", "This Angle  (in degrees) will be added to the angle needed to align Edges.", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_align_edges.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_joint_points.setToolTip(QtGui.QApplication.translate("Form", "Joint Point(s) from selected object(s) to the last Point selected.\n"
" - Click first to select a Point of an object or several Points from several objects.\n"
"These objects will be moved. \n"
" - Click second to select an Point to joint to (the last object is fixed and will never move).\n"
"Then Click the button.\n"
"\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_joint_points.setText(QtGui.QApplication.translate("Form", "Joint Points", None, QtGui.QApplication.UnicodeUTF8))
        self.button_joint_faces.setToolTip(QtGui.QApplication.translate("Form", "Joint Face(s) from selected object(s) to the last Face selected.\n"
" - Click first to select a Face of an object or several Faces from several objects. \n"
"These objects will be moved.\n"
" - Click second to select a Face to joint to (the last object is fixed and will never move).\n"
"Then Click the button.\n"
"\n"
"  Two clicks will rotate by 180 deg the moving objects.\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.button_joint_faces.setText(QtGui.QApplication.translate("Form", "Joint Faces", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.align_tab), QtGui.QApplication.translate("Form", "Align", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Form", "Object", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_select_object.setToolTip(QtGui.QApplication.translate("Form", "Select the Object to cut:\n"
"First Click on the object in the view \n"
"and push this button to accept...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_select_object.setText(QtGui.QApplication.translate("Form", "Select Object", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_select_line.setToolTip(QtGui.QApplication.translate("Form", "Select the Line to cut the Object along:\n"
"First Click on the line/edge in the view \n"
"and push this button to accept...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_select_line.setText(QtGui.QApplication.translate("Form", "Select Cut Line", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_select_plane.setToolTip(QtGui.QApplication.translate("Form", "Select the Reference Plane to cut the Object from:\n"
"First Click on the plane in the view \n"
"and push this button to accept...\n"
"\n"
"The Reference Plane is the Plane you pose the object on before to use a saw! \n"
"(Note that the Angle is calculated from the Normal at this Plane)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_select_plane.setText(QtGui.QApplication.translate("Form", "Select Ref. Plane", None, QtGui.QApplication.UnicodeUTF8))
        self.label_angle.setToolTip(QtGui.QApplication.translate("Form", "Angle of cutting  relative to the Normal of the Reference Plane (in degrees).\n"
"\n"
"  0.0 means that the Plane of cutting is along the Cut Line with \n"
"a 90 deg angle with Reference Plane.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_angle.setText(QtGui.QApplication.translate("Form", "Angle", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_cut_object.setToolTip(QtGui.QApplication.translate("Form", "Angle of cutting  relative to the Normal of the Reference Plane (in degrees).\n"
"\n"
"  0.0 means that the Plane of cutting is along the Cut Line with \n"
"a 90 deg angle with Reference Plane.", None, QtGui.QApplication.UnicodeUTF8))
        self.angle_cut_object.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_thickness.setToolTip(QtGui.QApplication.translate("Form", "Thickness of the Cut.\n"
"\n"
"i.e. the thickness of a saw.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_thickness.setText(QtGui.QApplication.translate("Form", "Thickness", None, QtGui.QApplication.UnicodeUTF8))
        self.thickness_cut_object.setToolTip(QtGui.QApplication.translate("Form", "Thickness of the Cut.\n"
"\n"
"i.e. the thickness of a saw.", None, QtGui.QApplication.UnicodeUTF8))
        self.thickness_cut_object.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_reset.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_apply.setToolTip(QtGui.QApplication.translate("Form", "Cut an object by selecting a Line cut, a Plane and an Angle regarding the Plane.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cut_apply.setText(QtGui.QApplication.translate("Form", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.cut_tab), QtGui.QApplication.translate("Form", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_button_select.setToolTip(QtGui.QApplication.translate("Form", "- Select one or several object(s) in the view and \n"
"- Click on this button.\n"
"\n"
"NB\n"
"Once object(s) are selected an other Click will unselect them !\n"
"Selected Object(s) will be displayed with 75% of transparency.", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_button_select.setText(QtGui.QApplication.translate("Form", "Select Object(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_comboBox_axis.setItemText(0, QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_comboBox_axis.setItemText(1, QtGui.QApplication.translate("Form", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_comboBox_axis.setItemText(2, QtGui.QApplication.translate("Form", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_comboBox_axis.setItemText(3, QtGui.QApplication.translate("Form", "To select", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_button_select_axis.setText(QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QtGui.QApplication.translate("Form", "Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_comboBox_center.setItemText(0, QtGui.QApplication.translate("Form", "Origin", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_comboBox_center.setItemText(1, QtGui.QApplication.translate("Form", "Base Obj.", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_comboBox_center.setItemText(2, QtGui.QApplication.translate("Form", "Center Obj.(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_comboBox_center.setItemText(3, QtGui.QApplication.translate("Form", "To select", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_button_select_center.setText(QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QtGui.QApplication.translate("Form", "Center", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Angle of rotation :", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_7), QtGui.QApplication.translate("Form", "Define", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_button_select_angle.setToolTip(QtGui.QApplication.translate("Form", "Calculate angle from 2 objects.\n"
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
"  Normals of Planes will be used.    ", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_button_select_angle.setText(QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_10), QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_lineEdit_angle.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_angle_2.setText(QtGui.QApplication.translate("Form", " (deg)", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_button_reset.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjRot_button_apply.setText(QtGui.QApplication.translate("Form", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.rotate_tab), QtGui.QApplication.translate("Form", "Rotate", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_button_select.setToolTip(QtGui.QApplication.translate("Form", "- Select one or several object(s) in the view and \n"
"- Click on this button.\n"
"\n"
"NB\n"
"Once object(s) are selected an other Click will unselect them !\n"
"Selected Object(s) will be displayed with 75% of transparency.", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_button_select.setText(QtGui.QApplication.translate("Form", "Select Object(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_duplicate.setToolTip(QtGui.QApplication.translate("Form", "Toggle this check box to generate copies the object during the Translation.\n"
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
"  ending point,  and so on!", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_duplicate.setText(QtGui.QApplication.translate("Form", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_spin.setToolTip(QtGui.QApplication.translate("Form", "The number of copies.", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_deepCopy.setToolTip(QtGui.QApplication.translate("Form", "Toggle this check box to realize \"deep\" copies. \n"
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
"On the last result the same Sketch is both link to Pad001 but also still to Pad.", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_deepCopy.setText(QtGui.QApplication.translate("Form", "Deep", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Starting Point :", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_start.setItemText(0, QtGui.QApplication.translate("Form", "Origin", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_start.setItemText(1, QtGui.QApplication.translate("Form", "Base Obj.", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_start.setItemText(2, QtGui.QApplication.translate("Form", "Center Obj.(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_start.setItemText(3, QtGui.QApplication.translate("Form", "To select", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_start.setItemText(4, QtGui.QApplication.translate("Form", "To define", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_button_select_start.setText(QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "X :", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_start_x.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Y :", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_start_y.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Z :", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_start_z.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5), QtGui.QApplication.translate("Form", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Ending Point :", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_end.setItemText(0, QtGui.QApplication.translate("Form", "Origin", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_end.setItemText(1, QtGui.QApplication.translate("Form", "Base Obj.", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_end.setItemText(2, QtGui.QApplication.translate("Form", "Center Obj.(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_end.setItemText(3, QtGui.QApplication.translate("Form", "To select", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_end.setItemText(4, QtGui.QApplication.translate("Form", "To define", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_comboBox_end.setItemText(5, QtGui.QApplication.translate("Form", "Relative", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_button_select_end.setText(QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Z :", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_end_z.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Y :", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_end_y.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "X :", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_end_x.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), QtGui.QApplication.translate("Form", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_button_reset.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.ObjTrans_button_apply.setText(QtGui.QApplication.translate("Form", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.translate_tab), QtGui.QApplication.translate("Form", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Modif_Tab), QtGui.QApplication.translate("Form", "Modif.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_alignview.setToolTip(QtGui.QApplication.translate("Form", "Set the current view perpendicular to the selected Face, \n"
"or aligned to the selected Axis, \n"
"or aligned on 2 Points.\n"
"ReClick with same selection, will reverse the direction.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_alignview.setText(QtGui.QApplication.translate("Form", "Align View to ...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_trackcamera.setText(QtGui.QApplication.translate("Form", "Camera Track", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.View_Tab), QtGui.QApplication.translate("Form", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isView.setToolTip(QtGui.QApplication.translate("Form", "Detect the position of the camera.\n"
"The returned value is the value provided \n"
"by the function getCameraOrientation().", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isView.setText(QtGui.QApplication.translate("Form", "View ?", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isCoplanar.setToolTip(QtGui.QApplication.translate("Form", "Check if two faces or two Edges are Coplanar:\n"
"- Select the 2 faces/planes or 2 Edges/Lines and\n"
"Click this button\n"
"\n"
"NB: You can change the tolerance in \"Ori. Pref.\"  TAB", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isCoplanar.setText(QtGui.QApplication.translate("Form", "are Coplanar ?", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isParallel.setToolTip(QtGui.QApplication.translate("Form", "Check if two faces or two Edges are Parallel:\n"
"- Select the 2 faces/planes or 2 Edges/Lines and\n"
"Click this button\n"
"\n"
"NB: You can change the tolerance in \"Ori. Pref.\"  TAB", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isParallel.setText(QtGui.QApplication.translate("Form", "are Parallel ?", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isAngle.setToolTip(QtGui.QApplication.translate("Form", "Check for two Edges/Planes angle:\n"
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
"  Normals of Planes will be used.     ", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isAngle.setText(QtGui.QApplication.translate("Form", "Angle ?", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isLength.setToolTip(QtGui.QApplication.translate("Form", "Check for Line Length:\n"
"Length measurement and Delta values (on main Axes) for a Line\n"
"- Select the Line and\n"
"Click this button\n"
" ", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isLength.setText(QtGui.QApplication.translate("Form", "Length ?", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isDistance.setToolTip(QtGui.QApplication.translate("Form", "Check for two Points distance:\n"
"Distances measurement and Delta values (on main Axes) between two Points\n"
"- Select the 2 Points and\n"
"Click this button\n"
" ", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isDistance.setText(QtGui.QApplication.translate("Form", "Distance ?", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isPerpendicular.setToolTip(QtGui.QApplication.translate("Form", "Check if two faces or two Edges are Perpendicular:\n"
"- Select the 2 faces/planes or 2 Edges/Lines and\n"
"Click this button\n"
"\n"
"NB: You can change the tolerance in \"Ori. Pref.\"  TAB", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isPerpendicular.setText(QtGui.QApplication.translate("Form", "are Perpendicular ?", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isClearance.setToolTip(QtGui.QApplication.translate("Form", "Check for two Objects Clearance distance:\n"
"Quick measurements between parallel faces and similarly placed objects\n"
"- Select the 2 Objects and\n"
"Click this button", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isClearance.setText(QtGui.QApplication.translate("Form", "Distance Clearance ?", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isArea.setToolTip(QtGui.QApplication.translate("Form", "Check for surface Area:\n"
"Area measurement for a Plane or a set of Planes.\n"
"- Select One or several Planes and\n"
"Click this button", None, QtGui.QApplication.UnicodeUTF8))
        self.button_isArea.setText(QtGui.QApplication.translate("Form", "Area ?", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Form", "Check", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_0.setTabText(self.tabWidget_0.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "W. F.", None, QtGui.QApplication.UnicodeUTF8))
        self.button_WF_quit.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_release.setText(QtGui.QApplication.translate("Form", "2015", None, QtGui.QApplication.UnicodeUTF8))

