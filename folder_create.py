import os
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
            with open(rf'{f_name}\{File_name}','w') as f:
                f.write("Hello World.")
                print("Folder and File Created")
    
    @classmethod
    def delete(cls,f_name):
        if os.path.exists(f_name):
            shutil.rmtree(f_name)
            print("Folder Deleted.")
        else:
            print("Folder Dosen't exist.")




print("1.Create Folder.\n2.Delete Folder.\n3.Dircetory List.\n4.Change Dir.\n5.Exit.")

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







    