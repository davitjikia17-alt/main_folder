"""
fleppa Ordering System
---------------------
This program simulates a small food stand.
Customers can order half pita, full pita, or a deal.
They choose salads, pay with cash or credit,
and at the end the program calculates total profit.

"""
# Prices
half_pita = 15
pita = 25
deal = 33

salad_list =["salad", "humus", "tehini", "harif", "amba", "cabbage", "pickles", "chips", "onion"]
orders = []  #customer's toppings
guest = "yes"
total_pay = 0
change = 0
pitas = 0  # Counter for pitas sold
half_pitas = 0  # Counter for half pitas sold
deals = 0   # Counter for deals sold
amounts = 0  # Cash given by customer
# Earnings
total_earn_halfpita = 0
total_earn_pita = 0
total_earn_deal = 0
"""
Main customer loop
Runs as long as there are more customers
"""
while guest == "yes" :
    print("this is our FLEPPA. please choose what do you want to order:")
    print(f"1 half {half_pita} (with 4 salads)\n2 mana {pita} (with 7 salads)\n3 deal {deal} (with 7 salads)")
    your_order = int(input("enter order num:"))
    """
    half pita order
    """
    if your_order == 1:
        half_pitas += 1  # Count half pita sold
        for i in range (4,0,-1):   # Customer can choose up to 4 salads
            print(f"you have {i} toppings left to chose.")
            print(f"you can choose between:\n{salad_list}\nor enter stop if you're done.")
            order = input("what do you want in your pita? ")
            if order in salad_list :
                salad_list.remove(order)
                orders.append(order)
            elif order == "stop" or i == 0 :
                break
        print(f"you got {orders} . you need to pay: {half_pita}")
        pay = int(input("how would you like to pay? 1. cash 2. credit card "))
        if pay == 1 :
            while amounts < half_pita:
                amount = int(input("please enter cash:"))
                amounts += int(amount)
            change = amounts - half_pita
            print(f"thank you! you get back {change}. have a nice FLEPPA!")
        elif pay == 2:
            code = input("please enter your 4 digit code:")
            while (code != "1234") and (code != "4322" ) :
                code = input("please enter you 4 digit code:")
            if (code == "1234") or (code == "4322"):

                print(f"your payment is received. have a nice FLEPPA!")

    """
    Ddeal order 
    Including chips and soda
    """
    if your_order == 3:
        deals += 1
        for i in range (7,0,-1):
            print(f"you have {i} toppings left to chose.")
            print(f"you can choose between:\n{salad_list}\nor enter stop if you're done.")
            order = input("what do you want in your pita? ")
            if order in salad_list :
                salad_list.remove(order)
                orders.append(order)
                orders.append("chips")
                orders.append("soda")
            elif order == "stop" or i == 0 :
                orders.append("chips")
                orders.append("soda")
                break
        print(f"you got {orders} . you need to pay: {deal}")
        pay = int(input("how would you like to pay? 1. cash 2. credit card "))
        if pay == 1 : # Cash payment until it is paid full
            while amounts < deal:
                amount = int(input("please enter cash:"))
                amounts += int(amount)
            change = amounts - deal
            print(f"thank you! you get back {change}. have a nice FLEPPA!")
        elif pay == 2:   # Credit card verification
            code = input("please enter your 4 digit code:")
            while (code != "1234") and (code != "4322"):
                code = input("please enter you 4 digit code:")
            if (code == "1234") or (code == "4322"):
                print(f"your payment is received. have a nice FLEPPA!")
    """
    pita order
    """
    if your_order == 2:
        pitas += 1
        for i in range (7,0,-1):
            print(f"you have {i} toppings left to chose.")
            print(f"you can choose between:\n{salad_list}\nor enter stop if you're done.")
            order = input("what do you want in your pita? ")
            if order in salad_list :
                salad_list.remove(order)
                orders.append(order)
            elif order == "stop" or i == 0 :
                break
        print(f"you got {orders} . you need to pay: {pita}")
        pay = int(input("how would you like to pay? 1. cash 2. credit card "))
        if pay == 1 :
            while amounts < pita:
                amount = int(input("please enter cash:"))
                amounts += int(amount)
            change = amounts - pita
            print(f"thank you! you get back {change}. have a nice FLEPPA!")

        elif pay == 2:
            code = input("please enter you 4 digit code:")
            while (code != "1234") and (code != "4322"):
                code = input("please enter your 4 digit code:")
            if (code == "1234") or (code == "4322"):
                print(f"your payment is received. have a nice FLEPPA!")
    """
    Check if there is another customer
    """
    costumer = input("another costumer? yes/no")
    if costumer == "no" :
        guest = "no"

    elif costumer == "yes" :
        guest = "yes"
"""
profit calculation
"""
print("good day today! you sold:")
profit_deal =0
profit_halfpita = 0
profit_pita = 0
if half_pitas != 0 :
    print(f"half {total_earn_halfpita}")
    total_earn_halfpita = half_pita * half_pitas
    profit_halfpita = total_earn_halfpita

if pitas != 0 :
    print(f"pita {total_earn_pita}")
    total_earn_pita = pita * pitas
    profit_pita = total_earn_pita * 0.7
if deals != 0 :
    print(f"Deal {total_earn_deal}")
    total_earn_deal = deal * deals
    profit_deal = total_earn_deal * 0.5
profit = profit_deal + profit_halfpita + profit_pita
print(f"you earned: {profit}")


