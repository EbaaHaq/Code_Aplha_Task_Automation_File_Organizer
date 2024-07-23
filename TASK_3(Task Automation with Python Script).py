print("TASK3: Task Automation with Python Script")
print("File Organizer")

import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Dictionary to map file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac','.m4a'],
        'Video': ['.mp4', '.avi', '.mov', '.mkv'],
        'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
        'Executable': ['.exe'],
        'Scripts': ['.py', '.sh', '.bat', '.js', '.html', '.css']
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1].lower()
            moved = False
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(directory, folder, file_name))
                    moved = True
                    break
            if not moved:
                if not os.path.exists(os.path.join(directory, 'Others')):
                    os.makedirs(os.path.join(directory, 'Others'))
                shutil.move(file_path, os.path.join(directory, 'Others', file_name))

    print("Files have been organized.")

# Example usage
organize_files('E:\\')
