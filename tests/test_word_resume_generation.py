import unittest
from datetime import datetime
from mailmerge import MailMerge
from components.word_resume import generate_word_resume
import os

class TestWordResumeGeneration(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.data = {
            'basics': {
                'name': 'John Doe',
                'shortname': 'JD',
                'label': 'Software Engineer',
                'email': 'john.doe@example.com',
                'phone': '+1234567890',
                'url': 'https://johndoe.com',
                'location': {
                    'address': '123 Main St, Springfield',
                    'countryCode': 'US'
                },
                'linkedin': 'https://linkedin.com/in/johndoe',
                'github': 'https://github.com/johndoe',
                'summary': 'Experienced software engineer with a passion for development.',
                'intro': 'An innovative developer with a background in agile methodologies.',
                'lang': 'en'
            },
            'work': [
                {
                    'name': 'Company A',
                    'position': 'Developer',
                    'startDate': '2020-01-01',
                    'endDate': '2021-01-01',
                    'summary': 'Developed various applications.',
                    'skills': ['Python', 'Django'],
                    'word_show': True
                },
                {
                    'name': 'Company B',
                    'position': 'Senior Developer',
                    'startDate': '2021-02-01',
                    'endDate': '',
                    'summary': 'Led a team of developers.',
                    'skills': ['JavaScript', 'React'],
                    'word_show': False
                }
            ],
            'education': [
                {
                    'institution': 'University X',
                    'area': 'Computer Science',
                    'startDate': '2015-09-01',
                    'endDate': '2019-06-01'
                }
            ],
            'languages': [
                {'fluency': '100%', 'language': 'English'},
                {'fluency': '80%', 'language': 'Spanish'}
            ],
            'personal_interests': [
                'Reading', 'Hiking', 'Coding'
            ],
            'personal_activities': [
                'Volunteering at local shelters', 'Organizing tech meetups'
            ],
            'interests': [
                'AI research', 'Open source contributions'
            ],
            'skills': ['Python', 'Django', 'JavaScript', 'React'],
            'certificates': [
                {'name': 'Certified Python Developer'}
            ],
            'projects': [
                            {
                                'name': 'Project A',
                                'summary': 'A project about something interesting.',
                                'url': 'https://projecta.com'
                            }
                        ],
                        'volunteer': [
                            {
                                'organization': 'Charity X',
                                'position': 'Volunteer',
                                'summary': 'Helped in various activities.',
                                'startDate': '2018-01-01',
                                'endDate': '2019-01-01',
                                'url': 'https://charityx.com'
                            }
                        ]
                    }
        self.translations = {
                        'profile': 'Profile',
                        'profile_summary': 'Profile Summary',
                        'contact': 'Contact',
                        'languages': 'Languages',
                        'personal_interests': 'Personal Interests',
                        'personal_activities': 'Personal Activities',
                        'work_experience': 'Work Experience',
                        'education': 'Education',
                        'skills': 'Skills',
                        'professional_interests_activities': 'Professional Interests and Activities',
                        'tech_skills': 'Technical Skills',
                        'certificates': 'Certificates',
                        'hobby_projects': 'Hobby Projects',
                        'more_work_related': 'More Work-Related Information',
                        'non_work_related_roles': 'Non-Work Related Roles',
                        'present': 'Present'
                    }
        self.output_path = 'test_resume.docx'

    def tearDown(self):
        # Remove the generated Word file after testing
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_generate_word_resume(self):
        generate_word_resume(self.data, self.translations, self.output_path)

        # Verify the Word file is created
        self.assertTrue(os.path.exists(self.output_path))

        # Additional checks can be performed here to verify the contents of the generated Word document

if __name__ == '__main__':
    unittest.main()
