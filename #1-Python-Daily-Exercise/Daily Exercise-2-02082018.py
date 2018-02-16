#Joe Gutierrez - Python Daily Exercise - 2/16/18

# 2. Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. Clue input()

name = input('What is your Full name:')
           
year = int(input('What is your age:'))

yeet = (2018 - year) + 100

print ('Hello ' + name + ' you will be 100 years old in the year ' + str(yeet) + '.')



