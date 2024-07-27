
##Using OOPS concept to build a Hotel Booking Software
import cv2
from fpdf import FPDF
import pyttsx3  
import time
import os

# Class for text-to-speech functionality
class TextToSpeech:
    def __init__(self):
        self.con = pyttsx3.init() 
        voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
        self.con.setProperty('rate', 130)
        self.con.setProperty('volume', 4.0)
        self.con.setProperty('voice', voice_id)

# Main class inheriting from TextToSpeech, displaying main menu
class Main(TextToSpeech):
    def mainmenu(self):
        time.sleep(1)
        print("✨✨    \033[1m Welcome to Pawar Hotels \033[0m    ✨✨".center(150))
        self.con.say("Welcome to Pawar Hotels") 
        self.con.runAndWait()
        print("How are you doing Sir/Madam? \nHope Everything is going well")
        self.con.say("How are you doing Sir,Madam? Hope Everything is going well.")
        self.con.runAndWait()
        ask = AskUserDetails()
        ask.ask_name()
    
# Class to handle user details collection
class AskUserDetails:
    def ask_name(self):
        time.sleep(2)
        self.name = input("Please enter your Name : ").capitalize()
        print(f"You name is {self.name} right?")
        try:
            time.sleep(2)
            ask = int(input("Enter \033[1m1 \033[0m for Yes Enter  \033[1m0 \033[0m for No : "))
        except:
            print("Enter 1/0")
            self.ask_name()
        if ask == 1:
            self.ask_age()
        elif ask == 0:
            print("Ok enter again")
            self.ask_name()
        else:
            print("Enter a valid digit")
            self.ask_name()
    
    def ask_age(self):
        time.sleep(2)
        try:
            self.age = int(input("Please enter your Age in years : "))
        except:
            print("Please enter Valid Digits")
            self.ask_age()
        print(f"You age is {self.age} years right?")
        try:
            time.sleep(2)
            ask = int(input("Enter \033[1m1 \033[0m for Yes Enter  \033[1m0 \033[0m for No : "))
        except:
            print("Enter 1/0")
            self.ask_age()
        if ask == 1:
            self.ask_email_id()
        elif ask == 0:
            print("Ok enter again")
            self.ask_age()
        else:
            print("Enter a valid digit")
            self.ask_age()
    
    def ask_email_id(self):
        time.sleep(2)
        self.email_id = input("Please enter your Email : ")
        print(f"You Email is {self.email_id} right?")
        try:
            time.sleep(2)
            ask = int(input("Enter \033[1m1 \033[0m for Yes Enter  \033[1m0 \033[0m for No : "))
        except:
            print("Enter 1/0")
            self.ask_email_id()
        if ask == 1:
            self.ask_mobile_no()
        elif ask == 0:
            print("Ok enter again")
            self.ask_email_id()
        else:
            print("Enter a valid digit")
            self.ask_email_id()

    def ask_mobile_no(self):
        time.sleep(2)
        try:
            self.mobile_no = int(input("Please enter your 10 digit Mobile  : "))
        except:
            print("Please enter 10 Valid Digits")
            self.ask_mobile_no()
        if len(str(self.mobile_no)) != 10:
            print("Please enter 10 Valid Digits")
            self.ask_mobile_no()
        print(f"You Mobile Number is {self.mobile_no} right?")
        try:
            time.sleep(2)
            ask = int(input("Enter \033[1m1 \033[0m for Yes Enter  \033[1m0 \033[0m for No : "))
        except:
            print("Enter 1/0")
            self.ask_mobile_no()
        if ask == 1:
            self.ask_no_of_persons()
        elif ask == 0:
            print("Ok enter again")
            self.ask_mobile_no()
        else:
            print("Enter a valid digit")
            self.ask_mobile_no()

    def ask_no_of_persons(self):
        time.sleep(2)
        try:
            self.no_of_persons = int(input("Please enter Number of Persons : "))
        except:
            print("Please enter Valid Digits")
            self.ask_no_of_persons()
        print(f"The number of persons are {self.no_of_persons} right?")
        try:
            time.sleep(2)
            ask = int(input("Enter \033[1m1 \033[0m for Yes Enter  \033[1m0 \033[0m for No : "))
        except:
            print("Enter 1/0")
            self.ask_no_of_persons()
        if ask == 1:
            self.ask_room_type()
        elif ask == 0:
            print("Ok enter again")
            self.ask_no_of_persons()
        else:
            print("Enter a valid digit")
            self.ask_no_of_persons()

    def ask_room_type(self):
        time.sleep(2)
        print("Select Your Room Type")
        print("Comfy/Luxura/Business")
        print('For Comfy enter "1"\nFor Luxara enter "2"\nFor Business enter "3"')
        
        # Display room images
        

        select = int(input("Enter Your Choice : "))
        if select == 1:
            self.room_type = "Comfy"
            self.calculate_bill()
        elif select == 2:
            self.room_type = "Luxara"
            self.calculate_bill()
        elif select == 3:
            self.room_type = "Business"
            self.calculate_bill()

    # Calculate bill based on room type
    def calculate_bill(self):
        if self.room_type == "Comfy":
            self.price_for_comfy = 1500
            self.total_bill = self.price_for_comfy * self.no_of_persons
        elif self.room_type == "Luxara":
            self.price_for_luxara = 4500
            self.total_bill = self.price_for_luxara * self.no_of_persons
        elif self.room_type == "Business":
            self.price_for_business = 3000
            self.total_bill = self.price_for_business * self.no_of_persons
        self.display()

    # Display user details and total bill
    def display(self):
        display = UserDetails(self.name, self.age, self.email_id, self.mobile_no, self.no_of_persons, self.room_type, self.total_bill)
        display.__init__

