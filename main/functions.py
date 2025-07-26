import os

# Always use path relative to this file
FILEPATH = os.path.join(os.path.dirname(__file__), "totos.txt")

def get_todos(filepath=FILEPATH):
    """Reads a text file and returns the list of to-do items."""
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass  # Create empty file if not found
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        print("Reading from:", filepath)

    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Writes the to-do items list to the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print("Hello from functions")

