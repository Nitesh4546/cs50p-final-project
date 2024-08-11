# File Security Project

This project provides a way to secure your files using encryption (via the `cryptography` library in Python). Encryption ensures that your files are protected from unauthorized access, a practice that dates back long before the advent of computers. Today, as we store more sensitive information on computers, securing this data is crucial.

While working on this project, I sometimes encrypted my files and forgot to store the encryption keys `:|`(hopefully, you won't do that `:)`).


## Video Demo:

[Watch the video demo here](#)(https://www.youtube.com/watch?v=dwiXy3zxQvA)

## Description

The project includes files that secure your files (stored in a folder) using encryption.

## Table of Contents

1. [Description and Explanation of Files](#1-description-and-explanation-of-files)
2. [Libraries Used](#2-libraries-used)
3. [Steps to Use](#3-steps-to-use)

## 1. Description and Explanation of Files

The project consists of four Python files and a test folder with images. Here's an explanation of each file:

### i) `securityfun.py`

This file is the core of the project. It contains functions for validating the path, encrypting files, decrypting files, and more. Without this file, the other files are useless.

### ii) `main_en.py`

This file takes the path of the folder containing the files you want to encrypt (avoid having any subfolders along with the files). After encrypting, it saves `Encrypt_dir.txt`, `names.txt`, and `TheKey.key` in the `Data` folder. Handle these files with care—any changes (like renaming or editing the content) can cause you to lose your data. These files will be used to decrypt the files in the future. You can store these files in another location. This file also assigns fake names to the files, making them unpredictable in terms of file type, even to you.

### iii) `main_de.py`

This file checks if `Encrypt_dir.txt`, `names.txt`, and `TheKey.key` are in the `Data` folder. Using these files, it decrypts the files, restores their original names and data types, and makes them readable.

### iv) `test_security.py`

This test file was created to clear the conditions for the final project. It tests four functions. The `Test` folder with images was created to test the functions. The images are from Duolingo, just to show off my scores.

## 2. Libraries Used

The project uses the following libraries:

- `cryptography`: For encryption and decryption.
- `sys`: To exit the code when an error occurs.
- `os`: To find files and check the validity of the path.
- `send2trash`: To send files to the recycle bin.

## 3. Steps to Use

### First:

Open the folder `CS50_Project` and in the path bar, type:

```bash
pip install -r requirements.txt
```
### Second
Open the CS50_Project folder in cmd and run: 
```
python main_en.py
```
Enter the path of the folder without quotes. Example: C:\User\name\folderpath

### Third
To decrypt the files, move Encrypt_dir.txt, names.txt, and TheKey.key back to the Data folder. Open CS50_Project folder in command prompt and type:
```
python main_de.py
```
Run it to decrypt the files.

Watch the video for a deeper understanding of the instructions.

# Requirements
1. Python compiler
2. Must excuete the step 3 of installing python lib
# Contact
1. Email:- niteshnunia91@gmail.com
2. GitHub:-Nitesh4546
