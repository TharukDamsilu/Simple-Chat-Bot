from calendar import calendar
import random
import time


R_EATING = "I don't feel anything because I'm a Program!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_TIME = time.asctime()


def unknown():
    response = ["...",
                "What does that mean?"][
        random.randrange(2)]
    return response