from datetime import datetime
from .utils import utils
import os

def commit(args):
    cwd = os.getcwd()
    repo_path = utils.find_repository(cwd)

    if repo_path is None:
        print("not in a repository")
        return
    

    time = datetime.now().time()
    date = datetime.now().date()
    msg = ""
    if len(args) == 0:
        msg = f"Committed at {time}-{date}"
    else:
        if args[0] != '-m' or len(args) > 2:
            print("invalid command usage, syntax: 'gitgitty commit [-m <msg>]'")
            return
        
        msg = args[1]


    try:
        repo_files = os.path.join(repo_path, "..")
        new_snapshot_path = os.path.join(repo_path, "snapshots", str(utils.get_latest(repo_path) + 1))
        
        utils.copy_existing_files(repo_files, new_snapshot_path)
        utils.increment_latest(repo_path)
        utils.set_head(repo_path, utils.get_latest(repo_path))
        utils.append_log(repo_path, utils.get_latest(repo_path), date, time, msg)

        print("commit success")
    except Exception as e:
        print(f"{e}\ncommit failure")