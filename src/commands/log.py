import os
from .utils import utils

def log(args):
    cwd = os.getcwd()
    repo_path = utils.find_repository(cwd)

    if repo_path is None:
        print("not in a repository")
        return
    
    if len(args) != 0:
        print("invalid command usage, syntax: 'gitgitty log'")


    logs = utils.get_log(repo_path).split('\n')[:-1]

    if len(logs) > 0:
        print("vID | Date       -       Time        |  Commit Message")
    for log in logs:
        columns = log.split(',')
        
        print(f"{columns[0]}" +
              f"    {columns[1]} - {columns[2]}" +
              f"    {columns[3]}" +
              "\n\n"
              )
