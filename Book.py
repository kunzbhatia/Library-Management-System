import mysql.connector
import Tables
#----------------------------------------------------------------------------------------
#Admin Operation on Books
def displayBook():
    print()
    print("Book Records: \n")
    mycursor.execute("""SELECT BookRecord.BookID,BookRecord.BookName,BookRecord.Author,BookRecord.Publisher,UserRecord.UserName,UserRecord.UserID
                        FROM BookRecord
                        LEFT JOIN UserRecord ON BookRecord.BookID=UserRecord.BookID""")
    records=mycursor.fetchall()
    row_no=0
    for rows in records :
        row_no+=1
        print("******************************","Row no.",row_no,"******************************")
        print("\t             BookID: ", rows[0])
        print("\t           BookName: ", rows[1])
        print("\t             Author: ", rows[2])
        print("\t          Publisher: ", rows[3])
        print("\t          Issued By: ", rows[4])
        print("\t         His UserID: ", rows[5])
        print()
    x=input("Press Enter to return to the User Menu")
    return
#----------------------------------------------------------------------------------------        
def insertBook():
    while True :
        data=()
        print()
        BookID=input(" Enter BookID: ")
        BookName=input(" Enter Book Name: ")
        Author=input(" Enter Author Name: ")
        Publisher=input(" Enter Publisher Name: ")
        data=(BookID, BookName, Author, Publisher)
        query="INSERT INTO BookRecord VALUES (%s, %s, %s, %s)"
        mycursor.execute(query,data)
        mydb.commit()
        print()
        ch=input("Do you wish to do add more Books?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return

#----------------------------------------------------------------------------------------        
def deleteBook():
    while True:
        print()
        BookID=input(" Enter BookID whose details to be deleted : ")
        mycursor.execute("DELETE from BookRecord where BookID = {0} ".format("\'"+BookID+"\'"))
        mydb.commit()
        ch=input("Do you wish to delete more Books?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return

#----------------------------------------------------------------------------------------    
def searchBook():
    while True:
        print()
        Search=input("Enter BookID to be Searched:")
        mycursor.execute("SELECT BookRecord.BookID,BookRecord.BookName,BookRecord.Author,BookRecord.Publisher,UserRecord.UserName,UserRecord.UserID\
                        FROM BookRecord\
                        LEFT JOIN UserRecord ON BookRecord.BookID=UserRecord.BookID\
                        WHERE BookRecord.BookID={0}".format("\'"+Search+"\'"))  
        records=mycursor.fetchall()
        row_no=0
        if records:
            for rows in records :
                row_no+=1
                print("******************************","Searched Book Record","******************************")
                print("\t             BookID: ", rows[0])
                print("\t           BookName: ", rows[1])
                print("\t             Author: ", rows[2])
                print("\t          Publisher: ", rows[3])
                print("\t          Issued By: ", rows[4])
                print("\t         His UserID: ", rows[5])
                print()
        else:
            print("Search Unsuccesfull")
            
        ch=input("Do you wish to Search more Books?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return

#----------------------------------------------------------------------------------------
def updateBook():
    while True:
        print()
        data=()
        BookID=input(" Enter Book ID for whose details need to be updated : ")
        BookName=input(" Enter updated Book Name : ")
        Author=input(" Enter updated Author Name : ")
        Publisher=input(" Enter the updated Publisher Name : ")
        query="UPDATE BookRecord SET Bookname = %s, Author = %s, Publisher = %s WHERE BookID = %s" 
        data=(BookName,Author,Publisher,BookID)
        mycursor.execute(query,data)
        mydb.commit()
        print("Updated succesfully")
        ch=input("Do you wish to do Update more Books?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#User Operation on Books
def BookList():
    print()
    print("Book Records: \n")
    mycursor.execute("""SELECT * from BookRecord""")
    records=mycursor.fetchall()
    row_no=0
    for rows in records :
        row_no+=1
        print("******************************","Row no.",row_no,"******************************")
        print("\t             BookID: ", rows[0])
        print("\t           BookName: ", rows[1])
        print("\t             Author: ", rows[2])
        print("\t          Publisher: ", rows[3])
        print()
    x=input("Press any key to return to the User Menu")
    return
    
def IssueBook():
    check=input("Enter your UserID:")
    mycursor.execute("Select BookID from UserRecord where UserID={0}".format("\'"+check+"\'"))
    checking=mycursor.fetchone()
    if checking==(None,):
        print()
        print("Available Books: \n")
        mycursor.execute("""SELECT BookRecord.BookID,BookRecord.BookName, BookRecord.Author,BookRecord.Publisher,UserRecord.UserName,UserRecord.UserID
                         FROM BookRecord
                         LEFT JOIN UserRecord ON BookRecord.BookID=UserRecord.BookID""")
        records=mycursor.fetchall()
        row_no=0
        for rows in records:
            if rows[5]==None:
                
                row_no+=1
                print("******************************","Row no.",row_no,"******************************")
                print("\t             BookID: ", rows[0])
                print("\t           BookName: ", rows[1])
                print("\t             Author: ", rows[2])
                print("\t          Publisher: ", rows[3])
                print()
        if row_no==0:
            print("Sorry, there are no available books in the Library")
            print("Please Wait for some time till someone return the book you want")
            x=input("Press any key to return to the User Menu")
            return
        data=()                
        UserID=input("Enter yor UserID:")               
        Issue=input("Enter the BookID available to be issued:")
        query="UPDATE UserRecord SET BookID=%s WHERE UserID = %s" 
        data=(Issue,UserID)
        mycursor.execute(query,data)
        mydb.commit()
        print("Book Successfully Issued")
        x=input("Press any key to return to the User Menu")
        return
    else:
        print("Book Already Issued, Kindly Return That first")
        x=input("Press any key to return to the User Menu")
        return    
#----------------------------------------------------------------------------------------
def ShowIssuedBook():
    print()
    UserID=input("Enter yor UserID:")
    mycursor.execute("SELECT UserID, UserName, UserRecord.BookID, BookName\
                    FROM Library.UserRecord INNER JOIN Library.BookRecord\
                    ON BookRecord.BookID=UserRecord.BookID\
                    WHERE UserID={0}".format("\'"+UserID+"\'"))
    records=mycursor.fetchall()
    row_no=0
    if records:
        for rows in records :
            row_no+=1
            print("******************************","Issued Book","******************************")
            print("\t             UserID: ", rows[0])
            print("\t           UserName: ", rows[1])
            print("\t             BookID: ", rows[2])
            print("\t           BookName: ", rows[3])
            print()
        x=input("Press any key to return to the User Menu")
        return
    else:
        print("No Book Issued")
        x=input("Press Enter to return to the User Menu")
        return  
#----------------------------------------------------------------------------------------
def returnBook():
    print()
    data=()
    UserID=input("Enter yor UserID:")
    Rec=input("Enter BookID to be return:")
    query="""UPDATE UserRecord SET BookID = %s WHERE UserID= %s and BookID=%s"""            
    data=(None,UserID,Rec)
    mycursor.execute(query,data)
    mydb.commit()
    print("Return Successfull")
    x=input("Press Enter to return to the User Menu")
    return   
#----------------------------------------------------------------------------------------

mydb=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="Library")
mycursor=mydb.cursor()
