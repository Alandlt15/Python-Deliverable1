import math

name = input("Welcome to GC mini golf! What is your name? ")
holes = int(input(f"Hi {name}!, Would you like to play 3 or 6 holes today? "))
score = 0
par = 0

if holes == 3:
    par = 9
    for x in range(3):
        score += int(input(f"How many putts for hole {x+1}? (par is 3) "))

elif holes == 6:
    par = 18
    for x in range(6):
        score += int(input(f"How many putts for hole {x + 1}? (par is 3) "))

if score > par:
    print(f"Nice try, {name}! Your total score was: +{(score - par)}")
elif score < par:
    print(f"Great job, {name}! Your total score was: -{(par - score)}")
elif score == par:
    print(f"Good game, {name}! Your total score was: 0")
    