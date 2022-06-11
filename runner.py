import os
import json
import uuid
import subprocess

def main(runfile):
    getback = os.getcwd()
    fileloc = os.getcwd() + '\\' + runfile
    #print(fileloc)
    if os.path.exists(fileloc) == False:
        print("File does not exist")
        exit(1)

    os.chdir(fileloc)

    with open("Project.mtd", "r") as f:
        mtd = json.load(f)
        #print(mtd.get('appauthor'))

    # print key named "execlocation" from json file
    #print(mtd.get('appdata')[0].get('execlocation'))

    execlocation = mtd.get('appdata')[0].get('execlocation')
    nexeclocation = execlocation.replace('.sc', '.py')

    os.rename(execlocation, nexeclocation)

    subprocess.call(nexeclocation, shell=True)

    os.rename(nexeclocation, execlocation)
    os.chdir(getback)