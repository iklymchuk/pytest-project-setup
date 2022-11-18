from random import choices

def random_user():
    users = ["guest", "regular", "admin"]
    return choices(users)[0]