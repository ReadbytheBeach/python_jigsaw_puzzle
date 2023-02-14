# 目标：
    # 找到当前目录下的所有pdf文件
    # 按文档名排序
    # 除了第一页外，将每个PDF的所有页面写入输出的文档
# 执行：
    # 调用os.listdir(), 找到当前工作目录中的所有pdf文件
    # 调用列表的sort()，将文档名按字母排序
    # 为输出的PDF文档创建PdfFileWriter对象
    # 循环遍历每个PDF文档，为它创建PdfFileReader对象
    # 针对每个PDF文档，循环遍历每一页（第一页除外）
    # 将页面添加到输出的PDF
    # 将输出的PDF写入一个文档，名为all.PDF

    # ToDo:  任意组合几个PDF文档，这里插几页，那里加一页，之后再插入几页其他源头的PDF

#! python3

import PyPDF2, os
# get all the pdf files
pdfFiles = []
for filename in os.listdir('.'): # '.'表示当前目录下 
    if filename.endswith('.pdf'): 
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()  # 生成一个pdfWrite的对象

# loop throgh all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')  # 将文档以二进制打开赋值给一个File对象： pdfFileObj
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # 将pdfFileObj赋值给一个PDFFileReader对象： pdfReader
    # Loop through all the pages (except the 1st page) and add them.
    for pageNam in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNam)    # 取出页面
        pdfWriter.addPage(pageObj)  # 页面加入pdfWriter对象
# save the resulting PDF to a file
pdfOutput = open('all.pdf','wb')  # 将一个pdf文件赋予二进制写入并生成一个文件对象： pdfOutput
pdfWriter.write(pdfOutput) # 将PDF写入对象： pdfWriter中的内容赋给该文件对象
pdfOutput.close() # 写完，关闭文件


