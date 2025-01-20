import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state['todo_input'] + '\n'
    todos.append(local_todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('Type in a to-do')
st.text('This app is to increase your productivity1')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='todo_input', label_visibility='collapsed',
              placeholder='Enter a todo...',
              on_change=add_todo, key='todo_input')
