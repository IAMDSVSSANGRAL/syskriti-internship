def calculate_electricity_bill(units: float) -> float:
    """
    Calculate electricity bill based on slab rates.
    
    Rates:
    - First 100 units @ 2/unit
    - Next 100 units @ 3/unit
    - Next 300 units @ 5/unit
    - Above 500 units @ 8/unit
    - Fixed charge ₹50 if units > 0
    """

    if units <= 0:
        return 0

    bill = 0

    if units <= 100:
        bill = units * 2

    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)

    elif units <= 500:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    else:
        bill = (100 * 2) + (100 * 3) + (300 * 5) + ((units - 500) * 8)

    bill += 50  # fixed charge

    return bill



#USING Match Case
units = float(input("Enter electricity units: "))
bill = 0

if units <= 0:
    print("Invalid units entered.")
else:
    match units:
        case u if u <= 100:
            bill = u * 2

        case u if u <= 200:
            bill = (100 * 2) + ((u - 100) * 3)

        case u if u <= 500:
            bill = (100 * 2) + (100 * 3) + ((u - 200) * 5)

        case _:
            bill = (100 * 2) + (100 * 3) + (300 * 5) + ((units - 500) * 8)

    bill += 50
    print(f"Total electricity bill for {units} units is: ₹{bill}")