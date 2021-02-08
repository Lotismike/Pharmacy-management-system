import sqlite3
import usersData as UD
from datetime import datetime
import pharmacyLoginController as PLC
class mainController():
    #loadstock
    @staticmethod
    def loadSales():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            salesData = cur.execute("SELECT created_AT,billNumber,category,drugName,batch,sellingPrice,qtn,total,discount,"
                                    "discountedAmount,payMethod,paidBy,workedOnBy FROM sales")
            return salesData
        except Exception as e:
            print(e)

    # get names
    @staticmethod
    def getUserData():
        try:
            listUsernameData = []
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            getusernameData = cur.execute("SELECT id,username From users WHERE username !='admin'")
            usernameData = getusernameData.fetchall()

            for row in usernameData:
                dbCatData = UD.usersData(row[0], row[1])  # id,catName
                listUsernameData.append(dbCatData)
            return listUsernameData
        except Exception as e:
            print(e)
        finally:
            conn.close()

    # searchSales
    @staticmethod
    def searchSales(searchWord, searchType,startDate,endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            if searchType == "username":
                salesData = cur.execute(
                    "SELECT created_AT,billNumber,category,drugName,batch,sellingPrice,qtn,total,discount,"
                    "discountedAmount,payMethod,paidBy,workedOnBy FROM  sales WHERE workedOnBy=? AND entryDate"
                    " BETWEEN ? AND ?", (searchWord,startDate,endDate))

                return salesData
            elif searchType == "category":
                salesData = cur.execute(
                    "SELECT created_AT,billNumber,category,drugName,batch,sellingPrice,qtn,total,discount,"
                    "discountedAmount,payMethod,paidBy,workedOnBy FROM  sales WHERE category=?"
                    " AND entryDate BETWEEN ? AND ?", (searchWord,startDate,endDate))

                return salesData
            elif searchType == "drugName":
                salesData = cur.execute(
                    "SELECT created_AT,billNumber,category,drugName,batch,sellingPrice,qtn,total,discount,"
                    "discountedAmount,payMethod,paidBy,workedOnBy FROM sales WHERE drugName LIKE ?"
                    " AND entryDate BETWEEN ? AND ?", ('%' + searchWord + '%',startDate,endDate))
                return salesData
            elif searchType == "batch":
                salesData = cur.execute(
                    "SELECT created_AT,billNumber,category,drugName,batch,sellingPrice,qtn,total,discount,"
                    "discountedAmount,payMethod,paidBy,workedOnBy FROM sales WHERE batch=?"
                    " AND entryDate BETWEEN ? AND ?", (searchWord,startDate,endDate))
                return salesData
        except Exception as e:
            print(e)

    #search fastSales
    @staticmethod
    def searchFastSales(searchWord, searchType,startDate,endDate):
        try:
            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            if searchType == "category":
                searchFastData = cur.execute(
                    "SELECT drugID,drugName,category,SUM(qtn) ,COUNT(drugID),SUM(total),SUM(discount),SUM(discountedAmount) FROM  sales "
                    "WHERE category=? AND entryDate BETWEEN ? AND ? GROUP BY drugID ORDER BY COUNT(drugID) DESC ", (searchWord,startDate,endDate))
                return searchFastData
            elif searchType == "drugName":
                searchFastData = cur.execute(
                    "SELECT drugID,drugName,category,SUM(qtn),COUNT(drugID),SUM(total),SUM(discount),SUM(discountedAmount) FROM  sales "
                    "WHERE drugName=? AND entryDate BETWEEN ? AND ? GROUP BY drugID ORDER BY COUNT(drugID) DESC ", (searchWord,startDate,endDate))
                return searchFastData
        except Exception as e:
            print(e)
    #load fast sales
    @staticmethod
    def loadFastSales():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            salesData = cur.execute("SELECT drugID,drugName,category,SUM(qtn),COUNT(drugID),SUM(total),SUM(discount),SUM(discountedAmount) FROM  sales "
                    "GROUP BY drugID ORDER BY COUNT(drugID) DESC LIMIT 100 ")
            return salesData
        except Exception as e:
            print(e)

    # loadUsersales
    @staticmethod
    def loadUserSales():
        try:
            userN = PLC.pharmacyLoginController.getUsername()
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            salesData = cur.execute(
                "SELECT created_AT,billNumber,category,drugName,batch,sellingPrice,qtn,total,discount,"
                "discountedAmount,payMethod,paidBy,workedOnBy FROM sales WHERE workedOnBy=?",(userN,))
            return salesData
        except Exception as e:
            print(e)

    # searchSales
    @staticmethod
    def searchUserSales(searchWord, searchType, startDate, endDate):
        try:
            userN = PLC.pharmacyLoginController.getUsername()
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            if searchType == "category":
                salesData = cur.execute(
                    "SELECT created_AT,billNumber,category,drugName,batch,sellingPrice,qtn,total,discount,"
                    "discountedAmount,payMethod,paidBy,workedOnBy FROM  sales WHERE workedOnBy=? AND category=?"
                    " AND entryDate BETWEEN ? AND ? ", (userN,searchWord, startDate, endDate))

                return salesData
            elif searchType == "drugName":
                    salesData = cur.execute(
                        "SELECT created_AT,billNumber,category,drugName,batch,sellingPrice,qtn,total,discount,"
                        "discountedAmount,payMethod,paidBy,workedOnBy FROM sales WHERE workedOnBy=? AND drugName LIKE ?"
                        " AND entryDate BETWEEN ? AND ?", (userN,'%' + searchWord + '%', startDate, endDate))
                    return salesData
            elif searchType == "batch":
                salesData = cur.execute(
                    "SELECT created_AT,billNumber,category,drugName,batch,sellingPrice,qtn,total,discount,"
                    "discountedAmount,payMethod,paidBy,workedOnBy FROM sales WHERE workedOnBy=? AND batch=?"
                    " AND entryDate BETWEEN ? AND ?", (userN,searchWord, startDate, endDate))
                return salesData
        except Exception as e:
            print(e)

    @staticmethod
    def loadSalesCredit():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            salesDatax = cur.execute(
                "SELECT billNumber,payDate,clientName,clientPhone,bill,cashDown,balance,workedOnBy,created_AT FROM credit"
                " WHERE Status = ? ORDER BY id DESC",(1,))
            return salesDatax
        except Exception as e:
            print(e)

    @staticmethod
    def loadSalesCreditCleared():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            salesDatay = cur.execute(
                "SELECT billNumber,clientName,clientPhone,recentPay,bill,cashDown,balance,workedOnBy,Cleared_AT FROM creditCleared "
                "ORDER BY id DESC")

            return salesDatay
        except Exception as e:
            print(e)

    @staticmethod
    def searchSalesCredit(searchWord, searchType, startDate, endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            if searchType == "billNumber":
                salesData = cur.execute(
                    "SELECT billNumber,payDate,clientName,clientPhone,bill,cashDown,balance,workedOnBy,created_AT "
                    "FROM  credit WHERE Status = ? AND billNumber=? AND created_AT "
                    " BETWEEN ? AND ? ORDER BY id DESC", (1,searchWord, startDate, endDate))

                return salesData
            elif searchType == "clientName":
                salesData = cur.execute(
                    "SELECT billNumber,payDate,clientName,clientPhone,bill,cashDown,balance,workedOnBy,created_AT "
                    "FROM  credit WHERE Status = ? AND clientName=? AND created_AT "
                    " BETWEEN ? AND ? ORDER BY id DESC", (1, searchWord, startDate, endDate))

                return salesData
            elif searchType == "user":
                salesData = cur.execute(
                    "SELECT billNumber,payDate,clientName,clientPhone,bill,cashDown,balance,workedOnBy,created_AT "
                    "FROM  credit WHERE Status = ? AND workedOnBy=? AND created_AT "
                    " BETWEEN ? AND ? ORDER BY id DESC", (1, searchWord, startDate, endDate))
                return salesData

        except Exception as e:
            print(e)

    @staticmethod
    def searchSalesCreditClear(searchWord, searchType, startDate, endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            if searchType == "billNumber":
                salesData = cur.execute(
                    "SELECT billNumber,clientName,clientPhone,recentPay,bill,cashDown,balance,workedOnBy,Cleared_AT FROM creditCleared "
                    "WHERE billNumber=? AND Cleared_AT BETWEEN ? AND ? ORDER BY id DESC", (searchWord, startDate, endDate))

                return salesData
            elif searchType == "clientName":
                salesData = cur.execute(
                    "SELECT billNumber,clientName,clientPhone,recentPay,bill,cashDown,balance,workedOnBy,Cleared_AT FROM creditCleared "
                    "WHERE clientName=? AND Cleared_AT BETWEEN ? AND ? ORDER BY id DESC", (searchWord, startDate, endDate))

                return salesData
            elif searchType == "user":
                salesData = cur.execute(
                    "SELECT billNumber,clientName,clientPhone,recentPay,bill,cashDown,balance,workedOnBy,Cleared_AT FROM creditCleared "
                    " WHERE workedOnBy=? AND Cleared_AT BETWEEN ? AND ? ORDER BY id DESC", ( searchWord, startDate, endDate))
                return salesData
        except Exception as e:
            print(e)






