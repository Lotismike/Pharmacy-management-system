
import sqlite3
from datetime import datetime
class graphController():

    #salesGraph
    @staticmethod
    def salesGraph(startDate,endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            salesData = cur.execute("SELECT drugName, SUM(discountedAmount) as totals FROM sales WHERE entryDate BETWEEN ? AND ? GROUP BY drugID",(startDate, endDate))
            return salesData
        except Exception as e:
            print(e)

    @staticmethod
    def fastMovingGraph(startDate,endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            salesData = cur.execute(
                "SELECT drugName,COUNT(drugID) as myCount FROM  sales WHERE entryDate BETWEEN ? AND ? GROUP BY drugID ORDER BY COUNT(drugID) DESC LIMIT 100 ",(startDate, endDate))
            return salesData
        except Exception as e:
            print(e)

    @staticmethod
    def staffSalesGraph(startDate, endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            salesData = cur.execute(
                "SELECT workedOnBy,SUM(discountedAmount) as totals FROM  sales WHERE entryDate BETWEEN ? AND ? GROUP BY workedOnBy",
                (startDate, endDate))
            return salesData
        except Exception as e:
            print(e)

    #staffExpGraph
    @staticmethod
    def staffExpGraph(startDate, endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            salesData = cur.execute(
                "SELECT username,SUM(amount) as totals FROM  expense WHERE entryDate BETWEEN ? AND ? GROUP BY username",
                (startDate, endDate))
            return salesData
        except Exception as e:
            print(e)

    #salesProfitGraph
    @staticmethod
    def salesProfitGraph(startDate, endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            salesData = cur.execute(
                "SELECT ss.drugName, SUM(ss.discountedAmount) as totalsSales,"
                "(SELECT buyingPrice FROM stock as S WHERE ss.drugID = S.id)*ss.qtn as totalBuying,"
                "(SUM(ss.discountedAmount)-((SELECT buyingPrice FROM stock as S WHERE ss.drugID = S.id)*ss.qtn)) as profit"
                " FROM sales as ss WHERE ss.entryDate BETWEEN ? AND ?  GROUP BY ss.drugID",(startDate, endDate))
            return salesData
        except Exception as e:
            print(e)

    # loadStockHistory
    @staticmethod
    def loadStockHistory():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            salesData = cur.execute("SELECT entryDate,action,actionBY,drugName,category,cost,qty,created_At FROM  stockhistory")
            return salesData
        except Exception as e:
            print(e)

    #SearchStockHistory
    @staticmethod
    def searchStockHistory(startDate, endDate,drugName):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            if drugName =="":
                salesData = cur.execute(
                    "SELECT entryDate,action,actionBY,drugName,category,cost,qty,created_At FROM  stockhistory WHERE entryDate BETWEEN ? AND ?",(startDate, endDate))
            else:
                salesData = cur.execute(
                    "SELECT entryDate,action,actionBY,drugName,category,cost,qty,created_At FROM  stockhistory WHERE entryDate BETWEEN ? AND ?"
                    "AND drugName like ? ",(startDate, endDate,'%'+drugName+'%'))

            return salesData
        except Exception as e:
            print(e)


