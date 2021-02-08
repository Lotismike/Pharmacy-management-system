
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime
from PyQt5.QtGui import QCursor
import errors as E
import graphController as GC
import pharmacyLoginController as PLC
from PyQt5.QtGui import QIcon, QPixmap
class Ui_graphAdmin(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("adminPages")
        Dialog.setFixedSize(942, 604)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 950, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("header")
        self.backImg = QtWidgets.QLabel(self.frame)
        self.backImg.setGeometry(QtCore.QRect(30, 16, 40, 41))
        self.backImg.setObjectName("backImg")
        self.backImg.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        pixmap = QPixmap('data/images/back2.png')
        self.backImg.setPixmap(pixmap)
        self.backImg.setScaledContents(True)
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(250, 20, 451, 50))
        self.title.setObjectName("pagesTitle")
        self.username = QtWidgets.QLabel(self.frame)
        self.username.setGeometry(QtCore.QRect(830, 20, 120, 50))
        self.username.setObjectName("usernameLabel")
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))
        ##############################################################################
        ##############################################################################
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 90, 920, 501))
        self.tabWidget.setObjectName("")
        ##################################################
        #       Stock History
        ####################################################
        self.trackStocktab = QtWidgets.QWidget()
        self.trackStocktab.setObjectName("adminTab")
        self.dateEdit_11 = QtWidgets.QDateEdit(self.trackStocktab)
        self.dateEdit_11.setGeometry(QtCore.QRect(80, 10, 121, 28))
        self.dateEdit_11.setObjectName("adminDate")
        self.label_14 = QtWidgets.QLabel(self.trackStocktab)
        self.label_14.setGeometry(QtCore.QRect(10, 9, 65, 31))
        self.label_14.setObjectName("searchLabel")
        self.label_15 = QtWidgets.QLabel(self.trackStocktab)
        self.label_15.setGeometry(QtCore.QRect(210, 10, 41, 31))
        self.label_15.setObjectName("searchLabel")
        self.pushButton_7 = QtWidgets.QPushButton(self.trackStocktab)
        self.pushButton_7.setGeometry(QtCore.QRect(740, 10, 160, 31))
        self.pushButton_7.setObjectName("graphBTN")
        self.pushButton_7.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_12 = QtWidgets.QDateEdit(self.trackStocktab)
        self.dateEdit_12.setGeometry(QtCore.QRect(260, 10, 121, 28))
        self.dateEdit_12.setObjectName("adminDate")
        self.label = QtWidgets.QLabel(self.trackStocktab)
        self.label.setGeometry(QtCore.QRect(420, 10, 71, 31))
        self.label.setObjectName("searchLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.trackStocktab)
        self.lineEdit.setGeometry(QtCore.QRect(520, 10, 191, 28))
        self.lineEdit.setObjectName("adminDate")
        self.tableWidget = QtWidgets.QTableWidget(self.trackStocktab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 892, 381))
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.refreshBTN = QtWidgets.QPushButton(self.trackStocktab)
        self.refreshBTN.setGeometry(QtCore.QRect(360, 435, 191, 33))
        self.refreshBTN.setStyleSheet("border-radius:4px;")
        self.refreshBTN.setObjectName("pagesBTN")
        self.refreshBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.addTab(self.trackStocktab, "")
        #################################
        #       sales
        #################################
        self.SalesTab = QtWidgets.QWidget()
        self.SalesTab.setObjectName("adminTab")
        self.dateEdit = QtWidgets.QDateEdit(self.SalesTab)
        self.dateEdit.setGeometry(QtCore.QRect(130, 10, 171, 28))
        self.dateEdit.setObjectName("adminDate")
        self.label_4 = QtWidgets.QLabel(self.SalesTab)
        self.label_4.setGeometry(QtCore.QRect(40, 9, 91, 31))
        self.label_4.setObjectName("searchLabel")
        self.pushButton = QtWidgets.QPushButton(self.SalesTab)
        self.pushButton.setGeometry(QtCore.QRect(650, 10, 181, 31))
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("graphBTN")
        self.line_2 = QtWidgets.QFrame(self.SalesTab)
        self.line_2.setGeometry(QtCore.QRect(40, 52, 791, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.SalesTab)
        self.dateEdit_2.setGeometry(QtCore.QRect(420, 11, 171, 28))
        self.dateEdit_2.setObjectName("adminDate")
        self.label_5 = QtWidgets.QLabel(self.SalesTab)
        self.label_5.setGeometry(QtCore.QRect(330, 10, 91, 31))
        self.label_5.setObjectName("searchLabel")
        self.salesWidget = QtWidgets.QWidget(self.SalesTab)
        self.salesWidget.setGeometry(QtCore.QRect(40, 60, 791, 411))
        self.salesWidget.setObjectName("salesWidget")
        self.salesVLayout = QtWidgets.QVBoxLayout(self.salesWidget)
        self.salesVLayout.setContentsMargins(0, 0, 0, 0)
        self.salesVLayout.setObjectName("salesVLayout")
        self.widget_5 = QtWidgets.QWidget(self.salesWidget)
        self.widget_5.setObjectName("widget_5")
        self.salesVLayout.addWidget(self.widget_5)
        self.tabWidget.addTab(self.SalesTab, "")
        #################################
        #       Fast
        #################################
        self.fastTab = QtWidgets.QWidget()
        self.fastTab.setObjectName("adminTab")
        self.label_10 = QtWidgets.QLabel(self.fastTab)
        self.label_10.setGeometry(QtCore.QRect(330, 10, 91, 31))
        self.label_10.setObjectName("searchLabel")
        self.dateEdit_7 = QtWidgets.QDateEdit(self.fastTab)
        self.dateEdit_7.setGeometry(QtCore.QRect(420, 11, 171, 28))
        self.dateEdit_7.setObjectName("adminDate")
        self.dateEdit_8 = QtWidgets.QDateEdit(self.fastTab)
        self.dateEdit_8.setGeometry(QtCore.QRect(130, 10, 171, 28))
        self.dateEdit_8.setObjectName("adminDate")
        self.line_5 = QtWidgets.QFrame(self.fastTab)
        self.line_5.setGeometry(QtCore.QRect(40, 52, 791, 2))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line")
        self.label_11 = QtWidgets.QLabel(self.fastTab)
        self.label_11.setGeometry(QtCore.QRect(40, 9, 91, 31))
        self.label_11.setObjectName("searchLabel")
        self.pushButton_4 = QtWidgets.QPushButton(self.fastTab)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 10, 181, 31))
        self.pushButton_4.setObjectName("graphBTN")
        self.pushButton_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.fastWidget = QtWidgets.QWidget(self.fastTab)
        self.fastWidget.setGeometry(QtCore.QRect(40, 60, 791, 411))
        self.fastWidget.setObjectName("fastWidget")
        self.fastVLayout = QtWidgets.QVBoxLayout(self.fastWidget)
        self.fastVLayout.setContentsMargins(0, 0, 0, 0)
        self.fastVLayout.setObjectName("fastVLayout")
        self.widget = QtWidgets.QWidget(self.fastWidget)
        self.widget.setObjectName("widget")
        self.fastVLayout.addWidget(self.widget)
        self.tabWidget.addTab(self.fastTab, "")
        #################################
        #       Staff
        #################################
        self.staffTab = QtWidgets.QWidget()
        self.staffTab.setObjectName("adminTab")
        self.label_6 = QtWidgets.QLabel(self.staffTab)
        self.label_6.setGeometry(QtCore.QRect(330, 11, 91, 31))
        self.label_6.setObjectName("searchLabel")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.staffTab)
        self.dateEdit_3.setGeometry(QtCore.QRect(420, 12, 171, 28))
        self.dateEdit_3.setObjectName("adminDate")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.staffTab)
        self.dateEdit_4.setGeometry(QtCore.QRect(130, 11, 171, 28))
        self.dateEdit_4.setObjectName("adminDate")
        self.line_3 = QtWidgets.QFrame(self.staffTab)
        self.line_3.setGeometry(QtCore.QRect(40, 52, 791, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(self.staffTab)
        self.label_7.setGeometry(QtCore.QRect(40, 10, 91, 31))
        self.label_7.setObjectName("searchLabel")
        self.pushButton_2 = QtWidgets.QPushButton(self.staffTab)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 11, 181, 31))
        self.pushButton_2.setObjectName("graphBTN")
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.staffWidget = QtWidgets.QWidget(self.staffTab)
        self.staffWidget.setGeometry(QtCore.QRect(40, 60, 791, 411))
        self.staffWidget.setObjectName("staffWidget")
        self.staffVLayout = QtWidgets.QVBoxLayout(self.staffWidget)
        self.staffVLayout.setContentsMargins(0, 0, 0, 0)
        self.staffVLayout.setObjectName("staffVLayout")
        self.widget_2 = QtWidgets.QWidget(self.staffWidget)
        self.widget_2.setObjectName("widget_2")
        self.staffVLayout.addWidget(self.widget_2)
        self.tabWidget.addTab(self.staffTab, "")
        #################################
        #       Expenditure
        #################################
        self.expTab = QtWidgets.QWidget()
        self.expTab.setObjectName("adminTab")
        self.label_8 = QtWidgets.QLabel(self.expTab)
        self.label_8.setGeometry(QtCore.QRect(330, 9, 91, 31))
        self.label_8.setObjectName("searchLabel")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.expTab)
        self.dateEdit_5.setGeometry(QtCore.QRect(420, 10, 171, 28))
        self.dateEdit_5.setObjectName("adminDate")
        self.dateEdit_6 = QtWidgets.QDateEdit(self.expTab)
        self.dateEdit_6.setGeometry(QtCore.QRect(130, 9, 171, 28))
        self.dateEdit_6.setObjectName("adminDate")
        self.line_4 = QtWidgets.QFrame(self.expTab)
        self.line_4.setGeometry(QtCore.QRect(40, 52, 791, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(self.expTab)
        self.label_9.setGeometry(QtCore.QRect(40, 8, 91, 31))
        self.label_9.setObjectName("searchLabel")
        self.pushButton_3 = QtWidgets.QPushButton(self.expTab)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 9, 181, 31))
        self.pushButton_3.setObjectName("graphBTN")
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.expWidget = QtWidgets.QWidget(self.expTab)
        self.expWidget.setGeometry(QtCore.QRect(40, 60, 791, 411))
        self.expWidget.setObjectName("expWidget")
        self.expVLayout = QtWidgets.QVBoxLayout(self.expWidget)
        self.expVLayout.setContentsMargins(0, 0, 0, 0)
        self.expVLayout.setObjectName("expVLayout")
        self.widget_3 = QtWidgets.QWidget(self.expWidget)
        self.widget_3.setObjectName("widget_3")
        self.expVLayout.addWidget(self.widget_3)
        self.tabWidget.addTab(self.expTab, "")
        #################################
        #       Profit
        #################################
        self.profitTab = QtWidgets.QWidget()
        self.profitTab.setObjectName("adminTab")
        self.dateEdit_9 = QtWidgets.QDateEdit(self.profitTab)
        self.dateEdit_9.setGeometry(QtCore.QRect(130, 11, 171, 31))
        self.dateEdit_9.setObjectName("adminDate")
        self.dateEdit_10 = QtWidgets.QDateEdit(self.profitTab)
        self.dateEdit_10.setGeometry(QtCore.QRect(420, 12, 171, 31))
        self.dateEdit_10.setObjectName("adminDate")
        self.label_12 = QtWidgets.QLabel(self.profitTab)
        self.label_12.setGeometry(QtCore.QRect(330, 11, 91, 31))
        self.label_12.setObjectName("searchLabel")
        self.line_6 = QtWidgets.QFrame(self.profitTab)
        self.line_6.setGeometry(QtCore.QRect(40, 52, 791, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line")
        self.profitWidget = QtWidgets.QWidget(self.profitTab)
        self.profitWidget.setGeometry(QtCore.QRect(40, 60, 791, 411))
        self.profitWidget.setObjectName("profitWidget")
        self.profitVLayout = QtWidgets.QVBoxLayout(self.profitWidget)
        self.profitVLayout.setContentsMargins(0, 0, 0, 0)
        self.profitVLayout.setObjectName("profitVLayout")
        self.widget_4 = QtWidgets.QWidget(self.profitWidget)
        self.widget_4.setObjectName("widget_4")
        self.profitVLayout.addWidget(self.widget_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.profitTab)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 11, 181, 31))
        self.pushButton_6.setObjectName("graphBTN")
        self.pushButton_6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.label_13 = QtWidgets.QLabel(self.profitTab)
        self.label_13.setGeometry(QtCore.QRect(40, 10, 91, 31))
        self.label_13.setObjectName("searchLabel")
        self.tabWidget.addTab(self.profitTab, "")
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ##my intials
        self.stockEntry()
        colHeaders = ['Entry Date','Action','Action By','Drug Name', 'Category', 'Cost Price',
                      'Quantity', 'Created At']
        self.tableWidget.setHorizontalHeaderLabels(colHeaders)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)

        self.pushButton.clicked.connect(self.drawSalesGraph)
        self.pushButton_4.clicked.connect(self.drawFastGraph)
        self.pushButton_2.clicked.connect(self.drawStaffSalesGraph)
        self.pushButton_3.clicked.connect(self.drawStaffExpGraph)
        self.pushButton_6.clicked.connect(self.drawSalesProfitGraph)
        self.refreshBTN.clicked.connect(self.stockEntry2)
        self.pushButton_7.clicked.connect(self.searchStockHistory)
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))

    # stockEntries
    def stockEntry(self):
        eObj = E.errors()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(GC.graphController.loadStockHistory()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    #stockEntries2
    def stockEntry2(self):
        eObj = E.errors()
        self.tableWidget.setRowCount(0)
        if len(GC.graphController.loadStockHistory().fetchall())>0:
            for row_number, row_data in enumerate(GC.graphController.loadStockHistory()):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            eObj.errorBox("Error","No data to show")
    #searchStockHistory
    def searchStockHistory(self):
        eObj = E.errors()
        sDate = self.dateEdit_11.text()
        eDate = self.dateEdit_12.text()
        drugNa = self.lineEdit.text()

        # sub dates
        start_date = datetime.strptime(sDate, "%d/%m/%Y")
        end_date = datetime.strptime(eDate, "%d/%m/%Y")
        diff = end_date - start_date

        if diff.days == 0:
            eObj.errorBox("Error", "Please enter date interval")
        elif diff.days < 0:
            eObj.errorBox("Error", "End date should be greater than start date")
        else:
            self.tableWidget.setRowCount(0)
            if len(GC.graphController.searchStockHistory(sDate, eDate, drugNa).fetchall()) > 0:
                for row_number, row_data in enumerate(GC.graphController.searchStockHistory(sDate, eDate, drugNa)):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                eObj.errorBox("Error", "No data to show in the specified date interval")

    # draw sales
    def drawSalesGraph(self):
        eObj = E.errors()
        sDate = self.dateEdit.text()
        eDate=self.dateEdit_2.text()

        # sub dates
        start_date = datetime.strptime(sDate, "%d/%m/%Y")
        end_date = datetime.strptime(eDate, "%d/%m/%Y")
        diff = end_date - start_date

        if diff.days == 0:
            eObj.errorBox("Error", "Please enter date interval")
        elif diff.days < 0:
            eObj.errorBox("Error", "End date should be greater than start date")
        else:
            #delete old graph
            self.clearSalesGraph()
            salesData = GC.graphController.salesGraph(sDate,eDate).fetchall()

            drugNames =[]
            totalSales =[]
            if len(salesData)>0:
                for row in salesData:
                    drugNames.append(row[0])
                    totalSales.append(int(row[1]))

                #drawing graph
                fig1 = Figure()
                plt = fig1.add_subplot(111)
                ypos = np.arange(len(drugNames))
                plt.set_title("A Bar Graph Showing Sales Made Per Drug")
                plt.set_xlabel("Drug Name")
                plt.set_ylabel("Total Sales")
                plt.bar(ypos,totalSales)

                plt.set_xticks(ypos)
                plt.set_xticklabels(drugNames, fontsize=9)

                #Draw the figure
                self.canvas = FigureCanvas(fig1)
                self.salesVLayout.addWidget(self.canvas)
                self.canvas.draw()

            else:
                eObj.errorBox("Error", "No data for the selected date interval")

    # clearSalesGraph
    def clearSalesGraph(self, ):
        for i in reversed(range(self.salesVLayout.count())):
            self.salesVLayout.itemAt(i).widget().setParent(None)

    #drawFastGraph
    def drawFastGraph(self):
        eObj = E.errors()
        sDate = self.dateEdit_8.text()
        eDate = self.dateEdit_7.text()

        # sub dates
        start_date = datetime.strptime(sDate, "%d/%m/%Y")
        end_date = datetime.strptime(eDate, "%d/%m/%Y")
        diff = end_date - start_date

        if diff.days == 0:
            eObj.errorBox("Error", "Please enter date interval")
        elif diff.days < 0:
            eObj.errorBox("Error", "End date should be greater than start date")
        else:
            # delete old graph
            self.clearFastGraph()
            salesData = GC.graphController.fastMovingGraph(sDate, eDate).fetchall()

            drugNames = []
            totalSales = []
            if len(salesData) > 0:
                for row in salesData:
                    drugNames.append(row[0])
                    totalSales.append(int(row[1]))

                # drawing graph
                fig1 = Figure()
                plt = fig1.add_subplot(111)
                plt.set_title("A Pie Chart Showing Fast Moving 100 Drugs", color="b")
                plt.axis("equal")
                plt.pie(totalSales, radius=1.2, labels=drugNames, autopct='%0.0f%%', shadow=True,textprops={'fontsize': 9})
                # Draw the figure
                self.canvas = FigureCanvas(fig1)
                self.fastVLayout.addWidget(self.canvas)
                self.canvas.draw()

            else:
                eObj.errorBox("Error", "No data for the selected date interval")

    # clearSalesGraph
    def clearFastGraph(self, ):
        for i in reversed(range(self.fastVLayout.count())):
            self.fastVLayout.itemAt(i).widget().setParent(None)

    #drawStaffSalesGraph
    def drawStaffSalesGraph(self):
        eObj = E.errors()
        sDate = self.dateEdit_4.text()
        eDate = self.dateEdit_3.text()

        # sub dates
        start_date = datetime.strptime(sDate, "%d/%m/%Y")
        end_date = datetime.strptime(eDate, "%d/%m/%Y")
        diff = end_date - start_date

        if diff.days == 0:
            eObj.errorBox("Error", "Please enter date interval")
        elif diff.days < 0:
            eObj.errorBox("Error", "End date should be greater than start date")
        else:
            # delete old graph
            self.clearStaffSalesGraph()
            salesData = GC.graphController.staffSalesGraph(sDate, eDate).fetchall()

            staffNames = []
            totalSales = []
            if len(salesData) > 0:
                for row in salesData:
                    staffNames.append(row[0])
                    totalSales.append(int(row[1]))

                # drawing graph
                fig1 = Figure()
                plt = fig1.add_subplot(111)
                ypos = np.arange(len(staffNames))
                plt.set_title("A Bar Graph Showing Total Sales Made By Staff Members")
                plt.set_xlabel("Staff Username")
                plt.set_ylabel("Total Sales")
                plt.bar(ypos, totalSales,color="#728C00")

                plt.set_xticks(ypos)
                plt.set_xticklabels(staffNames, fontsize=9)

                # Draw the figure
                self.canvas = FigureCanvas(fig1)
                self.staffVLayout.addWidget(self.canvas)
                self.canvas.draw()

            else:
                eObj.errorBox("Error", "No data for the selected date interval")

    # clearSalesGraph
    def clearStaffSalesGraph(self, ):
        for i in reversed(range(self.staffVLayout.count())):
            self.staffVLayout.itemAt(i).widget().setParent(None)

    #drawStaffExpGraph
    def drawStaffExpGraph(self):
        eObj = E.errors()
        sDate = self.dateEdit_6.text()
        eDate = self.dateEdit_5.text()

        # sub dates
        start_date = datetime.strptime(sDate, "%d/%m/%Y")
        end_date = datetime.strptime(eDate, "%d/%m/%Y")
        diff = end_date - start_date

        if diff.days == 0:
            eObj.errorBox("Error", "Please enter date interval")
        elif diff.days < 0:
            eObj.errorBox("Error", "End date should be greater than start date")
        else:
            # delete old graph
            self.clearStaffExpGraph()
            salesData = GC.graphController.staffExpGraph(sDate, eDate).fetchall()

            staffNames = []
            totalExpenses = []
            if len(salesData) > 0:
                for row in salesData:
                    staffNames.append(row[0])
                    totalExpenses.append(int(row[1]))

                # drawing graph
                fig1 = Figure()
                plt = fig1.add_subplot(111)
                plt.set_title("A Pie Chart Showing Expenses Made By Staff Members", color="b")
                plt.axis("equal")
                plt.pie(totalExpenses, radius=1.2, labels=staffNames, autopct='%0.0f%%', shadow=True,
                        textprops={'fontsize': 9})
                # Draw the figure
                self.canvas = FigureCanvas(fig1)
                self.expVLayout.addWidget(self.canvas)
                self.canvas.draw()

            else:
                eObj.errorBox("Error", "No data for the selected date interval")

    # clearStaffExpGraph
    def clearStaffExpGraph(self, ):
        for i in reversed(range(self.expVLayout.count())):
            self.expVLayout.itemAt(i).widget().setParent(None)

    #drawSalesProfitGraph
    def drawSalesProfitGraph(self):
        eObj = E.errors()
        sDate = self.dateEdit_9.text()
        eDate = self.dateEdit_10.text()

        # sub dates
        start_date = datetime.strptime(sDate, "%d/%m/%Y")
        end_date = datetime.strptime(eDate, "%d/%m/%Y")
        diff = end_date - start_date

        if diff.days == 0:
            eObj.errorBox("Error", "Please enter date interval")
        elif diff.days < 0:
            eObj.errorBox("Error", "End date should be greater than start date")
        else:
            # delete old graph
            self.clearSalesProfitGraph()
            salesData = GC.graphController.salesProfitGraph(sDate, eDate).fetchall()

            drugNames = []
            totalSales = []
            profit = []
            if len(salesData) > 0:
                for row in salesData:
                    drugNames.append(row[0])
                    totalSales.append(int(row[1]))
                    profit.append(int(row[3]))

                # drawing graph
                fig1 = Figure()
                plt = fig1.add_subplot(111)
                ypos = np.arange(len(drugNames))
                plt.set_title("A Graph Showing Total Sales Against Total Profit Made Per Drug")
                plt.set_xlabel("Staff Username")
                plt.set_ylabel("Total Sales")

                plt.bar(ypos-0.2, totalSales,width=0.4,label="Total Sales")
                plt.bar(ypos+0.2, profit,width=0.4, label="Total Profit")
                plt.legend()

                plt.set_xticks(ypos)
                plt.set_xticklabels(drugNames, fontsize=9)

                # Draw the figure
                self.canvas = FigureCanvas(fig1)
                self.profitVLayout.addWidget(self.canvas)
                self.canvas.draw()

            else:
                eObj.errorBox("Error", "No data for the selected date interval")

    #clearStaffExpGraph
    def clearSalesProfitGraph(self, ):
        for i in reversed(range(self.profitVLayout.count())):
            self.profitVLayout.itemAt(i).widget().setParent(None)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Graphs | UG - Pharmacy Management System"))

        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "Graphical Representations"))
        self.username.setText(_translate("Dialog", "Username"))
        self.label_14.setText(_translate("Dialog", "Start From"))
        self.label_15.setText(_translate("Dialog", "End At"))
        self.pushButton_7.setText(_translate("Dialog", "Track Stock Entries"))
        self.label.setText(_translate("Dialog", "Drug Name "))
        self.refreshBTN.setText(_translate("Dialog", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trackStocktab), _translate("Dialog", "Stock Entries"))
        self.label_4.setText(_translate("Dialog", "Start From"))
        self.pushButton.setText(_translate("Dialog", "Generate Graph"))
        self.label_5.setText(_translate("Dialog", "End At"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SalesTab), _translate("Dialog", "Sales Graph"))
        self.label_10.setText(_translate("Dialog", "End At"))
        self.label_11.setText(_translate("Dialog", "Start From"))
        self.pushButton_4.setText(_translate("Dialog", "Generate Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fastTab), _translate("Dialog", "Fast Moving Graph"))
        self.label_6.setText(_translate("Dialog", "End At"))
        self.label_7.setText(_translate("Dialog", "Start From"))
        self.pushButton_2.setText(_translate("Dialog", "Generate Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.staffTab), _translate("Dialog", "Staff Sales Graph"))
        self.label_8.setText(_translate("Dialog", "End At"))
        self.label_9.setText(_translate("Dialog", "Start From"))
        self.pushButton_3.setText(_translate("Dialog", "Generate Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.expTab), _translate("Dialog", "Staff Expenses Graph"))
        self.label_12.setText(_translate("Dialog", "End At"))
        self.pushButton_6.setText(_translate("Dialog", "Generate Graph"))
        self.label_13.setText(_translate("Dialog", "Start From"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profitTab), _translate("Dialog", "Profit Vs Sales "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_graphAdmin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

