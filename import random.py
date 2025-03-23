import random


def compare_number(number, user_guess):
    cowbull = [0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[I]:
           cowbull[1] += 1
        else:
           cowbull[0] += 1
    return cowbull


if __name__ == "__main__":
    playing = True
    number = str(random.randint(1000, 10000))
    guesses = 0

    print("Let's Play A Game Of Cows And Bulls!")
    print("I Will Generate A 4 Digit Number, And You Have To Guess The Numbers One Digit At A Time.")
    print("For Every Number I The Wrong Place, You Get A Bull. For Every Number In The Right Place, You Get A Cow.")
    print("The Game Will End When You Get 4 Bulls.")
    print("Type Exit At Any Prompt To Exit!")

while playing:
    user_guess = input("Give Me The Best You Got!: ")
    if user_guess.lower() == "exit":
        break
    cowbull_count = compare_number(number, user_guess)
    guesses += 1
    print(f"You Have {cowbull_count[1]} Cows, And {cowbull_count[0]} Bulls.")

    if cowbull_count[1] == 4:
        playing = False
        print(f"You Win The Game After {guesses} Guess(es)!. The Number Was {number}.")
        break
    else:
        print(f"Your Guess Isn't Quite Right, Tyr Again!.")