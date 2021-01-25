import random

highest= 10
answer= random.randint(1, highest)

guess = 0
print("please guess a number between 1 and {}:".format(highest))

while guess != answer:
    guess = int(input())
    if guess == "exit".casefold():
        break
    if guess == answer:
        print("good job")
        break
    else:
        if guess < answer:
            print("go higher!")
        else:
            print("guess lower")






# if guess < answer:
#     print("nope, try again")
#     guess=int(input())
#     if guess == answer:
#         print("nice job!")
#     else:
#         print("nah, wrong again")
# elif guess> answer:
#     print("go down!")
#     guess=int(input())
#     if guess == answer:
#         print("nice job!")
#     else:
#         print("nah, wrong again")
# else:
#     print("well done!")