import os
from pyPdf import PdfFileReader

path = "/Users/KevinKoshy/PycharmProjects/RealPythonEg"

input_file_name = os.path.join(path, "Pride and Prejudice.pdf")
input_file = PdfFileReader(file(input_file_name, "rb"))

print "Number of pages = ", input_file.getNumPages()
print "Title = ", input_file.getDocumentInfo().title