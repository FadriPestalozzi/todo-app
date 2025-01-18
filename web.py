import streamlit as st
import functions

todos = functions.get_todos()

st.title('My Todo App')
st.subheader('Type in a to-do')
st.text('This app is to increase your productivity1')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Enter a todo...')
