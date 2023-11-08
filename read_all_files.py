import os

path = '.'
filelist = os.listdir(path) # получаем список файлов/папок

text = []
for name in filelist: # 
    with open(os.path.join(path, name), "r") as f:
        text.append(f.readlines())