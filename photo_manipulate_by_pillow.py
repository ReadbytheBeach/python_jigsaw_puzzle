from PIL import Image


catIm = Image.open('zophie.png')
# print('catIm size: ', catIm.size)
width, height = catIm.size
print('catIm size: width=%d, height=%d'%(width, height))
print('catIm file type: ', catIm.format)

# 取图
catIm.save('zophie.jpg')
catImJpg = Image.open('zophie.jpg')
print('catImJpg type: ', catImJpg.format_description )

im = Image.new('RGBA',(20,20))
im.save('TransparanetImage.png')

# 换色
im_1 = Image.new('RGBA', (100,200),'purple')
im_1.save('purpleImage.png')

im_2 = Image.new('RGBA',(20,20))
im_2.save('transparentImage.png')

# 剪切一块
croppedIm = catIm.crop((335,345,565,560))
croppedIm.save('cropped.png')

# 贴图
catCopyIm = catIm.copy()
print(croppedIm.size)
catCopyIm.paste(croppedIm,(0,0))
catCopyIm.paste(croppedIm,(400,500))
catCopyIm.save('pasted.png')

# 图像填充
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = croppedIm.size
catCopyTwo = catIm.copy()
for left in range (0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        catCopyTwo.paste(catCopyIm, (left, top))
        # print(left, top)
catCopyTwo.save('tiled.png')

# 缩放
catCopyThree = catIm.copy()
quartsizedImage = catCopyThree.resize((int(catImWidth/2),int(catImHeight/2)))
quartsizedImage.save('quartsized.png')
sveIteIm = catCopyThree.resize((catImWidth, catImHeight + 300))
sveIteIm.save('svelte.png')

# 旋转并适当放大
catCopyFour = catIm.copy()
catCopyFour.rotate(90).save('rotated90.png')
catCopyFour.rotate(6, expand=True).save('rotated6_expand.png')

# 镜像
catCopyFour.transpose(Image.FLIP_LEFT_RIGHT).rotate(-6,expand = True).save('horizontal_flip.png')

    