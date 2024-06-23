# Future release
# to use the spire.doc library, you need to install the library's
# pip install Spire.Doc
# AND
# pip install plum-dispatch==1.7.4
#
# Below code is untested! As I cannot install the library on my machine

# UNMOMMENT FROM NEXT LINE TO END OF FILE
# from spire.doc import *
# from spire.doc.common import *\

def generate_pdf_resume(language:str = ""):
    return "This function is not implemented yet"
#     if language == "":
#         return
#     # Create a Document object
#     document = Document()
#     # Load a Word DOCX file
#     document.LoadFromFile(f"output/{language}_resume.docx")
#     # Or load a Word DOC file
#     #document.LoadFromFile("Sample.doc")

#     # Create a ToPdfParameterList object
#     parameters = ToPdfParameterList()

#     # Create PDF bookmarks using Word bookmarks
#     parameters.CreateWordBookmarks = True
#     # Or create PDF bookmarks using Word headings
#     #parameters.CreateWordBookmarksUsingHeadings = True

#     #Save the file to a PDF file
#     document.SaveToFile(f"output/{language}_resume.pdf", parameters)
#     document.Close()
