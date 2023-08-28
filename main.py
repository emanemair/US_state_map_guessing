# Import necessary libraries
import turtle
import pandas as pd
from turtle import Turtle, Screen

# Load the data from a CSV file
us_data = pd.read_csv("50_states.csv")
state_name = us_data['state'].tolist()

# Set up the turtle graphics window
screen = Screen()
screen.title("US State")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Initialize variables
number_of_correct_guessing = 0
state_done = []

# Main loop to guess state names
while number_of_correct_guessing < 50:
    # Get user input
    user_answers = screen.textinput(title=f"{len(state_done)}/55 States Correct",
                                    prompt="Enter another state name: ").title()

    # Check if user wants to exit
    if user_answers == "Exit":
        break

    # Check if the user's answer is correct
    if user_answers in state_name:
        state_name.remove(user_answers)
        state_done.append(user_answers)

        # Create a turtle to display the state name
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        state_data = us_data[us_data.state == user_answers]
        turtle.goto(x=int(state_data.x), y=int(state_data.y))
        turtle.write(state_data.state.item(), font=("Arial", 5, "bold"))

    # Increment the number of correct guesses
    number_of_correct_guessing += 1

# Create dataframes for completed and remaining states
completed_state = {"state": state_done}
remain_state = {"state": state_name}
completed_state_df = pd.DataFrame.from_dict(completed_state)
remain_state_df = pd.DataFrame.from_dict(remain_state)

# Save the dataframes to CSV files
completed_state_df.to_csv("completed.csv")
remain_state_df.to_csv("remain.csv")

#
# def get_mouse_on_click(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_on_click)
#
#
# turtle.mainloop()
screen.exitonclick()
