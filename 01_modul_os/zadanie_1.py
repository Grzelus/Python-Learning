import os

#1
current_dir = os.getcwd()
print(current_dir)

#2
current_dir_elements = os.listdir(current_dir)

#3
print('Lista elementow w obecnym folderze:')
for index, element in enumerate(current_dir_elements, start=1):
    print(f"{index}: {element}")

    path = os.path.join(current_dir, element)
    if os.path.isfile(path):
        file_size = os.path.getsize(path)
        print(f"{element} to plik o wielkosci {file_size} bajtow")
    elif os.path.isdir(path):
        print(f"{element} to folder")
    print()

