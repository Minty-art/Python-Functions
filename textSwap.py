import os
import shutil
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")
def switch(dest, sc):
    with open(dest, 'r') as b:
        smth = b.read()
        print("read dest")

    with open(sc, 'r') as a:
        data= a.read()
        print("read source")

    with open(dest, 'w') as a:
        a.write(data)
        print("write dest")

    with open(sc, 'w')as a:
        a.write(smth)
        print("write source")

switch(source, destination)