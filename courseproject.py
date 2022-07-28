#store greeting
print("Hello, welcome to Yarn Stop!")

#selecting delivery date
print("To begin, please select a delivery date on the calendar.")

#import calendar module
import calmodule
from calmodule import delivery_date

#import receipt module
import projcustomerlist
db = {1:("Crochet Blanket", 40.00), 2:("Knit Stuffed Bear", 15.00), 3:("Crochet Shawl", 25.00), 4:("Knit Hat", 10.00)}
print("Please select from the following products: ") #items for sale
for k, v in db.items():
    print("{}) {}: $ {}".format(k, v[0], v[1]))
customer_list = []
keep_choosing = "Y"         #customer selection
while keep_choosing == "Y":
    choice = int(input("\nWhat is your choice: "))
    if choice in db.keys():                         #if-else statement
        customer_list.append((db[choice][0], db[choice][1]))
    else:
        print("Invalid choice, please try again")
    keep_choosing = input("Keep choosing? (Y for yes, N for no): ").upper() #uppercase input

projcustomerlist.total(customer_list)

#order detail classes
class OrderDetails():       #class for order item details
    details = []
    
    def __init__(self):
        print("Please provide additional details about your order below.")

    def size(self):
        self.size = input("What size item would you like to order? Choose from S/M/L. ")

    def color(self):
        self.color = input("What color item would you like to order? ")

item1 = OrderDetails()
item1.size()
item1.color()

class ContactInfo():        #class for contact information
    def __init__(self):
        print("Please provide contact information for your order.") #contact info prompt

    def phone(self):
        self.phone = int(input("Please enter your phone number: ")) #phone number prompt

    def email(self):
        self.email = input("Please enter your email: ") #email prompt

def getphone():
    while True:
        try:
            assert self.phone.isdigit()
            #if input is invalid
            print("Invalid phone number, please try again.")
            #else return phone number
        except ValueError:
            print("Invalid phone number, please try again.")
            break   

info1 = ContactInfo()
info1.phone()
info1.email()

print("Selected size: ", item1.size)
print("Selected color: ", item1.color)
print("Phone number: ", info1.phone)
print("Email: ", info1.email)

print("Thank you for your order!")


