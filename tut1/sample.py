import json
import random
import time
from datetime import datetime
from tut1.dice import roll_dice
import requests


def add(a, b):
    return a + b


def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be less than zero")


def save_dict(_dict, filepath):
    json.dump(_dict, open(filepath, 'w'))
    print("saved")


class Student:

    def __init__(self, name, dob, branch, credits):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = credits

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def add_credits(self, value):
        self.credits += value

    def get_credits(self):
        return self.credits


def is_eligible_for_degree(student):
    return student.get_credits() >= 20


class Engineer:
    def __init__(self, name, dob, role, experience):
        self.name = name
        self.dob = dob
        self. role = role
        self. experience = experience

    def get_experience(self):
        return self.experience


def find_senior(engineers):
    return max(engineers, key=lambda engineer: engineer.get_experience())


def guess_number(num):
    result = roll_dice()
    if result == num:
        return "You won!"
    else:
        return "You lost!"


def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']


def random_sum():
    a = random.randint(1, 10)
    b = random.randint(1, 7)
    return a + b

def silly():
    params = {
        "timestamp": time.time(),
        "number": random.randint(1, 6)
    }

    response = requests.get("https://httpbin.org/get", params)
    if response.status_code == 200:
        return response.json()['args']
