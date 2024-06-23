import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_hreflang_links(basics, languages, default_language):
    base_url = "https://theovandersluijs.nl"
    hreflang_links = {lang_code: f"{base_url}/{lang_code}_resume.html" for lang_code in languages}
    hreflang_links["x-default"] = f"{base_url}/index.html"
    return hreflang_links
