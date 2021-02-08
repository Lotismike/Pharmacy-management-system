import sqlite3

class addUserController():

    @staticmethod
    def checkUsername(uname):
        myreturn =0
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            getUname = cur.execute("SELECT username,id FROM users WHERE username=?",(uname,))

            if(len(getUname.fetchall())>0):
                myreturn = 1
            else:
                myreturn = 0

        except Exception as e:
            print(e)
        finally:
            conn.close()
        return myreturn
    #checkOtherUsername 2 used when updatig
    @staticmethod
    def checkOtherUsername(uname,id):
        myreturn = 0
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            getUname = cur.execute("SELECT username,id FROM users WHERE username=? AND id !=?", (uname,id))

            if (len(getUname.fetchall()) > 0):
                myreturn = 1
            else:
                myreturn = 0

        except Exception as e:
            print(e)
        finally:
            conn.close()
        return myreturn
    #addUser
    def storeUser(self, uname, fname, lname, dob, sex, status, natID,homeD,currentD,currentAdd,
                        phone, email, kinName,kinPhone,salary,pass1,joinDate, createDate):

        myreturn2 = 0
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            cur.execute(
                "INSERT into users(username,fname,lname,dob,status,sex,natID,homeDist,currentDist,currentAddress,"
                "phone,email,salary,password,joinDate,kinName,kinPhone,created_AT,accountType)  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (uname, fname, lname, dob, status,sex,natID,homeD,currentD,currentAdd,phone,email,salary,pass1,
                 joinDate, kinName, kinPhone,createDate,"USER"))
            conn.commit()
            myreturn2 = 1
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return myreturn2

    # searchUsers
    @staticmethod
    def searchUsers(searchWord, searchType):
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            if searchType == "username":
                stockData = cur.execute(
                    "SELECT id,username,fname,lname,dob,sex,status,natID,homeDist,currentDist,currentAddress,"
                    "phone,email,salary,joinDate,password,kinName,kinPhone,created_AT  FROM users WHERE username=?", (searchWord,))
                return stockData

        except Exception as e:
            print(e)

    # loadUsers
    @staticmethod
    def loadUsers():
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            stockData = cur.execute(
                "SELECT id,username,fname,lname,dob,sex,status,natID,homeDist,currentDist,currentAddress,"
                "phone,email,salary,joinDate,password,kinName,kinPhone,created_AT  FROM users ")
            return stockData
        except Exception as e:
            print(e)

        # addUser

    def updateUser(self, uname, fname, lname, sex, status, natID, homeD, currentD, currentAdd,
                  phone, email, kinName, kinPhone, salary, pass1,myID):

        myreturn2 = 0
        try:
            conn = sqlite3.connect('conn/pharmacy.db')
            cur = conn.cursor()
            cur.execute(
                "UPDATE users SET username=?,fname=?,lname=?,status=?,sex=?,natID=?,homeDist=?,currentDist=?,currentAddress=?,"
                "phone=?,email=?,salary=?,password=?,kinName=?,kinPhone=? WHERE id=?",
                (uname, fname, lname,status, sex, natID, homeD, currentD, currentAdd, phone, email, salary, pass1,kinName, kinPhone,myID))
            conn.commit()
            myreturn2 = 1
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return myreturn2

