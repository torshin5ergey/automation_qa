from dataclasses import dataclass


@dataclass
class Person:  # Class to store a variety of a person parameters
    full_name: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    age: int = None
    salary: int = None
    department: str = None
    current_address: str = None
    permanent_address: str = None
    phone: str = None
