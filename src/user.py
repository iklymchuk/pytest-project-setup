import fire
from random import choices


def random_user():
    users = ["guest", "regular", "admin"]
    return choices(users)[0]

def greeting(user=random_user()):
  return f"Hello {user} user!"

if __name__ == '__main__':
  fire.Fire(greeting)