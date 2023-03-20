import streamlit as st

import functions


todolist = functions.get_todolist()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todolist.append(todo_local)
    functions.write_todolist(todolist)


st.title("My todo App")
st.subheader("This is my Todo-App.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todolist):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todolist.pop(index)
        functions.write_todolist(todolist)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new To-Do...",
              key="new_todo", on_change=add_todo)

