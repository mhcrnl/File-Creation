#!/usr/bin/python

import os
'''
    *os* and *os.path* modules include many functions to interact with the file system.
'''
import shutil


class fun:
    def __init__(self,op,f_name,File_name):
        self.op=op
        self.f_name=f_name
        self.File_name=File_name
        
    @classmethod
    def create(cls,f_name,File_name):
        if os.path.exists(f_name):
            print("folder Alredy Created.")
        else:
            os.mkdir(f_name)
            # For linux separator is / and windows is \
            with open(rf'{f_name}/{File_name}','w') as f:
                f.write("Hello World.")
                print("Folder and File Created")

    @classmethod
    def delete(cls,f_name):
        if os.path.exists(f_name):
            shutil.rmtree(f_name)
            print("Folder Deleted.")
        else:
            print("Folder Dosen't exist.")

    @classmethod
    def create_README_file(self, f_name):
        '''
        if os.path.exists(f_name):menu driven
            print("Folder Alredy Created")
        else:
        '''
        try:
            os.chdir(f_name)
            with open("README.md", "w") as f:
                f.write("Helo, README file!")
        except FileNotFoundError:
            print("File not created!")
        

'''
print("1.Create Folder.\n2.Create README file.\n3.Delete Folder.\n4.Dircetory List.\n5.Change Dir.\n6.Exit.")
print("Operating System Module : ", os.name)
print("Current Working Directory: ", os.getcwd())

while True:
    try:
        ch=int(input("Enter Choice: "))
    except ValueError:
            print("Enter Valid Choice: ")

    else:
        break


if ch==1:
    name,filename=input("Enter Folder && File Name: ").split(',')
    fun2=fun.create(name,filename)

#elif ch==2:
    fun.create_README_file(name)
elif ch==2:
    name=input("Enter Folder name: ")
    fun2=fun.delete(name)
elif ch==3:
    print(os.listdir())
elif ch==4:
    dir_name=input("Enter Dircetory Name: ")
    os.chdir(rf"{dir_name}")
    print(os.getcwd())
    print(os.listdir())
else:
    exit
    print("System Closed")
'''
