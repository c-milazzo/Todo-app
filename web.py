import streamlit as st
import Functions

todos = Functions.get_todos()

st.title('My Checklist')
st.subheader('This is my checklist')
st.write('This app is to increase your productivity'
         ' by allowing you to keep track of tasks that need '
         'to be completed.')


for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder="Enter a task: ")


print("hello")