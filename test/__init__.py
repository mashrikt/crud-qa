from random import randint

from faker import Faker


fake = Faker()


class EmployeeFactory(object):
    def __init__(self):
        # FiXME: find a better way to generate username
        self.username = fake.name().replace(' ', '_').replace('.', '')
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = fake.email()
        self.department = fake.job()
        self.age = randint(15, 99)
        self.salary = randint(40000, 500000)
