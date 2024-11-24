from product import Product
from typing import List, Tuple


class Store:


    def __init__(self, products):
        """
        Initializes a new Store instance and adds products to it.

        The constructor accepts a product or a list of products to be added to
        the store upon instantiation. It uses the `add_product` method to handle
        both individual products and lists of products.

        Args:
            products (Product or list): A single Product instance or a list of Product instances
                                        to be added to the store.

        Note:
            The method calls the `add_product` method to ensure proper validation of
            the product(s) being added. If a list is passed, the method verifies
            that all elements are instances of the `Product` class.
        """
        self.products = []
        self.add_product(products)


    def add_product(self, product):
        """
        Adds a product or a list of products to the store.

        If a single Product instance is provided, it is added to the products list.
        If a list of products is provided, the method checks if all elements in the
        list are instances of the Product class. If so, all products are added to
        the products list. If the list contains non-Product elements, a ValueError
        is raised.

        Args:
            product (Product or list): A single Product instance or a list of Product instances to add to the store.

        Raises:
            ValueError: If a list is provided, and it contains any element that is not an instance of Product.
        """
        if isinstance(product, Product):
            self.products.append(product)
        elif isinstance(product, list) and all(isinstance(item, Product) for item in product):
            self.products.extend(product)
        else:
            raise ValueError("Argument must be a Product instance or a list of Product instances.")


    def remove_product(self, product):
        """
        Removes a product from the store.

        This method removes the specified product from the store's product list.
        If the provided product is not an instance of the `Product` class, a
        `ValueError` is raised.

        Args:
            product (Product): The product to be removed from the store. It must be an instance
                                of the `Product` class.

        Raises:
            ValueError: If the provided product is not an instance of the `Product` class.
        """
        if isinstance(product, Product):
            self.products.remove(product)
        else:
            raise ValueError("The product must be an instance of the Product class.")


    def get_total_quantity(self):
        """
        Calculates the total quantity of all products in the store.

        This method sums up the `quantity` attribute of all products in the
        `self.products` list. If a product does not have a `quantity` attribute,
        it is treated as having a quantity of 0.

        Returns:
            float: The total quantity of all products in the store.
        """
        return sum(getattr(product, 'quantity', 0) for product in self.products if product.quantity != float('inf'))


    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all active products in the store.

        This method filters the `self.products` list and returns only those
        products whose `active` attribute is set to `True`. If a product
        is inactive (i.e., `active` is `False`), it will not be included
        in the returned list.

        Returns:
        List[Product]: A list of active Product instances.
        """
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order for multiple products and calculates the total cost.

        This method takes a list of tuples where each tuple contains a `Product`
        instance and an integer quantity. It iterates through the list, calling
        the `buy` method on each product with the specified quantity, and accumulates
        the total cost of the order.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples, each containing
                a `Product` instance and a quantity (int) to purchase.
        Returns:
            float: The total price for all products in the shopping list.
        """
        total_ordering = 0.0
        if all(isinstance(item, tuple) for item in shopping_list):
            for item in shopping_list:
                product, quantity = item
                total_ordering += product.buy(quantity)
        return total_ordering


    def __contains__(self, item):
        """
        Check if an item exists in the collection of products.

        This method is called when using the 'in' keyword to test membership.

        Args:
            item: The item to check for in the collection.

        Returns:
            bool: True if the item is in the collection of products, False otherwise.
        """
        return item in self.products


    def __add__(self, other):
        """
        Combine the products from two stores into a new store.

        Args:
            other (Store): Another store whose products will be added.

        Returns:
            Store: A new store containing products from both stores.
        """
        # Combine the products from both stores
        combined_products = self.products + other.products

        # Create a new store with the combined products
        return Store(combined_products)


    def __str__(self):
        """
        Return a string representation of the store's products.

        If the store has products, their names are joined into a comma-separated string.
        If the store has no products, "None" is returned.

        Returns:
            str: A comma-separated string of product names if products exist,
                 otherwise "None".
        """
        products_str = None if not self.products else ', '.join((str(product.name) for product in self.products))
        return products_str

