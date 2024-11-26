FILEPATH = "../todos.txt"


def get_todos(filepath=FILEPATH):  # filepath is a parameter here
	""" Read a text file and return the list of to_do items."""
	with open(filepath, "r") as file_local:
		todos_local = file_local.readlines()  # the type of todos in here is a list
	return todos_local



def write_todos(todos_arg, filepath=FILEPATH):  # if we had wrote todos_arg after filepath, we would get an error because it's not a default value
	""" Write a to_do items list in the text file."""
	with open(filepath, "w") as file_local: # w overrides that file, basically it creates a new file with that name, and then it writes the lists in that file
		file_local.writelines(todos_arg)  # writelines as an output gets a list
# this function will return None

print("Hello from the functionsapp1!")
print(__name__)  # if we print __name__ here, we will get __main__, because we execute it here
# in other words it's value is __main__ only if we execute functionsapp1.py directly
# if you import functionsapp1 in app.py file and then execute app.py, the value of __name__ is now functionsapp1 now
# to sum it up, when you run app.py and app.py runs functionsaap1.py through an import statement, then the value of __name__ is the name of that file. functionsapp1 in this case
# but when you run functionsapp1.py directly, the value of that variable is __main__
# __name__ is a variable, a variable which is defined hiddenly by python
print(type(__name__))  # it's a string

if __name__ == "__main__":  # why we wrote this if condition? because we wanted these lines under the if block to only execute when we run this particular file
	print("Hello you are in functionsapp1 file.")
	print(__name__)
	print(get_todos())
	print(help(get_todos))  # without ()
	print("-" * 40)