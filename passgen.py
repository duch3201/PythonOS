import getpass
from cryptography.fernet import Fernet
import os
import json

passw = getpass.getpass("Password: ")
key = Fernet.generate_key()
f = Fernet(key)

# encrypt string called passw
encrypted_passw = f.encrypt(passw.encode())

usr = input("Username: ")

try:
    os.mkdir("User")
except:
    pass
os.chdir("User")
os.mkdir(usr)
os.chdir(usr)

passfile = open("pass.enc", "wb")
passfile.write(encrypted_passw)
keyfile = open("key.enc", "wb")
keyfile.write(key)

os.chdir("..")

anws = input("Do you want to set this user as admin? (y/n): ")
if anws == "y" or anws == "Y":
    IsAdmin = True
    print("This user is now admin")
else:
    IsAdmin = False


usrcfg = open("config.cfg", "w")
# generate a json file with user confguration
str(usr)
str(encrypted_passw)
data = {'users':[{'EncPassword': encrypted_passw.decode(), 'username': usr, 'IsAdmin': IsAdmin}]}

# write json data to config file
usrcfg.write(json.dumps(data))
print(json.dumps(data, indent=4))




