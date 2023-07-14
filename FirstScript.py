import os
import shutil


source=input("enter the source path:")

destination=input("enter the destination path:")




# Copy the content of
# source to destination
if shutil.copyfile(source, destination):
    print("copied sucessfully")
else:
    print("unsucessfull")    







