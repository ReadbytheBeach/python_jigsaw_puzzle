# 取得完整的word文档的文本

import docx

'''
append()中使用的技巧:  巧妙添加'缩进'
return中使用的技巧

'''
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs: # 遍历所有的段落对象
        # fullText.append(para.text)  # 将段落的text依次存入fullText列表
        fullText.append('    '+ para.text) # 巧妙添加'缩进'


    return '\n'.join(fullText)  # 段与段之间以回车连接
    # return '\n\n'.join(fullText) # 段与段之间加空行

file_name = 'HFL118 Sales Pitch.docx'
print(getText(file_name))


