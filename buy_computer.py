available_parts = [
    ("what do you want?",
     [
         (1, "computer"),
         (2, "monitor"),
         (3, "keyboard"),
         (4, "mouse"),
         (5, "mouse mat"),
         (6, "hdmi cable")
     ]
     ),

    ("How about a whole one?",
     [
         (1, "desktop"),
         (2, "Laptop"),
         (3, "tablet")
     ]
     )
]

print(available_parts)
print("=============================")
print(available_parts[0][1][3])

print("================================================")

for i in enumerate (available_parts):
    print(i)




# valid_choices = []
# for i in range(1, len(available_parts) + 1):
#     valid_choices.append(str(i))
#     print(valid_choices)
# current_choice = "_"
# computer_parts = []  # create an empty list
#
# while current_choice != '0':
#     if current_choice in valid_choices:
#         index = int(current_choice) - 1
#         chosen_parts = available_parts[index]
#         if chosen_parts in computer_parts:
#             # it's already in so remove it
#             print("removing {}".format(current_choice))
#             computer_parts.remove(chosen_parts)
#         else:
#             print("adding {}".format(current_choice))
#             computer_parts.append(chosen_parts)
#             print("your list now contains: {}".format(chosen_parts))
#
#     else:
#         print("please add option from below list:")
#         for number, part in enumerate(available_parts):
#             print("{0}: {1}".format(number +1, part))
#         print("please add option from below list:")
#
#     current_choice = input()
#
# print(computer_parts)