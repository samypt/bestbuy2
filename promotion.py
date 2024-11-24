from abc import ABC, abstractmethod
# from product import Product

class Promotion(ABC):
    """
    Abstract base class for promotions.

    Attributes:
        name (str): The name of the promotion.
    """

    def __init__(self, name):
        """
        Initialize a Promotion instance.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Abstract method to calculate the total price after applying the promotion.

        Args:
            product (Product): A product instance.
            quantity (int): The number of items purchased.

        Returns:
            float: The total price after the promotion is applied.
        """
        pass

    def __str__(self):
        """
        Return a string representation of the promotion.

        Returns:
            str: The name of the promotion.
        """
        return f"{self.name}"


class SecondHalfPrice(Promotion):
    """
    Promotion that applies a 'Second Half Price' discount, where every second item in a pair is half price.
    """

    def apply_promotion(self, product, quantity):
        """
        Calculate the total cost with a 'Second Half Price' promotion.

        Args:
            product (Product): A product instance.
            quantity (int): The number of items purchased.

        Returns:
            float: The total cost after applying the promotion.
        """
        # Pair items into groups of two
        full_price_items = quantity // 2  # Number of full-price items in pairs
        half_price_items = full_price_items  # Number of half-price items in pairs
        leftover_items = quantity % 2  # Remaining items not in pairs

        # Calculate total cost
        total_cost = (full_price_items * product.price) + \
                     (half_price_items * product.price * 0.5) + \
                     (leftover_items * product.price)

        return total_cost


class ThirdOneFree(Promotion):
    """
    Promotion where every third item is free.
    """

    def apply_promotion(self, product, quantity):
        """
        Calculate the total cost with a 'Third One Free' promotion.

        Args:
            product (Product): A product instance.
            quantity (int): The total number of items purchased.

        Returns:
            float: The total cost after applying the promotion.
        """
        # Number of free items (every third item is free)
        free_items = quantity // 3

        # Total cost
        total_cost = (quantity - free_items) * product.price

        return total_cost


class PercentDiscount(Promotion):
    """
    Promotion that applies a percentage discount to the product price.

    Attributes:
        percent (float): The percentage discount to apply.
    """

    def __init__(self, member, percent=0):
        """
        Initialize a PercentDiscount instance.

        Args:
            member (str): The name of the promotion or membership type.
            percent (float): The percentage discount. Must be between 0 and 100.

        Raises:
            ValueError: If the percentage is not within the range 0 to 100.
        """
        super().__init__(member)
        if percent < 0 or percent > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Calculate the discounted price based on a percentage discount.

        Args:
            product (Product): A product instance.
            quantity (int): The total number of items purchased.

        Returns:
            float: The price after the discount.
        """
        discount_amount = (self.percent / 100) * product.price
        final_price = (product.price - discount_amount) * quantity

        return final_price
