import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.title("Aviator Game Simulation")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create turtle for drawing the betting interface
betting_turtle = turtle.Turtle()
betting_turtle.hideturtle()
betting_turtle.penup()
betting_turtle.color("white")
betting_turtle.goto(0, 0)

# Draw the "plane" (simple triangle to represent the plane)
plane = turtle.Turtle()
plane.shape("triangle")
plane.color("white")
plane.penup()
plane.goto(-280, -280)  # Start from bottom-left corner
plane.setheading(45)  # Point the plane towards the top-right

# Game variables
bet_amount = 0
target_multiplier = 0
multiplier = 1.0
running = False
crash_point = 0
speed = 0.01

# Display multiplier on screen
multiplier_turtle = turtle.Turtle()
multiplier_turtle.hideturtle()
multiplier_turtle.penup()
multiplier_turtle.color("white")
multiplier_turtle.goto(-200, 260)
multiplier_turtle.write(f"Multiplier: {multiplier:.2f}x", font=("Arial", 16, "normal"))

# Function to display betting screen
def show_betting_screen():
    betting_turtle.clear()
    betting_turtle.goto(0, 100)
    betting_turtle.write("Welcome to Aviator!", align="center", font=("Arial", 24, "bold"))
    betting_turtle.goto(0, 50)
    betting_turtle.write("Enter your bet amount in dollars:", align="center", font=("Arial", 18, "normal"))

# Function to handle betting input
def handle_bet_input():
    global bet_amount, target_multiplier, running, crash_point
    try:
        bet_amount = float(turtle.textinput("Bet Amount", "Enter your bet amount in dollars:"))
        target_multiplier = float(turtle.textinput("Target Multiplier", "Enter your target multiplier:"))
        if bet_amount > 0 and target_multiplier > 1:
            betting_turtle.clear()
            betting_turtle.goto(0, 0)
            betting_turtle.write(f"Your bet: ${bet_amount:.2f}", align="center", font=("Arial", 18, "normal"))
            betting_turtle.goto(0, -50)
            betting_turtle.write(f"Target Multiplier: {target_multiplier:.2f}x", align="center", font=("Arial", 18, "normal"))
            # Set a random crash point
            crash_point = random.uniform(1.5, 10.0)
            running = True
            turtle.ontimer(start_flying, 2000)  # Start the flying game after 2 seconds
        else:
            betting_turtle.write("Invalid input. Try again.", align="center", font=("Arial", 18, "normal"))
    except ValueError:
        betting_turtle.write("Please enter valid numbers.", align="center", font=("Arial", 18, "normal"))

# Function to start the game
def start_flying():
    global bet_amount, target_multiplier, multiplier, running, speed, crash_point
    if running:
        while running:
            screen.update()  # Update screen
            screen.tracer(0)  # Disable automatic screen updates

            # Move the plane upwards diagonally (45 degree angle)
            plane.forward(2)
            multiplier += 0.01

            # Update the multiplier display
            multiplier_turtle.clear()
            multiplier_turtle.write(f"Multiplier: {multiplier:.2f}x", font=("Arial", 16, "normal"))

            # Increase the speed as the multiplier increases
            if multiplier >= 1.5:
                speed = max(0.001, speed - 0.0005)  # Speed up, minimum delay of 0.001 seconds

            # Check if the plane has crashed
            if multiplier >= crash_point:
                running = False
                plane.color("red")  # Change plane color to red to indicate crash
                betting_turtle.clear()
                betting_turtle.goto(0, 0)
                if multiplier >= target_multiplier:
                    winnings = bet_amount * target_multiplier
                    betting_turtle.write(f"You won ${winnings:.2f}!\nFinal Multiplier: {multiplier:.2f}x\nBet Amount: ${bet_amount:.2f}", align="center", font=("Arial", 24, "bold"))
                else:
                    betting_turtle.write(f"You lost!\nFinal Multiplier: {multiplier:.2f}x\nBet Amount: ${bet_amount:.2f}", align="center", font=("Arial", 24, "bold"))
                break

            time.sleep(speed)  # Delay based on speed

# Initialize game setup
show_betting_screen()
turtle.ontimer(handle_bet_input, 1000)  # Wait a second before asking for input

# Keep the screen open until the user closes it
screen.mainloop()
