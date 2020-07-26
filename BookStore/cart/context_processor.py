from .cart import Cart

def cart(requuest):
    return {'cart': Cart(requuest)}