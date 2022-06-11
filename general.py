import os
import json
import uuid

def about(abtapp):
    if os.path.exists(abtapp) == False:
        print("app does not exist")
        return
    os.chdir(abtapp)
    with open("Project.mtd", 'r') as f:
        mtd = json.load(f)

    print(mtd.get('appdata')[0].get('appname'))
    print(mtd.get('appdata')[0].get('appauthor'))
    #print(mtd.get('appdata')[0].get('appdesc'))
    print(mtd.get('appdata')[0].get('appversion'))
    print(mtd.get('appdata')[0].get('execlocation'))

def projgen(usr):
    print("Project Generator")
    print("==========")
    projectname = input("Project name: ")
    prjdir = input("Project directory: ")
    appauthor = usr
    execlocation = input("Executable location: ")
    appid = uuid.uuid4()
    appid = str(appid)
    if not os.path.exists(prjdir):
        print("Project directory does not exist")
        exit(1)
    prjfile = open("{}/Project.mtd".format(prjdir), "w")

    data = {'appdata':[{'appauthor': appauthor, 'execlocation': execlocation}]}

    prjfile.write(json.dumps(data))
    print(json.dumps(data, indent=4))