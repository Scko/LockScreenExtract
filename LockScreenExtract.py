import shutil
import os

def main():
    source, destination = GetPaths()

    lockScreens = GetLockScreenFileNames(source)

    if not os.path.exists(destination):
        os.mkdir(destination)

    CopyLockScreensToDropZone(lockScreens, source, destination)

def GetPaths():
    home = os.path.expanduser('~')
    src = os.path.join(home, 'AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')
    dst = os.path.join(home, 'Desktop\DropZone')
    return src, dst

def GetLockScreenFileNames(source):
    return [fileName for fileName in os.listdir(source) if os.path.isfile(os.path.join(source, fileName))]

def CopyLockScreensToDropZone(lockScreens, source, destination):
    for lockScreen in lockScreens:
        print(os.path.join(destination, lockScreen+".png"))
        shutil.copy2(os.path.join(source, lockScreen), os.path.join(destination, lockScreen+".png"))

if __name__ == '__main__':
    main()

