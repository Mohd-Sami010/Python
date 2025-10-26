# Create a text-based interactive story where the user's decisions dictate the narrative path and outcome. This project focuses on branching logic and user input.

import time

def PrintText(text, delayInCharacters = 0.1, newLine = True):
    for c in text:
        print(c,end="", flush=True)
        time.sleep(delayInCharacters)
    if newLine:
         print()

def TakeUserInput(textToPrint, delay = 0.0):
        PrintText(textToPrint, delay, False)
        userInput = input()
        return (userInput.strip()).lower()

# Introduction to Story
story = {"Hello adventurer" : [{
        "Go left": [{
             "Swim Across River": "Win",
             "Don't cross the river": "Lose"
        }], "Go right": {
             "Climb tree": "Lose",
             "Don't climb Tree": "Lose"
        }}]}
dialogueNum = 1
# while True:
#      print(story.keys)
print(story.get("Hello adventurer"))