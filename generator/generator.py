import random
from pathlib import Path
from faker import Faker
from data.data import Person


faker_ru = Faker('ru_RU')  # Faker object configured for Russian language
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
    return f.name, test_file_path
