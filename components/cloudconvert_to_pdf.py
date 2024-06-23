#Function to convert a Word Docx file into a PDF file with the cloudconvert API
#You will upload the Word Docx file to the cloudconvert API and download the converted PDF file
#The converted PDF file will be saved in the output directory
#
# NOT TESTED FEATURE !!!
#
import requests

def convert_to_pdf(word_file_path: str = "", language: str = "", cloudconvert_api: str = ""):
    if word_file_path == "" or language == "" or cloudconvert_api == "":
        return

    # Set up the API endpoint
    api_endpoint = "https://api.cloudconvert.com/v2/pdf"

    # Set up the headers
    headers = {
        "Authorization": f"Bearer {cloudconvert_api}",
        "Content-Type": "application/json"
    }

    # Set up the payload
    payload = {
        "inputformat": "docx",
        "outputformat": "pdf",
        "input": "upload",
        "file": open(word_file_path, "rb")
    }

    # Make the request to the API
    response = requests.post(api_endpoint, headers=headers, files=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the PDF file
        with open(f"output/{language}_resume.pdf", "wb") as pdf_file:
            pdf_file.write(response.content)
    else:
        print("Error converting Word file to PDF")
        print(response.text)
