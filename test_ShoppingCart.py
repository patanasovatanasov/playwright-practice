from shopping_cart import ShoppingCart

def test_empty_cart():
    cart1 = ShoppingCart()
    assert cart1.total() == 0

def test_add_item():
    cart2 = ShoppingCart()
    cart2.add("tomato", 2)
    cart2.add("cheese", 3.5)
    assert cart2.total() == 5.5

def test_remove_item():
    cart3 = ShoppingCart()
    cart3.add("tomato", 2)
    cart3.add("cheese", 3)
    cart3.add("sausage", 4)
    assert cart3.total() == 9
    cart3.remove("tomato")
    assert cart3.total() == 7

