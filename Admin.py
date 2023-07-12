import mysql.connector
import Tables
#---------------------------------------------------------------------------------------------------------                 
def displayAdmin():
    print()
    print("Admin Records: \n")
    mycursor.execute("SELECT * FROM AdminRecord")
    records=mycursor.fetchall()
    row_no=0
    for rows in records :
        row_no+=1
        print("******************************","Row no.",row_no,"******************************")
        print("\t             AdminID: ", rows[0])
        print("\t            Password: ", rows[1])
        print()
    x=input("Press Enter to continue")
    return
#---------------------------------------------------------------------------------------------------------         
def insertAdmin():
    while True :
        data=()
        print()
        AdminID=input("Enter AdminID: ")
        Password=input(" Enter Password to be set: ")
        data=(AdminID,Password)
        query="INSERT INTO AdminRecord VALUES (%s, %s)"
        mycursor.execute(query,data)
        mydb.commit()
        print()
        ch=input("Do you wish to do add more Administrators?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#---------------------------------------------------------------------------------------------------------         
def deleteAdmin():
    while True:
        print()
        AdminID=input(" Enter AdminID whose details to be deleted : ")  
        mycursor.execute("DELETE from AdminRecord where AdminID={0}".format("\'"+AdminID+"\'"))
        mydb.commit()
        ch=input("Do you wish to delete more Administrators?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#---------------------------------------------------------------------------------------------------------     
def searchAdmin():
    while True:
        print()
        Search=input(" Enter AdminID to be Searched: ")  
        mycursor.execute("SELECT * FROM AdminRecord where AdminID={0}".format("\'"+Search+"\'"))
        records=mycursor.fetchall()
        row_no=0
        if records:
            for rows in records :
                row_no+=1
                print("******************************","Searched Admin Record","******************************")
                print("\t             AdminID: ", rows[0])
                print("\t            Password: ", rows[1])
                print()
        else:
            print("Search Unsuccesfull")
            
        ch=input("Do you wish to Search more Administrators?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#--------------------------------------------------------------------------------------------------------- 
def updateAdmin():
    while True:
        print()
        data=()
        AdminID=input(" Enter Admin ID for whose details need to be updated : ")
        Password=input(" Enter new Password : ")
        query="UPDATE AdminRecord SET Password = %s WHERE AdminID=%s"
        data=(Password,AdminID)
        mycursor.execute(query,data)
        mydb.commit()
        ch=input("Do you wish to Search more Administrators?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#--------------------------------------------------------------------------------------------------------- 
mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="Library")
mycursor=mydb.cursor()
     
