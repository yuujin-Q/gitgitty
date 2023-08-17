import shutil
import os
from datetime import datetime
from .utils import utils

def init(args):
    if len(args) != 0:
        print("invalid command usage, syntax: 'gitgitty init'")
        return

    cwd = os.getcwd()
    
    repo_directory = os.path.join(cwd, ".gitgitty")

    try:
        os.makedirs(repo_directory, exist_ok=False)
        
        # log file
        log_path = os.path.join(repo_directory, "log")
        with open(log_path, 'w') as log_file:
            log_file.write(f"version=0, date={datetime.now().date()}, time={datetime.now().time()}, msg=init;")

        # head file
        head_path = os.path.join(repo_directory, "head")
        with open(head_path, 'w') as head_file:
            head_file.write("0")

        # latest
        latest_path = os.path.join(repo_directory, "latest")
        with open(latest_path, 'w') as latest_file:
            latest_file.write("0")

        # snapshots folder
        snapshots_path = os.path.join(repo_directory, "snapshots")
        snapshot_0_path = os.path.join(snapshots_path, "0")
        os.makedirs(snapshots_path, exist_ok=True)
        os.makedirs(snapshot_0_path, exist_ok=True)

        # copy existing files in cwd to snapshot 0
        utils.copy_existing_files(cwd, snapshot_0_path)

        print(f"initialized repository {os.path.basename(cwd)}")
        
    except FileExistsError as e:
        print(f"FileExistsError: repository is already created")

    except Exception as e:
        print(f"Error: {e}")

        print("undoing changes")
        shutil.rmtree(repo_directory)


