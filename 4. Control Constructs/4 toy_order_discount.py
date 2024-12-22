# Program to Calculate Net Amount for Toy Orders with Discounts

# function definition
def calculate_discount(product_code, order_amount):
    if product_code == 1:  # battery Based Toys
        if order_amount > 1000:
            return order_amount * 0.9  # 10% discount
        else:
            return order_amount
    elif product_code == 2:  # key-based Toys
        if order_amount > 100:
            return order_amount * 0.95  # 5% discount
        else:
            return order_amount
    elif product_code == 3:  # electrical Charging Based Toys
        if order_amount > 500:
            return order_amount * 0.9  # 10% discount
        else:
            return order_amount
    else:
        return "Invalid product code"


# taking inputs from product code(product type) and order amount
product_code = int(
    input(
        "Enter the product code (1 for Battery, 2 for Key-based, 3 for Electrical Charging): "
    )
)
order_amount = float(input("Enter the order amount: "))

net_amount = calculate_discount(product_code, order_amount)  # function call
print(f"The net amount to be paid is: Rs. {net_amount}")
