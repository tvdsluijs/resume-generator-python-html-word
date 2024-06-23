import unittest
from datetime import datetime
from jinja2 import Environment, DictLoader
from components.template_utils import convert_newlines_to_paragraphs, generate_resume
import os

class TestResumeGeneration(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.template_content = "<html><body>{{ translations.greeting }} {{ data.name }}</body></html>"
        self.env = Environment(loader=DictLoader({'resume_template.html': self.template_content}))
        self.template = self.env.get_template('resume_template.html')
        self.data = {
            'name': 'John Doe',
            'basics': {
                'name': 'John Doe',
                'label': 'Software Engineer',
                'email': 'john.doe@example.com',
                'phone': '+1234567890',
                'url': 'https://johndoe.com',
                'location': {
                    'address': '123 Main St, Springfield',
                    'countryCode': 'US'
                },
                'profiles': [
                    {'url': 'https://linkedin.com/in/johndoe'},
                    {'url': 'https://github.com/johndoe'}
                ]
            }
        }
        self.translations = {'greeting': 'Hello'}
        self.hreflang_links = {'en': 'https://example.com/en_resume.html'}
        self.downloads = [{'url': 'en_resume.docx', 'name': 'English Resume', 'icon': 'word.svg'}]
        self.output_path = 'test_resume.html'

    def tearDown(self):
        # Remove the generated HTML file after testing
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_convert_newlines_to_paragraphs(self):
        input_string = "Paragraph one.\n\nParagraph two."
        expected_output = "<p>Paragraph one.</p><p>Paragraph two.</p>"
        self.assertEqual(convert_newlines_to_paragraphs(input_string), expected_output)

    def test_generate_resume(self):
        generate_resume(self.template, self.data, self.translations, self.hreflang_links, self.output_path, self.downloads)

        # Verify the HTML file is created
        self.assertTrue(os.path.exists(self.output_path))

        # Load the generated HTML file and verify its content
        with open(self.output_path, 'r') as file:
            content = file.read()

        self.assertIn('Hello John Doe', content)
        self.assertIn(str(datetime.now().year), content)

if __name__ == '__main__':
    unittest.main()
