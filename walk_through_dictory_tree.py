import os

for folderName, subfolders, filenames in os.walk(r'd:\\00_Persuit'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print ('Subfolder of '+ folderName + ':' + subfolder)
    
    for filename in filenames:
        print('File insdie' + folderName + ':' + filename)
    
    print('')