# having intermediate variables makes it easier to debug, but it's really about your preference
# True == 1 -> True     False == 0 -> True     False + 1 = 1     Everything except 0 which ia False, consider True
# if(75.2 + 3j): print("Hi") -> it will print Hi   or    if(-4): print("Hi") -> it will also print Hi
# limit all lines to the maximum of 79 character.
# py console is only use for throw away code, like quick code that you want to test out how it works
# py console pro: you can quickly get output
# py console com: the code is lost once you close the console
# if you don't use () for methods, the output simply just says that this is a method
# capitalize method only capitalize the very first letter of a sentence, but title method capitalize every first letter of a word
# if you don't specify anything in the (), it would be spaces by default
# there is nothing that a list comprehension does that a for-loop doesn't.
# The opposite is not true meaning in certain cases the for-loop is the only way around.
# The rule of thumb is if you can do something with a list comprehension, do it as it is less code than a for-loop.
# here are two types of files, binary and non-binary.
# Non-binary files are files such as .txt, .csv, .py, .html, .json, and any other file whose content can be viewed on any text editor program
# Match-case is generally faster. If you can use it, do so.
# However, match-case is more limited. It can only check if one value is equal to another.
# It cannot check if one value is less/greater than another, or other more complex conditions. For such advanced conditions, you should use if-elif-else
# in with contexts manager, you don't need to close the program. even if there was an error in one of the with block lines, with will automatically close our file.
# enumerate:
# a = ["x", "y", "z"]
# print(enumerate(a))  #
# print(list(enumerate(a)))  # if you convert enumerate function to a list, this is what we get, a list of tuples. but if we convert it to a string using str(), we'll see '<enumerate object at ...>'
# for i, j in enumerate(a):
# 	print(i + 1, ".", j)
# zip:
# a = [1, 2, 3]
# b = [10, 20, 30]
# print(zip(a, b))
# print(list(zip(a, b)))  # zip is also a list of tuples

from modules.functionsapp1 import get_todos, write_todos
from modules import functionsapp1
# from modules import functionsapp1
from time import strftime  # this a standard module
# in this case we have to write modules.functionsapp1 , because app.py and functionsapp1.py are not in the same directory
# if they were in the same directory, we could just scipe the modules. part
print(functionsapp1)
#          month day, year hour:minute      %m shows the number of the month, for example 05    %b -> name of the month, for example April
now = strftime("%b %d, %Y %H:%M")
print("This is time below.")
print("it's", now)
print(dir(functionsapp1))


while True:
	user_action = input("Type add, show, edit, complete or exit: ")  # if we had used strip in here it wouldn't be saved
	user_action = user_action.strip()

	if user_action.startswith("add") or user_action.startswith("new"): # you can't use expressions after case, case only expects a pattern such as a string. so we changed match-case to if-else.
		todo = user_action[4:].capitalize() + "\n"
		# todo = user_action.strip("add ") + "\n"

		todos = get_todos()  # "files/todos.txt" is a argument value

		todos.append(todo)  # todo is a str so we could also write todos.append(todo + "\n") instead of doing it like this in some lines above: todo = user_action[4:].capitalize() + "\n"
		# append is a list method
		# to see todos is a list write print(todos)

		write_todos(todos)

	elif user_action.startswith("show"):

		todos = get_todos()

		if len(todos) == 0:
			print("Your todo list is empty.")
		else:
			for index, item in enumerate(todos):
				print(f"{index + 1}.{item.strip("\n")}")  # f-string
				# print("{}.{}".format(index + 1, item))  # format
				# print(index + 1, ".", item, sep="")
			# if we had wrote print(index, item) outside this for loop, we would get the last (index, item).

	elif user_action.startswith("edit"):

		try:

			number = int(user_action[5:])

			if number < len(todos):
				todos = get_todos(filepath="todos.txt")

				new = input("Enter the new todo: ").capitalize()
				todos[number - 1] = new + "\n"

				write_todos(todos)

			else:
				print(f"There is no item with that number. You only have {len(todos)} todo items.")

		except ValueError as V:
			print(V)  # this will produce this: invalid literal for int() with base 10:
			print("Your command is invalid! You should write a number after edit.")
			continue  # continue statement will ignore everything that comes underneath it and will goe back again to the beginning of the while loop

	elif user_action.startswith("complete"):

		try:
			number = int(user_action[9:])

			todos = get_todos()

			index = number - 1
			todo_to_remove = todos[index].strip("\n")  # if you execute the code on the line below, you'll see that todo_to_remove actually had a \n at the end of it
			# so when we print(F"Todo {todo_to_remove} was removed from your list successfully."), it showed sth like this Todo Clean
			#  was removed from your list successfully.
			# print(repr(todo_to_remove))

			todos.pop(index)  # pop
			# todos.remove(todos[number - 1])  # remove

			write_todos(todos)

			print(F"Todo {todo_to_remove} was removed from your list successfully.")
		except IndexError as I:
			print(I)
			print(f"There is no item with that number. You only have {len(todos)} todo items.")
			continue
	elif "exit" in user_action:
		break

	else:
		print("You entered an unknown command")

print("See You Next Time.")
