from product import Product, NonStockedProduct, LimitedProduct
from store import Store


def get_user_input():
    """
    Prompts the user to choose a number between 1 and 4.

    Continuously asks for input until a valid integer within the specified range is entered.
    If the user enters a non-integer or a number outside the range, an error message is displayed,
    and the user is prompted again.

    Returns:
        int: The user's choice, an integer between 1 and 4.
    """
    while True:
        try:
            user_input = int(input("Please choose a number between 1 and 4: "))
            if 1 <= user_input <= 4:
                return user_input
            else:
                print("Invalid choice! Enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def list_all_products(store_list):
    """
    Lists all active products in the store.

    This function retrieves all active products from the provided store object and prints them.
    Each product is displayed with an index number for reference. The function uses the `get_all_products`
    method from the store object to fetch the active products and then iterates over them to display their details.

    Args:
        store_list (Store): An instance of the Store class that contains a list of products.
    """
    products = store_list.get_all_products()
    for  product in products:
        print(product.show())


def show_total_amount(store):
    """
    Displays the total quantity of items available in the store.

    This function retrieves the total quantity of all products currently in the store
    using the `get_total_quantity` method of the store object. It then prints the result
    in a formatted message.

    Args:
        store (Store): The store object containing the list of products.

    Returns:
        None: This function doesn't return a value; it only prints the total quantity.
    """
    print(f"Total of {store.get_total_quantity()} items in store")


def menu_handler(choice, store):
    """
    Handles the user's menu choice and calls the corresponding function.

    This function retrieves the appropriate action based on the user's input (choice).
    It then executes the corresponding function (e.g., listing products, showing total amount, or making an order).
    If the user's choice is invalid, an error message is displayed.

    Args:
        choice (int): The user's menu selection, which determines the action to be performed.
        store (Store): The store object that holds the products and processes actions such as making an order.

    Returns:
        None: This function doesn't return any value; it simply executes the selected action or displays an error message.
    """
    action = menu_actions.get(choice)  # Retrieve the function associated with the user's choice

    if action:
        action(store)  # Call the corresponding action with the store object as an argument
    else:
        print("Invalid choice. Please try again.")  # Display an error message for invalid choices


def choose_product(list_of_products):
    """
    Prompts the user to choose a product from a list.

    The function continuously asks the user to select a product by number from the list of available products.
    If the user enters a valid product number (between 1 and the length of the list), it returns the selected product.
    If the input is invalid, the function will prompt the user again with an error message.
    If the user wants to finish the order, they can enter an empty string.

    Args:
        list_of_products (List[Product]): A list of available products to choose from.

    Returns:
        Product or None: The selected product, or None if the user decides to finish the order by entering an empty string.
    """
    while True:

        print("\nWhen you want to finish the order, enter an empty text.")

        product_num = input("Which product # do you want to choose? ")

        if product_num == "":
            return None  # User chooses to finish the order

        try:
            product_num = int(product_num)
            if 1 <= product_num <= len(list_of_products):
                return list_of_products[product_num - 1]  # Return the selected product
            else:
                print("Error: Please enter a number between 1 and", len(list_of_products))
        except ValueError:
            print("Error: Invalid input. Please enter a valid product number.")


def get_amount(amount):
    """
    Prompts the user to input the quantity of a product they want to buy.

    This function asks the user to input a number (integer) for the quantity of a product they wish to purchase.
    It checks if the entered amount is valid (i.e., a non-negative integer that does not exceed the available stock).
    If the input is invalid or exceeds the available stock, an error message is displayed, and the user is prompted again.

    Args:
        amount (int): The available stock quantity for the product.

    Returns:
        int: The valid quantity of the product that the user wants to purchase.
             It will be a value between 1 and the available stock (inclusive).
    """
    while True:
        try:
            product_amount = int(input(f"What amount do you want? (Available: {amount}): "))
            if 0 < product_amount <= amount:
                return product_amount
            else:
                print(f"Please enter a valid quantity (1 - {amount}).")
        except ValueError:
            print("Invalid input! Please enter a number.")


def make_an_order(store):
    """
    Facilitates the process of making an order in the store.

    This function allows the user to choose products from the store and specify the quantity they want to purchase.
    The user can add multiple products to the order and the total payment will be calculated.
    The process continues until the user decides to stop ordering.

    The function does the following:
    1. Displays the list of available products.
    2. Prompts the user to select a product and specify the quantity.
    3. Adds the selected product to the order if enough quantity is available.
    4. Continues the order process until the user opts to stop.
    5. Displays the total payment for the order.

    Args:
        store (Store): The store instance from which products are ordered.

    Returns:
        None: The function prints the order summary (total payment) or a message indicating no products were ordered.
    """
    list_all_products(store)  # Show available products
    print("----------")
    total_payment = 0.0

    while True:
        product = choose_product(store.get_all_products())  # Let the user select a product
        if product is None:
            print("No valid product selected. Exiting order process.")
            break  # Exit if no valid product is selected

        # Get the amount the user wants to buy
        amount = get_amount(product.quantity)
        if amount == 0:
            print("Amount can't be zero. Please select a valid amount.")
            continue  # Ask for input again if amount is zero

        # Add to the total payment
        try:
            total_payment += store.order([(product, amount)])  # Attempt the order
        except Exception as e:
            print(f"An error occurred while processing your order: {e}")
            continue  # If there's an error, ask again

    # Final statement after order completion
    if total_payment > 0:
        print(f"Order complete! Total payment: ${total_payment:.2f}")
    else:
        print("No products ordered. Thank you!")


def start(store):
    """
    Displays the store menu and handles user input to perform actions.

    This function runs a loop where it displays a menu with options to the user:
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit

    The function repeatedly prompts the user to select an option until they choose to quit.
    It processes the user's choice by calling the appropriate handler function for each option.
    When the user selects 'Quit', the function exits the loop and terminates the program.

    Args:
        store (Store): The store object that contains the list of products and supports various actions.

    Returns:
        None: This function does not return a value; it simply controls the flow of the program.
    """
    user_input = 0
    while user_input != 4:
        print("""
            Store Menu
            ----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit\n
        """)
        user_input = get_user_input()  # Assuming get_user_input() returns the user's choice
        print("----------")

        if user_input == 4:
            print("Exiting the store. Goodbye!")
            return  # Exit the start function and stop the loop

        menu_handler(user_input, store)  # Process the selected option
        print("----------")


menu_actions = {
    1: list_all_products,
    2: show_total_amount,
    3: make_an_order,
}


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
