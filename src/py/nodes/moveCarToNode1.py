import bge

def move_car_to_node1():
    # Get the current controller
    controller = bge.logic.getCurrentController()
    
    # Get the objects from the scene
    car = bge.logic.getCurrentScene().objects.get("car")
    node1 = bge.logic.getCurrentScene().objects.get("node1")
    
    if car and node1:
        # Move the car to the position of node1
        car.worldPosition = node1.worldPosition

move_car_to_node1()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

