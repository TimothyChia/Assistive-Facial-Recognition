import os

# misc template code.
# dir = os.listdir(os.getcwd())
# print( "The dir is: %s"%dir[0])
# if not entry.name.startswith('.') and entry.is_file():
# print(entry.name)

# Creates a list of all the subject_id in the Training set, based on the folder structure.
subject_id = []
with os.scandir('.\Training Set') as it:
    for dir in it:
        if dir.is_dir():
            subject_id.append(dir.name)

print(subject_id)