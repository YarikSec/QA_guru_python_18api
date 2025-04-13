from selene import browser, have

URL_WEB = 'https://demowebshop.tricentis.com/'

def set_cookie_and_open_cart(cookies):
    browser.open(URL_WEB + 'cart')
    browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookies})
    browser.open(URL_WEB + 'cart')

def cart_should_product(product):
    browser.element('.cart-item-row').should(have.text(product))

def cart_should_multiple_products(product_1, product_2):
    browser.all('.cart-item-row').first.should(have.text(product_1))
    browser.all('.cart-item-row').second.should(have.text(product_2))

def cart_should_be_empty():
    browser.element('.page-body').should(have.text('Your Shopping Cart is empty!'))

def cart_should_product_with_quantity(product, quantity):
    browser.element('.cart-item-row').should(have.text(product))
    browser.element('.qty-input').should(have.value(str(quantity)))