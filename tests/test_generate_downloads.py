import unittest
from components.downloads import generate_downloads

class TestGenerateDownloads(unittest.TestCase):
    def test_generate_downloads_no_language(self):
        """Test that generate_downloads returns an empty list when no language is provided."""
        downloads = generate_downloads()
        self.assertEqual(downloads, [])

    def test_generate_downloads_word_only(self):
        """Test that generate_downloads returns only the Word resume link when word is True."""
        downloads = generate_downloads(language='en', word=True)
        self.assertEqual(len(downloads), 1)
        self.assertEqual(downloads[0]['url'], 'en_resume.docx')
        self.assertEqual(downloads[0]['name'], 'en Resume')
        self.assertEqual(downloads[0]['icon'], 'word.svg')

    def test_generate_downloads_pdf_only(self):
        """Test that generate_downloads returns only the PDF resume link when pdf is True."""
        downloads = generate_downloads(language='en', pdf=True)
        self.assertEqual(len(downloads), 1)
        self.assertEqual(downloads[0]['url'], 'en_resume.pdf')
        self.assertEqual(downloads[0]['name'], 'en Resume')
        self.assertEqual(downloads[0]['icon'], 'pdf.svg')

    def test_generate_downloads_both_word_and_pdf(self):
        """Test that generate_downloads returns both Word and PDF resume links when both are True."""
        downloads = generate_downloads(language='en', word=True, pdf=True)
        self.assertEqual(len(downloads), 2)
        self.assertEqual(downloads[0]['url'], 'en_resume.docx')
        self.assertEqual(downloads[0]['name'], 'en Resume')
        self.assertEqual(downloads[0]['icon'], 'word.svg')
        self.assertEqual(downloads[1]['url'], 'en_resume.pdf')
        self.assertEqual(downloads[1]['name'], 'en Resume')
        self.assertEqual(downloads[1]['icon'], 'pdf.svg')

if __name__ == '__main__':
    unittest.main()
