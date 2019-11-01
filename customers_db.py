import time
import random
import re
import pickle
import os

#----------------------------------------BOOK---------------------------------------------------------

class Book:
    def __init__(self,a):
        random.seed(time.time())
        self.status = a
        self.id = "BID00000"
        if(a==1):
            self.status = a
            self.id = "BID" + str(int((random.random()*(10**6))))
            self.name = input("\nName:  ")
            self.author =(input("\nAuthor:  "))
            self.price= int(input("\nPrice:  "))
            self.number_of_pages = int(input("\nNo. of Pages:  "))
            
    # The default function is overwritten
    def __str__(self):
        if(self.status==1):
            return "%s\t%s\t\t%s\t\t%d\t\t%s" % (self.id,self.name,self.author,self.price,self.number_of_pages)
        else:
            return "\n\nEND OF FILE"
    def showdata(self):
        print("The details of desired Books are as follows: ")
        print(self.id)
        print(self.name)
        print(self.author)
        print(self.price)
        print(self.number_of_pages)
def Display_All_Book():
        print("Book List")
        print("\n-----------------------------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print("Sr.no\t  ID\t\tName\t\tAuthor Name\tPrice\t\tNumber of Pages")
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        l = 1
        with open('book.txt','rb') as file:
            while True:
                try:
                    B = pickle.load(file)
                    print(l,"\t",B)
                    l = l + 1
                except EOFError:
                    print("\n\nFile finished.......")
                    break

def Create_Book():
	B = Book(1) 
	with open('book.txt','ab') as file:
		pickle.dump(B,file)
	print("\n\nCreating Book Record. Please Wait...........")
	time.sleep(3)
	print("\nBook Record Created...")

def Display_Book(cust_id):
	B = Customer(0)
	with open('book.txt','rb') as file:
		while(cust_id != B.id):
			B = pickle.load(file)

	B.showdata()

def Modify_Book(cust_id):
	with open('book.txt','rb+') as file:
		B = pickle.load(file)
	
		print("Choose the parameter to modify:\n\n[1]Name\n\n[2]Author\n\n[3]Price\n\n[4]Number_of_Pages")
		p = int(input())
			
		while(cust_id != B.id):
			B = pickle.load(file)
			
		if(p==1):
			B.name = input("Enter the new data:  ")
			file.seek(-56,1)
			pickle.dump(B,file)
		
		elif(p==2):
			B.author = int(input("Enter the new data:  "))
			file.seek(-56,1)
			pickle.dump(B,file)
			
		elif(p==3):
			B.price = input("Enter the new data:  ")
			file.seek(-56,1)
			pickle.dump(B,file)

		elif(p==4):
			B.number_of_pages = int(input("Enter the new data:  "))
			file.seek(-56,1)
			pickle.dump(B,file)

		else:
			print("Invalid Option!")
		
		if p==1 or p==2 or p==3 or p==4:
			print("\nModifying Book Record........Please Wait")
			time.sleep(3)
			print("Book Record Modified")

def Delete_Book(cust_id):
	books = []

	with open('book.txt','rb') as file:
		while True:
			try:
				books.append(pickle.load(file))
			except EOFError:
				break

	for i in range(0,len(books)) :
		if books[i].id == cust_id :
			break

	del books[i]

	os.system("rm book.txt")
	os.system("touch book.txt")

	for book in books:
		with open('book.txt','ab') as file:
			pickle.dump(book,file)

	print("\nDeleting Books Record........Please Wait")
	time.sleep(3)
	print("Book Record Deleted")

#----------------------------------------/BOOK--------------------------------------------------------
#----------------------------------------Customer-----------------------------------------------------
#This is the regular expression format for validating email-id
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# Mobile no. and email-id validator
def isValid(s,n):
	if n==1:
		Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
		return Pattern.match(s)
	elif n==2:
		return re.search(regex,s)

class Customer:
	def __init__(self,a):
		random.seed(time.time())
		self.status = a
		self.id = "UID00000"
		if(a==1):
			self.status = a
			self.id = "UID" + str(int((random.random()*(10**6))))
			self.name = input("\nName:  ")
			self.age = int(input("\nAge:  "))
			self.mobile_no = int(input("\nMobile No.:  "))
			while ((isValid(str(self.mobile_no),1))==False):
				self.mobile_no = int(input("\nInvalid mobile no!\nEnter mobile no. again:  "))
			self.occupation = input("\nOccupation:  ")
			self.email_id = input("\nEmail-id:  ")
			while ((isValid(self.email_id,2))==False):
				self.email_id = input("\nInvalid email id!\nEnter email-id again:  ")
			self.books_purchased = 0

# The default function is overwritten
	def __str__(self):
		if(self.status==1):
			return "%s\t%s\t\t%d\t\t%d\t\t%s" % (self.id,self.name,self.mobile_no,self.books_purchased,self.email_id)
		else:
			return "\n\nEND OF FILE"

	def showdata(self):
		print("The details of desired customer are as follows: ")
		print(self.id)
		print(self.name)
		print(self.age)
		print(self.mobile_no)
		print(self.occupation)
		print(self.email_id)
		print(self.books_purchased)

def Create_New_Customer():
	C = Customer(1) 
	with open('customers.txt','ab') as file:
		pickle.dump(C,file)
	print("\n\nCreating Customer Record. Please Wait...........")
	time.sleep(3)
	print("\nCustomer Record Created...")

def Display_All_Records():		
	print("CUSTOMER LIST")
	print("\n-----------------------------------------------------------------------------------------------------------------------------------")
	print("-----------------------------------------------------------------------------------------------------------------------------------")
	print("Sr.no\t  ID\t\tName\t\t\t\tMobile No\tBooks Purchased\t\tEmail")
	print("-----------------------------------------------------------------------------------------------------------------------------------")
	print("-----------------------------------------------------------------------------------------------------------------------------------")
	m = 1
	with open('customers.txt','rb') as file:
		while True:
			try:
				C = pickle.load(file)
				print(m,"\t",C)
				m = m + 1
			except EOFError:
				print("\n\nFile finished.......")
				break

def Display_Record(cust_id):
	C = Customer(0)
	with open('customers.txt','rb') as file:
		while(cust_id != C.id):
			C = pickle.load(file)

	C.showdata()

def Modify_Record(cust_id):
	with open('customers.txt','rb+') as file:
		C = pickle.load(file)
			
		print("Choose the parameter to modify:\n\n[1]Name\n\n[2]Mobile number\n\n[3]Email-id\n\n[4]Books Purchased")
		p = int(input())
			
		while(cust_id != C.id):
			C = pickle.load(file)
			
		if(p==1):
			C.name = input("Enter the new data:  ")
			file.seek(-56,1)
			pickle.dump(C,file)
		
		elif(p==2):
			C.mobile_no = int(input("Enter the new data:  "))
			while ((isValid(str(C.mobile_no),1))==False):
				C.mobile_no = int(input("\nInvalid mobile no!\nEnter mobile no. again:  "))
			file.seek(-56,1)
			pickle.dump(C,file)
			
		elif(p==3):
			C.email_id = input("Enter the new data:  ")
			while ((isValid(C.email_id,2))==False):
				C.email_id = input("\nInvalid email id!\nEnter email-id again:  ")
			file.seek(-56,1)
			pickle.dump(C,file)

		elif(p==4):
			C.books_purchased = int(input("Enter the new data:  "))
			file.seek(-56,1)
			pickle.dump(C,file)

		else:
			print("Invalid Option!")
		
		if p==1 or p==2 or p==3 or p==4:
			print("\nModifying Customer Record........Please Wait")
			time.sleep(3)
			print("Customer Record Modified")

def Delete_Record(cust_id):
	customers = []

	with open('customers.txt','rb') as file:
		while True:
			try:
				customers.append(pickle.load(file))
			except EOFError:
				break

	for i in range(0,len(customers)) :
		if customers[i].id == cust_id :
			break

	del customers[i]

	os.system("rm customers.txt")
	os.system("touch customers.txt")

	for customer in customers:
		with open('customers.txt','ab') as file:
			pickle.dump(customer,file)

	print("\nDeleting Customer Record........Please Wait")
	time.sleep(3)
	print("Customer Record Deleted")
#------------------------------------------------------/Customer----------------------------------------
def Book_Purchase():
	print("Welcome To Book Purchase Portal")
	print("Please Enter Mode of Search")
	n=int(input("1: By Name\t2:By Author"))
	if(n==1):
		name=str(input("Enter Book Name:"))

	if(n==2):
		auth=str(input("Enter Author Name:"))
		
def Book_Donate():
		print("Book Donate Portal")
		print("Thanks To Donate To Our Franchise")
		print("Please Enter Book Details")
		dh1 = 'y'
		while dh1=='y' or dh1=='Y':
			Create_Book()
			dh1 = 'N'
			dh1 = input("\nDo you want to Donate more book...(y/N)?")
#---------------------------------------------------MainMenu--------------------------------------------------
def Admin_Menu():
	ch0 = 'y'
	while ch0=='y' or ch0=='Y':
		os.system("clear")
		print("ADMINISTRATOR MENU")
		print("\n1. CREATE CUSTOMER RECORD")
		print("\n2. DISPLAY ALL CUTOMERS RECORD")
		print("\n3. DISPLAY SPECIFIC CUSTOMER RECORD")
		print("\n4. MODIFY CUSTOMER RECORD")
		print("\n5. DELETE CUSTOMER RECORD")
		print("\n6. CREATE BOOK")
		print("\n7. DISPLAY ALL BOOKS")
		print("\n8. DISPLAY SPECIFIC BOOK")
		print("\n9. MODIFY BOOK")
		print("\n10. DELETE BOOK")
		print("\n11. BACK TO MAIN MENU")
		n = int(input("\nPlease Enter Yout Choice (1-11)"))

		if n==1:
			ch1 = 'y'
			while ch1=='y' or ch1=='Y':
				Create_New_Customer()
				ch1 = 'N'
				ch1 = input("\nDo you want to add more record...(y/N)?")	

		if n==2:
			Display_All_Records()

		if n==3:
			ch3 = 'y'
			while ch3=='y' or ch3=='Y' :
				print("Enter the ID of the customer:  ",end=" ")
				cust_id = input()
				Display_Record(cust_id)
				ch3 = 'N'
				ch3 = input("\n\nDo you want to print details of another customer...(y/N)?  ")
			
		if n==4:
			print("Enter the ID of the customer:  ",end=" ")
			cust_id = input()
			ch4 = 'y'
			while ch4=='y' or ch4=='Y':
				Modify_Record(cust_id)
				ch4 = 'N'
				print("\nDo you want to modify another record...(y/N)?  ",end=" ")
				ch4 = input()

		if n==5:
			cust_id = input("Enter the customer ID:  ")
			ch5 = 'y'
			while ch5=='y' or ch5=='Y':
				Delete_Record(cust_id)
				ch5 = 'N'
				print("\nDo you want to delete another record...(y/N)?  ",end=" ")
				ch5 = input()

		if n==6:
			bh1 = 'y'
			while bh1=='y' or bh1=='Y':
				Create_Book()
				bh1 = 'N'
				bh1 = input("\nDo you want to add more book...(y/N)?")
			
		
		if n==7:
			Display_All_Book()
		
		if n==8:
			bh3 = 'y'
			while bh3=='y' or bh3=='Y' :
				print("Enter the ID of the Book:  ",end=" ")
				cust_id = input()
				Display_Record(cust_id)
				bh3 = 'N'
				bh3 = input("\n\nDo you want to print details of another customer...(y/N)?  ")		
		if n==9:
			print("Enter the ID of the Book:  ",end=" ")
			cust_id = input()
			bh4 = 'y'
			while bh4=='y' or bh4=='Y':
				Modify_Book(cust_id)
				bh4 = 'N'
				print("\nDo you want to modify another record...(y/N)?  ",end=" ")
				bh4 = input()
		
		if n==10:
			cust_id = input("Enter the Book ID:  ")
			bh5 = 'y'
			while bh5=='y' or bh5=='Y':
				Delete_Book(cust_id)
				bh5 = 'N'
				print("\nDo you want to delete another book record...(y/N)?  ",end=" ")
				bh5 = input()

		if n==11:
			Main_Menu()

		ch0 = 'N'
		ch0 = input("\n\nDo you want to choose another option....(y/N)?  ")


def Main_Menu():
	print("MAIN MENU")
	print("\n1. BOOK PURCHASE")
	print("\n2. BOOK DONATE")
	print("\n3. ADMINISTRATOR MENU")
	print("\n4. EXIT")
	n = int(input("\nPlease Select Your Option (1-4)  "))

	if(n==1):
		Book_Purchase()
	if(n==2):
		Book_Donate()
	if(n==3):
		Admin_Menu()

	if(n==4):
		exit(0)

Main_Menu()
