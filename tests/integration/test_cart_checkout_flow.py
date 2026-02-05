import pytest
from services.cart.service import add_item
from services.checkout.service import checkout

@pytest.mark.integration
def test_flow():
    cart = add_item([], 'apple')
    assert checkout(cart)
