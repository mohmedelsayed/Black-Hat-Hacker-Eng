import os
import shutil
os.getcwd()
Folder_Target = input("Path Target : ")
File_Extension = input("What Is The File Extension ? [For Example >> pdf , txt , exe , ...etc] : ")
Folder_Path = input("Path To Move in it : ")
Transformes_Loges = input("Path To Send Logs Of Operation in : ")
x=0
file_logs=open(Transformes_Loges+"\\Logs.txt",mode="a+")

for folder, sub_folder, file in os.walk(Folder_Target):
    for sub_folder in file:
        if os.path.join(folder, sub_folder)[-3:]==File_Extension:
           path= os.path.join(folder, sub_folder)
           file_logs.write(path+" =====================  Was Moved to ========================>> "+Folder_Path )
           file_logs.write("\n")
           shutil.move(path, Folder_Path)
           x+=1
file_logs.close()
print("["+str(x)+"]"+"File Transformed")