starter_items = {"Starter 1": 100, "Starter 2": 200}
menu_items = {"Menu 1": 100, "Menu 2": 200}
drinks_items = {"Drink 1": 100, "Drink 2": 200}
dessert_items = {"Dessert 1": 100, "Dessert 2": 200}

cart = {}


def display_items(category_name, items):
    """Displays the items in a particular category."""
    print(f"\n--- {category_name} ---")
    counter = 1
    for item, price in items.items():
        print(f"{counter}. {item} - ₹{price}")
        counter += 1


def add_to_cart(category_name, items):
    """Allows the user to add items to the cart."""
    while True:
        display_items(category_name, items)
        choice = int(input("Enter the item number to add to cart: "))
        selected_item = list(items.keys())[choice - 1]
        selected_price = items[selected_item]

        if selected_item in cart:
            cart[selected_item][0] += 1
        else:
            cart[selected_item] = [1, selected_price]

        print(f"{selected_item} added to cart.")
        if input(f"Do you want to exit {category_name}? (yes/no): ").lower() == "yes":
            break


def generate_bill():
    """Generates and displays the bill for the items in the cart."""
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n--- Bill ---")
    total = 0
    for item, (quantity, price) in cart.items():
        item_total = quantity * price
        total += item_total
        print(f"{item} - {quantity} x ₹{price} = ₹{item_total}")

    print(f"\nTotal items: {len(cart)}")
    print(f"Total amount: ₹{total}")


def main():
    """Main function to control the flow of the program."""
    while True:
        choice = int(
            input("""
  Choose what you want:
  Press 1 for Starter
  Press 2 for Menu
  Press 3 for Drinks
  Press 4 for Dessert
  Press 5 to Bill and Exit
  """)
        )

        if choice == 1:
            add_to_cart("Starter", starter_items)
        elif choice == 2:
            add_to_cart("Menu", menu_items)
        elif choice == 3:
            add_to_cart("Drinks", drinks_items)
        elif choice == 4:
            add_to_cart("Dessert", dessert_items)
        elif choice == 5:
            generate_bill()
            print("Thank you for your order!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
