# move_object_in_increments.py

# import the blender game engine
import bge

# get controller running this script
controller = bge.logic.getCurrentController()

# get game object controller is on
obj = controller.owner

# move the object by 0.1
obj.position.y += 0.03

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

