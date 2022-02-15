def createfolderwithnameindesktop(name):
    import os
    import shutil
    import subprocess
    import sys
    if sys.platform == "win32":
        path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    else:
        path = os.path.join(os.environ['HOME'], 'Desktop')
    path = os.path.join(path, name)
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print("Folder already exists")
    return path
createfolderwithnameindesktop('test')