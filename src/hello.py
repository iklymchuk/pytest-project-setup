from random import choices

def user():
    users = ["user1", "user2", "user3"]
    return choices(users)[0]

print(user())