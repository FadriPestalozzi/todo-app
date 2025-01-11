import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo')
add_button = sg.Button('Add')

# layout = list of lists to populate gui rows
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])

# display gui and await user interaction
window.read()

window.close()
