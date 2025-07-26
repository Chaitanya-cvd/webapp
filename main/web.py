import streamlit as st
import sys
import os

# Add path to your `functions.py`

from functions import get_todos, write_todos

todos = get_todos()

# Title and description
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# Handle checkbox completion
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")  # Unique key per item
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        st.rerun()  # Refresh the app after removal

# Add new todo
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)
    st.session_state["new_todo"] = ""  # clear input
    st.rerun()

st.text_input(label="Enter a todo",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")
