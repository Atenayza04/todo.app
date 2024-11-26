import modules.functionsapp1
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a to-do")
input_box = FSG.InputText(tooltip="Enter todo")
add_button = FSG.Button("Add")

window = FSG.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()


