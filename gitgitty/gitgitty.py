import sys
import commands.checkout as checkout
import commands.commit as commit
import commands.init as init
import commands.log as log

def main():
    help = ("available commands:\n" +
              "     init                    create an empty gitgitty repository\n" +
              "     commit [-m <msg>]       record snapshot to the repository\n" +
              "     log                     show commit logs\n" +
              "     checkout <version-id>   change version head\n"
              )
    
    args = sys.argv[1:]

    if len(args) == 0:
        print("usage: gitgitty <command> [<args>]")
        print(help)

        return

    if args[0] == "help":
        print(help)
    elif args[0] == "init":
        init.init(args);
    elif args[0] == "commit":
        commit.commit(args)
    elif args[0] == "log":
        log.log(args) 
    elif args[0] == "checkout":
        checkout.checkout(args)
    else:
        print("invalid syntax\n'gitgitty help' list available commands")



if __name__ == "__main__":
    main()