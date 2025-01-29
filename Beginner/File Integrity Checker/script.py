import sys
import hashlib
import os



def hashfile(file):
    BUF_SIZE = 65536

    sha_256 = hashlib.sha256()

    with open(file, "rb") as f:
        while True:
            data = f.read(BUF_SIZE)

            if not data:
                break

            sha_256.update(data)
    
    return sha_256.hexdigest()

if len(sys.argv) < 3:
    print("Usage: python [scriptname].py <file1_path> <file2_path>")


file1_path = sys.argv[1]
file2_path = sys.argv[2]


if not os.path.isfile(file1_path):
    print(f"Error: {file1_path} is not a file or cannot be accessed.")
    sys.exit(1)

if not os.path.isfile(file2_path):
    print(f"Error: {file1_path} is not a file or cannot be accessed.")
    sys.exit(1)


try:
    hash1 = hashfile(file1_path)
    hash2 = hashfile(file2_path)
    print(f"Hash of {file1_path}: {hash1}")
    print(f"Hash of {file2_path}: {hash2}")

    if hash1 == hash2:
        print("Both files are identical.")
    else:
        print("Both files are different.")

except FileNotFoundError:
    print("Error: The specified file was not found.")
except PermissionError as e:
    print(f"Error: Permission denied. {e}")
except Exception as e:
    print(f"Error: {e}")



