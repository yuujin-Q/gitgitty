import os
import shutil

def copy_existing_files(source, destination):
    existing_files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]

    try:
        for filename in existing_files:
            source_file_path = os.path.join(source, filename)
            destination_file_path = os.path.join(destination, filename)
        
            shutil.copy(source_file_path, destination_file_path)

    except PermissionError as e:
        print(f"PermissionError: {e}\nfile copy failed")
        raise e
