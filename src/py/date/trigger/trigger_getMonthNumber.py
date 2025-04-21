import bge
from getMonthNumber import getMonthNumber

def on_click():
    # Get the current controller
    controller = bge.logic.getCurrentController()
    
    # Get the object the script is attached to
    obj = controller.owner
    
    # Get the sensors
    mouse_over_sensor = controller.sensors["MouseOver"]
    mouse_click_sensor = controller.sensors["MouseLeftClick"]
    
    # Check if the mouse is over the object and the left button is clicked
    if mouse_over_sensor.positive and mouse_click_sensor.positive:
        print(getMonthNumber())
        
        # Get the current scene
        theScene = bge.logic.getCurrentScene()
        
        # Get the text object named 'date'
        date_object = theScene.objects.get('monthNumber')
        
        if date_object:
            # Change the Text property of the text object
            theScene.objects['monthNumber']['Text'] = f"{getMonthNumber()}"
        else:
            print("Text object named 'monthNumber' not found.")

# Run the function
on_click()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

