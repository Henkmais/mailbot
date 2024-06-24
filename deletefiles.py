import os

def delete_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("Alle bestanden in", directory, "zijn verwijderd!")
    except OSError:
        print("Er is een fout opgetreden bij het verwijderen van bestanden in", directory)

# Voorbeeldgebruik:
directory_to_clean = "ymalbk"
delete_files_in_directory(directory_to_clean)

directory_to_clean = "weatherdata"
delete_files_in_directory(directory_to_clean)
