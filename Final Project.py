#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Admin functionalities

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        # Generate FoodID automatically
        food_item.food_id = len(self.food_items) + 1
        self.food_items.append(food_item)
        print("Food item added successfully.")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item edited successfully.")
                return
        print("Food item not found.")

    def view_all_food_items(self):
        for food_item in self.food_items:
            print(f"FoodID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print(f"Stock: {food_item.stock}")
            print()

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully.")
                return
        print("Food item not found.")

# User functionalities

class User:
    def __init__(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_new_order(self, food_items):
        selected_items = []
        for food_id in food_items:
            for food_item in admin.food_items:
                if food_item.food_id == food_id:
                    selected_items.append(food_item)
                    break
        if len(selected_items) == 0:
            print("No items selected.")
            return
        self.orders.append(selected_items)
        print("Order placed successfully.")

    def view_order_history(self):
        if len(self.orders) == 0:
            print("No order history found.")
            return
        for order in self.orders:
            print("Order:")
            for food_item in order:
                print(f"- {food_item.name}")
            print()

    def update_profile(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        print("Profile updated successfully.")

# Admin actions
admin = Admin()
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
admin.add_food_item("Vegan Burger", "1 piece", 320, 0, 5)
admin.add_food_item("Truffle Cake", "500gm", 900, 0, 2)

# User actions
user = User("John Doe", "1234567890", "john@example.com", "123 Street, City", "password")
user.place_new_order([2, 3])  # Selects Vegan Burger and Truffle Cake
user.view_order_history()

user.update_profile("John Smith", "9876543210", "john.smith@example.com", "456 Avenue, City", "newpassword")

