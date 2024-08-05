# DEMOQA Automated Testing Framework

This repository contains a project with automated website testing framework using Python and Selenium WebDriver.
This framework is designed to test the functionalities of the [demoqa.com](https://demoqa.com/).
It is inspired by a YouTube course project [Автоматизация тестирования python](https://www.youtube.com/playlist?list=PL8jIzbooWPdXN6thJ_bGnd9uZjby07DPC) by [ARTVLAD | Automation Craft](https://www.youtube.com/@AutomationCraft)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Notes](#notes)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)

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
├── data  # Test data structures
│   └── data.py  # Data class definition
├── generator  # Test mock data generator
│   └── generator.py  # Mock data generator for tests
├── locators  # Pages locators
│   ├── awf_page_locators.py  # Locators for elements in Alerts, Frame & Windows section
│   ├── elements_page_locators.py  # Locators for elements in Elements section
│   ├── forms_page_locators.py  # Locators for elements in Forms section
│   ├── interactions_page_locators.py  # Locators for elements in Interactions section
│   └── widgets_page_locators.py  # Locators for elements in Widgets section
├── pages  # Page objects
│   ├── afw_page.py  # Alerts, Frame & Windows page classes
│   ├── base_page.py  # BasePage class for common page functionalities
│   ├── element_page.py  # Elements section page classes
│   ├── forms_page.py  # Forms section page classes
│   ├── interactions_page.py  # Interactions section page classes
│   └── widgets_page.py  # Widgets section page classes
├── tests # Module for test cases
│   ├── afw_test.py  # Test cases for Alerts, Frame & Windows section
│   ├── elements_test.py  # Test cases for Elements section
│   ├── forms_test.py  # Test cases for Forms section
│   ├── interactions_test.py  # Test cases for Interactions section
│   └── widgets_test.py  # Test cases for Widgets section
├── conftest.py  # Pytest configuration and fixture definition
├── README.md  # This README file
└── requirements.txt  # Project dependencies
```

- `data`: Test data classes.
- `generator`: Fake data generator.
- `locators`: Web pages element locators.
- `pages`: Page objects representing individual web pages.
- `tests`: Test cases for website objects.
  - `afw_test.py`: Test cases for Alerts, Frame & Windows pages.
    - `TestBrowserWindows` **Browser Windows** page test cases. Both tests assert the header to confirm that the new tab or window has opened correctly and displays the
    - `TestAlerts` **Alerts** page test cases. Checking the text of a normal alert, a delayed alert appearing after 6 seconds, and a confirmation box alert with input
    - `TestFrames` **Frames** page test cases. Verifying the content and dimensions of two frames on the page.
    - `TestNestedFrames` **Nested Frames** page test cases. Includes a test for verifying the text content within both the parent and child frames on the nested frames page.
    - `TestModalDialogs` **Modal Dialogs** page test cases. Includes tests for verifying the title and text length of both small and large modals on the modal dialogs page.
  - `elements_test.py`: Test cases for Elements pages.
    - `TestTextBox` **Text Box** page test case. It fills all text fields with fake user data and asserts that the filled data matches the expected data for each field.
    - `TestCheckBox` **Check Box** page test case. It toggles all items, selects a random checkboxes, retrieves the checked checkboxes, and asserts that the selected checkboxes match the output result.
    - `TestRadioButton` **Radio Button** page test case. It selects all radio buttons and asserts that the expected output matches the selected radio button for each option.
    - `TestWebTable` **Web Table** page test cases. It contains: Add person, Search person by random its random data, Edit person's random data field, Delete person by email, Change number of rows displayed per page.
    - `TestButtonsPage` **Buttons** pge test cases. It contains: Double-click button, Right-click (context-click) button, Left-click dynamic ID button.
    - `TestLinksPage` **Links** page test cases. It contains: Simple link ([200 OK](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200), to home), Dynamic simple link ([200 OK](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200), to home), Created link ([201 Created](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201)), No content ([204 No Content](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204)),Moved link ([301 Moved Permanently](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301)), Bad request link([400 Bad Request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400)), Unauthorized link ([401 Unauthorized](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401)), Forbidden link ([403 Forbidden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403)), Not Found link ([404 Not Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)).
    - `TestUploadDownload` **Upload and Download files** page test cases. It contains: Upload and download file.
    - `TestDynamicProperties` **Dynamic Properties** page test case. It contains: The "Enable After 5 Seconds" button becomes clickable within a timeout, The color of the "Color Change" button changes after a 5 seconds delay, The "Visible After 5 Seconds" button becomes visible after a 5 seconds delay. *This tests may not work correctly with the `webdriver_manager` library, because in that case the test startup will be much later than the change of dynamic properties.*
  - `forms_test.py`: Test cases for Practice Form in Forms section.
    - `TestFormsPage` **Practice Form** page test case. Generates data and verifies that the form can be correctly filled and submitted.
  - `interactions_test.py`: Test cases for Interactions section.
    - `TestSortable`: **Sortable** page test cases. Verifies that the list and grid elements can be shuffled.
    - `TestSelectable`: **Selectable** page test cases. Verifies that the correct number of list and grid items are selected.
    - `TestResizable`: **Resizable** page test cases. Verifies that the resizable elements (w/ constraints and w/o) correctly resizes to the maximum and minimum specified sizes.
  - `widgets_test.py`:  Test cases for Widgets section.
    - `TestAccordian`: **Accordian** page test cases. Verifies that the headers and texts of all three sections in the accordion component are correctly displayed and not empty on the accordion page.
    - `TestAutoComplete`: **Auto Complete** page test cases. Contains tests for verifying the addition and removal of multiple colors in a multi-select autocomplete field, and the addition of a single color in a single-select autocomplete field on the autocomplete page.
    - `TestDatePicker` **Date Picker** page test cases. Contains date and datetime select tests.
    - `TestSlider` **Slider** page test cases. Contains drag'n'drop slider action.
    - `TestProgressBar` **Progress Bar** page test case. Verifies that the progress bar value changes after starting and stopping it.
    - `TestTabs` **Tabs** page test case. Checks that the tabs on the page open correctly and contain the expected amount of text.
    - `TestToolTips` **Tool Tips** page test case. Ensures that tooltips display the correct text when hovering over various elements on the page.
    - `TestMenu` **Menu** page test case. Verifies that the menu on the demo page contains exactly 8 non-empty items.
- `conftest.py`: Pytest configuration file and fixture definitions.
- `requirements.txt`: Project dependencies.

## Notes

- Test creation algorythm:
  1. Create locators.
  2. Create page and load locators.
  3. Create page methods.
  4. Create test class and its methods.
- [Page Object Model (POM)](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/) is used in this project. POM is a **design pattern** in test automation that separates the logic of testing from the logic of managing web elements. Each web page is represented as a **Page Object** containing methods to interact with page elements (e.g., clicks, text inputs, etc.) and properties to access these elements. By implementing POM, tests become more stable, readable, and easily maintainable. It reduces code duplication and enhances modularity, allowing development and testing teams to efficiently handle changes in the application.
- [Faker](https://faker.readthedocs.io/en/master/) library is used in this project. Faker is a Python library that generates fake data, such as names, addresses, and phone numbers. By using Faker you can populate data, create **mock user profiles**, and simulate realistic scenarios without relying on actual sensitive or confidential information. Faker enhances test automation by providing a convenient way to generate diverse and customizable test data, improving test coverage and accuracy.
- [Requests](https://requests.readthedocs.io/en/latest/) library is used for making HTTP requests (GET, POST), checking response content.
- **Automated file download check**. The process of checking and creating a file. This methos is used in the `download_file` method of the `UploadDownloadPage` class in the `elements_page.py` file. It creates a temporary .jpg file, then decodes **base64** data and writes it to the file starting from the JPEG header. After this, the existence of the file is checked using os.path.exists, and the file is deleted after successful verification.
- This project uses [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) inspired **docstrings**.

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