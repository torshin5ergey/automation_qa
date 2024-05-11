from faker import Faker

from data.data import Person


faker_ru = Faker('ru_RU')  # Faker object configured for Russian language
Faker.seed()  # Generating seed for Faker to ensure consistent fake data


# Generator function to yield instances of Person class with fake data
def generate_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )
