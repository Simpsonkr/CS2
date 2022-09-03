import calculations

day=["Friday","Saturday","sunday"]
weekendCost=0.0
for x in day:
    print(f"{x} Night Party")
    guests=int(input("How many people will be attending?"))
    pizzaSlices=float(input("How many slices will each person be allowed to eat?"))
    price=float(input("What is cost of a pizza?"))

    amountOfPizzas=calculations.numberOfPizzas(guests, pizzaSlices)
    costOfPizzas=amountOfPizzas*price
    print(f"You will need {amountOfPizzas} pizzas, it will cost ${costOfPizzas:.2f}")
    tax=calculations.tax(costOfPizzas)
    print(f"Tax is ${tax:.2f}")
    deliveryFee=calculations.delivery(costOfPizzas, tax)
    print(f"deliveryFee is ${deliveryFee:.2f}")
    finalCost=costOfPizzas+tax+deliveryFee
    print(f"Cost of the party is ${finalCost:.2f}")
    weekendCost=weekendCost+finalCost
print(f"Cost of the weekend is ${weekendCost:.2f}")
