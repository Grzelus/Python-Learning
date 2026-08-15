import os

def find_files_by_extention(root_dir, extention):
    if not os.path.exists(root_dir):
        raise FileNotFoundError('plik nie istnieje')

    if not extention.startswith('.'):
        extention = '.' + extention

    file_paths = []
    total_space = 0

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(extention):
                file_path = os.path.join(dirpath, file)
                file_paths.append(file_path)
                total_space += os.path.getsize(file_path)

    print('Lista plikow:')
    for file_path in file_paths:
        print(f"{file_path}")
    print(f"pliki z rozszerzeniem {extention} zajmuja lacznie {total_space/1024:.2f} KB")

    return file_paths

