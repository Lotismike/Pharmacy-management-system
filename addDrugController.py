import sqlite3
import time
from datetime import datetime
import pharmacyLoginController as PLC
class addDrugController():

    def storeDrug(self,drugName,qtn,batchNo,cat,supplier,prdDate,expDate,entryDate,buyPrice,sellPrice,creatDate,userName):
        myreturn = 0
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            checkName = cur.execute("SELECT id,drugName FROM stock WHERE drugName=? AND category=?",(drugName,cat))
            if len(checkName.fetchall())>0:
                #check if the found drug qty is zero
                checkDrugQty = cur.execute("SELECT id,drugName FROM stock WHERE drugName=? AND category=? AND qty=?",(drugName, cat, 0))
                if len(checkDrugQty.fetchall())==1:
                    cur.execute(
                        "UPDATE stock SET drugName=?,qty=?,batchNumber=?,category=?,supplier=?,sellingPrice=?,buyingPrice=?,reorderLevel=?,"
                        "expiryDate=?,entryDate=?,created_BY=?,created_AT=? WHERE drugName=? AND category=?",
                        (drugName, qtn, batchNo, cat, supplier,sellPrice, buyPrice, prdDate, expDate, entryDate, userName, creatDate,drugName,cat))
                    conn.commit()

                    #insert into stock histor
                    cur.execute(
                        "INSERT into stockhistory(entryDate,action,actionBy,drugName,category,cost,qty,created_At)  VALUES(?,?,?,?,?,?,?,?)",
                        (entryDate, 'UPDATED', userName, drugName, cat, buyPrice, qtn,creatDate))
                    conn.commit()

                    myreturn = "updated"

                else:
                    myreturn = "failed"

            else:
                cur.execute("INSERT into stock(drugName,qty,batchNumber,category,supplier,sellingPrice,buyingPrice,reorderLevel,"
                            "expiryDate,entryDate,created_BY,created_AT)  VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(drugName,qtn,batchNo,cat,supplier,
                            sellPrice,buyPrice,prdDate,expDate,entryDate,userName,creatDate))
                conn.commit()

                # insert into stock histor
                cur.execute(
                    "INSERT into stockhistory(entryDate,action,actionBy,drugName,category,cost,qty,created_At)  VALUES(?,?,?,?,?,?,?,?)",
                    (entryDate, 'INSERTED', userName, drugName, cat, buyPrice, qtn, creatDate))
                conn.commit()
                myreturn = "inserted"

            #Insert into stock entry table
            cur.execute("INSERT into user_stock_entry(drugName,qty,batchNumber,category,supplier,sellingPrice,buyingPrice,reorderLevel,"
                        "expiryDate,entryDate,created_BY,created_AT)  VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (drugName, qtn, batchNo, cat, supplier,sellPrice, buyPrice, prdDate, expDate, entryDate, userName, creatDate))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return myreturn

    #Check drug
    @staticmethod
    def checkDrug(drugName,cat):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            checkDrug = cur.execute("SELECT id,drugName FROM stock WHERE drugName=? AND category=? AND qty=?",
                                   (drugName, cat, 0))
            return checkDrug
        except Exception as e:
            print(e)
        finally:
            conn.close()

    #loadstock
    @staticmethod
    def loadStock():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            stockData = cur.execute("SELECT entryDate,id,drugName,batchNumber,category,qty,buyingPrice,(qty*buyingPrice),"
                                    "sellingPrice,(qty*sellingPrice),supplier,reorderLevel,expiryDate,created_BY,created_AT  FROM stock")
            return stockData
        except Exception as e:
            print(e)


    #searchDrug
    @staticmethod
    def searchDrug(searchWord,searchType):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            if searchType == "drugName":
                stockData = cur.execute(
                    "SELECT entryDate,id,drugName,batchNumber,category,qty,buyingPrice,(qty * buyingPrice), sellingPrice,(qty*sellingPrice),supplier,reorderLevel,expiryDate,"
                    "created_BY,created_AT  FROM stock WHERE drugName LIKE ?",('%'+searchWord+'%',))
                return stockData
            elif searchType == "category":
                stockData = cur.execute(
                    "SELECT entryDate,id,drugName,batchNumber,category,qty,buyingPrice,(qty * buyingPrice), sellingPrice,(qty*sellingPrice),supplier,reorderLevel,expiryDate,"
                    "created_BY,created_AT  FROM stock WHERE category=?",(searchWord,))
                return stockData
            elif searchType == "batch":
                stockData = cur.execute(
                    "SELECT entryDate,id,drugName,batchNumber,category,qty,buyingPrice,(qty * buyingPrice), sellingPrice,(qty*sellingPrice),supplier,reorderLevel,expiryDate,"
                    "created_BY,created_AT  FROM stock WHERE batchNumber LIKE ?",('%'+searchWord+'%',))
                return stockData
        except Exception as e:
            print(e)

    #searchOutStock
    @staticmethod
    def searchOutStock(searchWord, searchType):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            if searchType == "drugName":
                stockData = cur.execute(
                    "SELECT entryDate,id,drugName,batchNumber,category,qty,buyingPrice,sellingPrice,supplier,reorderLevel,expiryDate,"
                    "created_BY,created_AT  FROM stock WHERE drugName LIKE ? AND qty<reorderLevel", ('%' + searchWord + '%',))

                return stockData
            elif searchType == "category":
                stockData = cur.execute(
                    "SELECT entryDate,id,drugName,batchNumber,category,qty,buyingPrice,sellingPrice,supplier,reorderLevel,expiryDate,"
                    "created_BY,created_AT  FROM stock WHERE category=?  AND qty<reorderLevel", (searchWord,))
                return stockData
            elif searchType == "batch":
                stockData = cur.execute(
                    "SELECT entryDate,id,drugName,batchNumber,category,qty,buyingPrice,sellingPrice,supplier,reorderLevel,expiryDate,"
                    "created_BY,created_AT  FROM stock WHERE batchNumber LIKE ?  AND qty<reorderLevel", ('%' + searchWord + '%'))

                return stockData
        except Exception as e:
            print(e)

    #loadOutStock
    @staticmethod
    def loadOutStock():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            stockData = cur.execute(
                "SELECT entryDate,id,drugName,batchNumber,category,qty,buyingPrice,sellingPrice,supplier,reorderLevel,expiryDate,"
                "created_BY,created_AT  FROM stock WHERE  qty<reorderLevel")
            return stockData
        except Exception as e:
            print(e)

    # searchExpire
    @staticmethod
    def searchExpire(searchWord, searchType):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            if searchType == "drugName":

                stockData = cur.execute("SELECT entryDate, id, drugName,"
                                        "CASE "
                                        "WHEN (strftime('%s', expiryDate) - strftime('%s', date('now')))>0 THEN cast(julianday(expiryDate) - julianday('now')As Integer)"
                                        "ELSE (0)"
                                        "END AS days,"
                                        "reorderLevel,expiryDate,batchNumber,category,qty,buyingPrice,sellingPrice,supplier FROM stock "
                                        "WHERE drugName LIKE ? AND days <186 ORDER BY days ASC",
                                        ('%' + searchWord + '%',))
                return stockData
            elif searchType == "category":
                stockData = cur.execute("SELECT entryDate, id, drugName,"
                                        "CASE "
                                        "WHEN (strftime('%s', expiryDate) - strftime('%s', date('now')))>0 THEN cast(julianday(expiryDate) - julianday('now')As Integer)"
                                        "ELSE (0)"
                                        "END AS days,"
                                        "reorderLevel,expiryDate,batchNumber,category,qty,buyingPrice,sellingPrice,supplier FROM stock "
                                        "WHERE category=? AND days <186 ORDER BY days ASC",(searchWord,))

                return stockData
            elif searchType == "batch":
                stockData = cur.execute("SELECT entryDate, id, drugName,"
                                        "CASE "
                                        "WHEN (strftime('%s', expiryDate) - strftime('%s', date('now')))>0 THEN cast(julianday(expiryDate) - julianday('now')As Integer)"
                                        "ELSE (0)"
                                        "END AS days,"
                                        "reorderLevel,expiryDate,batchNumber,category,qty,buyingPrice,sellingPrice,supplier FROM stock "
                                        "WHERE batchNumber LIKE ? AND days <186 ORDER BY days ASC", ('%' + searchWord + '%',))

                return stockData
        except Exception as e:
            print(e)

    # loadOutStock
    @staticmethod
    def loadExpire():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            stockData = cur.execute("SELECT entryDate, id, drugName,"
                                    "CASE "
                                    "WHEN (strftime('%s', expiryDate) - strftime('%s', date('now')))>0 THEN cast(julianday(expiryDate) - julianday('now')As Integer)"
                                    "ELSE (0)"
                                    "END AS days,"
                                    "reorderLevel,expiryDate,batchNumber,category,qty,buyingPrice,sellingPrice,supplier FROM stock "
                                    "WHERE days <186 ORDER BY days ASC")

            return stockData
        except Exception as e:
            print(e)

    ################ user stock entry##############

    @staticmethod
    def loadUserEntryStock():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            salesData = cur.execute(
                "SELECT entryDate,created_BY,id,drugName,batchNumber,category,qty,buyingPrice,sellingPrice,supplier,reorderLevel,expiryDate,"
                        "created_AT  FROM user_stock_entry WHERE created_BY !=?",("Admin",))
            return salesData
        except Exception as e:
            print(e)

    # searchSales
    @staticmethod
    def searchUserEntryStock(searchWord, searchType, startDate, endDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            startDate = datetime.strptime(str(startDate), "%d/%m/%Y").strftime('%Y-%m-%d')
            endDate = datetime.strptime(str(endDate), "%d/%m/%Y").strftime('%Y-%m-%d')

            if searchType == "username":
                salesData = cur.execute(
                    "SELECT entryDate,created_BY,id,drugName,batchNumber,category,qty,buyingPrice,sellingPrice,supplier,reorderLevel,expiryDate,"
                        "created_AT  FROM  user_stock_entry WHERE created_BY =? AND entryDate"
                    " BETWEEN ? AND ?", (searchWord, startDate, endDate))

                return salesData
            elif searchType == "category":
                salesData = cur.execute(
                    "SELECT entryDate,created_BY,id,drugName,batchNumber,category,qty,buyingPrice,sellingPrice,supplier,reorderLevel,expiryDate,"
                        "created_AT  FROM user_stock_entry WHERE category=? AND created_BY !=? "
                    " AND entryDate BETWEEN ? AND ?", (searchWord,"Admin", startDate, endDate))

                return salesData
            elif searchType == "drugName":
                salesData = cur.execute(
                    "SELECT entryDate,created_BY,id,drugName,batchNumber,category,qty,buyingPrice,sellingPrice,supplier,reorderLevel,expiryDate,"
                        "created_AT  FROM user_stock_entry  WHERE drugName LIKE ? AND created_BY !=?"
                    " AND entryDate BETWEEN ? AND ?", ('%' + searchWord + '%',"Admin", startDate, endDate))
                return salesData

        except Exception as e:
            print(e)

    #updateStock
    @staticmethod
    def updateStock(drugID,ddName,ddBatch,ddQtn,ddBuy,ddSell,ddSup,ddReorder,ddCat):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            cur.execute("UPDATE stock SET drugName=?,batchNumber=?,qty=?,buyingPrice=?,sellingPrice=?,supplier=?,reorderLevel=?"
                        " WHERE id=?",(ddName,ddBatch,ddQtn,ddBuy,ddSell,ddSup,ddReorder,drugID))
            conn.commit()

            # insert into stock histor
            uName = PLC.pharmacyLoginController.getUsername()
            unix = time.time()
            mDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            entryDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
            cur.execute(
                "INSERT into stockhistory(entryDate,action,actionBy,drugName,category,cost,qty,created_At)  VALUES(?,?,?,?,?,?,?,?)",
                (entryDate, 'UPDATED', uName, ddName, ddCat, ddBuy, ddQtn, mDate))
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            conn.close()

    #deleteDrug
    @staticmethod
    def deleteDrug(drugID,ddName,ddQtn,ddBuy,ddCat):

        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM stock WHERE id=?",(drugID,))
            conn.commit()
            # insert into stock histor
            uName = PLC.pharmacyLoginController.getUsername()
            unix = time.time()
            mDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            entryDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
            cur.execute(
                "INSERT into stockhistory(entryDate,action,actionBy,drugName,category,cost,qty,created_At)  VALUES(?,?,?,?,?,?,?,?)",
                (entryDate, 'DELETED', uName, ddName, ddCat, ddBuy, ddQtn, mDate))
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            conn.close()

