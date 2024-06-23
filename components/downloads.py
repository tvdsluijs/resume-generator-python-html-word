
def generate_downloads(language:str="", word:bool=False, pdf:bool=False):
    downloads = []
    if not language:
        return downloads

    if word:
        download = {'url': f"{language}_resume.docx", 'name': f"{language} Resume", 'icon': 'word.svg'}
        downloads.append(download)
    if pdf:
        download = {'url': f"{language}_resume.pdf", 'name': f"{language} Resume", 'icon': 'pdf.svg'}
        downloads.append(download)
    return downloads
