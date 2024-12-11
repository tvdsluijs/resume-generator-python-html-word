def generate_downloads(language: str = "", word: bool = False, pdf: bool = False, tldr: bool = False):
    """
    Generate a list of downloadable resume links based on the given parameters.

    Args:
        language (str): The language code for the resume. Example: 'en', 'fr', etc.
        word (bool): Whether to include the Word resume link. Default is False.
        pdf (bool): Whether to include the PDF resume link. Default is False.

    Returns:
        list: A list of dictionaries containing download information. Each dictionary includes:
              - 'url': The URL of the resume file.
              - 'name': The name of the resume file.
              - 'icon': The icon associated with the file type.
    """
    downloads = []  # Initialize an empty list to hold the download links

    # If no language is provided, return an empty list
    if not language:
        return downloads

    # If the Word option is selected, add the Word resume link to the list
    if word:
        download = {
            'url': f"{language}_resume.docx",
            'name': f"{language} MS-Word resume",
            'icon': 'word.svg',
            'width': '24px',
            'height': '42px'
        }
        downloads.append(download)
        if tldr:
            download = {
                'url': f"{language}_resume_tldr.docx",
                'name': f"{language} MS-Word 1 page resume",
                'icon': 'word-1p.svg',
                'width': '24px',
                'height': '32px'
            }
            downloads.append(download)
    # If the PDF option is selected, add the PDF resume link to the list
    if pdf:
        download = {
            'url': f"{language}_resume.pdf",
            'name': f"{language} PDF resume",
            'icon': 'pdf.svg',
            'width': '32px',
            'height': '32px'
        }
        downloads.append(download)
        if tldr:
            download = {
                'url': f"{language}_resume_tldr.pdf",
                'name': f"{language} PDF 1 page resume",
                'icon': 'pdf-1p.svg',
                'width': '32px',
                'height': '32px'
            }
            downloads.append(download)
    return downloads  # Return the list of download links
