import time 
def cash(total_cost):
    c = 0
    while True:
        print()
        payment = float(input("Enter the amount you are paying: "))
        if payment >= total_cost:
            print("Thank you for your purchase!")
            remaining = payment - total_cost
            print("Remaining Amount", remaining)
            c = 1
            generate_receipt(cart, menu_items, total_cost, payment, "Cash Payment")
            exit()
        else:
            print("Insufficient payment. Please pay the total amount.")
            switch = input("Enter 'yes' to switch to card payment, otherwise press any key to exit: ")
            if switch.lower() == 'yes':
                card(total_cost)
                return True
            else:
                return False

def card(total_cost):
    c = 0
    while True:
        print()
        card_number = input("Enter your card number: ")
        expiry_date = input("Enter card expiry date (MM/YY): ")
        cvv = input("Enter CVV: ")
        if len(card_number) == 16 and card_number.isdigit():
            parts = expiry_date.split('/')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                if len(cvv) == 3 and cvv.isdigit():
                    amount = float(input("Enter Your Card Amount "))
                    if total_cost < amount:
                        print("Processing payment...")
                        time.sleep(2)  # Add a delay of 2 seconds
                        print("Payment successful!")
                        print("Thank you for your purchase!")
                        print()
                        remaining = amount - total_cost
                        print("Remaining Balance ", remaining)
                        c = 1
                        exit()
                    else:
                        print("Insufficient Balance")
                        switch = input("Enter 'yes' to switch to cash payment, otherwise press any key to exit: ")
                        if switch.lower() == 'yes':
                            cash(total_cost)
                            return True
                        else:
                            return False

        else:
            print("Card Is Not Valid")
        if c == 1:
            break

def generate_receipt(cart, menu, total_cost, payment_method):
    print("\nReceipt:")
    print("Item\tQuantity\tPrice\tTotal")
    for item, quantity in cart.items():
        item_total_cost = quantity * menu[item]
        print(f"{item}:\t{quantity}\t\t{menu[item]}\t{item_total_cost}")  
    print("=====================================")
    print(f"Total cost = {total_cost}")
    print(f"Payment method: {payment_method}")

def buy(cart, menu):
    total_cost = 0
    print("\nItem\tQuantity\tPrice\tTotal")
    for item, quantity in cart.items():
        item_total_cost = quantity * menu[item]
        total_cost += item_total_cost
        print(f"{item}:\t{quantity}\t\t{menu[item]}\t{item_total_cost}")  
    print("=====================================")
    print(f"Total cost = {total_cost}")

    while True:
        choice = input("Enter 'add' to add more items, 'remove' to remove an item, 'card' to pay by card, or 'cash' to pay by cash: ")    
        if choice.lower() == 'card':
            card(total_cost)
            generate_receipt(cart, menu, total_cost, "Card Payment")
            break
        elif choice.lower() == 'cash':
            cash(total_cost)
            generate_receipt(cart, menu, total_cost, "Cash Payment")
            break            
        elif choice.lower() == 'add':
            display_menu(menu)
            item_input = input("Enter item name with quantity to add (e.g., 'Apples 2'): ").split()
            if len(item_input) != 2 or not item_input[1].isdigit():
                print("Invalid input. Please enter item name and quantity separated by space.")
                continue

            item_name = item_input[0].capitalize()
            quantity = int(item_input[1])
            if item_name not in menu:
                print("Item not found in menu. Please choose from the available items.")
                continue

            if item_name in cart:
                cart[item_name] += quantity
            else:
                cart[item_name] = quantity
            print(f"{quantity} {item_name}(s) added to cart.")
            print()
            print("Items in your cart:")
            
            total_cost = 0  # Reset total cost
            for item, quantity in cart.items():
                item_total_cost = quantity * menu[item]
                total_cost += item_total_cost
                print(f"{item}:\t{quantity}\t\t{menu[item]}\t{item_total_cost}")  
            print("=====================================")
            print(f"Total cost = {total_cost}")
            
        elif choice.lower() == 'remove':
            item_name = input("Enter the name of the item you want to remove: ").capitalize()
            if item_name in cart:
                removed_quantity = cart.pop(item_name)  # Remove the item from the cart and get the removed quantity
                removed_cost = removed_quantity * menu[item_name]  # Calculate the cost of the removed item
                total_cost -= removed_cost  # Subtract the removed cost from the total cost
                print(f"{item_name} removed from cart.")
                print()
                print("Items in your cart:")
                for item, quantity in cart.items():
                    item_total_cost = quantity * menu[item]
                    total_cost += item_total_cost
                    print(f"{item}:\t{quantity}\t\t{menu[item]}\t{item_total_cost}")  
                print("=====================================")
                print(f"Total cost = {total_cost}")
            else:
                print("Item not found in cart.")
        else:
            print("Invalid choice. Please enter 'add', 'remove', 'card', or 'cash'.")
    
def display_menu(menu):
    print("Item\tAmount")
    for item, amount in menu.items():
        print(f"{item}: {amount}")

def main():
    menu_items = {
        "Apples": 50,
        "Banana": 50,
        "Orange": 20,
        "Maggie": 50,
        "Cold Drink": 80
    }

    print("Welcome to the Store")
    display_menu(menu_items)

    while True:
        cart = {}
        while True:
            item_input = input("Enter item name with quantity (e.g., 'Apples 2'): ").split()
            item_name = item_input[0].capitalize()
            if len(item_input) != 2 or not item_input[1].isdigit():
                print("Invalid input. Please enter item name and quantity separated by space.")
                continue

            quantity = int(item_input[1])
            if item_name not in menu_items:
                print("Item not found in menu. Please choose from the available items.")
                continue

            if item_name in cart:
                cart[item_name] += quantity
            else:
                cart[item_name] = quantity

            add_more = input("Enter 'y' to add more items, otherwise press any key to proceed: ")
            if add_more.lower() != 'y':
                break

        if buy(cart, menu_items):
            break
        else:
            print("Failed to complete purchase. Please try again.")

if __name__ == "__main__":
    main()
