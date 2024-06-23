Sure, based on the provided structure and files, here’s a comprehensive README for your project:

# Resume Generator: Python, HTML, and Word (and sometimes PDF)

This project generates resumes in multiple languages from JSON files. The JSON files contain the data for the resumes, and the script uses Jinja2 templates to generate the HTML output. The script also generates structured data in JSON-LD format for each resume and creates Word documents using a predefined template.

If you have a non Mx OS machine you will also be able to create PDF files.

## Features

- Generates HTML resumes from JSON data.
- Creates Word documents from the same JSON data.
- Supports multiple languages with translations.
- Generates structured data (JSON-LD) for SEO.
- Creates a sitemap.xml and robots.txt for SEO.

## Project Structure

```
resume-generator-python-html-word/
├── components/
│   ├── json_utils.py
│   ├── template_utils.py
│   ├── structured_data.py
│   ├── word_resume.py
├── config/
│   ├── cloudconvert_sample.txt
├── output/
│   ├── icons/
│   ├── images/
│   ├── fonts/
│   ├── flags/
│   ├── style.css
├── resume_json_files/
│   ├── resume_en.json
├── test/
├── templates/
│   ├── resume_template.docx
│   ├── resume_template.html
├── translations/
│   ├── en.json
├── main.py
├── pixi.toml
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:tvdsluijs/resume-generator-python-html-word.git
   cd resume-generator-python-html-word
   ```

2. Install dependencies using Pixi:
   ```bash
   pixi install
   ```

3. Ensure you have `pdflatex` and `rsvg-convert` installed if you plan to convert files.

### PIP users

If you are not using Pixi (you should) and want to use PIP install the required packages:

```bash
pip install jinja2
pip install python-docx
pip install python-docx-mailmerge
pip install requests
```

## Usage

1. Place your JSON resume files in the `resume_json_files` directory.
2. Place your translation files in the `translations` directory.
3. Place your HTML and Word templates in the `templates` directory.

### Generating Resumes

Run the main script to generate the HTML, structured data, and Word documents:

```bash
python main.py
```

### Key Components

- `json_utils.py`: Utility functions for handling JSON data.
- `template_utils.py`: Functions for managing Jinja2 templates.
- `structured_data.py`: Functions for generating JSON-LD structured data.
- `word_resume.py`: Functions for creating Word documents using the MailMerge library.

### Example JSON Data

An example of a JSON resume file:

```json
{
  "basics": {
    "lang": "en",
    "name": "John Doe",
    "label": "Software Engineer",
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "location": {
      "countryCode": "US",
      "address": "123 Main Street, Anytown, USA"
    },
    "profiles": [
      {
        "network": "LinkedIn",
        "url": "https://linkedin.com/in/johndoe",
        "icon": "linkedin.svg"
      }
    ]
  },
  "work": [
    {
      "name": "Tech Company",
      "position": "Senior Developer",
      "startDate": "2020-01-01",
      "endDate": "Present",
      "summary": "Developing awesome applications.",
      "url": "https://techcompany.com",
      "location": "Remote"
    }
  ],
  "education": [
    {
      "institution": "University",
      "area": "Computer Science",
      "startDate": "2010-09-01",
      "endDate": "2014-06-01"
    }
  ],
  "skills": [
    "Python",
    "Django",
    "JavaScript"
  ],
  "languages": [
    {
      "language": "English",
      "fluency": "Native speaker"
    }
  ]
}
```

### Example Translation File

An example of a translation file (`en.json`):

```json
{
  "resume": "Resume",
  "profile_summary": "Profile Summary",
  "contact": "Contact",
  "languages": "Languages",
  "work_experience": "Work Experience",
  "education": "Education",
  "skills": "Skills",
  "present": "Present"
}
```

### Templates

- **HTML Template**: Located at `templates/resume_template.html`
- **Word Template**: Located at `templates/resume_template.docx`

If you want to change the FIELDS in Word fn+Option+F9 fn+F9 to toggle between fields and code.

