import os
import shutil

def clear_staging_directory(directory_path):
    try:
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if item != ".gitgitty" and os.path.exists(item_path):
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    print(f"Deleted file: {item}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"Deleted folder: {item}")
        print("Deletion completed.")

    except FileNotFoundError as e:
        print(f"{e}\nThe directory '{directory_path}' does not exist.")
        raise e
    except PermissionError as e:
        print(f"{e}\nfile copy failed")
        raise e
    except OSError as e:
        print(f"{e}\n file copy failed")
        raise e
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e


def copy_existing_files(source, destination):
    existing_files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
    existing_directory = [d for d in os.listdir(source) if os.path.isdir(os.path.join(source, d)) and d != ".gitgitty"]

    if not os.path.exists(destination):
        os.makedirs(destination, exist_ok=False)

    try:
        for filename in existing_files:
            source_file_path = os.path.join(source, filename)
            destination_file_path = os.path.join(destination, filename)
        
            shutil.copy(source_file_path, destination_file_path)
        
        for foldername in existing_directory:
            source_file_path = os.path.join(source, foldername)
            destination_file_path = os.path.join(destination, foldername)
        
            shutil.copytree(source_file_path, destination_file_path)

    except PermissionError as e:
        print(f"{e}\nfile copy failed")
        shutil.rmtree(destination)
        raise e
    except OSError as e:
        print(f"{e}\n file copy failed")
        shutil.rmtree(destination)
        raise e


def find_repository(start_directory):
    for root, dirs, files in os.walk(start_directory):
        if ".gitgitty" in dirs:
            return os.path.join(root, ".gitgitty")

        del dirs[:]

    return None  # If the target folder is not found


def get_int_file(repository_path, filename):
    file_path = os.path.join(repository_path, filename)

    try:
        with open(file_path, "r") as file:
            content = file.read()
        return int(content)

    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_int_file(repository_path, filename, value):
    file_path = os.path.join(repository_path, filename)

    try:
        with open(file_path, "w") as file:
            content = file.write(str(value))

    except Exception as e:
        print(f"An error occurred: {e}")


def get_latest(repository_path):
    try:
        return get_int_file(repository_path, "latest")
    except Exception as e:
        return -1


def get_head(repository_path):
    try:
        return get_int_file(repository_path, "head")
    except Exception as e:
        return -1
    
def set_head(repository_path, value):
    try:
        write_int_file(repository_path, "head", value)
    except Exception as e:
        print("failed to set head")


def increment_latest(repository_path):
    try:
        write_int_file(repository_path, "latest", get_latest(repository_path) + 1)
    except Exception as e:
        print("failed to set latest")


def get_log(repository_path):
    file_path = os.path.join(repository_path, "log")

    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The log file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def append_log(repository_path, id, date, time, msg):
    try:
        with open(os.path.join(repository_path, "log"), "a") as file:
            new_log = f"{id}, {date}, {time}, {msg}\n"
            file.write(new_log)

    except Exception as e:
        print(f"An error occurred: {e}")

