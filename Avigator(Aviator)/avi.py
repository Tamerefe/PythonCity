import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.title("Aviator Game Simulation")
screen.bgcolor("black")
screen.setup(width=1280, height=720)  # Ekran genişliği uzun uçuşlar için ayarlandı

# Set background image
screen.bgpic("Avigator(Aviator)/bg.gif")  # background.gif yerine kendi resim dosyanızın adını yazın

# Create turtle for drawing the betting interface
betting_turtle = turtle.Turtle()
betting_turtle.hideturtle()
betting_turtle.penup()
betting_turtle.color("white")
betting_turtle.goto(0, 0)

# Create the "plane" turtle (use an image instead of a triangle)
plane = turtle.Turtle()
# Load the plane image
screen.addshape("Avigator(Aviator)/plane.gif")
# Set the plane turtle's shape to the plane image
plane.shape("Avigator(Aviator)/plane.gif")
plane.penup()
plane.goto(-615, -340)  # Daha küçük ekran için başlangıç konumu küçültüldü
plane.setheading(26)  # Uçağı sağ üst köşeye daha yatık bir açıyla yönlendir

# Create a turtle for drawing the trail
trail_turtle = turtle.Turtle()
trail_turtle.hideturtle()
trail_turtle.penup()
trail_turtle.color("#ffd25d")  # Renk kodu ffd25d (sarımsı ton)
trail_turtle.goto(-615, -340)  # İz çizim başlangıç konumu küçültüldü
trail_turtle.pendown()

# Game variables
bet_amount = 0
target_multiplier = 0
multiplier = 1.0
running = False
crash_point = 0
speed = 0.01

# Display multiplier and winnings on screen
multiplier_turtle = turtle.Turtle()
multiplier_turtle.hideturtle()
multiplier_turtle.penup()
multiplier_turtle.color("white")
multiplier_turtle.goto(-600, 300)

winnings_turtle = turtle.Turtle()
winnings_turtle.hideturtle()
winnings_turtle.penup()
winnings_turtle.color("white")
winnings_turtle.goto(-600, 270)

# Function to display betting screen
def show_betting_screen():
    betting_turtle.clear()
    betting_turtle.goto(0, 100)
    betting_turtle.write("Welcome to Aviator!", align="center", font=("Courier", 24, "bold"))
    betting_turtle.goto(0, 50)
    betting_turtle.write("Enter your bet amount in dollars:", align="center", font=("Courier", 18, "normal"))

# Function to handle betting input
def handle_bet_input():
    global bet_amount, target_multiplier, running, crash_point
    try:
        bet_amount = float(turtle.textinput("Bet Amount", "Enter your bet amount in dollars:"))
        target_multiplier = float(turtle.textinput("Target Multiplier", "Enter your target multiplier:"))
        if bet_amount > 0 and target_multiplier > 1:
            betting_turtle.clear()
            betting_turtle.goto(0, 0)
            betting_turtle.write(f"Your bet: ${bet_amount:.2f}", align="center", font=("Courier", 18, "normal"))
            betting_turtle.goto(0, -50)
            betting_turtle.write(f"Target Multiplier: {target_multiplier:.2f}x", align="center", font=("Courier", 18, "normal"))
            # Set a random crash point
            crash_point = random.uniform(1.5, 10.0)
            running = True
            turtle.ontimer(start_flying, 2000)  # Start the flying game after 2 seconds
        else:
            betting_turtle.write("Invalid input. Try again.", align="center", font=("Courier", 18, "normal"))
    except ValueError:
        betting_turtle.write("Please enter valid numbers.", align="center", font=("Courier", 18, "normal"))

# Function to start the game
def start_flying():
    global bet_amount, target_multiplier, multiplier, running, speed, crash_point
    current_winnings = bet_amount  # Start winnings with the bet amount
    if running:
        betting_turtle.clear()  # Clear the welcome message when the game starts
        
        trail_turtle.clear()  # Clear the trail from previous rounds
        trail_turtle.penup()
        trail_turtle.goto(-615, -340)  # Reset the trail to the starting point (smaller scale)
        trail_turtle.pendown()
        trail_turtle.begin_fill()  # Begin filling the trail's underside with color
        
        while running:
            screen.update()  # Update screen
            screen.tracer(0)  # Disable automatic screen updates

            # Move the plane upwards diagonally (26 degree angle for more horizontal movement)
            plane.forward(1)  # Hareket küçültüldü, daha küçük grafik
            multiplier += 0.01

            # Update the current winnings based on the multiplier
            current_winnings = bet_amount * multiplier

            # Move the trail turtle to the plane's position to draw the line
            trail_turtle.goto(plane.xcor(), plane.ycor())

            # Update the multiplier and winnings display
            multiplier_turtle.clear()
            multiplier_turtle.write(f"Multiplier: {multiplier:.2f}x", font=("Courier", 16, "normal"))
            winnings_turtle.clear()
            winnings_turtle.write(f"Current Winnings: ${current_winnings:.2f}", font=("Courier", 16, "normal"))

            # Increase the speed as the multiplier increases
            if multiplier >= 1.5:
                speed = max(0.001, speed - 0.0005)  # Speed up, minimum delay of 0.001 seconds

            # Check if the plane has crashed
            if multiplier >= crash_point:
                running = False
                betting_turtle.clear()
                betting_turtle.goto(0, 0)
                if multiplier >= target_multiplier:
                    winnings = bet_amount * target_multiplier
                    betting_turtle.write(f"You won ${winnings:.2f}!\nFinal Multiplier: {multiplier:.2f}x\nBet Amount: ${bet_amount:.2f}", align="center", font=("Courier", 24, "bold"))
                else:
                    betting_turtle.write(f"You lost!\nFinal Multiplier: {multiplier:.2f}x\nBet Amount: ${bet_amount:.2f}", align="center", font=("Courier", 24, "bold"))
                
                # Complete the trail filling
                trail_turtle.goto(plane.xcor(), -340)  # Daha küçük ekran için iz tamamlama
                trail_turtle.goto(-615, -340)  # Başlangıç noktasına geri dön
                trail_turtle.end_fill()  # Finish filling the trail
                break

            time.sleep(speed)  # Delay based on speed

# Initialize game setup
show_betting_screen()
turtle.ontimer(handle_bet_input, 1000)  # Wait a second before asking for input

# Keep the screen open until the user closes it
screen.mainloop()
