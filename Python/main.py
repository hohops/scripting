import os

path = os.getcwd()

dir = input("directory to change")
cd = os.chdir(dir)



print(path)
print(cd)
print(os.getcwd())