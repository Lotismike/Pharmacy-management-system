import sqlite3

import pharmacyLoginController as PLC
class accountController():
    # login
    @staticmethod
    def userData():
        userName = PLC.pharmacyLoginController.getUsername()
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        try:
            logData = cur.execute("SELECT username, fname, lname, dob,sex,status,kinName,sex, natID, homeDist, currentDist,"
                                  " currentAddress,phone,email,kinPhone,password FROM users WHERE username=?",(userName,))
        except Exception as e:
            print(e)
        return logData

    @staticmethod
    def updateUser(status,phone,kinName,cDist,cAddr,email,kinPhone):
        userName = PLC.pharmacyLoginController.getUsername()
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        myReturn = 0
        try:
            cur.execute(
                "UPDATE users SET status=?,phone=?,kinName=?,currentDist=?,"
                " currentAddress=?,email=?,kinPhone=? WHERE username=?", (status,phone,kinName,cDist,
                cAddr,email,kinPhone,userName))
            conn.commit()
            myReturn = 1
        except Exception as e:
            print(e)
        return myReturn

    #checkUser
    @staticmethod
    def checkUserPass2(cPass):
        userName = PLC.pharmacyLoginController.getUsername()
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        cPData = 0
        try:
            uData = cur.execute("SELECT id,username FROM users WHERE username=? AND password=? AND accountType=?",
                                 (userName,cPass,"USER"))
            cPData = len(uData.fetchall())
        except Exception as e:
            print(e)
        finally:
            conn.commit()
        return cPData

    #update password
    @staticmethod
    def upadateUserPass(pass1):
        userName = PLC.pharmacyLoginController.getUsername()
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        uPass = 0
        try:
            cur.execute("UPDATE users set password=? WHERE username=?",
                                (pass1,userName))
            conn.commit()
            uPass = 1
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return uPass



