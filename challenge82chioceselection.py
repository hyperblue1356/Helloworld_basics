# available_exits = ["north", "south", "East", "west"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     if chosen_exit.casefold() == "that way":
#         print("which way?")
#     chosen_exit = input("please choose a direction")
#     if chosen_exit.casefold() == "quit":
#         print("cya")
#         break

# print("Finally, he left, thank god")

print("Let's plan your day: you can...")
print("\t1. Slam some booty.")
print("\t2. Take yulias virginity.")
print("\t3. Slam some more booty.")
print("\t4. Stay at home.")
print("\t5. Finish this course")


while True:
    user_choice = int(input("pick an option"))
    if user_choice >= 5 or user_choice == 0:
        break
    if user_choice == 1:
        print("go get it son")
    elif user_choice == 4:
        print("use your weak hand")
    elif user_choice == 2:
        print("go get it son")
    elif user_choice == 3:
        print("rain hell upon the women folk")
        break

print("we could knock a few off the list today actually")
user_choice = int(input("pick an option"))
if user_choice in range (1, 4):
    print("that's a good combo")

while user_choice >= 5:
    print(" try again")
    user_choice = int(input("pick an option"))
    if user_choice >= 5 or user_choice == 0:
        break
    if user_choice == 1:
        print("go get it son")
    elif user_choice == 4:
        print("use your weak hand")
    elif user_choice == 2:
        print("go get it son")
    elif user_choice == 3:
        print("rain hell upon the women folk")
    break

for user_choice in 0, 1:
    print(" oh oh oh ")
















