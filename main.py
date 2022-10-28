import mysql.connector
do=mysql.connector.connect(host="localhost",user="root",passwd="admin",database="ta_lib")
if do.is_connected():
    print("Successfully Connected to Mysql Database")
    mycursor1 = do.cursor()

Book_Id="" 
Book_name=""
Sub="" 
ISBN=""
Standard=""
Author=""
Price=""

Member_id=""
Member_name=""
Email=""
Contact_no=""
Standard=""
DOJL=""






#--------------------------------------------------------------------------------------------------*/
def add_book():
    print('-'*50)
    print('Welcome to add book module\n')
    Book_Id=input('Enter book id(numeric): ') 
    Book_name=input('Enter book name: ')
    Sub=input('Enter subject: ') 
    ISBN=input('Enter ISBN: ') #International Standard Book Number
    Standard=input('Enter standard: ')
    Author=input('Enter author: ')
    Price=input('Enter price: ')
    sql="insert into Books values ('"+Book_Id+"','"+Book_name+"','"+Sub+"','"+ISBN+"','"+Standard+"','"+Author+"','"+Price+"')"
    #print(sql)
    mycursor1.execute(sql)
    do.commit()
#--------------------------------------------------------------------------------------------------*/
def search_book_id():
    print('-'*50)
    print('Welcome to search book by id module\n')
    Book_Id=input('Enter book id(numeric): ') 
    sql="select * from Books where Book_Id="+Book_Id
    #print(sql) 
    mycursor1.execute(sql)
    data=mycursor1.fetchone()
    count=mycursor1.rowcount
    #print("Total number of rows restricted in resultset : ",count)
    print("\n\tBook id  ",data[0])
    print("\tBook name", data[1])
    print("\tSubject  ", data[2])
    print("\tISBN     ", data[3])
    print("\tStandard ", data[4])
    print("\tAuthor   ",data[5])
    print("\tPrice    ",data[6])
#--------------------------------------------------------------------------------------------------*/
def modify_book():
    print('-'*50)
    print('Welcome to modify book module\n')
    Book_Id=input('Enter book id(numeric): ') 
    Book_name=input('Enter book name: ')
    Sub=input('Enter subject: ') 
    ISBN=input('Enter ISBN: ') #International Standard Book Number
    Standard=input('Enter standard: ')
    Author=input('Enter author: ')
    Price=input('Enter price: ')
    sql="update Books set Book_name='"+Book_name+"', Sub='"+Sub+"', ISBN='"+ISBN+"', Standard='"+Standard+"' , Author='"+Author+"', Price='"+Price+"' where Book_Id="+Book_Id
    #print(sql)
    mycursor1.execute(sql)
    do.commit()
#--------------------------------------------------------------------------------------------------*/
def remove_book():
    print('-'*50)
    print('Welcome to remove book module\n')
    Book_Id=input("Enter book id : ") #1234
    sql="delete from Books where Book_Id="+Book_Id
    #print(sql)
    print('Book removed')
    mycursor1.execute(sql)
    do.commit()
#--------------------------------------------------------------------------------------------------*/
def search_book_name():
    print('-'*50)
    print('Welcome to search book by name module\n') 
    Book_name=input('Enter book name: ')
    sql="select * from Books where Book_name like '%"+Book_name+"%' "
    #print(sql)
    mycursor1.execute(sql)
    mydata=mycursor1.fetchall()
    count=mycursor1.rowcount
    do.commit()

    #print("Total number of rows restricted in resultset : ",count)
    for data in mydata:
        print("\n\tBook id  ",data[0])
        print("\tBook name", data[1])
        print("\tSubject  ", data[2])
        print("\tISBN     ", data[3])
        print("\tStandard ", data[4])
        print("\tAuthor   ",data[5])
        print("\tPrice    ",data[6])
#--------------------------------------------------------------------------------------------------*/
def listall_books():
    print('-'*50)
    print('Welcome to list all books module\n')
    sql="select * from Books"
    #print(sql)
    mycursor1.execute(sql)
    mydata=mycursor1.fetchall()
    count=mycursor1.rowcount
    do.commit()
    if count==0:
        print('No data to display')
    for data in mydata:
        print('-'*20,'\n')
        print("\tBook id  ",data[0])
        print("\tBook name", data[1])
        print("\tSubject  ", data[2])
        print("\tISBN     ", data[3])
        print("\tStandard ", data[4])
        print("\tAuthor   ",data[5])
        print("\tPrice    ",data[6])
    

    
