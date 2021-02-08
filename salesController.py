import sqlite3
class salesController:

    # searchDrug
    @staticmethod
    def searchDrug(searchWord, searchType):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            if searchType == "drugname":
                stockData = cur.execute(
                    "SELECT id,drugName,batchNumber,category,sellingPrice,supplier FROM stock WHERE drugName LIKE ?", ('%' + searchWord + '%',))

                return stockData
            elif searchType == "category":
                stockData = cur.execute(
                    "SELECT id,drugName,batchNumber,category,sellingPrice,supplier  FROM stock WHERE category=?", (searchWord,))
                return stockData
            elif searchType == "batch":
                stockData = cur.execute(
                    "SELECT entryDate,id,drugName,batchNumber,category,qty,buyingPrice,sellingPrice,supplier,productDate,expiryDate,"
                    "created_BY,created_AT  FROM stock WHERE batchNumber LIKE ?", ('%' + searchWord + '%',))
                return stockData
        except Exception as e:
            print(e)

    #check for cat
    @staticmethod
    def checkCat(catName):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            catTotal = cur.execute("SELECT SUM(qty) FROM stock WHERE category=?", (catName,))
            return catTotal
        except Exception as e:
            print(e)


    @staticmethod
    def addSales(billNumber,dID,drugName,batchNo,cat,sellingPrice,qty,total,discount,
                 disAmount,payMethod,paidBy,username,createdAT,entryDate):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            #uploading to the sales
            cur.execute("INSERT INTO sales(billNumber,drugID,drugName,batch,category,sellingPrice,qtn,total,discount,discountedAmount,"
                        "payMethod,paidBy,workedOnBy,created_AT,entryDate) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(billNumber,dID,drugName,batchNo,cat,
                        sellingPrice,qty,total,discount,disAmount,payMethod,paidBy,username,createdAT,entryDate))
            conn.commit()

            # updating to the stock
            cur.execute("UPDATE stock set qty =qty-? WHERE id=?",(qty,dID))
            conn.commit()

            #updating temp in stock
            cur.execute("UPDATE stock set temp=? WHERE id=?", (0, dID))
            conn.commit()

        except Exception as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def addCredit(billNumber,paidBy,clientPhone,disAmount,cashDown,payDate,username,createdAT,payMethod):

        bal = float(disAmount)-float(cashDown)
        bal = round(bal,2)
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            # Insert into credit
            if payMethod == "Credit":
                cur.execute(
                    "INSERT INTO credit(billNumber,clientName,clientPhone,bill,cashDown,balance,payDate,"
                    "workedOnBy,created_AT) VALUES(?,?,?,?,?,?,?,?,?)",
                    (billNumber, paidBy, clientPhone, disAmount, cashDown,bal,payDate,username,createdAT))
                conn.commit()

                if int(cashDown)>0:
                    # insert into clear credit
                    cur.execute(
                        "INSERT INTO creditCleared(billNumber,clientName,clientPhone,recentPay,bill,cashDown,balance,"
                        "workedOnBy,Cleared_AT) VALUES(?,?,?,?,?,?,?,?,?)",
                        (billNumber, paidBy, clientPhone, cashDown, disAmount, cashDown, bal, username, createdAT))
                    conn.commit()

        except Exception as e:
            print(e)
        finally:
            conn.close()

    # update credit
    @staticmethod
    def clearDebt(pay,billNo,clientName, clientPhone, bill, amount, balance,username, createDate):
        pay = int(pay)
        newBal = int(balance)-pay
        newCashDown = (pay + int(amount))
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            myReturn = None
            #insert into clear credit
            cur.execute(
                "INSERT INTO creditCleared(billNumber,clientName,clientPhone,recentPay,bill,cashDown,balance,"
                "workedOnBy,Cleared_AT) VALUES(?,?,?,?,?,?,?,?,?)",
                (billNo, clientName, clientPhone,pay, bill,newCashDown,newBal,username,createDate))
            conn.commit()
            #updating credit table
            cleared = int(bill) - (pay+int(amount))
            if cleared == 0:
                cur.execute("UPDATE credit SET cashDown=?,balance=?,Status=? WHERE billNumber=?",(newCashDown,0,0,billNo))
                conn.commit()
                myReturn ="cleared"
            else:
                cur.execute("UPDATE credit SET cashDown=?,balance=? WHERE billNumber=?", (newCashDown, newBal,billNo))
                conn.commit()
                myReturn = "clearedPartially"
            return  myReturn
        except Exception as e:
            print(e)
            myReturn = "error"
        finally:
            conn.close()

    # update credit
    @staticmethod
    def checkDrug(drugID):

        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            catTotal = cur.execute("SELECT drugID,drugName FROM sales WHERE drugID=?", (drugID,))
            return catTotal
        except Exception as e:
            print(e)












