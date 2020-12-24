#%%
import csv
import time


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

    j_jacks = input("How many sets of Jumping Jacks did you do?:\n")
    if not j_jacks:
        j_jacks = 0

    curls = input("How many sets of Bicep Curls did you do?:\n")
    if not curls:
        curls = 0

    r_curls = input("How many sets of Reverse Curls did you do?:\n")
    if not r_curls:
        r_curls = 0

    h_curls = input("How many sets of Hammer Curls did you do?:\n")
    if not h_curls:
        h_curls = 0

    pushups = input("How many sets of Pushups did you do?:\n")
    if not pushups:
        pushups = 0

    ovr_curls = input("How many sets of Overhead Curls did you do?:\n")
    if not ovr_curls:
        ovr_curls = 0

    windmills = input("How many sets of Windmills did you do?:\n")
    if not windmills:
        windmills = 0

    w_pushups = input("How many sets of Wall Pushups did you do?:\n")
    if not w_pushups:
        w_pushups = 0

    squats = input("How many sets of Squats did you do:?\n")
    if not squats:
        squats = 0

    conf_str = f"You entered {j_jacks} JJacks, {curls} Curls, {r_curls} RCurls, {h_curls} HCurls, {pushups} Pups, {ovr_curls} OVCurls, {windmills} Windmills, {w_pushups} WPups, {squats} Squats \n"
    print(conf_str)
    input("Press Enter to write this data, or ALT + C to escape.")

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


if __name__ == "__main__":
    questions()
