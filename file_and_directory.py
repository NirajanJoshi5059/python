
from pathlib import Path

path = Path("Python")
#remove the directory
path.rmdir()
#check the directory is present or not
print(path.exists())
#make a directory
path.mkdir()
print(path.exists())

path =Path()
for file in path.glob("*.py"):
    print(file)