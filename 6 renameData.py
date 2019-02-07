import os

# Folder path
path = "training12"

# Get address of current working directory
folder =  os.path.join(os.getcwd(), 'training', path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)
i = 26

for filename in filenames:
    # Replace everything in target directory with ordered namings
    os.rename(os.path.join(folder, filename), os.path.join(folder, filename.replace(filename, 'training11_raw-{}v1.npy'.format(i))))    
    i += 1