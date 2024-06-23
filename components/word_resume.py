from datetime import datetime
from mailmerge import MailMerge

# Placeholder for future RTL support
# pip install python-docx-rtl
# from docx.shared import Inches
# from docx.oxml.ns import qn
# from docx.oxml import OxmlElement

# def set_paragraph_direction(paragraph, direction='LTR'):
#     """
#     Set the paragraph direction. 'LTR' for left-to-right, 'RTL' for right-to-left.
#     """
#     if direction not in ['LTR', 'RTL']:
#         raise ValueError("direction must be either 'LTR' or 'RTL'")
#     p = paragraph._p  # the lxml element for the paragraph
#     pPr = p.get_or_add_pPr()
#     bidi = OxmlElement('w:bidi')
#     bidi.set(qn('w:val'), '1' if direction == 'RTL' else '0')
#     pPr.append(bidi)

def generate_word_resume(data, translations, output_path):
    """
    Generate a Word resume from a template and save it to the specified output path.

    Args:
        data (dict): The resume data to be included in the template.
        translations (dict): The translations for different text elements in the template.
        output_path (str): The path where the generated Word file will be saved.

    Returns:
        None
    """
    template_path = 'templates/resume_template.docx'  # Path to your Word template
    with MailMerge(template_path) as document:
        merge_data = {
            'name': data['basics']['name'],
            'shortname': data['basics']['shortname'],
            'label': data['basics']['label'],
            'email': data['basics']['email'],
            'phone': data['basics']['phone'],
            'url': data['basics']['url'],
            'address': data['basics']['location']['address'],
            'countryCode': data['basics']['location']['countryCode'],
            'summary': data['basics']['summary'],
            'intro': data['basics']['intro'],
            'linkedin': data['basics']['linkedin'],
            'github': data['basics']['github'],
            'year': datetime.now().year
        }

        # Add translations for headers
        merge_data.update({
            'trl_profile': translations['profile'],
            'trl_profile_summary': translations['profile_summary'],
            'trl_contact': translations['contact'],
            'trl_languages': translations['languages'],
            'trl_personal_interests': translations['personal_interests'],
            'trl_personal_activities': translations['personal_activities'],
            'trl_work_experience': translations['work_experience'],
            'trl_education': translations['education'],
            'trl_skills': translations['skills'],
            'trl_professional_interests_activities': translations['professional_interests_activities'],
            'trl_tech_skills': translations['tech_skills'],
            'trl_certificates': translations['certificates'],
            'trl_hobby_projects': translations['hobby_projects'],
            'trl_more_work_related': translations['more_work_related'],
            'trl_non_work_related_roles': translations['non_work_related_roles'],
        })

        # Add work experience details
        work_counter = 1
        for job in data['work']:
            if job['word_show']:
                work_skills = []
                for skill in job['skills']:
                    work_skills.append(skill)

                skills = ', '.join(work_skills)

                merge_data.update({
                    f'work_name_{work_counter}': job['name'],
                    f'work_position_{work_counter}': job['position'],
                    f'work_start_{work_counter}': job['startDate'],
                    f'work_end_{work_counter}': job['endDate'] or translations['present'],
                    f'work_summary_{work_counter}': job['summary'],
                    f'work_skills_{work_counter}': skills
                })
                work_counter += 1

        # Add education details
        for i, edu in enumerate(data['education'], start=1):
            merge_data.update({
                f'edu_institution_{i}': edu['institution'],
                f'edu_area_{i}': edu['area'],
                f'edu_start_{i}': edu['startDate'],
                f'edu_end_{i}': edu['endDate'] or translations['present']
            })

        # Add languages details
        for i, lang in enumerate(data['languages'], start=1):
            merge_data.update({
                f'fluency_{i}': lang['fluency'],
                f'language_{i}': lang['language']
            })

        # Add personal_interests details max 5
        for i, pi in enumerate(data['personal_interests'], start=1):
            merge_data.update({
                f'personal_interests_{i}': pi
            })

        # Add personal_activities details max 5
        for i, pi in enumerate(data['personal_activities'], start=1):
            merge_data.update({
                f'personal_activities_{i}': pi
            })

        # Add professional_activities details max 10
        for i, interest in enumerate(data['interests'], start=1):
            merge_data.update({
                f'professional_activities_{i}': interest
            })

        # Add tech_skills
        merge_data[f'skills'] = ', '.join(data['skills'])

        # Add certificates details max 5
        for i, cert in enumerate(data['certificates'], start=1):
            merge_data.update({
                f'certificate_{i}': cert['name']
            })

        # Add projects details max 3
        for i, proj in enumerate(data['projects'], start=1):
            merge_data.update({
                f'project_name_{i}': proj['name'],
                f'project_summary_{i}': proj['summary'],
                f'project_url_{i}': proj['url']
            })

        # Add volunteer details max 2
        for i, vol in enumerate(data['volunteer'], start=1):
            merge_data.update({
                f'volunteer_name_{i}': vol['organization'],
                f'volunteer_position_{i}': vol['position'],
                f'volunteer_summary_{i}': vol['summary'],
                f'volunteer_start_{i}': vol['startDate'],
                f'volunteer_end_{i}': vol['endDate'] or translations['present'],
                f'volunteer_url_{i}': vol['url']
            })

        document.merge(**merge_data)

        # Future feature: Set paragraph direction if language is Arabic
        # if data['basics']['lang'] == 'ar':
        #     for paragraph in document.paragraphs:
        #         set_paragraph_direction(paragraph, direction='RTL')

        document.write(output_path)
