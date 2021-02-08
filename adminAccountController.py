import time
import datetime
import sqlite3
class adminAccountController():

    #checkUsername(uzaname,myID)
    @staticmethod
    def checkUsername(uzaname,myID):

        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            myA = cur.execute("SELECT username FROM users WHERE id !=? AND username=?",(myID,uzaname))
            return myA
        except Exception as e:
            print(e)

    #changeUser()
    @staticmethod
    def changeUser(name,uzaname,myID):

        unix = time.time()
        creatDate = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        myRet3 = None
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            cur.execute(
                "UPDATE users SET fname=?,username=?,created_At=? WHERE id=?",(name,uzaname,creatDate,myID))
            conn.commit()
            myRet3 = "updated"
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return myRet3
    #changePass()
    @staticmethod
    def changePass(newPass, myID):
        unix = time.time()
        creatDate = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        myRet4 = None
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()

            cur.execute("UPDATE users SET password=?,created_At=? WHERE id=?", (newPass, creatDate, myID))
            conn.commit()
            myRet4 = "updated"
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return myRet4

    #upDateCred
    @staticmethod
    def checkPass(oldPass,id):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            newCred = cur.execute("SELECT username,password FROM users WHERE password=? AND id=?", (oldPass,id))
            return newCred
        except Exception as e:
            print(e)
























