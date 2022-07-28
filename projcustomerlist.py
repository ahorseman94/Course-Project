#receipt module

fout = open("receipt.text", "w")     #open receipt file to write

import calmodule
from calmodule import delivery_date

tax = 0.0775        #tax calculation

def total(customer_list):

    subtotal = 0

    for i in customer_list:
        subtotal += (i[1])

    print(customer_list)
    print("Subtotal is: $ {:.2f}" .format(subtotal)) #returns subtotal

    shipping = subtotal * 0.05
    print("Shipping: $ {:.2f}" .format(shipping)) #returns shipping cost

    t_amount = tax*subtotal
    print("Tax: \t $ {:.2f}" .format(t_amount)) #returns tax cost

    total = subtotal + t_amount + shipping
    print("Total: \t $ {:.2f}" .format(total)) #returns total price

    deliverydate = delivery_date
    print("Delivery date is: {}" .format(deliverydate)) #returns delivery date

    receipt(customer_list, subtotal, total, shipping, deliverydate)

def receipt(customer_list, subtotal, total, shipping, deliverydate):


    fout.write("**** RECEIPT ****\n")       #receipt formatting
    fout.write("Item        Price\n")
    fout.write("----         ----\n")

    for i in customer_list:
        fout.write("{} $ {}\n".format(i[0],i[1]))


    fout.write('''
------------------------------
Subtotal: $ {}
Shipping: $ {:.2f}
Tax:      % {}
Total:    $ {:.2f}
Delivery Date: {}
------------------------------
Thank you for shopping with us!
'''.format(subtotal, shipping, tax*100, total, deliverydate))

    fout.close()
    print("\nYour receipt has been printed in the receipt.txt file")
