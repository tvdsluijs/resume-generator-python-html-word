import unittest
from components.json_utils import generate_hreflang_links

class TestGenerateHreflangLinks(unittest.TestCase):

    def setUp(self):
        self.basics = {
            "name": "Theo van der Sluijs",
            "url": "https://theovandersluijs.eu"
        }
        self.languages = ["en", "nl", "de", "fr"]
        self.default_language = "en"
        self.expected_output = {
            "en": "https://theovandersluijs.eu/index.html",
            "nl": "https://theovandersluijs.eu/nl_resume.html",
            "de": "https://theovandersluijs.eu/de_resume.html",
            "fr": "https://theovandersluijs.eu/fr_resume.html",
            "x-default": "https://theovandersluijs.eu/index.html"
        }

    def test_hreflang_links(self):
        hreflang_links = generate_hreflang_links(self.basics, self.languages, self.default_language)
        self.assertEqual(hreflang_links, self.expected_output)

    def test_non_default_language(self):
        default_language = "nl"
        expected_output = {
            "en": "https://theovandersluijs.eu/en_resume.html",
            "nl": "https://theovandersluijs.eu/index.html",
            "de": "https://theovandersluijs.eu/de_resume.html",
            "fr": "https://theovandersluijs.eu/fr_resume.html",
            "x-default": "https://theovandersluijs.eu/index.html"
        }
        hreflang_links = generate_hreflang_links(self.basics, self.languages, default_language)
        self.assertEqual(hreflang_links, expected_output)

if __name__ == "__main__":
    unittest.main()
