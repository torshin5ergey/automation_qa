# DEMOQA Automated Testing Framework

This repository contains a project with automated website testing framework using Python and Selenium WebDriver.
This framework is designed to test the functionalities of the [demoqa.com](https://demoqa.com/).
It is inspired by a YouTube course project [Автоматизация тестирования python](https://www.youtube.com/playlist?list=PL8jIzbooWPdXN6thJ_bGnd9uZjby07DPC) by [ARTVLAD | Automation Craft](https://www.youtube.com/@AutomationCraft)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)
- [Notes](#notes)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/torshin5ergey/automation_qa.git
```
2. Navigate to the project directory:
```bash
cd automation-qa
```
3. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

## Usage

1. Update the `conftest.py` file to initialize the WebDriver instance with the appropriate driver using `webdriver-manager`.
2. Run the tests using pytest:
```bash
pytest
```

## Project structure

```
$PROJECT_ROOT
├── data # Module for storing test data
│   └── data.py # Data class definition
├── generator # Module for generating test data
│   └── generator.py # Script for generating fake data for tests
├── locators # Module for storing element locators
│   └── elements_page_locators.py # Locators for elements on test pages
├── pages # Module for defining page objects
│   ├── base_page.py # BasePage class for common page functionalities
│   └── element_page.py # Page classes for individual web pages
├── tests # Module for test cases
│   └── elements_test.py # Test cases for website elements
├── conftest.py # Pytest configuration and fixture definition
├── README.md # This README file
└── requirements.txt # File containing project dependencies
```
- `data`: Test data classes.
- `generator`: Generating fake data script.
- `locators`: Web pages element locators.
- `pages`: Page objects representing individual web pages.
- `tests`: Test cases for website objects.
  - `elements_test.py`: Test cases for Elements pages.
    - `TestTextBox` **Text Box** page test case. It fills all text fields with fake user data and asserts that the filled data matches the expected data for each field.
    - `TestCheckBox` **Check Box** page test case. It toggles all items, selects a random checkboxes, retrieves the checked checkboxes, and asserts that the selected checkboxes match the output result.
    - `TestRadioButton` **Radio Button** page test case. It selects all radio buttons and asserts that the expected output matches the selected radio button for each option. *The "No" radiobutton is disabled, and it is a bug that is founded by this test case*.
    - `TestWebTable` **Web Table** page test cases. It contains: Add person, Search person by random its random data, Edit person's random data field, Delete person by email, Change number of rows displayed per page.
    - `TestButtonsPage` **Buttons** pge test cases. It contains: Double-click button, Right-click (context-click) button, Left-click dynamic ID button.
- `conftest.py`: Pytest configuration file and fixture definitions.
- `requirements.txt`: Project dependencies.

## Requirements

- [pytest](https://pypi.org/project/pytest/) (8.2.0 used)
- [selenium](https://pypi.org/project/selenium/) (4.20.0 used)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/) (4.0.1 used)
- [Faker](https://pypi.org/project/Faker/) (25.1.0 used)  
- [requests](https://pypi.org/project/requests/) (2.31.0 used)

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)

## *Notes*

- [Page Object Model (POM)](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/) is used in this project. POM is a design pattern in test automation that separates the logic of testing from the logic of managing web elements. Each web page is represented as a "Page Object" containing methods to interact with page elements (e.g., clicks, text inputs, etc.) and properties to access these elements. By implementing POM, tests become more stable, readable, and easily maintainable. It reduces code duplication and enhances modularity, allowing development and testing teams to efficiently handle changes in the application.
- [Faker](https://faker.readthedocs.io/en/master/) library is used in this project. Faker is a Python library that generates fake data, such as names, addresses, and phone numbers. By using Faker you can populate data, create mock user profiles, and simulate realistic scenarios without relying on actual sensitive or confidential information. Faker enhances test automation by providing a convenient way to generate diverse and customizable test data, improving test coverage and accuracy.
- [Requests](https://requests.readthedocs.io/en/latest/) 
