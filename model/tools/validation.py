import re
from datetime import datetime

def title_validator(title):
    if type(title) == str and re.match(r"^[a-zA-Z\s]{3,30}$", title):
        return title
    else:
        raise ValueError("Invalid title !!!")

def name_validator(name):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError("Invalid name !!!")

def description_validator(description):
    if type(description) == str and re.match(r"^[a-zA-Z\s]{3,100}$", description):
        return description
    else:
        raise ValueError("Invalid description !!!")

def state_validator(state):
    if state in ["checked","not_checked"]:
        return state
    else :
        raise ValueError("Invalid status !!!")

def time_validator(start_time):
    try:
        if type(start_time) == str:
            return datetime.strptime(start_time, "%H:%M:%S").time()
    except:
        raise ValueError("Invalid Time !!!")

def date_validator(date):
    try:
        if type(date) == str:
            return datetime.strptime(date, "%Y-%m-%d").date()
    except:
        raise ValueError("Invalid date !!!")





