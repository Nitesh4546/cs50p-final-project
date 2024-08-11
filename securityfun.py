import os
from cryptography.fernet import Fernet
from send2trash import send2trash


def valid_path(path: str) ->bool:
    '''
    This function checks the validity of the path.
    '''
    if os.path.exists(path):
        return True
    return False

def writePath(safe: str,path_: str) ->str:
    '''
    Record the dir. that you want to encrypt in a file Encrypt_dir.txt
    '''
    with open(f"{safe}\\Encrypt_dir.txt",'a') as file:
        file.write(path_)
    return "Done"


def add_files(get_path: str, files: list) ->str:
    '''
    This function adds the file names inside folder to a text file named as
    names.txt.
    '''
    with open("Data\\names.txt",'a') as file:
        for i in files:#os.listdir(get_path):
            file.write(i+'\n')
    return "Names are added"

def fake_names(files: list, enPath:str) ->str:
    '''
    This function assigns the files a fake name which makes the files unable to
    recognize. file->list is list containg the file from the dir. that is going to be encrytpted.
    '''
    #files = os.listdir(enPath)
    total = len(files)
    fake = range(total)
    for i in range(len(files)):
        os.rename(os.path.join(enPath,files[i]),os.path.join(enPath,str(fake[i])).zfill(5))
    return "Fake names are given."

def encryption(safe :str,path :str) ->str:
    """
    This function takes one argument path -> str which you want to encrypt.
    And generate a key that will be used to decrypte the files in the future.
    file->list is list containg the file from the dir. that is going to be encrytpted.
    """
    os.chdir(path)
    files = os.listdir()
    key = Fernet.generate_key()#key generated
    with open(f'{safe}\\TheKey.key',"wb")  as thekey:
        thekey.write(key)

    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_encrypted)
    return "Files have been encrypted"

def decryption(files: list,safe: str,path : str) ->str:
    '''Decrypts the files using the key.
       path-> str is the path of the dir. you want to dencrypt.
       file->list is list containg the file from the dir. that is going to be decrytpted.'''

    os.chdir(path)
    #files = os.listdir()
    with open(f'{safe}\\TheKey.key',"rb")  as key:
        secertKey = key.read()#stored the key in secertKey variable

    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secertKey).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
    return ("Files have been decrypted")

def realName(safe: str,path: str)->str:
    '''
    Gives the files their real names.
    path-> str is the path of the dir. you decrypted.
    '''

    os.chdir(path)
    files = os.listdir()
    with open(f'{safe}\\names.txt','r') as name:
        data = name.read()
    names = data.split('\n')
    names.remove('')
    for i in range(len(files)):
        os.rename(files[i],names[i])
    os.chdir(safe)
    for i in ["names.txt","TheKey.key","Encrypt_dir.txt"]:
        send2trash(i)
    return("Original names are given back to the files")

def testrestore():
    try:
        os.rename(os.path.join(os.getcwd(),"Test/0"),os.path.join(os.getcwd(),"Test/0.png"))
        os.rename(os.path.join(os.getcwd(),"Test/1"),os.path.join(os.getcwd(),"Test/1.png"))
        return "Done"
    except FileNotFoundError:
        return "Error"
