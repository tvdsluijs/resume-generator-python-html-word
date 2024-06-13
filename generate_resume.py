import json
from jinja2 import Environment, FileSystemLoader

# Load JSON data
with open('resume.json', 'r') as file:
    # Parse the JSON data into a Python dictionary
    data = json.load(file)

# Set up the Jinja2 environment and specify the directory containing the template
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

# Load the Jinja2 template from the specified directory
template = env.get_template('resume_template_1.html')

# Render the template with the data from the JSON file
output = template.render(data)

# Save the rendered HTML to a file
with open('your_resume.html', 'w') as file:
    # Write the rendered HTML content to the file
    file.write(output)

print("Your resume is generated successfully!")
