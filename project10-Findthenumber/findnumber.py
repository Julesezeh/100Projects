import re 
from PyPDF2 import PdfFileReader

filename = "holdingstuff.pdf"
pdf_object =  open(filename,"rb")
pdfreader = PdfFileReader(pdf_object)

pattern1 = "\d+.\d+.\d+"

print(f"Total number of pages is {pdfreader.numPages}")
final =  {}
for x in range(pdfreader.numPages):
    page = pdfreader.getPage(x)
    page_text = page.extractText()
    matches = re.findall(pattern1,page_text)    
    if matches != []:
        final[f'page {x+1}'] = matches

pdf_object.close()

if len(final)>0:
    print("Match found ==>",end=' ')
    print(final)

