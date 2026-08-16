
import os

def sort_dir(root_dir):
    dictionaries = {
        'Grafika': ['.png', '.jpg', '.jpeg'],
        'Dokumenty': ['.pdf','.docx','.txt'],
        'Kod': ['.py', '.json','.sql']
    }

    for dictionary in dictionaries:
        os.makedirs(os.path.join(root_dir, dictionary), exist_ok=True)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in dictionaries]

        for filename in filenames:
            file, extention = os.path.splitext(filename)
            for key, value in dictionaries.items():
                if extention in value:
                    os.rename(os.path.join(dirpath, filename), os.path.join(root_dir, key, filename))



sort_dir("C:/Users/ninia/Documents/Pliki")