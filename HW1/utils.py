import requests
import random
import string
from faker import Faker
import csv


def read_requirements():
    file = open('requirements.txt')
    return file.read()


def generate_emails_and_names(count=100):
    fake = Faker()
    random_users = ''
    for _ in range(count):
        user_name = fake.name().split()[0]
        letters = string.ascii_lowercase
        random_word = ''.join(random.choice(letters) for _ in range(random.randint(5, 7)))
        random_users += f'{user_name}: {random_word + str(random.randint(0, 1000)) + "@mail.com"}; '
    return random_users


def read_and_count_file():
    height_inches_list = []
    weight_pounds_list = []
    with open('hw (2) (1).csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            height_inches_list.append((float(row[' "Height(Inches)"'])))
            weight_pounds_list.append(float(row[' "Weight(Pounds)"']))

    average_height_cm = round((sum(height_inches_list) / len(height_inches_list) * 2.54), 2)
    average_weight_kg = round((sum(weight_pounds_list) / len(weight_pounds_list) * 0.45359), 2)
    final_data = f'AVERAGE HEIGHT: {str(average_height_cm)} cm, AVERAGE WEIGHT: {str(average_weight_kg)} kg'
    return final_data


def count_spacemen():
    r = requests.get("http://api.open-notify.org/astros.json")
    return str(r.json()["number"])