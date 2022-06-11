import os
import getpass
import json
from cryptography.fernet import Fernet

def main(dell):
    passw = getpass.getpass("Password: ")

def login():
    print("Login")
    user = input("Username: ")
    passw = getpass.getpass("Password: ")
    with open("config.cfg", "r") as f:
        usrcfg = json.load(f)

    jpassw = usrcfg.get('users')[0].get('EncPassword')
    jusr = usrcfg.get('users')[0].get('username')
    os.chdir(jusr)
    # load key from keyfile
    with open("key.enc", "rb") as f:
        key = f.read()
    
    #encrypt passw with key
    f = Fernet(key)
    encrypted_passw = f.encrypt(passw.encode())

    # compare encrypted passw with encrypted passw from json file
    if encrypted_passw == jpassw:
        print("Login successful")
        return True
    

