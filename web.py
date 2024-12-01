import streamlit as s
import modules.functionsapp1 as func

# to run this, go to terminal and write streamlit run web.py

# order matters here
todos = func.get_todos()
s.title("My To-Do App")
s.subheader("This is my todo app")
s.write("This app is to increase your productivity.")
s.checkbox("Buy groceries")

for todo in todos:
	s.checkbox(todo)


s.text_input(label="Enter a todo:", placeholder="Add new todo...")  # you have to write label


print("Hello")  # each time we reload our page, it writes Hello
