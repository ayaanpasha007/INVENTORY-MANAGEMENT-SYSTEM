# Inventory Management System

inventory = {}

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    qty = int(input("Enter quantity: "))
    inventory[name] = {"price": price, "qty": qty}
    print("Product added successfully!")

def remove_product():
    name = input("Enter product name to remove: ")
    if name in inventory:
        del inventory[name]
        print("Product removed!")
    else:
        print("Product not found.")

def search_product():
    name = input("Enter product name to search: ")
    if name in inventory:
        print(name, inventory[name])
    else:
        print("Product not found.")

def update_stock():
    name = input("Enter product name: ")
    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name]["qty"] = qty
        print("Stock updated!")
    else:
        print("Product not found.")

def view_inventory():
    if not inventory:
        print("Inventory empty")
    else:
        for name, details in inventory.items():
            print(name, details)

def total_value():
    total = 0
    for details in inventory.values():
        total += details["price"] * details["qty"]
    print("Total Inventory Value:", total)

while True:
    print("\n--- Inventory Management System ---")
    print("1.Add Product")
    print("2.Remove Product")
    print("3.Search Product")
    print("4.Update Stock")
    print("5.View Inventory")
    print("6.Total Inventory Value")
    print("7.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_stock()
    elif choice == "5":
        view_inventory()
    elif choice == "6":
        total_value()
    elif choice == "7":
        break
    else:
        print("Invalid choice")
