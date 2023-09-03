def calculate_taxes(price):
    return price * 0.2

def print_receipt(total_price, is_special):
    total_taxes = sum(calculate_taxes(price) for price in parts_prices)
    total_price_with_taxes = total_price + total_taxes

    if is_special:
        total_price_with_taxes *= 0.9

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price}$")
    print(f"Taxes: {total_taxes}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes}$")

parts_prices = []
total_price = 0

while True:
    price_input = input()

    if price_input == "special":
        print_receipt(total_price, True)
        break

    if price_input == "regular":
        print_receipt(total_price, False)
        break

    try:
        price = float(price_input)

        if price <= 0:
            print("Invalid price!")
            continue

        total_price += price
        parts_prices.append(price)
    except ValueError:
        print("Invalid price!")
        continue

if total_price == 0:
    print("Invalid order!")
