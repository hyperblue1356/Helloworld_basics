available_things = ["david's dick", "barbies apparently", "a coffee shop", "a better laptop", "mochi"]

yulias_options = []
for i in range (1, len(available_things) + 1):
    yulias_options.append(str(i))

print(available_things)

current_choice = []
yulias_things = []
print("Which option would you like?")

if current_choice in yulias_options:
    yulias_things.append(current_choice)

while current_choice != '0':
    if current_choice in yulias_options:
        print("adding {}".format(current_choice))
        index = int(current_choice) - 1
        current_choice = available_things[index]
        yulias_things.append(current_choice)
    else:
        print("please choose another option")
        for number, part in enumerate(available_things):
            print("{0}: {1}".format(number +1, part))
        print("please add option from below list:")

    current_choice = input ()

print(yulias_things)

print(len(available_things))