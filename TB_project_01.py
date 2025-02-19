print("Welcome! This program will ask you about your educational background.")

name = input("What is your name? ")

college = input(f"Hello {name}! Which college do you attend? ")

high_school = input(f"Great! And which high school did you attend, {name}? ")

print(f"\nThank you for sharing, {name}! Here's a summary of your responses:")
print(f"Name: {name}")
print(f"College: {college}")
print(f"High School: {high_school}")

most_fun = input(f"\n{name}, which institution do you think is the most fun? ")
print(f"Interesting choice! {most_fun} does sound like a lot of fun!")

favorite_subject = input("What's your favorite subject? ")
career_goal = input("What's your career goal? ")
print(f"\nGreat to know that your favorite subject is {favorite_subject} and your career goal is to become a {career_goal}!")
