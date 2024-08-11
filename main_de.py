import securityfun as sf
import sys,os

def main_de():
    if len(os.listdir(os.path.join(os.getcwd(),"Data"))) != 3:
        sys.exit("No files in  the data folder.")
    with open(f'{os.path.join(os.getcwd(),"Data")}\\Encrypt_dir.txt','r') as file:
        get_path = file.read().strip()
    #Checks for the validity of the path emtered
    if not sf.valid_path(get_path):
        sys.exit("Invalid")
    
    #Imp. variables & imp.condition checks
    safe = os.path.join(os.getcwd(),"Data")
    files = os.listdir(get_path)

    #Decrypting the files
    print(sf.decryption(files,safe,get_path))

    #Giving the real names to the files
    print(sf.realName(safe, get_path))

if __name__=="__main__":
    main_de()