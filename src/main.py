def welcome_message(name):
    return f"{name}, welcome to the Data Engineering course. Hope you have fun!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(welcome_message(name))

def setting_goals(point):
    return f"Let's try together to earn {point} points!"

if __name__ == "__main__":
    point = input("How many points you are aiming for this assignment?: ")
    print(setting_goals(point))