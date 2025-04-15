import os
import glob

#Question-3:
#Given a directory, find out the file Name 
#having max size recursively 

directory=r"C:\Users\Sreya\handson"

def max_file(directory,filename,maxsize):
    p=directory+r"\*"
    items=glob.glob(p)
    for item in items:
        if(os.path.isdir(item)):
            maxsize,filename=max_file(item,filename,maxsize)
        else:
            size=os.path.getsize(item)
            if(size>maxsize):
                maxsize=size;
                filename=os.path.basename(item)
    return [maxsize,filename] 

print(max_file(directory,"no file is present in the directory",0)[1])



# Question-4:
# Recursively go below a dir and based on filter, dump those files in to  single file 
# (work with only text file)



copypath = r"C:\Users\Sreya\copyfile.txt"
filter = "txt"
import glob
import os
def copyall(directory, copyfile):
    directory_path = directory + r"\*"  # Consistent path handling
    items = glob.glob(directory_path)  # Retrieve all items in the directory
    
    for item in items:
        if os.path.isdir(item):  # Check if it's a directory
            copyall(item, copyfile)  # Recursive call for subdirectories
        elif item.endswith(f".{filter}"):  # Check file extension directly
            try:
                with open(item, "rt") as f1:
                    copyfile.write(f1.read())
                    copyfile.write("\n--- End of File ---\n")  # Separator for clarity
            except Exception as e:
                print(f"Error reading file {item}: {e}")

with open(copypath, "wt") as copyfile:  # Open file in write mode
     copyall(r"C:\Users\Sreya\handson", copyfile)


###################o/p############
hello world
hello world
hello world
hello world
hello world

--- End of File ---
