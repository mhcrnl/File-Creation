#!/usr/bin/python

import folder_create
from Controller import Controller
import os

#print("1.Create Folder.\n2.Create README file.\n3.Delete Folder.\n4.Dircetory List.\n5.Change Dir.\n6.Exit.")
print("Operating System Module : ", os.name)
print("Current Working Directory: ", os.getcwd())

while True:
    
    print("1.Create Folder.")
    print("2.Create README.md file.")
    print("3.Delete Folder.")
    print("4.Directory List.")
    print("5.Change dir 5.")
    print("6.Create README file.")
    print("7.Exit.")
          
    try:
        
        ch=int(input("Enter Choice: "))
        
    except ValueError:
        
        print("Enter Valid Choice: ")

    
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

    elif ch==5:

        exit()
        print("System Exit")

    elif ch==6:

        lang = input("Insert Extension: py, java, html, md :")
        filename = input("Insert filename: README, md etc: ")
        cont = Controller(None)
        cont.format_File(lang, filename)

    else:

        break

        
'''

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
