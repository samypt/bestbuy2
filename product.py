from typing import Optional

from  promotion import  Promotion


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
        self._price = float(price) # Store price as a float
        self.quantity = float(quantity) # Store quantity as an int
        self.active = True  # Default attribute
        self._promotions = []  # Initialize promotions as an empty list


    @property
    def price(self):
        """
        Getter method for the price.
        """
        return self._price  # Access the private attribute


    @price.setter
    def price(self, new_price):
        """
        Setter method for the price. Ensures the price is non-negative.

        Args:
            new_price (float): The new price to set.

        Raises:
            ValueError: If the new price is less than 0.
        """
        if new_price < 0:
            raise ValueError("Price cannot be lower than 0")
        self._price = new_price  # Modify the private attribute


    @property
    def promotion(self):
        # Getter method for promotion
        return self._promotions


    @promotion.setter
    def promotion(self, promotion):
        # Setter method for promotion
        if not isinstance(promotion, Promotion):
            raise ValueError("Promotion must be an instance of a Promotion class.")
        self._promotions.append(promotion)


    def set_promotion(self, promotion):
        if not isinstance(promotion, Promotion):
            raise ValueError("Promotion must be an instance of a Promotion class.")
        self._promotions.append(promotion)


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


    def __gt__(self, other):
        print(self._price, 'first')
        # print(other.price(), 'second')
        return self._price > other.price


    def __str__(self) -> str:
        """
        Returns a string representation of the product, including its name, price, quantity, and promotions.

        Returns:
            str: A string representing the product.
        """
        promotion_str = "No Promotion" if not self._promotions else ', '.join(str(promo) for promo in self._promotions)

        return f'{self.name}, Price: ${self._price}, Quantity: {self.quantity}, Promotion: {promotion_str}'


    def buy(self, quantity) -> Optional[float]:
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
            if not self._promotions:
                total_price = self._price * quantity
                print(f"Successfully purchased {quantity} of {self.name}.")
                print(f"Remaining quantity: {self.quantity}")
            else: # add all the promotions
                total_price = self._price * quantity
                total_discount = 0
                for promotion in self._promotions:
                    discounted_price = promotion.apply_promotion(self, quantity)
                    discount = total_price - discounted_price
                    total_discount += discount
                    total_price = discounted_price
                promotion_str = "No Promotion" if not self._promotions else ', '.join(
                    str(promo) for promo in self._promotions)
                print(f"Promotion: {promotion_str} applied")
                print(f"Successfully purchased {quantity} of {self.name}.")
                print(f"Remaining quantity: {self.quantity}")
            # Deactivate the product if quantity reaches 0
            if self.quantity == 0:
                self.deactivate()
            print(f"Total price: ${float(total_price)}\n")
            return float(total_price)
        else:
            print(f"Insufficient quantity of {self.name} in stock.\n")




class NonStockedProduct(Product):

    def __init__(self, name, price):
        super().__init__(name, price, quantity=float('inf'))


    def show(self) -> str:
        """
        Returns a string representation of the product, including its name, price, and promotions.

        Returns:
            str: A string representing the product, including promotions if applicable.
        """
        promotion_str = "No Promotion" if not self._promotions else ', '.join(str(promo) for promo in self._promotions)

        return f'{self.name}, Price: ${self._price}, Promotion: {promotion_str}'




class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum cannot be negative.")
        self.maximum = int(maximum)  # Store maximum as an int


    def show(self) -> str:
        """
        Returns a string representation of the product, including its name, price, quantity, maximum, and promotions.

        Returns:
            str: A string representing the product, including promotions if applicable.
        """
        promotion_str = "No Promotion" if not self._promotions else ', '.join(str(promo) for promo in self._promotions)

        return (f'{self.name}, Price: ${self._price}, Quantity: {self.quantity}, Maximum: {self.maximum},'
                f' Promotion: {promotion_str}')

    def buy(self, quantity) -> Optional[float]:
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

        if quantity > self.maximum:
            raise Exception(f"The maximum amount you can buy is {self.maximum}.")

        if quantity > self.quantity:
            raise Exception(f"Insufficient stock. Only {self.quantity} units are available.")

        if self.quantity >= quantity:
            self.quantity -= quantity
            if not self._promotions:
                total_price = self._price * quantity
                print(f"Successfully purchased {quantity} of {self.name}.")
                print(f"Remaining quantity: {self.quantity}")
            else: # add all the promotions
                total_price = self._price * quantity
                total_discount = 0
                for promotion in self._promotions:
                    discounted_price = promotion.apply_promotion(self, quantity)
                    discount = total_price - discounted_price
                    total_discount += discount
                    total_price = discounted_price
                promotion_str = "No Promotion" if not self._promotions else ', '.join(
                    str(promo) for promo in self._promotions)
                print(f"Promotion: {promotion_str} applied")
                print(f"Successfully purchased {quantity} of {self.name}.")
                print(f"Remaining quantity: {self.quantity}")
            # Deactivate the product if quantity reaches 0
            if self.quantity == 0:
                self.deactivate()
            print(f"Total price: ${float(total_price)}\n")
            return float(total_price)
        else:
            print(f"Insufficient quantity of {self.name} in stock.\n")