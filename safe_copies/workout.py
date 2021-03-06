import csv
import time

#%%
def get_todays_date():
    """returns todays date"""
    date = time.ctime().split()
    date = f"{date[1]} {date[2]} {date[4]}"
    return date


def get_previous_date():
    """returns yesterdays date"""
    date = time.ctime().split()
    date = f"{date[1]} {int(date[2]) - 1} {date[4]}"
    return date


def get_date():
    question_date = input(f"Todays date is {time.ctime()} is this correct?")
    if question_date == "y":
        date = get_todays_date()
        return date

    elif question_date == "n":  # ask to use yeasterdays date
        question_date = input("Would you like to use yesterdays date instead?")

        if question_date == "y":
            date = get_previous_date()
            return date


def questions():
    """gets set counts and writes to csv"""

    date = get_date()
    j_jacks = input("How many Jumping Jacks did you do?:\n")
    curls = input("How many Bicep Curls did you do?:\n")
    r_curls = input("How many Reverse Curls did you do?:\n")
    h_curls = input("How many Hammer Curls did you do?:\n")
    pushups = input("How many Pushups did you do?:\n")
    ovr_curls = input("How many Overhead Curls did you do?:\n")
    windmills = input("How many Windmills did you do?:\n")
    w_pushups = input("How many Wall Pushups did you do?:\n")
    squats = input("How many Squats did you do:?\n")

    with open("workout.csv", "a", newline="") as csv_file:
        # date = get_date()
        fieldnames = [
            "Date",
            "JJacks",
            "Curls",
            "RCurls",
            "HCurls",
            "Pups",
            "OVCurls",
            "Windmills",
            "WPups",
            "Squats",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # writer.writeheader() # only use if the headers haven't been written
        writer.writerow(
            {
                "Date": date,
                "JJacks": j_jacks,
                "Curls": curls,
                "RCurls": r_curls,
                "HCurls": h_curls,
                "Pups": pushups,
                "OVCurls": ovr_curls,
                "Windmills": windmills,
                "WPups": w_pushups,
                "Squats": squats,
            }
        )


questions()