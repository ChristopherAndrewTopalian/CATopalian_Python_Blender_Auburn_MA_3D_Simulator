import bge

def move_car_to_node1():
    # Get the current controller
    controller = bge.logic.getCurrentController()
    
    # Get the objects from the scene
    car = bge.logic.getCurrentScene().objects.get("car")
    node1 = bge.logic.getCurrentScene().objects.get("node1")
    
    if car and node1:
        # Get the current position of the car and node1
        current_position = car.worldPosition
        target_position = node1.worldPosition
        
        # Define the speed at which the car should move
        speed = 0.05
        
        # Move the car closer to node1 using linear interpolation (lerp)
        # Lerp formula: result = (1 - t) * start + t * end
        # t will be a small value that gradually increases towards 1
        car.worldPosition = current_position + (target_position - current_position) * speed

move_car_to_node1()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

