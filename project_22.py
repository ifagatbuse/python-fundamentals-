# Project 22: File Writer (overwrite + append)
# Topic: Writing text files

notes_file = "notes.txt"


with open(notes_file, "w", encoding="utf-8") as f:
    f.write("My first note.\n")
    f.write("Python makes file writing easy!\n")


with open(notes_file, "a", encoding="utf-8") as f:
    f.write("This line was appended later.\n")

print(f"Notes saved to '{notes_file}'.")