#--------------------------------------------------------------------------------------------------*/  
def add_member():
    print('-'*50)
    print('Welcome to add member module\n')
    Member_Id=input('Enter member id(numeric): ') 
    Member_name=input('Enter member name: ')
    Email=input('Enter email: ') 
    Contact_no=input('Enter contact no.: ') 
    Standard=input('Enter standard: ')
    DOJL=input('Enter date of joining: ')

    sql="insert into Members values ('"+Member_Id+"','"+Member_name+"','"+Email+"','"+Contact_no+"','"+Standard+"','"+DOJL+"')"
    #print(sql)
    print('Member added successfully')
    mycursor1.execute(sql)
    do.commit()
#--------------------------------------------------------------------------------------------------*/  
def search_member_id():    
    print('-'*50)
    print('Welcome to search member by id module\n')
    Member_Id=input('Enter member id(numeric): ') 
    sql="select * from Members where Member_Id="+Member_Id
    #print(sql) 
    mycursor1.execute(sql)
    data=mycursor1.fetchone()
    count=mycursor1.rowcount
    #print("Total number of rows restricted in resultset : ",count)
    print("\tMember id     ",data[0])
    print("\tMember name  ", data[1])
    print("\tEmail      ", data[2])
    print("\tContact no.  ", data[3])
    print("\tStandard    ", data[4])
    print("\tDOJL      ",data[5])
#--------------------------------------------------------------------------------------------------*/  
def modify_member():
    print('-'*50)
    print('Welcome to modify member module\n')
    Member_Id=input('Enter member id(numeric): ') 
    Member_name=input('Enter member name: ')
    Email=input('Enter email: ') 
    Contact_no=input('Enter contact no: ') 
    Standard=input('Enter standard: ')
    DOJL=input('Enter date of joining library: ')
    sql="update Members set Member_name='"+Member_name+"', Email='"+Email+"', Contact_no='"+Contact_no+"', DOJL='"+DOJL+"' where Member_Id="+Member_Id
    #print(sql)
    print('Member modify successful')
    mycursor1.execute(sql)
    do.commit()
#--------------------------------------------------------------------------------------------------*/  
def remove_member():
    print('-'*50)
    print('Welcome to remove member module\n')
    Member_Id=input("Enter member id : ") #1234
    sql="delete from Members where Member_Id="+Member_Id
    #print(sql)
    print('Member removed')
    mycursor1.execute(sql)
    do.commit()
#--------------------------------------------------------------------------------------------------*/  
def search_member_name():
    print('-'*50)
    print('Welcome to search member by name module\n') 
    Member_name=input('Enter member name: ')
    sql="select * from Members where Member_name like '%"+Member_name+"%' "
    #print(sql)
    mycursor1.execute(sql)
    mydata=mycursor1.fetchall()
    count=mycursor1.rowcount
    do.commit()

    #print("Total number of rows restricted in resultset : ",count)
    for data in mydata:
        #tab before member id...
        #dojl print statement mei 'YYYY-MM-DD'
        print("Member id  ", '\t',data[0])
        print("Member name  ", '\t', data[1])
        print("Email  ", '\t', data[2])
        print("Contact no.  ", '\t', data[3])
        print("Standard  ", '\t', data[4])
        print("DOJL  ", '\t', data[5])
#--------------------------------------------------------------------------------------------------*/  
def listall_member():  
    print('-'*50)  
    print('Welcome to list all member module\n')
    sql="select * from Members"
    #print(sql)
    mycursor1.execute(sql)
    mydata=mycursor1.fetchall()
    count=mycursor1.rowcount
    do.commit()
    if count==0:
        print('No data to display')
    for data in mydata:
        print('-'*20)
        print("Member id  ", '\t',data[0])
        print("Member name  ", '\t', data[1])
        print("Email  ", '\t', data[2])
        print("Contact no.  ", '\t', data[3])
        print("Standard  ", '\t', data[4])
        print("DOJL  ", '\t', data[5])
#--------------------------------------------------------------------------------------------------*/  
def manage_books():
    print('-'*50)
    print('Welcome to manage books module\n')
    ch=0
    while ch!=9:

        print('')
        print('Manage books menu')
        print('1. Add a new book ') 
        print('2. Search by book id')
        print('3. Modify a book')
        print('4. Remove a book')
        print('5. Search by book name')
        print('6. List all')
        print('9. Back to main menu')

        ch=int(input('Enter your choice: '))
        if ch==1:
            add_book()
        elif ch==2:
            search_book_id()
        elif ch==3:
            modify_book()
        elif ch==4:
            remove_book()    
        elif ch==5:
            search_book_name()
        elif ch==6:
            listall_books()
        elif ch==9:
            print('Thanks for using manage books module') 
            print('Tanish Kadam')
            print('Abhinav Dash')
            print('Guided by Ms.Pooja Saxena')
            print('Sagar Public School, Rohit Nagar') 
