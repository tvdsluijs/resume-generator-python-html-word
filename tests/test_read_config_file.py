import unittest
import os
from components.read_config import read_config_file

class TestReadConfigFile(unittest.TestCase):

    def setUp(self):
        # Create a sample config file for testing
        self.file_path = 'test_config.txt'
        self.sample_data = "sample config data"
        with open(self.file_path, 'w') as file:
            file.write(self.sample_data)

    def tearDown(self):
        # Remove the sample config file after testing
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_read_config_file(self):
        # Test if the config file is read correctly
        result = read_config_file(self.file_path)
        self.assertEqual(result, self.sample_data)

if __name__ == '__main__':
    unittest.main()
