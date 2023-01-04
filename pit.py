#Here I'm trying to split the user's input into separate strings
"""I've also used the strip and title functions on the same line 
that declares the name variable"""
name = input("What's your name? ").strip().title()
first, last= name.split(" ")
print(f"Hello there, {name}")