#--------------------------------------------------------------------------------------------------*/            
def manage_member():  
    #manage members ke upar line  
    print('-'*50)
    print('Welcome to manage members module\n')
    ch=0
    while ch!=9:

        print('')
        print('Manage members menu')
        print('1. Add a new member ') 
        print('2. Search by member id')
        print('3. Modify a member')
        print('4. Remove a member')
        print('5. Search by member name')
        print('6. List all')
        print('9. Back to main menu')
        ch=int(input('Enter your choice: '))
        if ch==1:
            add_member()
        elif ch==2:
            search_member_id()
        elif ch==3:
            modify_member()
        elif ch==4:
            remove_member()    
        elif ch==5:
            search_member_name()
        elif ch==6:
            listall_member()
        elif ch==9:
            print('Thanks for using manage books module') 
            print('Tanish Kadam')
            print('Abhinav Dash')
            print('Guided by Ms.Pooja Saxena')
            print('Sagar Public School, Rohit Nagar') 
#--------------------------------------------------------------------------------------------------*/
def book_issue():
    print('-'*50)
    print('Welcome to book issue module\n')
    print('')
    
    Book_Id=input('Enter book id(numeric): ')
    sql="select * from Books where Book_Id="+Book_Id
    #print(sql) 
    mycursor1.execute(sql)
    data=mycursor1.fetchone()
    count=mycursor1.rowcount
    #print("Total number of rows restricted in resultset : ",count)
    print("Book id  ",data[0])
    print("Book name  ", data[1])
    print("Subject  ", data[2])
    print("ISBN  ", data[3])
    print("Standard  ", data[4])
    print("Author  ",data[5])
    print("Price  ",data[6])
    sql1="select count(*) from Issue_return where Book_Id="+Book_Id+" and Return_date is NULL"
    #print(sql1) 
    print('\nCount is' ,count)
    mycursor1.execute(sql1)
    data=mycursor1.fetchone()
    count1=mycursor1.rowcount
    
    ans1=data[0]
    if ans1==0:
        print('Book is available\n')
        ans=input('Confirm issue? ')         
        if ans=='yes':
            Member_Id=input("Enter member id : ")
            Issue_date=input('Enter date of issue: ')
            #Return_date=input('Enter date of return: ')
            sql="insert into Issue_return (Book_Id,Member_id,Issue_date) values ('"+Book_Id+"','"+Member_Id+"','"+Issue_date+"')"
            #print(sql)
            mycursor1.execute(sql)
            do.commit()
            print('\nBook issue successful')
        else:
            print('Search for another book')
    else:
        print('\nBook is not available')    
    print('\nThanks for using book issue module') 
    print('Tanish Kadam')
    print('Abhinav Dash')
    print('Guided by Ms.Pooja Saxena')
    print('Sagar Public School, Rohit Nagar') 
#--------------------------------------------------------------------------------------------------*/
def book_return():
    print('-'*50)
    print('Welcome to book return module\n') 
    print('')
    
    Book_Id=input('Enter book id(numeric): ')
    sql1="select count(*) from Issue_return where Book_Id="+Book_Id+" and Return_date is NULL"
    
    mycursor1.execute(sql1)
    data=mycursor1.fetchone()
    count1=mycursor1.rowcount
    ans1=data[0]
    #print(sql1,ans1) 
    if ans1==1:
        print('Book is already issued, continue with return')

        Member_Id=input("Enter member id : ")
        Return_date=input('Enter date of return: ')
        Rating=input('Enter rating out of 5: ')
        sql="update Issue_return set Return_date='"+Return_date+"' , Rating='"+Rating+"' where Book_Id="+Book_Id+" and Member_Id="+Member_Id
        #print(sql)
        mycursor1.execute(sql)
        do.commit()    
        print('\nBook return successful')

        print('\nThanks for using book return module') 
        print('Tanish Kadam')
        print('Abhinav Dash')
        print('Guided by Ms.Pooja Saxena')
        print('Sagar Public School, Rohit Nagar') 
#--------------------------------------------------------------------------------------------------*/
def reports():
    print('Welcome to reports module\n')
#--------------------------------------------------------------------------------------------------*/    
def main1():
    ch=0
    while ch!=9:
        print('-'*50)
        print('')
        print('Main menu')
        print('1. Manage Books') 
        print('2. Manage Members')
        print('3. Book issue')
        print('4. Book return')
        print('5. Reports')
        print('9. Exit')
        ch=int(input('Enter your choice: '))
        if ch==1:
            manage_books()
        elif ch==2:
            manage_member()
        elif ch==3:
            book_issue()
        elif ch==4:
            book_return()    
        elif ch==5:
            reports()
        elif ch==9:
            print('Thanks for using our program') 
            print('Tanish Kadam')
            print('Abhinav Dash')
            print('Guided by Ms.Pooja Saxena')
            print('Sagar Public School, Rohit Nagar')     
        else:
            print('Invalid input. Enter a valid input')    
#--------------------------------------------------------------------------------------------------*/
print('Welcome to Library system')
print()
print('')

main1()