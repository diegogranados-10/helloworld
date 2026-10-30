from datetime import datetime


def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    if hour < 18:
        return "Good afternoon"
    return "Good evening"


def main():
    print("Hello, World!")

    name = input("What is your name? ").strip() or "friend"
    goal = input("What do you want to learn this semester? ").strip() or "something new"

    print(f"\n{get_greeting()}, {name}!")
    print(f"I hope you learn a lot about {goal}.")
    print(f"Today is {datetime.now():%A, %B %d, %Y}. Let's get coding!")


if __name__ == "__main__":
    main()
