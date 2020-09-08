"""
This program generates passages that are generated in mad-lib format. It's a story which takes input from the user of the program
Author: Shaq
"""

# The template for the story
STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print ("The program is running...") #Informs user that program is running

#Getting input from user
name = input("What's your name?: ")
adjective = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
noun = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

#Printing MadLibs story
print (STORY % (name, adjective, adjective2, animal, food, verb, noun, fruit, adjective3, name, superhero, name, country, name, dessert, name, year, noun2))
