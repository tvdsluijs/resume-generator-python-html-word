import os
import json
from datetime import datetime
from components.json_utils import load_json, generate_hreflang_links
from components.template_utils import generate_resume, convert_newlines_to_paragraphs
from components.structured_data import generate_structured_data
from components.word_resume import generate_word_resume
from components.downloads import generate_downloads
from components.pdf_resume import generate_pdf_resume
from components.read_config import read_config_file
from components.cloudconvert_to_pdf import convert_to_pdf

from jinja2 import Environment, FileSystemLoader

def main():
    # Set the default language
    default_language = "en"  # or whichever language you want to set as default

    # Set up the Jinja2 environment
    file_loader = FileSystemLoader('templates')
    not_files = ['resume_template.json', 'resume-schema.json']
    env = Environment(loader=file_loader)
    env.filters['nl2p'] = convert_newlines_to_paragraphs
    template = env.get_template('resume_template.html')

    # Paths
    json_dir = 'resume_json_files'
    translations_dir = 'translations'
    output_dir = 'output'

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Collect all languages
    languages = []

    # Process each JSON file
    for filename in os.listdir(json_dir):
        if filename.endswith('.json') and filename not in not_files:
            data = load_json(os.path.join(json_dir, filename))
            lang = data['basics']['lang']
            languages.append(lang)

    # Generate hreflang links
    hreflang_links = generate_hreflang_links(data['basics'], languages, default_language)

    # Generate resumes and structured data
    for filename in os.listdir(json_dir):
        if filename.endswith('.json') and filename not in not_files:
            data = load_json(os.path.join(json_dir, filename))
            lang = data['basics']['lang']
            downloads = generate_downloads(language=lang, word=True, pdf=True)
            translations = load_json(os.path.join(translations_dir, f"{lang}.json"))
            output_filename = f"{lang}_resume.html"
            if lang == default_language:
                output_filename = "index.html"
            structured_data_filename = f"{lang}_structured-data.json"
            word_output_filename = f"{lang}_resume.docx"
            output_path = os.path.join(output_dir, output_filename)
            structured_data_path = os.path.join(output_dir, structured_data_filename)
            word_output_path = os.path.join(output_dir, word_output_filename)

            # Generate resume, structured data, and Word document
            generate_resume(template, data, translations, hreflang_links, output_path, downloads)
            generate_structured_data(data, structured_data_path)
            generate_word_resume(data, translations, word_output_path)

            # Generate PDF with cloudconvert API you need to pay fo the API
            # First read api from configfile
            # cloudconvert_api = read_config_file("config/cloudconvert.txt")
            # convert_to_pdf(word_output_path, lang, cloudconvert_api)

            # OR use Generate PDF resume (not possible on Mac OS M1/M2/M3/Mx cpu's)
            #generate_pdf_resume(language:str = ""):

if __name__ == "__main__":
    main()
