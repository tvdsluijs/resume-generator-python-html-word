import json

def generate_structured_data(data, output_path):
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
    with open(output_path, 'w') as file:
        json.dump(structured_data, file, indent=4)
