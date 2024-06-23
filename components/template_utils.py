from datetime import datetime

def convert_newlines_to_paragraphs(value):
    paragraphs = value.split('\n\n')
    return ''.join(f'<p>{paragraph}</p>' for paragraph in paragraphs)

def generate_resume(template, data, translations, hreflang_links, output_path, downloads):
    data['translations'] = translations
    data['year'] = datetime.now().year  # Add the current year to the data
    data['hreflang_links'] = hreflang_links
    data['downloads'] = downloads
    with open(output_path, 'w') as file:
        file.write(template.render(data))
