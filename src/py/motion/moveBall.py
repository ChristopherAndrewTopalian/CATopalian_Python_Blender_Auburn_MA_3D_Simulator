import bge

def moveBall():
    cont = bge.logic.getCurrentController()
    own = cont.owner

    if own.name == "Ball":
        # Ball logic: movement, bouncing
        scene = bge.logic.getCurrentScene()
        ball = scene.objects["Ball"]
        speed = 10
        ball.applyForce([speed, 0, 0], True)

moveBall()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

