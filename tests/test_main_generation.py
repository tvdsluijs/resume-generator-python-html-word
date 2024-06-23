import unittest
import os
from your_module_name import main  # Replace with the correct module name
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
