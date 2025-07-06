import streamlit as st
import sys
import os
sys.path.append(r"C:\Users\Chaitanya Deshpande\PycharmProjects\cvd\GUI")

import functions
todos = functions.get_todos()





st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for todo in todos:
    st.checkbox(todo.strip())

st.text_input(label="Enter a todo",placeholder="Add new todo")