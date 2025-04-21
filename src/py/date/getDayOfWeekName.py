# getDayOfWeekName.py

import datetime as dt

def getDayOfWeekName():
    currentDate = dt.datetime.now()

    # 0 is Monday, 6 is Sunday
    dayOfWeek = currentDate.weekday()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # get name of day using day of week index
    dayName = days[dayOfWeek]

    return dayName

#print(getDayOfWeekName())
#input('')

# Monday

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

