import pytest
from product import Product


@pytest.fixture
def product():
    return Product("MacBook", price=1450, quantity=100)


def test_init_product(product):
    assert product.name == "MacBook"
    assert product.price == 1450
    assert product.quantity == 100


def test_create_product_invalid_name(product):
    with pytest.raises(ValueError, match="Name cannot be empty."):
        Product("", price=1450, quantity=100)


def test_create_product_invalid_price(product):
    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook", price=-1450, quantity=100)


def test_create_product_invalid_quantity(product):
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("MacBook", price=1450, quantity=-100)


def test_product_becomes_inactive(product):
    product.buy(product.quantity)
    assert product.is_active() == False


def test_buy_modifies_quantity(product):
    product.buy(product.quantity)
    assert  product.quantity == 0


def test_buy_too_much(product):
    with pytest.raises(Exception, match=f"Insufficient stock. Only {product.quantity} units are available.") :
        product.buy((product.quantity + 1))



# product = Product("MacBook", price=1450, quantity=100)
#
# print(product)
#
# print(product.is_active())