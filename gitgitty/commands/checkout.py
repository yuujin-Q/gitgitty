import os
from .utils import utils
def checkout(args):
    cwd = os.getcwd()
    repository_path = utils.find_repository(cwd)

    if repository_path is None:
        print("not in a repository")
        return
    
    if len(args) != 1:
        print("invalid command usage, syntax: 'gitgitty checkout <version-id>'")
        return
    
    try:
        version_id = int(args[0])
        working_directory = os.path.join(repository_path, "..")
        snapshot_checkout_path = os.path.join(repository_path, "snapshots", str(version_id))
        
        utils.clear_working_directory(working_directory)
        utils.copy_existing_files(snapshot_checkout_path, working_directory)
        utils.set_head(repository_path, version_id)

        print("checkout success")

    except ValueError as e:
        print(f"{e}\nversion id must be integer")
        return
    except Exception as e:
        print(f"{e}\checkout failure")