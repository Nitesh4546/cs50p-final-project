# 🔐 SecureShield: File Encryption & Obfuscation Suite

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CS50 Final Project](https://img.shields.io/badge/CS50-Final%20Project-red?style=flat)](https://cs50.harvard.edu/)
[![Cryptography](https://img.shields.io/badge/Security-Cryptography%20Fernet-blue?style=flat&logo=letsencrypt&logoColor=white)](https://cryptography.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end symmetric encryption and file-name obfuscation tool built in Python. **SecureShield** locks down entire directories by encrypting file contents and masking their names/extensions, preventing unauthorized inspection and tampering.

---

## 📺 Video Demo

[![Watch the Video Demo](https://img.shields.io/badge/YouTube-Watch%20Demo%20Video-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=dwiXy3zxQvA)

---

## ✨ Features

- **Robust Symmetric Encryption:** Uses the industry-standard `cryptography` library (AES-based Fernet) to encrypt file data.
- **File Metadata & Type Obfuscation:** Masks original file names and extensions with randomized placeholders so file types cannot be identified by sight.
- **Automated Key & Metadata Management:** Automatically generates and stores encryption keys and restoration mappings in a dedicated `Data/` directory.
- **One-Click Reversible Decryption:** Restores original filenames, formats, and contents seamlessly.
- **Safe File Operations:** Uses `send2trash` for non-destructive local cleanup.
- **Automated Unit Testing:** Includes test coverage for core security and validation routines.

---

## 📁 Repository Structure

```text
CS50_Project/
│
├── Data/                 # Stores generated keys and restoration maps (keep safe!)
│   ├── Encrypt_dir.txt   # Target folder path registry
│   ├── names.txt         # Obfuscated-to-original filename mapping
│   └── TheKey.key        # Generated Fernet symmetric encryption key
│
├── Test/                 # Sample files and test assets
│
├── securityfun.py        # Core utility library (validation, cipher routines)
├── main_en.py            # CLI entry point for folder encryption & obfuscation
├── main_de.py            # CLI entry point for folder decryption & restoration
├── test_security.py      # Unit test suite for validation & crypto helpers
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

```

---

## 🛠️ Module Breakdown

| File | Purpose |
| --- | --- |
| `securityfun.py` | **Core Engine:** Contains fundamental logic for path validation, key creation, file-stream encryption/decryption, and directory manipulation. |
| `main_en.py` | **Encryption Pipeline:** Prompts for target folder, generates `TheKey.key`, scrambles file names, encrypts file payloads, and saves mapping metadata. |
| `main_de.py` | **Decryption Pipeline:** Reads key and mapping files from `Data/`, decrypts contents, and recovers original filenames and file types. |
| `test_security.py` | **Unit Tests:** Validates core functions to ensure reliability across edge cases and path validation. |

---

## 🚀 Getting Started

### Prerequisites

* [Python 3.8+](https://www.python.org/downloads/)
* `pip` package manager

### 1. Clone & Install Dependencies

Clone the repository and install required third-party packages:

```bash
git clone [https://github.com/Nitesh4546/File-Security-Project.git](https://github.com/Nitesh4546/File-Security-Project.git)
cd CS50_Project
pip install -r requirements.txt

```

*(Or install packages manually):*

```bash
pip install cryptography send2trash pytest

```

---

## 📖 Usage Guide

### 🔒 Encrypting a Folder

1. Run the encryption script:
```bash
python main_en.py

```


2. When prompted, enter the absolute path to your target directory (without quotes):
```text
Enter folder path: C:\Users\Username\Documents\ConfidentialFiles

```


3. The script will:
* Encrypt each file in-place.
* Assign fake names/extensions to obscure file types.
* Generate `TheKey.key`, `names.txt`, and `Encrypt_dir.txt` inside the `Data/` folder.



> ⚠️ **IMPORTANT WARNING:**
> Store the contents of the `Data/` directory in a safe, secure backup location. **If you lose `TheKey.key` or edit `names.txt`, your encrypted data cannot be recovered.**

---

### 🔓 Decrypting a Folder

1. Ensure `TheKey.key`, `names.txt`, and `Encrypt_dir.txt` are placed in the `Data/` folder.
2. Run the decryption script:
```bash
python main_de.py

```


3. The script reads the saved directory path, decrypts all payloads, and restores original file names and extensions.

---

## 🧪 Running Tests

To verify that all cryptographic and validation routines are working properly:

```bash
pytest test_security.py

```

---

## 📦 Dependencies

* [`cryptography`](https://pypi.org/project/cryptography/) – Symmetric encryption implementation (`Fernet`)
* [`send2trash`](https://pypi.org/project/Send2Trash/) – Safe recycle-bin file deletion
* [`pytest`](https://pypi.org/project/pytest/) – Testing framework

---

## 👤 Author
[@Nitesh4546](https://github.com/Nitesh4546)
