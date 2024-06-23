from datetime import datetime

def convert_newlines_to_paragraphs(value):
    """
    Convert newlines in a string to HTML paragraph tags.

    Args:
        value (str): The input string containing newlines.

    Returns:
        str: The string with newlines converted to HTML paragraph tags.
    """
    paragraphs = value.split('\n\n')  # Split the input string into paragraphs using double newline as the delimiter
    return ''.join(f'<p>{paragraph}</p>' for paragraph in paragraphs)  # Join the paragraphs with <p> tags

def generate_resume(template, data, translations, hreflang_links, output_path, downloads):
    """
    Generate an HTML resume from a template and save it to the specified output path.

    Args:
        template (Template): The Jinja2 template object used to render the HTML.
        data (dict): The resume data to be included in the template.
        translations (dict): The translations for different text elements in the template.
        hreflang_links (dict): The hreflang links for different language versions of the resume.
        output_path (str): The path where the generated HTML file will be saved.
        downloads (list): The list of downloadable resume files (e.g., Word, PDF).

    Returns:
        None
    """
    data['translations'] = translations
    data['year'] = datetime.now().year  # Add the current year to the data
    data['hreflang_links'] = hreflang_links
    data['downloads'] = downloads
    with open(output_path, 'w') as file:  # Open the output file in write mode
        file.write(template.render(data))  # Render the template with the data and write the result to the file
