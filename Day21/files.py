import os
import shutil
print(os.getcwd())
os.chdir("/home/vicracker/Downloads")

if not os.path.exists("down-videos"):
    os.mkdir("down-videos")
elif not os.path.exists("down-images"):
    os.mkdir("down-images")
elif not os.path.exists("down-audion"):
    os.mkdir("down-audio")

else:
    print(f"Directory Exists")
for file_item in os.listdir():
    if ".mp4" in file_item:

        if
        print(f"Moved{file_item}")
        shutil.move(file_item, "/home/vicracker/Downloads/down-videos")


