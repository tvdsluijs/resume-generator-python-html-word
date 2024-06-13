# Resume Generator

This project is a simple resume generator that converts a JSON file containing resume data into an HTML resume using a Jinja2 template.

## Prerequisites

- Python 3.x
- Jinja2 library

## Installation

1. **Clone the repository** (if applicable):
    ```sh
    git clone https://github.com/yourusername/resume-generator.git
    cd resume-generator
    ```

2. **Install Jinja2**:
    ```sh
    pip install jinja2
    ```

## LinkedIn Profile Exporter to JSON
If you want to export your LinkedIn profile to JSON, you can use the following tool:
- [LinkedIn JSON Resume Exporter for Chrome](https://chromewebstore.google.com/detail/json-resume-exporter/caobgmmcpklomkcckaenhjlokpmfbdec)

## Usage

1. **Prepare your JSON data**:
    - Create a JSON file named `resume.json` with your resume data. The structure should follow the [JSON Resume schema](https://jsonresume.org/schema/).

2. **Create a Jinja2 template**:
    - Create an HTML template file named `resume_template.html` in the same directory. This template will define how your resume should be formatted. You can use placeholders for the data fields, e.g., `{{ basics.name }}`, `{{ work[0].position }}`, etc.

3. **Run the script**:
    - Save the following script as `generate_resume.py` in the same directory:

    ```python
    import json
    from jinja2 import Environment, FileSystemLoader

    # Load JSON data
    with open('resume.json', 'r') as file:
        data = json.load(file)

    # Load the Jinja2 template
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('resume_template.html')

    # Render the template with data
    output = template.render(data)

    # Save the output to an HTML file
    with open('your_resume.html', 'w') as file:
        file.write(output)

    print("Your resume is generated successfully!")
    ```

4. **Generate your resume**:
    - Run the script:
    ```sh
    python generate_resume.py
    ```

    - This will generate an HTML file named `your_resume.html` in the same directory, containing your formatted resume.

## Example

Here is an example of how the JSON data (`resume.json`) might look:

```json
{
  "basics": {
    "name": "YOUR NAME",
    "label": "YOUR PROFESSION",
    "email": "EMAIL",
    "phone": "MOBILE NUMBER",
    "location": {
      "address": "YOUR ADDRESS"
    },
    "profiles": [
      {
        "network": "LinkedIn",
        "username": "USERNAME",
        "url": "URL/"
      },
      {
        "network": "OTHER NETWORK NAME (e.g., Twitter)",
        "username": "USERNAME",
        "url": "https://twitter.com/USERNAME"
      }
    ]
  },
  "work": [
    {
      "name": "COMPANY NAME",
      "position": "YOUR POSITION",
      "startDate": "START DATE",
      "endDate": "",
      "summary": "JOB DESCRIPTION"
    }
    // Additional work experiences...
  ],
  // Additional sections (education, skills, etc.)...
}
```

And here is an example of how the Jinja2 template (`resume_template.html`) might look:

```html
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV - {{ basics.name }}</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; }
        .container { width: 80%; margin: auto; overflow: hidden; }
        header { background: #333; color: #fff; padding-top: 30px; min-height: 70px; border-bottom: #77A6F7 3px solid; }
        .main-header { text-align: center; background: #5D6D7E; color: #fff; padding: 30px 0; }
        section { padding: 20px 0; border-bottom: 1px solid #e4e4e4; }
        .section-title { font-size: 1.8em; margin-bottom: 10px; color: #333; }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>{{ basics.name }}</h1>
            <p>{{ basics.label }}</p>
        </div>
    </header>

    <div class="main-header">
        <div class="container">
            <h1>Curriculum Vitae</h1>
        </div>
    </div>

    <section>
        <div class="container">
            <h2 class="section-title">Contactgegevens</h2>
            <p>Email: {{ basics.email }}</p>
            <p>Telefoon: {{ basics.phone }}</p>
            <p>Adres: {{ basics.location.address }}</p>
            <p>LinkedIn: <a href="{{ basics.profiles[0].url }}">{{ basics.profiles[0].username }}</a></p>
            <p>Twitter: <a href="{{ basics.profiles[1].url }}">{{ basics.profiles[1].username }}</a></p>
        </div>
    </section>

    <section>
        <div class="container">
            <h2 class="section-title">Profiel</h2>
            <p>{{ basics.summary | safe }}</p>
        </div>
    </section>

    <section>
        <div class="container">
            <h2 class="section-title">Werkervaring</h2>
            {% for job in work %}
                <h3>{{ job.name }} - {{ job.position }}</h3>
                <p><strong>Startdatum:</strong> {{ job.startDate }}</p>
                <p>{% if job.endDate %}<strong>Einddatum:</strong> {{ job.endDate }}{% endif %}</p>
                <p>{{ job.summary | safe }}</p>
            {% endfor %}
        </div>
    </section>

    <!-- Additional sections for education, skills, etc. -->

    <footer>
        <p>&copy; 2024 Theo van der Sluijs. Alle rechten voorbehouden.</p>
    </footer>
</body>
</html>
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
