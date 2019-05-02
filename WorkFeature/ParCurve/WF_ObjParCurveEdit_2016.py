# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:53:08 2015

@author: laurent
"""
import sys
import os.path

import ParCurve.Ui.WF_ObjParCurve2DEditGui_2016 as EDIT_2D
import ParCurve.Ui.WF_ObjParCurve3DEditGui_2016 as EDIT_3D
import ParCurve.Ui.WF_ObjSurfaceEditGui_2016 as EDIT_SURF
import ParCurve.Utils.Text as txt

from PySide import QtCore, QtGui
import FreeCAD as App

# Get the path of the current python script
m_current_path = os.path.realpath(__file__)
# Update paths
if not sys.path.__contains__(m_current_path):
    sys.path.append(m_current_path)

global myDatabase2DName
myDatabase2DName = "Parametric2D.dat"
global myDatabase3DName
myDatabase3DName = "Parametric3D.dat"
global myDatabaseSurfName
myDatabaseSurfName = "ParametricSurf.dat"
####################################################################################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

index = ['Name', 'a', 'b', 'c', 'X', 'Y', 'Z', 'tmin', 'tmax', 'tstep']
d1 = ["default", 37, 1, '(a+cos(a*t)*2)*b', 'cos(t)*c', 'sin(t)*c', 0, 0., '2*pi', 0.01]
d2 = ["spiral", 5, 0, 10, 'c*sin(t)', 'c*cos(t)', 'a*0.05*t', .0, '20*pi', '0.05*pi']
d3 = ["Seam of a tennis ball", '5', '5', '2*(sqrt(a*b))', 'a*(cos(t))+b*(cos(3*t))',
      'a*(sin(t))-b*(sin(3*t))', 'c*(sin(2*t))', 0., '2*pi', '0.05*pi']


class Model(QtCore.QAbstractTableModel):
    def __init__(self, tableWidget):
        super(Model, self).__init__()
        self.table = []
        # print "Initialize table " + str(self.table)
        for i_row in range(tableWidget.rowCount()):
            m_line = []
            for i_column in range(tableWidget.columnCount()):
                # print str(i_column)
                m_item = tableWidget.item(i_row, i_column)
                if m_item is None:
                    break
                else:
                    # print str(tableWidget.item(i_row, i_column).text())
                    m_line.append(str(tableWidget.item(i_row, i_column).text()))

            if len(m_line) != 0:
                self.table.append(m_line)
        # print str(self.table)
        self.columnNumber = 0
        self.rowNumber = 0
        self.rowNumber = len(self.table)
        if self.rowNumber != 0:
            self.columnNumber = len(self.table[0])
        # print "self.rowNumber=" + str(self.rowNumber)
        # print "self.columnNumber=" + str(self.columnNumber)

    def rowCount(self, index=QtCore.QModelIndex()):
        return self.rowNumber

    def columnCount(self, index=QtCore.QModelIndex()):
        return self.columnNumber

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.table[index.row()][index.column()]

    def setData(self, index, role, value):
        if role == QtCore.Qt.DisplayRole:
            self.table[index.row()][index.column()] = value


class tableWidget():
    def __init__(self, database):
        """
        parameter database: the name of database file without path.
        """
        # Flag for common database
        self.database_exists = False
        self.database_name = None
        self.curves_number = 0
        self.curves_loaded = False
        # Flag for user database
        self.database_user_exists = False
        self.database_user_name = None
        self.curves_user_number = 0
        self.curves_user_loaded = False
        if database:
            # Check if database file exists in current script directory
            m_current = os.path.dirname(__file__)
            m_dirs_to_look = [str(m_current), str(m_current) + "/Ressources", ]
            for m_dir in m_dirs_to_look:
                self.database_path = m_dir + "/"
                # print self.database_path
                self.database_name = str(self.database_path) + str(database)
                if os.path.exists(self.database_name):
                    self.database_exists = True

            # Check if database file exists in home directory
            m_home = os.path.expanduser("~")
            self.database_path = m_home + "/"
            self.database_user_name = str(self.database_path) + str(database)
            if os.path.exists(self.database_user_name):
                self.database_user_exists = True

        self.header = None

        # This Object ill be created with the setupUi
        # self.tableWidget = QtGui.QTableWidget(Form)  
        self.tableWidget = None
# ===============================================================================
# class tableWidget2D(EDIT_2D.Ui_Form, tableWidget):
#     def __init__(self, database="Parametric2D.dat"):
#         EDIT_2D.Ui_Form.__init__(self)
#         tableWidget.__init__(self, database)
#         self.header = "Name, a (t), b (a,t), X (a,b,t), Y(a,b,t), Polar, tmin, tmax, tstep"
#
#     def setupUi(self, Form, combox):
#         EDIT_2D.Ui_Form.setupUi(self, Form)
#         tableWidget.setupUi(self, Form, combox)
# ===============================================================================
        self.dialog = None
        self.comboBox = None
        self.connections_for_button_pressed = None
        self.connections_for_combobox_changed = None
        self.model = None

    def setupUi(self, Form, combox):
        self.dialog = Form
        self.comboBox = combox
        self.updateModel()

        # Connect to functions
        self.connections_for_button_pressed = {
                            "button_addRow"         : "insertRowAfter",
                            "button_removeRow"      : "removeSelectedRow",
                            "button_load"           : "loadDatabase",
                            "button_save"           : "saveDatabase",
                            "button_quit"           : "widgetQuit", 
                            }
        self.connections_for_combobox_changed = {
                            "comboBox_select"       : "selectCurve",
                            }

        for m_key, m_val in self.connections_for_button_pressed.items():
            # print_msg( "Connecting: " + str(getattr(self, str(m_key))) + " and " + str(getattr(self, str(m_val))) )
            QtCore.QObject.connect(getattr(self, str(m_key)),
                                   QtCore.SIGNAL("pressed()"), getattr(self, str(m_val)))

        for m_key, m_val in self.connections_for_combobox_changed.items():
            # print_msg( "Connecting: " + str(getattr(self, str(m_key))) + " and " + str(getattr(self, str(m_val))) )
            QtCore.QObject.connect(getattr(self, str(m_key)),
                                   QtCore.SIGNAL("currentIndexChanged(QString)"), getattr(self, str(m_val)))
        self.curves_number = 0
        self.curves_user_number = 0
        if self.database_exists:
            self.curves_number = self.loadDatabase(self.database_name)
            print("Database: " + str(self.database_name))
            print("Loaded from common database: " + str(self.curves_number) + " curves !")
            if self.curves_number != 0:
                self.curves_loaded = True

        if self.database_user_exists:
            self.curves_user_number = self.loadDatabase(self.database_user_name)
            print("Database: " + str(self.database_user_name))
            print("Loaded from user database: " + str(self.curves_user_number) + " curves !")
            if self.curves_user_number != 0:
                self.curves_user_loaded = True

    def updateModel(self):
        self.model = Model(self.tableWidget)
        self.comboBox.setModel(self.model)
        self.comboBox.setModelColumn(0)

    def insertRow(self, row):
        self.tableWidget.insertRow(row)

    def insertRowAfter(self):
        self.insertRow(self.tableWidget.rowCount())

    def setRowCount(self, row):
        self.tableWidget.setRowCount(row)

    def removeSelectedRow(self):
        m_index = self.tableWidget.currentRow()
        self.removeRow(m_index)

    def removeRow(self, row):
        self.tableWidget.removeRow(row)
        self.updateModel()

    def removeLastRow(self):
        self.removeRow(self.tableWidget.rowCount() - 1)

    def insertDataAfter(self, data, rowCount):
        if isinstance(data, list) is not True:
            print("Type of input data must be a 'list'")
            return
        m_rowNumber = len(data)
        m_columnNumber = len(data[0])
        m_widget = self.tableWidget
        for i in range(m_rowNumber):
            self.insertRowAfter()
            for j in range(m_columnNumber):
                item = QtGui.QTableWidgetItem(str(data[i][j]))
                m_widget.setItem(rowCount + i, j, item)
        self.updateModel()

    def insertData(self, data):
        if isinstance(data, list) is not True:
            print("Type of input data must be a 'list'")
            return
        # print str(data)
        m_rowNumber = len(data)
        m_columnNumber = len(data[0])
        m_widget = self.tableWidget
        m_widget.setRowCount(m_rowNumber)
        # m_widget.setColumnCount(columns)
        # m_widget.setHorizontalHeaderLabels(['name', 'num','x','y','z'])
        for i in range(m_rowNumber):
            for j in range(m_columnNumber):
                item = QtGui.QTableWidgetItem(str(data[i][j]))
                m_widget.setItem(i, j, item)
        self.updateModel()

    def addCurveData(self, data):
        m_curveList = self.selectAllCurves()
        m_curveList.append(data)
        self.insertData(m_curveList)

    def loadDatabase(self, my_database_name):
        m_line = 0
        try:
            m_lines = txt.read_text_into_list(my_database_name)
            del m_lines[0]
            m_data = []
            for m_line in m_lines:
                d = eval(m_line)
                # print str(d)
                m_data.append(d)

            # print str(self.curves_number + self.curves_user_number)
            if (self.curves_number + self.curves_user_number) == 0:
                self.insertData(m_data)
            else:
                self.insertDataAfter(m_data, (self.curves_number + self.curves_user_number))

            return len(m_data)
        except:
            message = "Unable to load the database file \n" + str(my_database_name)
            message += "\nAt line \n" + str(m_line)
            print(message)
            App.Console.PrintError("\nERROR: " + message)

    def saveDatabase(self, my_database_name=None):
        if my_database_name in [None]:
            my_database_name = self.database_user_name

        if (self.curves_number) != 0:
            m_curves = self.selectAllCurvesFrom(self.curves_number)
        else:
            m_curves = self.selectAllCurves()

        # print str(m_curves)
        txt.write_text(filename=my_database_name, text=str(self.header))
        txt.append_text(filename=my_database_name, text="")
        for m_curve in m_curves:
            txt.append_text(filename=my_database_name, text=str(m_curve))

    def selectCurve(self, *argc):
        # print str(*argc)
        m_curveRow = self.tableWidget.row(self.tableWidget.findItems(str(*argc), QtCore.Qt.MatchExactly)[0])
        print(str(m_curveRow))
        m_line = []
        for i_column in range(self.tableWidget.columnCount()):
            # print str(i_column)
            m_item = self.tableWidget.item(m_curveRow, i_column)
            if m_item is None:
                break
            else:
                # print str(tableWidget.item(i_row, i_column).text())
                m_line.append(str(self.tableWidget.item(m_curveRow, i_column).text()))
        # print str(m_line)
        return m_line

    def selectAllCurvesFrom(self, row):
        m_lineList = []
        m_total_rows = self.tableWidget.rowCount()
        m_total_cols = self.tableWidget.columnCount()
        for i_row in range(row, m_total_rows):
            m_line = []
            for i_column in range(m_total_cols):
                m_item = self.tableWidget.item(i_row, i_column)
                if m_item is None:
                    break
                else:
                    m_line.append(str(self.tableWidget.item(i_row, i_column).text()))
            m_lineList.append(m_line)
        # print str(m_lineList)
        return m_lineList

    def selectAllCurves(self):
        m_lineList = []
        m_total_rows = self.tableWidget.rowCount()
        m_total_cols = self.tableWidget.columnCount()
        for i_row in range(m_total_rows):
            m_line = []
            for i_column in range(m_total_cols):
                m_item = self.tableWidget.item(i_row, i_column)
                if m_item is None:
                    break
                else:
                    m_line.append(str(self.tableWidget.item(i_row, i_column).text()))
            m_lineList.append(m_line)
        # print str(m_lineList)
        return m_lineList

    def widgetQuit(self):
        self.dialog.hide()


class tableWidget2D(EDIT_2D.Ui_Form, tableWidget):
    def __init__(self, database="Parametric2D.dat"):
        EDIT_2D.Ui_Form.__init__(self)
        tableWidget.__init__(self, database)
        self.header = "Name, a (t), b (a,t), X (a,b,t), Y(a,b,t), Polar, tmin, tmax, tstep"

    def setupUi(self, Form, combox):
        EDIT_2D.Ui_Form.setupUi(self, Form)
        tableWidget.setupUi(self, Form, combox)


class tableWidget3D(EDIT_3D.Ui_Form, tableWidget):
    def __init__(self, database="Parametric3D.dat"):
        EDIT_3D.Ui_Form.__init__(self)
        tableWidget.__init__(self, database)
        self.header = "Name, a (t), b (a,t),c (a,b,t), X (a,b,c,t), Y (a,b,c,t), Z (a,b,c,t), tmin, tmax, tstep, Cartesian"

    def setupUi(self, Form, combox):
        EDIT_3D.Ui_Form.setupUi(self, Form)
        tableWidget.setupUi(self, Form, combox)


class tableWidgetSurf(EDIT_SURF.Ui_Form, tableWidget):
    def __init__(self, database="ParametricSurf.dat"):
        EDIT_SURF.Ui_Form.__init__(self)
        tableWidget.__init__(self, database)
        self.header = "Name, a , b (a),c (a,b), X (a,b,c,U,V), Y (a,b,c,U,V), Z (a,b,c,U,V), U min, U max, U step, V min, V max, V step, Comment"

    def setupUi(self, Form, combox):
        EDIT_SURF.Ui_Form.setupUi(self, Form)
        tableWidget.setupUi(self, Form, combox)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app = QtGui.qApp
    # app.exec_()
    myNewWidget = QtGui.QDockWidget()
    myNewWidget = QtGui.QWidget()
    # myNewWidget.ui = Ui_Form()
    myNewWidget.ui = tableWidget()
    myNewWidget.ui.setupUi(myNewWidget)
    # myNewWidget.ui.insertRow(1)
    # myNewWidget.ui.insertRow(3)
    # myNewWidget.ui.removeRow(3)
    myNewWidget.ui.insertRowAfter()
    myNewWidget.ui.insertRowAfter()
    myNewWidget.ui.insertRowAfter()
    myNewWidget.ui.removeLastRow()
    # myNewWidget.ui.setRowCount(20)
    mydata = []
    mydata.append(d1)
    mydata.append(d2)
    mydata.append(d3)
    myNewWidget.ui.insertData(mydata)
    myNewWidget.show()

    # mw = app.activeWindow()
    # mw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewWidget)
    app.exec_()
