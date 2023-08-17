import os
import shutil

def copy_existing_files(source, destination):
    existing_files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]

    if not os.path.exists(destination):
        os.makedirs(destination, exist_ok=False)

    try:
        for filename in existing_files:
            source_file_path = os.path.join(source, filename)
            destination_file_path = os.path.join(destination, filename)
        
            shutil.copy(source_file_path, destination_file_path)

    except PermissionError as e:
        print(f"PermissionError: {e}\nfile copy failed")
        raise e
    except OSError as e:
        print(f"FileNotFoundError: {e}\n file copy failed")
        raise e


def find_repository(start_directory):
    for root, dirs, files in os.walk(start_directory):
        if ".gitgitty" in dirs:
            return os.path.join(root, ".gitgitty")

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
    # todo
    pass


def append_log(repository_path, id, date, time, msg):
    try:
        with open(os.path.join(repository_path, "log"), "a") as file:
            new_log = f"{id}, {date}, {time}, {msg}\n"
            file.write(new_log)

    except Exception as e:
        print(f"An error occurred: {e}")

