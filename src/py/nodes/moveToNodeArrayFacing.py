import bge
import mathutils

# The distance to determine when to switch to the next node
threshold = 0.1  

# List of node positions (assumes objects are named node1 to node10)
node_names = [f'node{i}' for i in range(1, 11)]

def move_car(cont):
    # Get the car object and the scene
    car = bge.logic.getCurrentScene().objects['car']
    scene = bge.logic.getCurrentScene()

    # Get the list of nodes based on their names
    nodes = [scene.objects[node_name].worldPosition for node_name in node_names]
    
    # Use the global variable to store the current node index
    if "current_node" not in bge.logic.globalDict:
        bge.logic.globalDict["current_node"] = 0

    # Get the current node index
    current_node_index = bge.logic.globalDict["current_node"]

    # Get the current node's position
    current_node_position = nodes[current_node_index]

    # Calculate the direction to the current node
    direction = current_node_position - car.worldPosition
    distance_to_node = direction.length

    # Only move if the car is not at the current node
    if distance_to_node > threshold:
        # Move the car towards the current node
        speed = 0.25
        move_vector = direction.normalized() * speed
        car.worldPosition += move_vector  # Move the car

        # Set the car's orientation to face the current node
        # Calculate the rotation needed to face the direction
        rot_quat = mathutils.Vector((0, 1, 0)).to_track_quat('Z', direction)
        car.worldOrientation = rot_quat.to_euler()

    else:
        # If at the node, move to the next one
        current_node_index = (current_node_index + 1) % len(nodes)
        bge.logic.globalDict["current_node"] = current_node_index  # Update to the next node

# Run the function
move_car(bge.logic.getCurrentController())

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

