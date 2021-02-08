import os
import sqlite3
import categoryData as CD
class categoryController():
    def __init__(self):
        self.intials()

    def intials(self):
        global conn

    # get names
    @staticmethod
    def getCatData():
        try:
            listCatData = []
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            getCatData = cur.execute("SELECT id,catName From category")
            catData = getCatData.fetchall()

            for row in catData:
                dbCatData= CD.categoryData(row[0], row[1]) #id,catName
                listCatData.append(dbCatData)
            return listCatData
        except Exception as e:
            print(e)
        finally:
            conn.close()

    # get data
    @staticmethod
    def getItemQtn(id):
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        rQtn = 0
        try:
            getQtn = cur.execute("SELECT (qty-temp),id FROM stock WHERE id=?", (id,))
            getQtnData = getQtn.fetchall()
            for row2 in getQtnData:
                rQtn = int(row2[0])
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return rQtn

    #update temp column
    @staticmethod
    def addUpdateTemp(id,qtn):
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        try:
            cur.execute("UPDATE stock SET temp=(temp+?) WHERE id=?", (qtn,id))
            conn.commit()

        except Exception as e:
            print(e)
        finally:
            conn.close()
    #sub trmp
    @staticmethod
    def subUpdateTemp(id, qtn):
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        try:
            cur.execute("UPDATE stock SET temp=(temp-?) WHERE id=?", (qtn, id))
            conn.commit()

        except Exception as e:
            print(e)
        finally:
            conn.close()

    # update temp column
    @staticmethod
    def updateTemp(id, qtn):
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        try:
            cur.execute("UPDATE stock SET temp=? WHERE id=?", (qtn, id))
            conn.commit()

        except Exception as e:
            print(e)
        finally:
            conn.close()

    # reset temp columns
    @staticmethod
    def restTemp():
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        try:
            cur.execute("UPDATE stock SET temp=?", (0,))
            conn.commit()

        except Exception as e:
            print(e)
        finally:
            conn.close()
