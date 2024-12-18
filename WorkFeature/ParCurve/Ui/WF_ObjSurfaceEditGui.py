# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WF_ObjSurfaceEditGui.ui'
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
        Form.resize(1247, 460)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_load = QPushButton(self.groupBox_2)
        self.button_load.setObjectName(u"button_load")

        self.horizontalLayout.addWidget(self.button_load)

        self.button_save = QPushButton(self.groupBox_2)
        self.button_save.setObjectName(u"button_save")

        self.horizontalLayout.addWidget(self.button_save)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 14):
            self.tableWidget.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(0, 7, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(0, 8, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(0, 9, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(0, 10, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(0, 11, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(0, 12, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(1, 5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(1, 6, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(1, 7, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setItem(1, 8, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(1, 9, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setItem(1, 10, __qtablewidgetitem40)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_addRow = QPushButton(self.groupBox)
        self.button_addRow.setObjectName(u"button_addRow")

        self.horizontalLayout_2.addWidget(self.button_addRow)

        self.button_removeRow = QPushButton(self.groupBox)
        self.button_removeRow.setObjectName(u"button_removeRow")

        self.horizontalLayout_2.addWidget(self.button_removeRow)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_select = QComboBox(Form)
        self.comboBox_select.setObjectName(u"comboBox_select")
        self.comboBox_select.setEnabled(False)
        self.comboBox_select.setMaximumSize(QSize(0, 0))
        self.comboBox_select.setModelColumn(1)

        self.horizontalLayout_4.addWidget(self.comboBox_select)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_quit = QPushButton(Form)
        self.button_quit.setObjectName(u"button_quit")

        self.horizontalLayout_3.addWidget(self.button_quit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"3D Database", None))
#if QT_CONFIG(tooltip)
        self.button_load.setToolTip(QCoreApplication.translate("Form", u"Click to load common and customs curves.", None))
#endif // QT_CONFIG(tooltip)
        self.button_load.setText(QCoreApplication.translate("Form", u"Load", None))
#if QT_CONFIG(tooltip)
        self.button_save.setToolTip(QCoreApplication.translate("Form", u"This will save customs curves only in your HOME directory under \"Parametric3D.dat\".", None))
#endif // QT_CONFIG(tooltip)
        self.button_save.setText(QCoreApplication.translate("Form", u"Save", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"a", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"b (a) ", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"c (a, b) ", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"X (a,b,c,u,v)", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Y (a,b,c,u,v)", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Z (a,b,c,u,v)", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"u min", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"u max", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"u step", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"v min", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"v max", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"v step", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"comments", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem17 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"Astroid", None));
        ___qtablewidgetitem18 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem19 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem20 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"a*pow(cos(v),3)*pow(cos(u),3)", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"b*pow(cos(v),3)*pow(sin(u),3)", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"c*pow(sin(v),3)", None));
        ___qtablewidgetitem24 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"0.0", None));
        ___qtablewidgetitem25 = self.tableWidget.item(0, 8)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"2*pi", None));
        ___qtablewidgetitem26 = self.tableWidget.item(0, 9)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"0.01", None));
        ___qtablewidgetitem27 = self.tableWidget.item(0, 10)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form", u"-2.0", None));
        ___qtablewidgetitem28 = self.tableWidget.item(0, 11)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form", u"2.0", None));
        ___qtablewidgetitem29 = self.tableWidget.item(0, 12)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Form", u"0.01", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Row", None))
#if QT_CONFIG(tooltip)
        self.button_addRow.setToolTip(QCoreApplication.translate("Form", u"Add a row into the table.", None))
#endif // QT_CONFIG(tooltip)
        self.button_addRow.setText(QCoreApplication.translate("Form", u"add", None))
#if QT_CONFIG(tooltip)
        self.button_removeRow.setToolTip(QCoreApplication.translate("Form", u"Remove a row from the table.", None))
#endif // QT_CONFIG(tooltip)
        self.button_removeRow.setText(QCoreApplication.translate("Form", u"remove", None))
        self.button_quit.setText(QCoreApplication.translate("Form", u"Quit", None))
    # retranslateUi

