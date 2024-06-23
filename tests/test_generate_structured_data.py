import unittest
import json
import os
from components.structured_data import generate_structured_data

class TestGenerateStructuredData(unittest.TestCase):

    def setUp(self):
        # Create a sample resume data for testing
        self.data = {
            "basics": {
                "name": "John Doe",
                "label": "Software Engineer",
                "email": "john.doe@example.com",
                "phone": "+1234567890",
                "url": "https://johndoe.com",
                "location": {
                    "address": "123 Main St, Springfield",
                    "countryCode": "US"
                },
                "profiles": [
                    {"url": "https://linkedin.com/in/johndoe"},
                    {"url": "https://github.com/johndoe"}
                ]
            },
            "work": [
                {
                    "name": "Company A",
                    "url": "https://companya.com"
                },
                {
                    "name": "Company B",
                    "url": "https://companyb.com"
                }
            ]
        }
        self.output_path = 'test_structured_data.json'

    def tearDown(self):
        # Remove the generated JSON-LD file after testing
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_generate_structured_data(self):
        # Generate the structured data
        generate_structured_data(self.data, self.output_path)

        # Verify the structured data file is created
        self.assertTrue(os.path.exists(self.output_path))

        # Load the generated JSON-LD file and verify its content
        with open(self.output_path, 'r') as file:
            structured_data = json.load(file)

        self.assertEqual(structured_data['name'], self.data['basics']['name'])
        self.assertEqual(structured_data['jobTitle'], self.data['basics']['label'])
        self.assertEqual(structured_data['email'], self.data['basics']['email'])
        self.assertEqual(structured_data['telephone'], self.data['basics']['phone'])
        self.assertEqual(structured_data['url'], self.data['basics']['url'])
        self.assertEqual(structured_data['address']['addressLocality'], self.data['basics']['location']['address'])
        self.assertEqual(structured_data['address']['addressCountry'], self.data['basics']['location']['countryCode'])
        self.assertEqual(structured_data['sameAs'], [profile['url'] for profile in self.data['basics']['profiles']])
        self.assertEqual(structured_data['worksFor'], [{"@type": "Organization", "name": job['name'], "sameAs": job['url']} for job in self.data['work']])

if __name__ == '__main__':
    unittest.main()
