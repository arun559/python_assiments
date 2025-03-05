print("welcome to mr. alone supermarket\n")

floors = {
    "5th floor": {
        "category": "groceries",
        "items": {"rice": 50, "toor dal": 120, "urad dal": 90, "moong dal": 100, "sugar": 40, "salt": 20}
    },
    "4th floor": {
        "category": "clothing",
        "items": {"shirt": 500, "pants": 700, "saree": 1200, "t-shirt": 400, "jeans": 800, "jacket": 1500}
    },
    "3rd floor": {
        "category": "cosmetics",
        "items": {"soap": 40, "shampoo": 150, "perfume": 500, "cream": 250, "lotion": 300, "lipstick": 350}
    },
    "2nd floor": {
        "category": "spices",
        "items": {"turmeric": 60, "chili powder": 80, "coriander powder": 70, "pepper": 90, "cumin": 110}
    },
    "1st floor": {
        "category": "toys",
        "items": {"car": 300, "doll": 250, "blocks": 450, "puzzle": 350, "teddy bear": 500, "remote car": 800}
    },
    "ground floor": {
        "category": "electronics",
        "items": {"mobile": 15000, "laptop": 50000, "headphones": 2000, "charger": 500, "smart watch": 4000}
    },
    "-1 floor": {
        "category": "parking",
        "items": {"bike parking": 50, "car parking": 100}
    }
}
cart = {}

while True:
    print("\navailable floors:")
    for floor, details in floors.items():
        print(f"{floor} - {details['category']}")

    floor_choice = input("\nenter floor (or 'exit' to finish): ").strip().lower()

    if floor_choice == "exit":
        break
    matched_floor = next((floor for floor in floors if floor.lower() == floor_choice), None)
    if matched_floor:
        category = floors[matched_floor]["category"]
        items = floors[matched_floor]["items"]
        print(f"\n{category} on {matched_floor}:")

        item_list = list(items.items())
        for i, (item, price) in enumerate(item_list, start=1):
            print(i, "-", item, price)
        try:
            index = int(input("enter product number: ")) - 1
            if 0 <= index < len(item_list):
                product, price = item_list[index]
                quantity = int(input(f"enter quantity for {product}: "))
                if quantity > 0:
                    if product in cart:
                        cart[product]["qty"] += quantity
                    else:
                        cart[product] = {"price": price, "qty": quantity}
                    print(f"{quantity} x {product} added to cart.")
                else:
                    print("invalid quantity. please enter a number greater than 0.")
            else:
                print("invalid choice.")
        except ValueError:
            print("enter a valid number.")
    else:
        print("invalid floor.")
if cart:
    subtotal = sum(item["price"] * item["qty"] for item in cart.values())
    discount = 0
    if subtotal > 5000:
        discount = subtotal * 0.10  # 10% discount
    elif subtotal > 2000:
        discount = subtotal * 0.05  # 5% discount
    gst = (subtotal - discount) * 0.18
    total = (subtotal - discount) + gst
    print("\n------ shopping cart ------")
    for item, details in cart.items():
        print(f"- {item}: {details['qty']} x {details['price']} = {details['qty'] * details['price']}")
    print(f"\nsubtotal: {subtotal:.2f}")
    print(f"discount: -{discount:.2f}")
    print(f"gst (18%): {gst:.2f}")
    print(f"total amount: {total:.2f}")
    print("\npayment methods: 1. cash  2. card  3. upi")
    payment_choice = input("select payment method: ")
    if payment_choice == "1":
        print("payment successful via cash.")
    elif payment_choice == "2":
        print("payment successful via card.")
    elif payment_choice == "3":
        print("payment successful via upi.")
    else:
        print("invalid payment method.")
    print("\n------ final bill ------")
    print("thank you for shopping at mr. alone supermarket!")
else:
    print("\ncart is empty.")