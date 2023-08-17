import os
from .utils import utils
def checkout(args):
    cwd = os.getcwd()
    repo_path = utils.find_repository(cwd)

    if repo_path is None:
        print("not in a repository")
        return
    
    if len(args) != 1:
        print("invalid command usage, syntax: 'gitgitty checkout <version-id>'")
        return
    
    try:
        version_id = int(args[0])
        repo_files = os.path.join(repo_path, "..")
        snapshot_checkout_path = os.path.join(repo_path, "snapshots", str(version_id))
        
        utils.clear_staging_directory(repo_files)
        utils.copy_existing_files(snapshot_checkout_path, repo_files)
        utils.set_head(repo_path, version_id)

        print("checkout success")

    except ValueError as e:
        print(f"{e}\nversion id must be integer")
        return
    except Exception as e:
        print(f"{e}\checkout failure")