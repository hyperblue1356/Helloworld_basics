available_exits = ["north", "south", "East", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    if chosen_exit.casefold() == "that way":
        print("which way?")
    chosen_exit = input("please choose a direction")
    if chosen_exit.casefold() == "quit":
        print("cya")
        break

print("Finally, he left, thank god")

print("will this change anything")