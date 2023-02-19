import os, PyPDF2
from pathlib import Path
import re
import shutil

pdf_path = Path(r'D:\03_program\python\source_folder')

encrypt_pdf_path = Path.cwd() # 生成pdf的地址在当前目录下
dest_path = Path(r'D:\03_program\python\destination_folder')

pdf_regex = re.compile(r'(.*)(.pdf)$')

print(Path.cwd())

new_postfix = '_encripted.pdf'
for dir, sub_dir, filenames in os.walk(pdf_path):
    for filename in filenames:
        if filename.endswith('.pdf'):
            dir_name = os.path.join(dir, filename) # 生成一个全路径

            print('Opening file...')
            pdf_reader = PyPDF2.PdfFileReader(open(dir_name,'rb')) # 打开一个pdf文件，并生成一个该文件的pdf对象
            pdf_write = PyPDF2.PdfFileWriter() # 生成一个新pdf的对象用于写人内容， 并加密
            
            
            # 新对象写入内容
            for pageNum in range(pdf_reader.numPages): # 总的页数
                # print(pageNum)
                pdf_write.addPage (pdf_reader.getPage(pageNum)) # 将原文件每一页写入新文件中

            # 新对象加密
            pdf_write.encrypt('xj')

            # 创建新文件名
            new_pdf_name = pdf_regex.search(filename).group(1) + new_postfix # 提取文件的名字, 并加上'_encripted.pdf'
            # print(new_pdf_name)
            # 创建新文件名的对象
            result_pdf  = open(new_pdf_name, 'wb')

            # 将内容写入新创建的pdf文件
            pdf_write.write(result_pdf)

            # 关闭result
            result_pdf.close()

            # 打开新生成的pdf文件，查看是否已加密
            re_pdf_reader = PyPDF2.PdfFileReader(open(new_pdf_name,'rb'))

            # 查看文件是否加密成功，如果不成功就输出一句， 然后执行下一条
            print('Is PDF- %s encripted?  Result is: %s' %(new_pdf_name, re_pdf_reader.isEncrypted)) # 查看文件是否已经加密


            current_addr = os.path.join(encrypt_pdf_path,new_pdf_name)
            # print(current_addr)
            dest_addr = os.path.join(dest_path, new_pdf_name)
            # print(dest_addr)

            # 将文件移到新地址
            try:
                shutil.move(current_addr,dest_path)
            # 文件移到新地址，但需要密码打开，允许该错误，并顺序执行下一个文件
            except PermissionError as err_1:
                print ('already moved the pdf to destination, but need use pswd to open the pdf document.')
            # 文件已存在目的地，则允许该错误，并顺序执行下一个文件
            except shutil.Error as err_2:
                print('destination path pdf document already exists.')

            # Todo: 用debugging来记录文件状态

print('Done.')
            
            