import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state['new_todo'] + '\n'
    todos.append(local_todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('Type in a to-do')
st.text('This app is to increase your productivity1')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='todo_input', label_visibility='collapsed',
              placeholder='Enter a todo...',
              on_change=add_todo, key='new_todo')

st.session_state