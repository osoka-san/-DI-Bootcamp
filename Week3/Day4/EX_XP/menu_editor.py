from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("Choose an option:")
    print("V: View an Item")
    print("A: Add an Item")
    print("D: Delete an Item")
    print("U: Update an Item")
    print("S: Show the Menu")
    print("E: Exit")

def add_item_to_menu():
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))
    item = MenuItem(name, price)
    item.save()
    print(f"Item '{name}' was added successfully.")

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuItem(name, 0)
    item.delete()
    print(f"Item '{name}' was deleted successfully.")

def update_item_from_menu():
    old_name = input("Enter the current name of the item: ")
    new_name = input("Enter the new name of the item: ")
    new_price = int(input("Enter the new price of the item: "))
    item = MenuItem(old_name, 0)
    item.update(new_name, new_price)
    print(f"Item '{old_name}' was updated successfully.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    for item in items:
        print(f"ID: {item[0]} | Name: {item[1]} | Price: {item[2]}")

if __name__ == "__main__":
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'V':
            name = input("Enter the name of the item: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"ID: {item[0]} | Name: {item[1]} | Price: {item[2]}")
            else:
                print("Item not found.")
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            show_restaurant_menu()
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")