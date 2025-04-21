# getDateTime12.py

import datetime as dt

def getDateTime12():
    currentDateTime = dt.datetime.now()

    # formatted date MM-DD-YY
    date = currentDateTime.strftime("%m-%d-%y")

    # formatted time HH:MM AM/PM
    time = currentDateTime.strftime("%I:%M %p")

    formattedDateTime = date + " " + time

    return formattedDateTime

# print(getDateTime12())
# input('')

# 06-11-24 05:33 PM

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

