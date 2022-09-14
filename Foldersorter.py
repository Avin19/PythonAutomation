import os
import shutil
path="C:\\Users\\Avinash\\Downloads\\"
file=os.listdir(path)
def createifnotexist(path,folder):
    if not os.path.exists(path+folder):
        os.makedirs(path+folder)


createifnotexist(path,'Images')
createifnotexist(path,'Docu')
createifnotexist(path,'EXCEl')
createifnotexist(path,'Media')
createifnotexist(path,"PDF")
createifnotexist(path,"Software")
createifnotexist(path,"stuff")
createifnotexist(path,"Android Kodular")
createifnotexist(path,"STL")
createifnotexist(path,"Model")
createifnotexist(path,"Arduino")
for files in file:
    if ".png" in files and not os.path.exists(path+"Images/"+files):
        shutil.move(path+files,path+"Images/"+files)
    if ".csv" in files and not os.path.exists(path + "SCHINDIA/" + files):
            shutil.move(path + files, path + "EXCEL/" + files)
    if ".xlsx" in files and not os.path.exists(path + "EXCEL/" + files):
            shutil.move(path + files, path + "EXCEL/" + files)
    if ".doc" in files and not os.path.exists(path + "Docu/" + files):
            shutil.move(path + files, path + "Docu/" + files)
    if ".pptx" in files and not os.path.exists(path + "Docu/" + files):
            shutil.move(path + files, path + "Docu/" + files)
    if ".ppt" in files and not os.path.exists(path + "Docu/" + files):
            shutil.move(path + files, path + "Docu/" + files)
    if ".pdf" in files and not os.path.exists(path + "PDF/" + files):
        shutil.move(path + files, path + "PDF/" + files)
    if ".PDF" in files and not os.path.exists(path + "PDF/" + files):
            shutil.move(path + files, path + "PDF/" + files)
    if ".exe" in files and not os.path.exists(path + "Software/" + files):
            shutil.move(path + files, path + "Software/" + files)
    if ".jpeg" in files and not os.path.exists(path+"Images/"+files):
        shutil.move(path+files,path+"Images/"+files)
    if ".jpg" in files and not os.path.exists(path+"Images/"+files):
        shutil.move(path+files,path+"Images/"+files)
    if ".mpeg" in files and not os.path.exists(path+"Media/"+files):
        shutil.move(path+files,path+"Media/"+files)
    if ".wav" in files and not os.path.exists(path+"Media/"+files):
        shutil.move(path+files,path+"Media/"+files)
    if ".mp3" in files and not os.path.exists(path+"Media/"+files):
        shutil.move(path+files,path+"Media/"+files)
    if ".mp4" in files and not os.path.exists(path+"Media/"+files):
        shutil.move(path+files,path+"Media/"+files)
    if ".zip" in files and not os.path.exists(path + "stuff/" + files):
            shutil.move(path + files, path + "stuff/" + files)
    if ".rar" in files and not os.path.exists(path + "stuff/" + files):
            shutil.move(path + files, path + "stuff/" + files)
    if ".apk" in files and not os.path.exists(path + "stuff/" + files):
            shutil.move(path + files, path + "stuff/" + files)
    if ".gif" in files and not os.path.exists(path + "Images/" + files):
        shutil.move(path + files, path + "Images/" + files)
    if ".aia" in files and not os.path.exists(path + "Android Kodular/" + files):
        shutil.move(path + files, path + "Android Kodular/" + files)
    if ".aix" in files and not os.path.exists(path + "Android Kodular/" + files):
        shutil.move(path + files, path + "Android Kodular/" + files)
    if ".json" in files and not os.path.exists(path + "Android Kodular/" + files):
        shutil.move(path + files, path + "Android Kodular/" + files)
    if ".stl" in files and not os.path.exists(path + "STL/" + files):
        shutil.move(path + files, path + "STL/" + files)
    if ".STL" in files and not os.path.exists(path + "STL/" + files):
        shutil.move(path + files, path + "STL/" + files)
    if ".fbx" in files and not os.path.exists(path + "Model/" + files):
        shutil.move(path + files, path + "Model/" + files)
    if ".blend" in files and not os.path.exists(path + "Model/" + files):
        shutil.move(path + files, path + "Model/" + files)
    if ".svg" in files and not os.path.exists(path + "Model/" + files):
        shutil.move(path + files, path + "Model/" + files)
    if ".unitypackage" in files and not os.path.exists(path + "Model/" + files):
        shutil.move(path + files, path + "Model/" + files)
    if ".ino" in files and not os.path.exists(path + "Arduino/" + files):
        shutil.move(path + files, path + "Arduino/" + files)
    else:
        pass




