from PyPDF2 import PdfFileReader
import os, sys, re

# https://www.analyticsvidhya.com/blog/2021/09/pypdf2-library-for-working-with-pdf-files-in-python/
# os.chdir(os.path.abspath(__file__))

pdf_path = r"interuptions.pdf"
with open(pdf_path, "rb") as f:
    pdf = PdfFileReader(f)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    # print(information)

print("Author" + ": " + information.author)
print("Creator" + ": " + information.creator)
print("Producer" + ": " + information.producer)

with open(pdf_path, "rb") as f:
    pdf_reader = PdfFileReader(f)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    text = ""
    for i in range(number_of_pages):
        # creating a page object
        pageObj = pdf_reader.getPage(i)
        # extracting text from page
        text = text + pageObj.extractText()

print(text)
