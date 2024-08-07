from datetime import datetime
import random
from pathlib import Path
from faker import Faker
from data.data import Person, Color, Date

faker_ru = Faker('ru_RU')  # Faker object configured for Russian language
faker_en = Faker('En')  # Faker object configured for English data
Faker.seed()  # Generating seed for Faker to ensure consistent fake data


def generate_person():
    """Generator to yield instances of Person class with fake data."""
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(10, 80),
        salary=random.randrange(10000, 100000, 10000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        phone=faker_ru.msisdn(),
    )


def generate_file(ext):
    """Generate test file.

    Args:
        ext (str): Generated file extension (e.g. txt, jpg).

    Returns:
        tuple: A tuple containing the generated file name and path to the file.
    """
    # Running file directory absolute path
    current_dir_path = Path(__file__).resolve().parent  # (...project/generator/)
    test_file_path = current_dir_path / Path(f'testfile{random.randint(0,999)}.{ext}')
    if ext == 'txt':
        with open(test_file_path, 'w+', encoding='utf-8') as f:
            f.write(f"Hello, World!{random.randint(0, 999)}")
    else:
        f = open(test_file_path, 'w+', encoding='utf-8')
    return f.name, test_file_path


def generate_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generate_random_time():
    hours = random.randint(0, 23)
    minutes = random.choice([0, 15, 30, 45])
    time = str(hours).rjust(2, '0') + ':' + str(minutes).rjust(2, '0')
    return time


def generate_date():
    yield Date(
        #year=faker_en.year(),
        year=str(random.randint(-4, 4) + datetime.now().year),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time=generate_random_time()
    )
