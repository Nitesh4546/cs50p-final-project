import securityfun as sf
import sys, os

def main_en():
    get_path = input("Path: ").strip()
    #Checks for the validity of the path emtered
    if not sf.valid_path(get_path):
        sys.exit("Invalid")
    
    #Imp. variables & imp.condition checks
    safe = os.path.join(os.getcwd(),"Data")
    files = os.listdir(get_path)
    if len(files) > 150:
        sys.exit("The path have file more than 250(max. limit)")

    #Recodring the dir. in txt file
    print(sf.writePath(safe, get_path))

    #Adding the file names to the txt file
    print(sf.add_files(safe, files))

    #Giving files fake names
    print(sf.fake_names(files,get_path))

    #Encrypting the files
    print(sf.encryption(safe, get_path))


if __name__=="__main__":
    main_en()