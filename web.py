import streamlit as st
import Functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    Functions.write_todos(todos)

todos = Functions.get_todos()

st.title('My Checklist')
st.subheader('This is my checklist')
st.write('This app is to increase your productivity'
         ' by allowing you to keep track of tasks that need '
         'to be completed.')


for todo in todos:
    st.checkbox(todo)

st.text_input(label='Enter a task that needs completion: ', placeholder="Enter a task: ",
              on_change=add_todo, key='new_todo')


print("hello")

st.session_state