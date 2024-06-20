import os

path = os.getcwd()
path=path+"\Pikachu v1.0\img"
files = os.listdir(path)

paths = []

for s in files:
    paths.append(path+s)

print(paths)    