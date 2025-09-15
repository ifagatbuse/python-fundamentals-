# Project 21: File Reader
# Topic: Reading text files safely with context managers

file_path = "sample.txt"  

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()  
    print("File content:\n")
    print(content)
except FileNotFoundError:
    print(f"Error: '{file_path}' was not found. Create it and try again.")
