import sqlite3
import time
import datetime
class pharmacyLoginController():

    #login
    @staticmethod
    def login(username,password):
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()
        rQtn = []
        global userID,accountType,uname2,fname,password1
        userID = None
        accountType = None
        uname2 = None
        fname = None
        password1 = None
        try:
            logData = cur.execute("SELECT id,accountType,username,fname,password FROM users WHERE username=? AND password=?",
                                 (username,password))
            getlogData = logData.fetchall()

            if len(getlogData) == 1:
                for row in getlogData:
                    userID = int(row[0])
                    accountType = row[1]
                    uname2 = row[2]
                    fname = row[3]
                    password1 = row[4]
                rQtn = 1
            else:
                rQtn = 0

        except Exception as e:
            print(e)
        return rQtn

    # regUser
    @staticmethod
    def regUser(udname, pass1, name):
        conn = sqlite3.connect('conn/pharmacy.db')
        cur = conn.cursor()

        unix = time.time()
        creatDate = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        try:
            cur.execute("INSERT INTO users(accountType,username,password,fname,created_AT) VALUES(?,?,?,?,?)",
                        ("ADMIN", udname, pass1, name, creatDate))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()

    #return user id
    @staticmethod
    def getUserID():
        return userID

    # return accountType
    @staticmethod
    def getAccountType():
        return accountType

    # return username
    @staticmethod
    def getUsername():
        return uname2

    # return name
    @staticmethod
    def getName():
        return fname

    @staticmethod
    def getPass():
        return password1






