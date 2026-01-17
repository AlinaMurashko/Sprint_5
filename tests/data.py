import random

def generate_random_email():
    names = ['alina', 'galina', 'polina', 'albina']
    surnames = ['murashko', 'murashkova', 'murashina']
    stream = '37'
    random_number = random.randint(100, 999)
    return f'{random.choice(names)}_{random.choice(surnames)}_{stream}_{random_number}@yandex.ru'


def get_test_password():
    return 'securePassword'
