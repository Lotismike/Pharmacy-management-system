import sqlite3
from datetime import datetime
import pharmacyLoginController as PLC
class expenseController:

    #add expense
    @staticmethod
    def addExpense(item,cost,qtn,total,detail,username,userID,entryDate,createDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            #uploading to the sales
            cur.execute("INSERT INTO expense(entryDate,userID,username,item,cost,qty,amount,details,created_AT)"
                        " VALUES(?,?,?,?,?,?,?,?,?)",(entryDate,userID,username,item,cost,qtn,total,detail,createDate))
            conn.commit()
            return  1
        except Exception as e:
            print(e)
            return  0
        finally:
            conn.close()

    # loadExpenses
    @staticmethod
    def searchExpenses(searchWord, startDate, endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            expensesData = cur.execute("SELECT id,entryDate,username,item,cost,qty,amount,details FROM  expense WHERE username=?"
                " AND entryDate BETWEEN ? AND ?", (searchWord, startDate, endDate))
            return expensesData
        except Exception as e:
            print(e)

    # loadExpenses
    @staticmethod
    def loadExpenses():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            expensesData = cur.execute("SELECT id,entryDate,username,item,cost,qty,amount,details FROM  expense")
            return expensesData
        except Exception as e:
            print(e)

    # loadExpenses
    @staticmethod
    def searchUserExpenses(startDate, endDate):
        try:
            userNameDD = PLC.pharmacyLoginController.getUsername()
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            expensesData = cur.execute(
                "SELECT id,entryDate,username,item,cost,qty,amount,details FROM  expense WHERE username=?"
                " AND entryDate BETWEEN ? AND ?", (userNameDD, startDate, endDate))
            return expensesData
        except Exception as e:
            print(e)

    # loadExpenses
    @staticmethod
    def loadUserExpenses():
        try:
            userIDID = PLC.pharmacyLoginController.getUserID()
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            expensesData = cur.execute("SELECT id,entryDate,username,item,cost,qty,amount,details"
                                       " FROM  expense WHERE userID = ?",(userIDID,))
            return expensesData
        except Exception as e:
            print(e)
