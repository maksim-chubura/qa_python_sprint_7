import random
import string
import time

def generate_random_courier_data():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    login = f"login_{random_string}_{int(time.time())}"
    password = f"pass_{random_string}"
    first_name = f"name_{random_string}"
    return login, password, first_name