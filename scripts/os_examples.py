import os

# get the current directory
cwd = os.getcwd()

print("Current working directory: {}".format(cwd))


# Change current working directory
# os.chdir('../')

# cwd = os.getcwd()

# print("Current working directory after changing path: {}".format(cwd))

# creating directory
directory = "testdata2"
parent_dir = "../data/"

# path = os.path.join(parent_dir, directory)
# os.mkdir(path)

# get the list of all files and directories
# os.rmdir(path) for directory
# os.remove(path) for file
path = "/"       # in the root directory
dir_list = os.listdir(path)
print("List of files and directories\n: {}".format(dir_list))

# delete file or directory
dir = "testdata2"
location = "../data/"
path = os.path.join(location, dir)
# os.rmdir(path)

# os.rename(): A file old.txt can be renamed to new.txt
# os.remove(): Using the Os module we can remove a file in our system using the remove() method
# os.path.exists(): This method will check whether a file exists or not by passing the name of the file as a parameter.
result = os.path.exists("../data/testdatas3")      # giving the name of the file as a parameter.

print(result)

# os.path.getsize(): In this method, python will give us the size of the file in bytes.
size = os.path.getsize("../data/testdatas3")

print("Size of the file is", size," bytes.")
