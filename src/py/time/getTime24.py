# getTime24.py

import datetime as dt

def getTime24():
    now = dt.datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    return currentTime

##

if __name__ == "__main__":
    print(getTime24())
    input('')

####

'''
19:30:10
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

