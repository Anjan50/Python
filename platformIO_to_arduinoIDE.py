import shutil as sh
import os

# Source directories
src = input("Enter path of project folder: ")

# Destination directories
dest = input("Enter path of Output folder: ")
# Removes the folders
# sh.rmtree(dest)

# Recreates the folders
os.mkdir(dest + "\Code")
dest = dest + "\Code"
# Copies the paths of files in a list
src_e = os.listdir(src + "\src")
include_e = os.listdir(src + "\include")

path_list = []

# ESP folders
for i in src_e:
    str = src + "\src" + "\\" + i
    path_list.append(str)

for i in include_e:
    str = src + "\include" + "\\" + i
    path_list.append(str)

for i in range(len(path_list)):
    sh.copy(path_list[i], dest)
