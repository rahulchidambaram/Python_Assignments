# Calculate restaurant bill
def calculate_restaurant_bill(meal_cost):
    #tax and tip is 5 %
    tax_and_tip = 0.05
    service_charge = meal_cost * 0.1
    amount_after_service = service_charge + meal_cost
    # adding amount after service tax + tax + tip amount
    tax_tip_amount = amount_after_service * tax_and_tip
    total = amount_after_service + tax_tip_amount + tax_tip_amount

    print(f''' 
Meal Cost: {meal_cost}
Service Charge (10%): {service_charge}
Amount after Service: {amount_after_service}
Tax (5%): {tax_tip_amount}
Tip (5%): {tax_tip_amount}
Total Bill: {total}
''')

bill = float(input("Enter the meal cost: "))
calculate_restaurant_bill(bill)


