from dataclasses import dataclass


@dataclass
class Person:  # Class to store a variety of a person parameters
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
