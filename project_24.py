# Project 24: To-Do List CLI
# Topic: Lists + loops + file writing

tasks = []
print("Simple To-Do (type 'q' to finish)\n")

while True:
    task = input("Add a task: ").strip()
    if task.lower() == "q":
        break
    if task:
        tasks.append(task)
        print(f"Added: {task}")
    else:
        print("Empty task ignored.")


out_file = "tasks.txt"
with open(out_file, "w", encoding="utf-8") as f:
    for t in tasks:
        f.write(t + "\n")

print(f"\nSaved {len(tasks)} task(s) to '{out_file}'.")
