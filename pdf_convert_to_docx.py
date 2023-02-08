from pdf2docx import Converter

pdf_file = r'D:\03_program\python\pdf_to_docx\Corner_Radar_SRR523_Standard.pdf'
docx_file = r'D:\03_program\python\pdf_to_docx\Corner_Radar_SRR523_Standard.docx'
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()