'''
Description:
This program is a number guessing game where the user has to guess a secret number chosen by the computer.
The user can choose the difficulty level (easy, medium, hard) which determines the range of numbers.
The program provides feedback on whether the guessed number is too high or too low and keeps track of the user's guesses.
The game continues until the user guesses the correct number or chooses to exit.

AI Used: ChatGPT; also labelled as "AI" in the code comments.
'''
import turtle as trtl
import random as rand

# Setup turtle screen
# Other Student 
window = trtl.Screen()
window.bgcolor("aquamarine")
window.title("Number Guessing Game")

# Setup turtle for displaying text
message_writer = trtl.Turtle()
message_writer.penup()
message_writer.hideturtle()

user_guessed_numbers = []
text_position = 150

# Other Student
message_writer.goto(0, text_position)
message_writer.write("Welcome to the Number Guessing Game!", align="center", font=("Courier", 16, "bold"))
message_writer.penup()

# Function to choose difficulty level
def choose_mode():
    while True:
        choose_level = window.textinput("Choose a level", "Easy, Medium, or Hard").lower().strip()
        if choose_level in ("easy", "medium", "hard"):
            return choose_level

        else:
            message_writer.clear()
            message_writer.goto(0, text_position)
            message_writer.write("Invalid mode! Please choose again: Easy, Medium, or Hard.", align="center", font=("Times new roman", 16, "normal"))


# Other Student
def reset_game(choose_level):
    global max_number
    user_guessed_numbers.clear()

    if choose_level == "easy":
        max_number = 31
    elif choose_level == "medium":
        max_number = 51
    elif choose_level == "hard":
        max_number = 101
    else:
        max_number = 31

    secret_number = rand.randint(1, max_number - 1)

    message_writer.clear()

    return secret_number


def start_game(player_name):
    global max_number
    choose_level = choose_mode()
    secret_number = reset_game(choose_level)

    message_writer.clear()
    message_writer.goto(0, text_position)
    message_writer.write("Hello, " + player_name + "! Let's begin!", align="center", font=("Courier", 16, "bold"))
    
    while True:
        user_input = window.textinput(player_name + "'s Guess", "Enter your guess (1 to " + str(max_number - 1) + "): ")
        if user_input is None: # AI: helped us how to use none in if statement
            message_writer.clear()
            message_writer.write("Game cancelled. Thanks for Playing!", align="center", font=("Courier", 16, "normal"))
            break

        if not user_input.isdigit(): # AI: helped us how to use not in if statement
            message_writer.clear()
            message_writer.goto(0, text_position)
            message_writer.write("Invalid input. Please enter a number.", align="center", font=("Courier", 16, "normal"))
            continue

        user_guess_number = int(user_input)
        if user_guess_number < 1 or user_guess_number >= max_number:
            message_writer.clear()
            message_writer.goto(0, text_position)
            message_writer.write("Your guess must be between 1 and " + str(max_number - 1), align="center", font=("Courier", 16, "normal"))
            continue

        user_guessed_numbers.append(user_guess_number)
        message_writer.clear()

        if user_guess_number < secret_number:
            message_writer.goto(0, text_position)
            message_writer.write("Your value is lower.", align="center", font=("Courier", 16, "normal"))
        elif user_guess_number > secret_number:
            message_writer.goto(0, text_position)
            message_writer.write("Your value is higher.", align="center", font=("Courier", 16, "normal"))
        else:
            message_writer.goto(0, text_position)
            message_writer.write("Congratulations, " + player_name + "!", align="center", font=("Courier", 16, "bold"))
            message_writer.goto(0, text_position - 30)
            message_writer.write("The secret number was: " + str(secret_number), align="center", font=("Courier", 16, "normal"))
            message_writer.goto(0, text_position - 60)
            message_writer.write("Your guesses were: " + str(user_guessed_numbers), align="center", font=("Courier", 12, "normal"))
            message_writer.goto(0, text_position - 90)
            message_writer.write("Total tries: " + str(len(user_guessed_numbers)), align="center", font=("Courier", 16, "normal"))

            play_again = window.textinput("Play Again", "Do you want to play again? (yes/no): ").lower().strip()
            if play_again == "yes":
                difficulty_level = choose_mode()
                secret_number = reset_game(difficulty_level)
            else:
                message_writer.clear()
                message_writer.goto(0, text_position - 50)
                message_writer.write("Thanks for playing! Goodbye!", align="center", font=("Courier", 16, "normal"))
                break

# Asks for player name and start game
player_name_input = window.textinput("Welcome!", "What's your name?")
if player_name_input:
    start_game(player_name_input)
else:
    start_game("Player")  

window.mainloop()
