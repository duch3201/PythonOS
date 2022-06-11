import os
import runner
import auth
from general import about

rootpath = os.getcwd()

currdir = os.getcwd()

def main():
    os.chdir(rootpath)
    usract = input(currdir + ":")
    print(usract)
    usrcmd = usract.split(" ")
    if usrcmd[0] == "run":
        runner.main(usrcmd[1])
    elif usrcmd[0] == "ls":
        print(os.listdir())
    elif usrcmd[0] == "cd":
        try:
            if currdir == rootpath:
                print("Cannot go outside of root path")
            elif usrcmd[1] == "\\":
                os.chdir(rootpath)
            os.chdir(usrcmd[1])
        except:
            print("Directory does not exist")
    elif usrcmd[0] == "mkdir":
        try:
            os.mkdir(usrcmd[1])
        except:
            print("Directory already exists")
    elif usrcmd[0] == "rm":
        try:
            dell = usrcmd[1]
            auth.main(dell)
        except:
            print("File does not exist")
    elif usrcmd[0] == "exit":
        exit(0)
    elif usrcmd[0] == "about":
        abtapp = usrcmd[1]
        about(abtapp)
    main()

def init():
    print("loading please wait")
    os.chdir("User")
    auth.login()
    main()

init()