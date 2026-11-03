def calculate_customer_totals(purchases):
    totals = {}

    for purchase in purchases:
        customer = purchase["customer"]
        amount = purchase["amount"]

        if customer not in totals:
            totals[customer] = 0

        totals[customer] += amount

    return totals


if __name__ == "__main__":
    purchases = [
        {"customer": "Ada", "amount": 2000},
        {"customer": "John", "amount": 1500},
        {"customer": "Ada", "amount": 3000},
        {"customer": "John", "amount": 500},
        {"customer": "Mary", "amount": 2500},
    ]

    totals = calculate_customer_totals(purchases)

    for customer, total in totals.items():
        print(f"{customer}: ₦{total:,}")