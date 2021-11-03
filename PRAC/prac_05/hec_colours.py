"""
CP1404/CP5632 Practical
Hex Colour Picker
"""

COLOUR_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Azure1": "#f0ffff",
               "beige": "#f5f5dc", "black": "#000000", "brown": "#a52a2a", "coral": "#ff7f50", "cyan": "#00ffff", "Gold": "#ffd700", }

colour = input("Enter Colour: ")
while colour != "":
    print(colour, "is", COLOUR_CODE[colour])
    colour = input("Enter Colour: ")
