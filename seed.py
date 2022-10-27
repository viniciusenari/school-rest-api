import os, django
from venv import create

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random, datetime
from school.models import  Student, Course, Enrollment

fake = Faker('en_US')
Faker.seed(10)

def create_students(amount):
    for _ in range(amount):
        name = fake.name()
        email = f'{name.lower()}@{fake.free_email_domain()}'.replace(' ','')
        phone = f'{random.randrange(100,999)}-{random.randrange(100,999)}-{random.randrange(1000,9999)}'
        birthday = fake.date_between(start_date='-25y', end_date='-18y')
        s = Student(name = name, email = email, phone = phone, birthday = birthday)
        s.save()

def create_courses(amount):
    for _ in range(amount):
        course_id = f'CS{random.randrange(100,200)}'
        descs = ['Python Fundamentals', 'Intermediary Python','Advanced Python', 'Python for Data Science', 'Python/React']
        description = random.choice(descs)
        descs.remove(description)
        level = random.choice("BIA")
        c = Course(course_id = course_id, description = description, level = level)
        c.save()


create_students(200)
create_courses(5)