# The solution was written with python 3.13.0

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigating to saucedemo website and logging in
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
username_input = driver.find_element(By.CSS_SELECTOR, 'input[data-test="username"]')
password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-test="password"]')
login_button = driver.find_element(By.CSS_SELECTOR, 'input[data-test="login-button"]')
username_input.clear()
username_input.send_keys("standard_user")
password_input.clear()
password_input.send_keys("secret_sauce")
login_button.click()

# Adding the third item to the cart and clicking checkout
bolt_tshirt_add_to_cart_button = driver.find_element(
    By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'
)
bolt_tshirt_add_to_cart_button.click()
shopping_cart = driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
shopping_cart.click()
checkout_button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="checkout"]')
checkout_button.click()

# Entering details to complete checkout
fake = Faker()
fake_first_name = fake.first_name()
fake_last_name = fake.last_name()
fake_postal_code = fake.postalcode()
first_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-test="firstName"]')
first_name_input.clear()
first_name_input.send_keys(fake_first_name)
last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-test="lastName"]')
last_name_input.clear()
last_name_input.send_keys(fake_last_name)
postal_code_input = driver.find_element(By.CSS_SELECTOR, 'input[data-test="postalCode"]')
postal_code_input.clear()
postal_code_input.send_keys(fake_postal_code)
continue_button = driver.find_element(By.CSS_SELECTOR, 'input[data-test="continue"]')
continue_button.click()
finish_button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="finish"]')
finish_button.click()

# Asserting that the order was completed successfully
complete_header = driver.find_element(By.CSS_SELECTOR, '[data-test="complete-header"]')
assert complete_header.is_displayed()
assert "Thank you for your order!" == complete_header.text
complete_text = driver.find_element(By.CSS_SELECTOR, '[data-test="complete-text"]')
assert complete_text.is_displayed()
assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" == complete_text.text
driver.close()
driver.quit()
