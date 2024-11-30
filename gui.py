# the difference between break statement and exit() function is that exit() stops the program completely
# as soon as the interpreter executes exit(), then nothing else is executed
#  the break statement only stops the while loop from executing again
# so when the interpreter execute break, only the loop is stopped




import modules.functionsapp1 as func
import FreeSimpleGUI as FSG
# import PySimpleGUI as PSG

label = FSG.Text("Type in a to-do")
input_box = FSG.InputText(tooltip="Enter todo", key="todo")  # if we haven't wrote key="todo", it would have shown the index for example 0 or 1 for the key part of the dictionary

add_button = FSG.Button("Add")
edit_button = FSG.Button("Edit")
complete_button = FSG.Button("Complete")
exit_button = FSG.Button("Exit")

list_box = FSG.Listbox(values=func.get_todos(),
                       key="todos",
                       enable_events= True,
                       size=(45, 10))

layout = [[label],
          [input_box, add_button, edit_button, complete_button],
          [list_box, exit_button]]

window = FSG.Window("My To-Do App",
                    layout=layout,
                    font=("Helvetica", 12))
                         # font family, font size

print()
while True:  # while loop keeps the window open, otherwise with only one time pressing Add or Edit, the window would disappear
    event, values = window.read()  # because window.read() returns sth, we wanted to store it in a variable
    print(1, event)  # window.read() is a tuple for example ('Add', {'todo': 'Play', 'todos': [Jump]})
    print(2, values)  # its first item is the label of the button
    print(3, values["todo"])
    match event:
        case "Add":
            todos = func.get_todos()  # again because this function returns us an output, we had to store it
            new_todos = values["todo"].capitalize() + "\n"
            todos.append(new_todos)
            func.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]  # values["todos"] is a list with only one item, so we wrote [0] to access the string
            new_todo = values["todo"].capitalize() + "\n"
            todos = func.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            func.write_todos(todos)
            window["todos"].update(values=todos)
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = func.get_todos()
            todos.remove(todo_to_complete)
            func.write_todos(todos)
            window()
        # case FSG.WINDOW_CLOSED:
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break  # if we had replace break with exit() function
                # which is a builtin function, the lines below it, would never execute,
                # so Bye would not be shown after we check the zarbedar

print("Bye")
window.close()





