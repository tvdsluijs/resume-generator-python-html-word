import json

def generate_structured_data(data, output_path):
    """
    Generate structured data in JSON-LD format and save it to the specified output path.

    Args:
        data (dict): The resume data from which structured data will be generated.
        output_path (str): The path where the generated JSON-LD file will be saved.

    Returns:
        None
    """
    # Create the structured data dictionary
    structured_data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": data['basics']['name'],
        "jobTitle": data['basics']['label'],
        "email": data['basics']['email'],
        "telephone": data['basics']['phone'],
        "url": data['basics']['url'],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": data['basics']['location']['address'],
            "addressCountry": data['basics']['location']['countryCode']
        },
        "sameAs": [profile['url'] for profile in data['basics']['profiles']],
        "worksFor": [
            {
                "@type": "Organization",
                "name": job['name'],
                "sameAs": job['url']
            } for job in data['work']
        ]
    }

    # Write the structured data to the output path in JSON format
    with open(output_path, 'w') as file:  # Open the output file in write mode
        json.dump(structured_data, file, indent=4)  # Dump the structured data to the file with an indentation of 4 spaces
