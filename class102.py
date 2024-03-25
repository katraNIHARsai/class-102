import os
import shutil

fromdir = "C:\\Users\\Madhu K\\Downloads\\C102_assets-main"
todir = "C:\\Users\\Madhu K\\Desktop\\PYTHON"
listoffiles = os.listdir(fromdir)

for file_name in listoffiles:
    name,extension = os.path.splitext(file_name)
    print(name,extension)
    #print(extension)
    if (extension == ''):
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = fromdir + '/' + file_name
        path2 = todir + '/' + 'image_files'
        path3 = todir + '/' + 'image_files' + '/' + file_name
        print(path1)
        print(path3)
        
        if os.path.exists(path2):
            print("moving" + file_name)
            shutil.move(path1,path3)
            
        else : 
            os.makedirs(path2)
            print("moving" + file_name)
            shutil.move(path1,path3)