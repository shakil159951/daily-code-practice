filename = "note.txt"

# Writing to a file
with open(filename, "w") as file:
    file.write("Python was named after Monty Python, not the snake.")

# Reading from a file
with open(filename, "r") as file:
    content = file.read()
    print(f"File content: {content}")
