import unittest
import json
import os
from components.json_utils import load_json

class TestLoadJson(unittest.TestCase):

    def setUp(self):
        # Create a sample JSON file for testing
        self.file_path = 'test_json.json'
        self.sample_data = {"key": "value", "number": 123}
        with open(self.file_path, 'w') as file:
            json.dump(self.sample_data, file)

    def tearDown(self):
        # Remove the sample JSON file after testing
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_load_json(self):
        # Test if the JSON file is loaded correctly
        result = load_json(self.file_path)
        self.assertEqual(result, self.sample_data)

if __name__ == '__main__':
    unittest.main()
