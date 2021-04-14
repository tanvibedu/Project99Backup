import os
import shutil
import time

#write the name of the directory here
days = 30
# path =  "C:\Users\admin\Videos "
seconds = time.time()

if os.path.exists(path+'/'+ext):
        os.walk(path)
        #This will go through each and every fille
        for file in list_of_files:
        name, ext = os.path.splitext(file)
        os.path.join()

        #This is going to store extension type
        ext = ext[1:]
        if days > 30:
             os.remove(path)

        else:
          
            print("Not found")
            break


#This will create a properly organized list 

list_of_files = os.listdir(path)

