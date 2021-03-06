low = 1
high = 1000
print("please think of a number between {} and {}".format(low, high))
input("press ENTER to start")

guesses: int = 1
while low != high:
    #print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     "Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()

    if high_low == "h":
        # guess higher
        low = guess + 1
    elif high_low == "l":
        # guess lower
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("please enter h, l or c")
    guesses = guesses +1
else:
    print("you thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))