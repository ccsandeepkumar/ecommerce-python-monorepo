import pytest
import time
from services.cart.service import add_item
from services.checkout.service import checkout
from services.order.service import create_order

@pytest.mark.e2e
def test_e2e():
    cart = add_item([], 'apple')
    assert checkout(cart)
    assert create_order(cart)['status'] == 'CREATED'
