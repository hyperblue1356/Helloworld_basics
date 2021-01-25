# Tuples are immutable, use tuples to avoid data being changed and causing errors.
# If data in tuple needs to be changed create a list from tuple as below, then change list. This way tuple stays intact.

yulia = [("welcome home sunshine", "Let me show you the master bedroom", "hello"),
         ("is blue", "is old", "hello"),
         ("is red", "has writing", "hello")
         ]

for burp, thing, things in yulia:
    print("statement 1: {}, statement 2: {}, statement 3: {}".format(burp[0], thing[1], things[2]))

# print(yulia)
# #print(yulia[0])
# #print(yulia[1])
# #print(yulia[2])
# statement_1, statement_2, statement_3 = yulia
# print(statement_1)
# print(statement_2)
# print(statement_3)
# table = ("coffee table", 200, 100, 75, 34)
# print(table[1] * table[2])
# name, length, width, height, price = table
# print(length * width)
# print(str(yulia))