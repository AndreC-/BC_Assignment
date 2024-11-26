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

# Adding third item to cart and clicking checkout
driver.find_element(
    By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'
).click()
driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
driver.find_element(By.CSS_SELECTOR, 'button[data-test="checkout"]').click()

# Entering details to complete checkout
fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.postalcode()
driver.find_element(By.CSS_SELECTOR, 'input[data-test="firstName"]').send_keys(first_name)
driver.find_element(By.CSS_SELECTOR, 'input[data-test="lastName"]').send_keys(last_name)
driver.find_element(By.CSS_SELECTOR, 'input[data-test="postalCode"]').send_keys(postal_code)
driver.find_element(By.CSS_SELECTOR, 'input[data-test="continue"]').click()
driver.find_element(By.CSS_SELECTOR, 'button[data-test="finish"]').click()

# Asserting that the order was completed successfully
complete_header = driver.find_element(By.CSS_SELECTOR, '[data-test="complete-header"]')
assert complete_header.is_displayed()
assert "Thank you for your order!" == complete_header.text
complete_text = driver.find_element(By.CSS_SELECTOR, '[data-test="complete-text"]')
assert complete_text.is_displayed()
assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" == complete_text.text
driver.close()
driver.quit()