## SEO Considerations

The project generates SEO-friendly structured data (JSON-LD) and includes a sitemap.xml and robots.txt:

- `sitemap.xml`: Lists all resume pages for search engines.
- `robots.txt`: Points to the sitemap.xml and sets crawling rules.

## Customization

### CSS

- The main stylesheet is located at `output/style.css`.
- Customize the CSS to change the look and feel of the HTML resumes.

### Icons and Images

- Icons are located in the `output/icons/` directory.
- Images are located in the `output/images/` directory.
- Flags are located in the `output/flags/` directory.

Sure! Here's a section to add to your README file that covers the test possibilities and instructions on how to run the tests using both `unittest` and `pixi` commands.

---

## Testing

### Overview

This project includes a suite of tests to ensure that all functionalities work correctly. The tests are written using the `unittest` framework and are located in the `test` directory. These tests cover various aspects of the project, including JSON file processing, template rendering, and file generation.

### Running Tests with Python's `unittest`

To run the tests using Python's built-in `unittest` framework, you can use the `discover` command, which will automatically find and run all the test files in the `test` directory.

1. **Navigate to the project root directory**:
    ```sh
    cd path/to/project/root
    ```

2. **Run the tests**:
    ```sh
    python -m unittest discover test
    ```

### Running Tests with `pixi`

If you are using `pixi` as your package manager, you can also configure it to run the tests.

1. **Ensure your `pixi.toml` is configured to include the test command**:
    ```toml
    [tool.pixi.scripts]
    test = "python -m unittest discover test"
    ```

2. **Run the tests using `pixi`**:
    ```sh
    pixi run test
    ```

### Example Test File

Here's an example test file located in the `test` directory, named `test_main_generation.py`:

```python
import unittest
import os
from main import main  # Adjust the import based on your project structure
from components.json_utils import load_json

class TestMainGeneration(unittest.TestCase):

    def setUp(self):
        # Ensure the output directory exists
        self.output_dir = 'output'
        os.makedirs(self.output_dir, exist_ok=True)

    def tearDown(self):
        # Remove generated files after testing
        for filename in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error: {e.strerror}")

    def test_main_generation(self):
        # Call the main function to generate the files
        main()

        # Verify the generated files exist
        expected_files = [
            'index.html',
            'en_structured-data.json',
            'en_resume.docx'
        ]
        for filename in expected_files:
            file_path = os.path.join(self.output_dir, filename)
            self.assertTrue(os.path.exists(file_path), f"{file_path} does not exist")

        # Additional checks can be performed here to verify the contents of the generated files

if __name__ == '__main__':
    unittest.main()
```

This test file includes a setup method to ensure the output directory exists and a teardown method to clean up generated files after tests run. The `test_main_generation` method runs the main function and checks if the expected files are generated.


## Demo

You can find a demo of this site (and downloadble Word & PDF file of the resume) at [https://theovandersluijs.eu](https://theovandersluijs.eu).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **Theo van der Sluijs**
  - [Website](https://itheo.tech)
  - [Email](mailto:info@itheo.tech)

## Contributions

Contributions are welcome! Please submit pull requests or open issues to improve the project.

## Version
0.1 - 2024-05-30 -> Having some ideas after friend asked me to build this
0.2 - 2024-06-01 -> Created first version of language file
0.3 - 2024-06-05 -> Created first version of my own resume in JSON
0.4 - 2024-06-17 -> Setting the basic structure.
0.5 - 2024-06-18 -> Creating the first HTML version
0.6 - 2024-06-19 -> Creating the first Word version
0.7 - 2024-06-20 -> Creating code
0.8 - 2024-06-21 -> Creating more code
0.9 - 2024-06-22 -> Tryng to create a PDF version
1.0 - 2024-06-23 -> First live verson, with test possibilities
- Initial release with support for generating resumes in HTML and Word formats.
- SEO optimizations with hreflang links, sitemap, and robots.txt.
