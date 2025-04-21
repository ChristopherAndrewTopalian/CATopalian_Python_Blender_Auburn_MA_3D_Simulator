import bge
import mathutils

# Speed at which the car will move
base_speed = 0.1
# Distance threshold to determine when the car has reached a node
threshold = 0.1

# List of node names in the scene that the car will move towards
node_names = [f'node{i}' for i in range(1, 11)] 

def move_car(cont):
    # Get the car object and the scene
    car = bge.logic.getCurrentScene().objects['car']  # Replace 'car' with your car object's name
    scene = bge.logic.getCurrentScene()
    
    # Get the list of nodes based on their names
    nodes = []
    
    # Check if all node names exist in the scene
    for name in node_names:
        if name in scene.objects:
            nodes.append(scene.objects[name].worldPosition)
        else:
            print(f"Warning: Object '{name}' not found in the scene!")

    if not nodes:
        print("No valid nodes found. Exiting the move_car function.")
        return

    # Use the worldwide variable to store the current node index
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
        # Get delta time using logic tic rate
        dt = bge.logic.getLogicTicRate()  # Number of game ticks per second (adjust for frame rate)
        
        # Use frame time for consistent speed regardless of frame rate
        speed = base_speed * dt * bge.logic.getCurrentScene().rate  # `rate` is the update rate (1.0 is default) 
        move_vector = direction.normalized() * speed
        car.worldPosition += move_vector  # Move the car

        # Set the car's orientation to face the current node
        direction_normalized = direction.normalized()
        rot_quat = mathutils.Vector((0, 0, 1)).to_track_quat('Z', direction_normalized)
        car.worldOrientation = rot_quat.to_euler()
    else:
        # At the node, move to the next one
        current_node_index = (current_node_index + 1) % len(nodes)
        bge.logic.globalDict["current_node"] = current_node_index  # Update to the next node

# Main function that will be called by the game engine
def main():
    cont = bge.logic.getCurrentController()
    move_car(cont)

# Execute the main function
main()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

