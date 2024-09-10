import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.title("Aviator Game Simulation")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Draw the "plane" (simple triangle to represent the plane)
plane = turtle.Turtle()
plane.shape("triangle")
plane.color("white")
plane.penup()
plane.goto(-280, -280)  # Start from bottom-left corner
plane.setheading(45)  # Point the plane towards the top-right

# Game variables
multiplier = 1.0  # Initial multiplier
running = True    # Game running state
crash_point = random.uniform(1.5, 10.0)  # Random crash point
speed = 0.01      # Initial speed (lower is faster)

# Display multiplier on screen
multiplier_turtle = turtle.Turtle()
multiplier_turtle.hideturtle()
multiplier_turtle.penup()
multiplier_turtle.color("white")
multiplier_turtle.goto(-200, 260)
multiplier_turtle.write(f"Multiplier: {multiplier:.2f}x", font=("Arial", 16, "normal"))

# Function to simulate plane movement and crash
def fly_plane():
    global multiplier, running, speed

    while running:
        time.sleep(speed)  # Delay based on speed
        
        # Move the plane upwards diagonally (45 degree angle)
        plane.forward(2)  # Smaller movement for smoother transition
        
        # Increase multiplier by a smaller value for smoother progression
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
            multiplier_turtle.goto(-150, 0)
            multiplier_turtle.write(f"Crash! Final Multiplier: {multiplier:.2f}x", font=("Arial", 24, "bold"))
            break

# Start flying the plane
fly_plane()

# Keep the screen open until the user closes it
screen.mainloop()
