import csv
from datetime import date

records = r"Code-main\Home\class12project\project\records.csv"
bill_file = r"Code-main\Home\class12project\project\billing.csv"

def new_prod():
    print("========================================================")
    print("Enter Details of new product:")
    id = int(input("Enter product Id for new entry:"))
    name = input("Enter the name of product:")
    company = input("Product is manufactured by:")
    exp_date = input("Enter product Expiry date:")
    price = float(input("Enter price of Product:"))
    quantity = int(input("Enter The quantity of product:"))

    new_product = [id, name, company, exp_date, price, quantity]

    try:
        with open(records, "a") as file:
            writer = csv.writer(file) 
            writer.writerow(new_product)
    except FileNotFoundError:
        with open(records, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Id", "Name", "Company", "Exp_date", "Price", "Quantity"])
            writer.writerow(new_product)

    Inventory()

def table_printer():
    try:
        with open(records, "r") as file:
            reader = csv.reader(file)
            print("Product Id\tProduct Name\tManufactured\tExpiry Date\t\tPrice\t\tQuantity")
            for row in reader:
                print("\t\t".join(row))
    except FileNotFoundError:
        print("No records found.")

def bill_printer():
    try:
        with open(bill_file, "r") as file:
            reader = csv.reader(file)
            print("Customer Id\tCustomer Name\tMobile\t\tBill Date\t\tBill Amount")
            for row in reader:
                if len(row) == 5:
                    print("\t\t".join(row))
                else:
                    print("\t\t".join(row[:3]) + "\t\t" + "\t\t".join(row[3:]))
    except FileNotFoundError:
        print("No bills found.")

def new_bill():
    print("=============================================================")
    print("Creating New bill Enter all details:")
    bill = 0.00
    id = int(input("Enter Id for new customer:"))
    name = input("Enter Name of customer:")
    mobile = input("Enter customer mobile Number:")
    bill_date = str(date.today())

    while True:
        table_printer()
        product_id = input("Enter product Id for item needed:")

        found = False
        with open(records, "r") as file:
            reader = csv.reader(file)
            record = list(reader)

        for row in record:
            try:
                if row[0] == product_id:
                    found = True
                    price = float(row[4])
                    quantity = int(row[5])
                    break
            except:
                pass

        if not found:
            print("Product ID not found, please try again.")
            continue

        quant_needed = int(input("Enter Quantity needed:"))

        if quant_needed > quantity:
            print("Not enough quantity available.")
            continue

        bill += price * quant_needed

        for row in record:
            try:
                if row[0] == product_id:
                    row[5] = str(quantity - quant_needed)
                    break
            except:
                pass

        with open(records, "w") as file:
            writer = csv.writer(file)
            writer.writerows(record)

        c = input("Do you want to buy more items?(Y/N):")
        if c.lower() == "n":
            print("Your bill Amount is " + str(bill))
            break

    new_cust = [id, name, mobile, bill_date, bill]

    try:
        with open(bill_file, "a") as file:
            writer = csv.writer(file)
            writer.writerow(new_cust)
    except FileNotFoundError:
        with open(bill_file, "w") as file:
            writer = csv.writer(file)
            writer.writerow(new_cust)

    billing()

def Inventory():
    print("\t\t ___________________________________________")
    print("\t\t|            Inventory Management           |")
    print("\t\t|___________________________________________|")
    print("\t\t Select Action to perform: \n\t\t 1. Enter New product \n\t\t 2. Show the inventory \n\t\t 3. Search Product \n\t\t 4. BACK ")
    n = int(input("\t\tEnter your choice of action:"))
    if n == 1:
        new_prod()
    elif n == 2:
        table_printer()
        Inventory()
    elif n == 3:
        search_product()
    elif n == 4:
        print("\t\t Exiting...")
        print("\n\n\n")
        first_view()
    else:
        print("\t\t Wrong choice, restarting...")
        print("\n\n\n")
        Inventory()

def billing():
    print("\t\t ___________________________________________")
    print("\t\t|               Billing System              |")
    print("\t\t|___________________________________________|")
    print("\t\t Select Action to perform: \n\t\t 1. Make NEW Bill \n\t\t 2. Print ALL Bills \n\t\t 3. Search Bill \n\t\t 4. Back")
    n = int(input("\t\tEnter your choice of action:"))
    if n == 1:
        new_bill()
    elif n == 2:
        bill_printer()
        billing()
    elif n == 3:
        search_bill()
    elif n == 4:
        print("\t\t Exiting...")
        print("\n\n\n")
        first_view()
    else:
        print("\t\t Wrong choice, restarting...")
        print("\n\n\n")
        billing()

def first_view():
    print("\t\t ___________________________________________")
    print("\t\t|        Inventory Management System        |")
    print("\t\t|___________________________________________|")
    print("\t\t Select Action to perform: \n\t\t 1. Access the Inventory \n\t\t 2. Access Billing\n\t\t 3. Exit")
    n = int(input("\t\tEnter your choice of action:"))
    if n == 1:
        Inventory()
    elif n == 2:
        billing()
    elif n == 3:
        print("Thank you for using this IMS.")
    else:
        print("\t\t Wrong choice, restarting...")
        print("\n\n\n")
        first_view()

def search_product():
    product_id = input("Enter Product ID to search: ")
    found = False
    try:
        with open(records, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == product_id:
                    found = True
                    print("Product found:")
                    print("Product Id\tProduct Name\tManufactured\tExpiry Date\t\tPrice\t\tQuantity")
                    print("\t\t".join(row))
                    break
        if not found:
            print("Product ID not found.")
    except FileNotFoundError:
        print("No records found.")

def search_bill():
    search_term = input("Enter Customer ID or Name to search bills: ")
    found = False
    try:
        with open(bill_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if search_term in row:
                    found = True
                    print("Matching bills:")
                    print("Customer Id\tCustomer Name\tMobile\t\tBill Date\t\tBill Amount")
                    if len(row) == 5:
                        print("\t\t".join(row))
                    else:
                        print("\t\t".join(row[:3]) + "\t\t" + "\t\t".join(row[3:]))
            if not found:
                print("No matching bills found.")
    except FileNotFoundError:
        print("No bills found.")

first_view()
