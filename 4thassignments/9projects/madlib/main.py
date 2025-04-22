
import random

print("Hello! ")
print("Enter your name")
# string concatenation (aka how to put string together)
# suppose we want to create astring that says "subscribe to ___"
# some string variable
name = input("Full Name :")

# a few ways to do this
print ("Welcome to madlib game" + name)
print("Lets start the game!")


adj = input("Adjective:")
verb1 = input("verb:")
verb2 = input("verb:")
famous_person = input("Famous person:")

madlib = f" Computer programing is so {adj}! It makes me so excited all the time because \
I love to {verb1}. stay Hydrated and {verb2} like you are {famous_person}!"

print(madlib)


