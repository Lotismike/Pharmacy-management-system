import sqlite3
from datetime import datetime

class profitController():

    #searchProfit
    @staticmethod
    def searchProfit(startDate, endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            salesData = cur.execute(
                "SELECT S.drugName,"
                "(SELECT ss.buyingPrice FROM stock as ss WHERE ss.id = S.drugID ) as buyPrice,"
                "SUM(S.qtn) as qtn,"
                "((SELECT ss.buyingPrice FROM stock as ss WHERE ss.id = S.drugID )*SUM(S.qtn)) as totalCosts,"
                "SUM(S.discountedAmount) as totals,"
                "(SUM(S.discountedAmount) - ((SELECT ss.buyingPrice FROM stock as ss WHERE ss.id = S.drugID )*SUM(S.qtn))) as profit,"
                "S.entryDate "
                "FROM sales as S WHERE S.entryDate BETWEEN ? AND ? GROUP BY S.drugID", (startDate, endDate))
            return salesData
        except Exception as e:
            print(e)

    # searchProfit
    @staticmethod
    def getTotalCredit(startDate, endDate):

        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            salesData = cur.execute(
                "SELECT SUM(balance) as balance FROM credit WHERE created_AT BETWEEN ? AND ?", (startDate, endDate))
            return salesData
        except Exception as e:
            print(e)

    #getTotalExpenses
    @staticmethod
    def getTotalExpenses(startDate, endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            salesData = cur.execute(
                "SELECT SUM(amount) as amount FROM expense WHERE entryDate BETWEEN ? AND ?", (startDate, endDate))
            return salesData
        except Exception as e:
            print(e)