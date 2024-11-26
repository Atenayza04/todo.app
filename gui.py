import modules.functionsapp1 as func
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a to-do")
input_box = FSG.InputText(tooltip="Enter todo", key="todo")
add_button = FSG.Button("Add")
edit_button = FSG.Button("Edit")
complete_button = FSG.Button("Complete")


window = FSG.Window("My To-Do App",
					layout=[[label], [input_box, add_button]],
					font=("Helvetica", 15))

print()
while True:  # while loop keeps the window open
	event, values = window.read()
	print(event)
	print(values)
	match event:
		case "Add":
			todos = func.get_todos()
			new_todos = values["todo"].capitalize() + "\n"
			todos.append(new_todos)
			func.write_todos(todos)
		case FSG.WINDOW_CLOSED:
			break

window.close()


