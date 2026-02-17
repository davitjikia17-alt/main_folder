def fee_monthly(years):
    if years > 3:
        return 1200
    elif years < 8:
        return 50 * years
    return 100 * years


def sigle_costumer():
    while True:
        years = int(input("Enter number of membership years (0 to exit): "))
        if years == 0:
            break

        fee = fee_monthly(years)
        print("Monthly fee:", fee)


def total_income_for_customers():
    total_income = 0
    for i in range(5000):
        years = int(input(f"Enter membership years for customer {i}: "))
        fee = fee_monthly(years)
        total_income += fee
    print("Total monthly income:", total_income)