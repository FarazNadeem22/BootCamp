import random


def guess_random_number(tries, start, stop):
    """
    Use the random module to generate a random number between the start and stop integers, inclusive. 
    Write a while loop that loops as long as tries is not equal to 0. 
    Inside the while loop, print the number of tries remaining. 
    Prompt the user to input a guess.
    Compare the number guessed to the secret_num number (the random number you previously created).
    If they are equal, print a success message and return out of the function. 
    If the number guessed is less than the secret_num number, print "Guess higher!"
    If the number guessed is greater than the secret_num number, print "Guess lower!"
    Decrement the value of tries by 1.
    If the user does not successfully guess the number by the time that tries has reached the number 0 and the while loop exits, then print a failure message.

    Args:
        tries (int): Number of tries
        start (int): Lower limit of the number range, inclusive
        stop (int): Higher number of the number range , inclusive 
    """
    # Use the random module to generate a random number between the start and stop integers, inclusive.
    secret_num = random.randint(start, stop)
    

    #  Write a while loop that loops as long as tries is not equal to 0
    while tries > 0:

        #  Print the number of tries remaining.
        print(f"Number of tries left: {tries}")

        # Prompt the user to input a guess.
        while True:
            try:
                guess = int(
                    input(f"Guess a number between {start} and {stop}: "))
                if guess in range(start, stop):
                    tries -= 1
                    break
                else:
                    print(
                        f"Your guess {guess} has to be with in the range ({start}, {stop})")
            except:
                print("Please enter and integer")

        # Compare the number guessed to the secret_num number (the random number you previously created)
        if guess == secret_num:
            #  Print a success message and return out of the function.
            print("You guessed the correct number!")
            return
        elif guess < secret_num:
            # If the number guessed is less than the secret_num number, print "Guess higher!"
            if tries != 0:
                print("Guess higher")
        elif guess > secret_num:
            # Guessed is greater than the secret_num number, print "Guess lower!"
            if tries != 0:
                print("Guess lower")

    # If the user does not successfully guess the number by the time that tries has reached the number 0 and the while loop exits, then print a failure message.
    print(f"You failed to guess the number: {secret_num}")
    return


def guess_random_num_linear(tries, start, stop):
    """
    Use the random module to generate a random number between the start  and stop integers, inclusive. 
    Write code that implements the linear search algorithm to compare each integer in the potential range to the randomly generated secret_num number.
    Hint: You can use a for loop to help with this. 
    Every time the computer makes a comparison, that is one guess. Decrement the tries variable and stop the function (using return) when there are no more tries left.
    Show the secret_num number, show each guess that the computer makes, and show appropriate success/failure messages. 

    Args:
        tries (int): Number of tries
        start (int): Lower limit of the number range, inclusive
        stop (int): Higher number of the number range , inclusive 
    """
    # Use the random module to generate a random number between the start and stop integers, inclusive.
    secret_num = random.randint(start, stop)

    # Write code that implements the linear search algorithm to compare each integer in the potential range to the randomly generated secret_num number.
    print(f"The number for the program to guess is: {secret_num}")
    for i in range(start, stop):
        print(f"The number of tries left: {tries}")
        tries -= 1
        print(f"The number the program is guessing ... {i}")
        if i == secret_num:
            print(f"Number {secret_num} found with {tries} remaining")
            return
        if tries == 0:
            break
    print(f"The function failed to guess the number {secret_num}")


def guess_random_num_binary(tries, start, stop):
    """
    Use the random module to generate a random number between the start and stop integers, inclusive. 

     Args:
        tries (int): Number of tries
        start (int): Lower limit of the number range, inclusive
        stop (int): Higher number of the number range , inclusive 
    """
    secret_num = random.randint(start, stop)
 

    lower_bound = start
    upper_bound = stop

    lst = [i for i in range(start, stop)]

    print(f"Random number to find: {secret_num}")
    if ((start+stop)/tries**2) < 1:
        print("I can guarantee that the program will find the number")
    while tries != 0:
        tries -= 1
        pivot = (lower_bound + upper_bound)//2
        pivot_value = lst[pivot]

        if pivot_value == secret_num:
            print(f"Fount it! {secret_num}")
            return

        if pivot_value > secret_num:
            print("Guessing lower")
            upper_bound = pivot - 1
        else:
            print("Guessing higher")
            lower_bound = pivot + 1
    print(f"Program failed to find the number {secret_num}")


def get_option(name):
    """
    Get selection from  user and return it. Make sure that selection is valid

    Args:
        name (string): name of the user 

    Returns:
        int: Selection made by the user
    """
    print(f"Welcome {name}")
    print("*******************Options*****************")
    print("-------------------------------------------")
    print("|        Option No 1. Play yourself       |")
    print("|        Option No 2. Linear Search       |")
    print("|        Option No 3. Binary Search       |")
    print("|        Option No 4. Quit                |")
    print("-------------------------------------------")
    while True:
        try:
            selection = int(
                input(f"Make your selection: "))
            if selection in range(1, 5):
                break
            else:
                print(
                    f"Your selection need to be 1,2 ,3 or 4")
        except:
            print("Please enter and integer")
    return selection


def act_on_selection(selection):
    """
    Act accordingly to selection made
    get start, stop and tries

    Args:
        selection (int): The selection to act upon
    """
    # Get start, stop and tries
    while True:
        try:
            start = int(
                input(f"Enter starting point: "))
            break
        except:
            print("Please enter and integer")
    while True:
        try:
            stop = int(
                input(f"Enter ending point: "))
            break
        except:
            print("Please enter and integer")
    while True:
        try:
            tries = int(
                input(f"Enter the number of tries: "))
            break
        except:
            print("Please enter and integer")

    # Act on selection
    if selection == 1:
        guess_random_number(tries, start, stop)
    elif selection == 2:
        guess_random_num_linear(tries, start, stop)
    elif selection == 3:
        guess_random_num_binary(tries, start, stop)
    return


name = input("Please enter you name: ")

while True:
    selection = get_option(name)
    if selection == 4:
        print(f"Good bye {name}")
        break
    act_on_selection(selection)


#guess_random_number(5, 1, 10)
#guess_random_num_linear(5, 1, 10)
#guess_random_num_binary(5, 0, 100)
