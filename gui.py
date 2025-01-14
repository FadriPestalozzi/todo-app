import functions
import FreeSimpleGUI as sg
import time

sg.theme('Black')

clock = sg.Text('',key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button(image_source=r'img\add.png', mouseover_colors='lightblue',
                       tooltip='Add todo', key='Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button(image_source=r'img\edit.png', mouseover_colors='lightblue',
                        tooltip='Edit todo', key='Edit')
complete_button = sg.Button(image_source=r'img\complete.png', mouseover_colors='lightblue',
                            tooltip='Complete todo', key='Complete')
exit_button = sg.Button(image_source=r'img\exit.png', mouseover_colors='lightblue',
                        tooltip='Exit', key='Exit')

# window = mother instance of the gui
# layout = list of lists to populate gui rows
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]
                           ],
                   font=('Helvetica', 20))

while True:
    # display gui and await user interaction
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]  # since value is a list, use [0] to access string inside
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case 'Exit':
            break
        case 'todos':  # user selected listbox entry
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
