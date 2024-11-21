class Product:

    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method.
        Creates the instance variables. Sets `active` to True by default.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (float): The quantity in stock.

        Raises:
            ValueError: If the name is empty or if price or quantity are negative.
        """

        # Validation checks
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        # Setting instance variables
        self.name = str(name) # Store name as a str
        self.price = float(price) # Store price as a float
        self.quantity = int(quantity) # Store quantity as an int
        self.active = True  # Default attribute


    def __str__(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"


    def get_quantity(self) -> float:
        """
        Getter function for quantity.

        Returns:
            float: The quantity of the product.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Setter function for quantity.

        Args:
            quantity (float): The new quantity to set.

        Raises:
            ValueError: If the quantity is negative.

        Deactivates the product if quantity reaches 0.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = float(quantity)

        # Deactivate product if quantity is 0
        if self.quantity == 0:
            self.active = False
            print(f"Product '{self.name}' is now inactive due to zero quantity.\n")
        else:
            self.active = True
            print(f"Quantity updated to {self.quantity}\n")


    def is_active(self) -> bool:
        """
        Getter function for active status.

        Returns:
            bool: True if the product is active, otherwise False.
        """
        return self.active


    def activate(self):
        """
        Activates the product by setting the `active` status to True.
        """
        if not self.active:
            self.active = True
            print(f"Product '{self.name}' has been deactivated.\n")
        else:
            print(f"Product '{self.name}' is already inactive.\n")


    def deactivate(self):
        """
        Activates the product by setting the `active` status to True.
        """
        if self.active:
            self.active = False
            print(f"Product '{self.name}' has been reactivated.\n")
        else:
            print(f"Product '{self.name}' is already active.\n")


    def show(self) -> str:
        """
         Returns a string representation of the product.

         Returns:
             str: A string representing the product, including its name, price, and quantity.
         """
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}'


    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Updates the quantity of the product and returns the total price of the purchase.

        Args:
            quantity (float): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            Exception: If the quantity is greater than the available stock or if the product is inactive.
        """
        if not self.active:
            raise Exception(f"The product '{self.name}' is not available for purchase because it is inactive.")

        if quantity <= 0:
            raise Exception("Quantity must be greater than zero.")

        if quantity > self.quantity:
            raise Exception(f"Insufficient stock. Only {self.quantity} units are available.")

        if self.quantity >= quantity:
            self.quantity -= quantity
            total_price = self.price * quantity
            print(f"Successfully purchased {quantity} of {self.name}.")
            print(f"Remaining quantity: {self.quantity}")
            # Deactivate the product if quantity reaches 0
            if self.quantity == 0:
                self.deactivate()
            print(f"Total price: ${float(total_price)}\n")
            return float(total_price)
        else:
            print(f"Insufficient quantity of {self.name} in stock.\n")


