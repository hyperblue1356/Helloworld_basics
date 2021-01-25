menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item, end=", ")

    else:
        print("There is {0} dollop of spam in this meal".format(meal.count("spam")))