# Class to handle displaying user details and generating receipt
class UserDetails(Main, AskUserDetails):
    time.sleep(2)
    def __init__(self, name, age, emailid, mobile_no, no_of_persons, room_type, total_bill):
        super().__init__()
        self.name = name
        self.age = age
        self.emailid = emailid
        self.mobile_no = mobile_no
        self.no_of_persons = no_of_persons
        self.room_type = room_type
        self.total_bill = total_bill
        print("Have A Look at your Details")
        print(f"Name : {self.name}\nAge: {self.age}\nEmail ID: {self.emailid}\nMobile Number: {self.mobile_no}\nNumber Of Persons: {self.no_of_persons}\n\n Room Type: {self.room_type}")
        time.sleep(5)
        print("Do you Want to Proceed?")
        select = int(input("Enter 1 for Yes, Enter 0 for No: "))
        if select == 1:
            gen = ("Generating Your Receipt.....")
            for i in range(7):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(gen)
                time.sleep(0.1525)
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(0.1525)
            receipt = GenerateReceipt()
            receipt.generate(self.name, self.age, self.emailid, self.mobile_no, self.no_of_persons, self.room_type, self.total_bill)
        elif select == 0:
            print("\n\n😊 Thank you For Visiting us 😊".center(150))
            self.con.say("Thank you For Visiting us")
            self.con.runAndWait()
        else:
            print("Enter 1/0")
            self.__init__

# Class to generate receipt as a PDF
class GenerateReceipt(Main):
    time.sleep(2)
    def generate(self, name, age, emailid, mobile_no, no_of_persons, room_type, total_bill):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=12)
        pdf.cell(200, 10, text="Hotel Booking Receipt", ln=True, align="C")
        pdf.cell(200, 10, text="", ln=True, align="C") 

        user_details = f"Name: {name}\nAge: {age}\nEmail ID: {emailid}\nMobile Number: {mobile_no}\nNumber Of Persons: {no_of_persons}\nRoom Type: {room_type} Total Bill : {total_bill}"
        pdf.multi_cell(0, 10, text=user_details)

        pdf.output("hotel_receipt.pdf")
        print("Successfully Generated")
        time.sleep(2)
        print("\n\n😊 Thank you For Visiting us 😊".center(150))
        self.con.say("Thank you For Visiting us")
        self.con.runAndWait()

# Instantiate Main class and show main menu
main = Main()
main.mainmenu()



class GenerateReceipt(Main):
    time.sleep(2)
    def generate(self, name, age, emailid, mobile_no, no_of_persons, room_type, total_bill):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=12)
        pdf.cell(200, 10, text="Hotel Booking Receipt", ln=True, align="C")
        pdf.cell(200, 10, text="", ln=True, align="C") 

        user_details = f"Name: {name}\nAge: {age}\nEmail ID: {emailid}\nMobile Number: {mobile_no}\nNumber Of Persons: {no_of_persons}\nRoom Type: {room_type} Total Bill : {total_bill}"
        pdf.multi_cell(0, 10, text=user_details)

        pdf.output("hotel_receipt.pdf")
        print("Successfully Generated")
        time.sleep(2)
        print("\n\n😊 Thank you For Visiting us 😊".center(150))
        self.con.say("Thank you For Visiting us")
        self.con.runAndWait()

# Instantiate Main class and show main menu
main = Main()
main.mainmenu()





var="hello"
print(var.up)
