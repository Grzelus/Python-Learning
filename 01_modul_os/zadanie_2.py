
import os

def create_project_structure(base_dir):
    current_dir = os.getcwd()
    project_dir = os.path.join(current_dir, base_dir)

    if os.path.exists(project_dir):
        raise FileExistsError('Plik juz istnieje')

    os.makedirs(project_dir)    

    subfolders = ['docs','tests', 'src']

    for subfolder in subfolders:
        subfolder_path = os.path.join(project_dir, subfolder)
        os.makedirs(subfolder_path)
        gitkeep_path = os.path.join(subfolder_path, '.gitkeep')
        with open(gitkeep_path, 'w') as file:
            pass 


create_project_structure('first')
    
