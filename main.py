import os
import shutil
path="pathhere"
def checkiffolderisemty(path):
    """
    Check if a folder is empty
    """
    if os.listdir(path):
        print("Folder is not empty")    
        return False
    else:
        print("Folder is empty")
        return True
checkiffolderisemty(path)

# def printallfolderinfolder(folder):
#     """
#     Print all folder in a folder
#     """
#     for root, dirs, files in os.walk(folder):
#         print(dirs)
# printallfolderinfolder("E:\C,C++\TAGI")
# print(dirs)
def printonlyfolderinfolder(folder):
    """
    Print all folder in a folder
    """
    global vai
    for root, vai, files in os.walk(folder):
        return vai
printonlyfolderinfolder(path)
a=printonlyfolderinfolder(path)
#print(a[0])
path1=path+a[1]
#print(path1)
def deletefolder(folder):
    """
    Delete a folder
    """
    if checkiffolderisemty(folder):
        print("Folder is empty")
        shutil.rmtree(folder)
        print("Folder deleted")
    else:
        print("Folder is not empty")
for i in range(len(a)):
    path2=path+a[i]
    b=printonlyfolderinfolder(path2)
    #print(path2)
    for item in range(len(b)):
        path1=path2+"/"+b[item]
        print(path1)
        deletefolder(path1)