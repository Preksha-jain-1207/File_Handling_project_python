# this project is supposed to target this folder rather than the entire operating system
from pathlib import Path
import os

def read_File_and_folded() :
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f" {i+1} in {items}")

def createFile():

    try:
        read_File_and_folded()
        name = str(input("Please enter the name of file you want to create "))
        p = Path(name)

        if not p.exists():
               with open(p, 'w') as fs:
                    data = input("Please enter the data you wish to see in the file ")
                    fs.write(data)
               print("FILE CREATED SUCCESSFULLY")     
        else:
             print("This file already exists ")
    except Exception as err:
           print(f"IS HAS AN ERROR {err} ")    

def readFile():

    try:
        read_File_and_folded() 
        name = input("Please enter the name of file you want to read ")
        p = Path(name)

        if p.exists() and p.is_file :
           with open(p, 'r') as fs:
                data = fs.read()
                print(data)
           print("DATA READ SUCCESSFULLY ")     
        else:
             print("This File doesnot exists or this is not a file")    

    except Exception as err:
           print(f"IS HAS AN ERROR {err} ") 
    

def updateFile():

    try:
        read_File_and_folded()
        name = str(input("Please enter the name of file you want to update "))
        p = Path(name)

        if p.exists() and p.is_file():

           print("press 1 if you want to change the file's name ")
           print("press 2 if you want to overwrite the file ")
           print("press 3 if you want to append something to the file ")

           res = int(input( "Enter the functionality you want "))

           if res == 1:
              name = input("Enter the name of the file you want to change ")
              p2 = Path(name)
              p.rename(p2)
              print("THE NAME OF THE FILE IS CHANGED SUCCESSFULLY ")

           if res == 2:
              with open(p, 'w') as fs:
                   data = input("Please enter the data you wish to overwrite in the file ")
                   fs.write(data)   
              print("DATA OVERWRITTEN SUCCESSFULLY ")     

           if res == 3:
              with open(p, 'a') as fs:
                   data = input("Please enter the data you wish to append in the file ")                
                   fs.write( " " + data)
              print("DATA APPENDED SUCCESSFULLY ")     
        else:
            print("This File doesnot exist ")          

    except Exception as err:
           print(f"IS HAS AN ERROR {err} ")  

def deleteFile():

    try:
        read_File_and_folded()
        name = input("Enter the name of the file you want to delete ")
        p = Path(name)

        if p.exists() and p.is_file():
           os.remove(p)
           print("FILE DELETED SUCCESSFULLY")
        else:
             print("this file doesnot exist")     

    except Exception as err:
           print(f"An error has occurred {err}")    


print("press 1 to create a file")
print("press 2 to read a file")
print("press 3 to update a file")
print("press 4 to delete a file")

num = int(input( "Enter a number accordingly " ))

if num == 1 :
   createFile()
elif num == 2 :
     readFile()
elif num == 3 :
     updateFile()
else :
    deleteFile()

