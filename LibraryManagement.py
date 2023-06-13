import os
import datetime
class Library:
   def __init__(self,List_of_Books,library_name):
        self.List_of_Books=List_of_Books
        self.library_name=library_name
        self.book_dict={}
        ID=1001
        with open(self.List_of_Books) as bk:
            content=bk.readlines()
        for i in content:
            self.book_dict.update({str(ID):{"book_title":i.replace("\n",""),"Lender_name":"","status":"Available","issue_date":""}})
            ID=ID+1
   def display(self):
       for key,value in self.book_dict.items():
           print(key,"\t\t",value.get("book_title"),"\t\t",value.get("Lender_name"),"\t\t","[",value.get("status"),"]","\t\t",value.get("issue_date"))

   def issueBook(self):
       book_id=input("Enter Book ID......")
       current_time=datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
       if book_id in self.book_dict.keys():
           if not self.book_dict[book_id]["status"]=='Available':
               print(f"Book of id {book_id} is already issued on {self.book_dict[book_id]['issue_date']} by {self.book_dict[book_id]['Lender_name']}")
           elif self.book_dict[book_id]["status"]=='Available':
               your_name=input("Enter your name.....")
               self.book_dict[book_id]['Lender_name']=your_name
               self.book_dict[book_id]['issue_time']=current_time
               self.book_dict[book_id]["status"]='already issued'
               print("your book issued successfully!!!!")
   def addBook(self):
       NewBook=input("Enter title of new book.....")
       if(NewBook==""):
           return self.addBook()
       elif(len(NewBook)>15):
           print("Title is too long ,title must conatin only 10 characters.....")
       else:
           with open(self.List_of_Books,'a') as bk:
               bk.writelines(f"{NewBook}\n")
           self.book_dict.update({str(int(max(self.book_dict))+1):{"book_title":NewBook,"Lender_name":"","status":'Available',"issue_date":''}})
           print("Book is added successfully!!!")
   def returnBook(self):
    book_id=input("Enter your book ID...")
    if book_id in self.book_dict.keys():
       if self.book_dict[book_id]["status"]=='Available':
           print(f"This book of {book_id} already exist in library")
       elif not self.book_dict[book_id]["status"]=='Available':
           self.book_dict[book_id]["status"]='Available'
           self.book_dict[book_id]["Lender_name"]=''
           self.book_dict[book_id]['issue_time']=''
           print("Returning process is successfully completed!!!!")
    else:
        print("Book ID is not found.....")
try:
 obj=Library('List_of_Books.txt',"Python's library")
 press_key_list={"D":"Display Books","I":"Issue Book","A":"Add Book","R":"Return Book","Q":"Quit"}
 key_press=False
 print("")
 print(f"-------------------------WELCOME TO {obj.library_name} Library management system-----------------------")
 print("")
 for key,value in press_key_list.items():
         print(f"press {key} to {value}")
 while(key_press!="q"):
     key_press=input("press key:")
    #  os.system('cls')
     if key_press=='i':
             print("Your selection : Issue Book")
             obj.issueBook()
     elif key_press=='a':
             print("Your selection : Add Book")
             obj.addBook()
     elif key_press=='d':
             print("Your selection : Display Book")
             obj.display()
     elif key_press=='r':
             print("Your selection : Return Book")
             obj.returnBook()
     elif key_press=='q':
             print("You are successfully exit from application........")
             break
except:
    print("something went wrong , please check out your input !!!!")

 