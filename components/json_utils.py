import json

def load_json(file_path):
    """
    Load and return the contents of a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The contents of the JSON file as a dictionary.
    """
    with open(file_path, 'r') as file:  # Open the file in read mode
        return json.load(file)  # Load and return the JSON content as a dictionary

def generate_hreflang_links(basics, languages, default_language):
    """
    Generate hreflang links for different language versions of the resume.

    Args:
        basics (dict): The basic information dictionary.
        languages (list): A list of language codes.
        default_language (str): The default language code.

    Returns:
        dict: A dictionary of hreflang links.
    """
    base_url = "https://theovandersluijs.eu"

    # Generate hreflang links with a special case for the default language
    hreflang_links = {
        lang_code: f"{base_url}/index.html" if lang_code == default_language else f"{base_url}/{lang_code}_resume.html"
        for lang_code in languages
    }

    # Add the x-default link
    hreflang_links["xdefault"] = f"{base_url}/index.html"

    return hreflang_links
