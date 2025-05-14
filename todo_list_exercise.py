# interactive todo list 
header = """
print(*******************)
print(TO DO LIST APP)
print(*******************)
"""
print(header)
todos =[]
completed = []

while True:
    for i in range(len(todos)):
         print(f" {i + 1}) {todos[i]}")

    print("*"* 20)
    print("Enter a command. Type 'h' for help:")
    command = input ("> ")
    if command == "q":
        break
    elif command == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("to add a todo, type it and hit enter")
        print("to complete a todo, type its number in the task list")
    elif command.isnumeric():
         idx = int(command) - 1
         if idx >= len(todos):
            print("THERE IS NO TODO WITH THAT NUMBER")
         else:
            done_todo= todos.pop(idx)
            completed.append(done_todo)
    else:
        todos.append(command)
    #print todos from list
if completed:
    print(f"you completed {len(completed)} todos today): ")
    for todo in completed:
        print(f"* {todo}")

