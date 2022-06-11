import os
#import fernet
import uuid
import json
from cryptography.fernet import Fernet

print("App Signer")
print("==========")
prjdir = input("Project directory: ")
projectname = input("Project name: ")
appversion = input("App version: ")
appauthor = input("App author: ")
execlocation = input("Executable location: ")
appid = uuid.uuid4()
appid = str(appid)

key = Fernet.generate_key()
f = Fernet(key)
print(f)
if not os.path.exists(prjdir):
    print("Project directory does not exist")
    exit(1)
prjfile = open("{}/Project.mtd".format(prjdir), "w")

data = {'appdata':[{'appversion': appversion, 'appauthor': appauthor, 'appid': appid, 'execlocation': execlocation}]}

prjfile.write(json.dumps(data))
print(json.dumps(data, indent=4))
