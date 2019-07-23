blueWords = [
    ["Authentic", "Harmonious", "Compassionate"],
    ["Unique", "Empathetic", "Communicative"],
    ["Devoted", "Warm", "Personable"],
    ["Loving", "Inspirational", "Dramatic"],
    ["Vivacious", "Affectionate", "Sympathetic"]
]

orangeWords = [
    ["Active", "Opportunistic", "Spontaneous"],
    ["Competitive", "Impetuous", "Impactful"],
    ["Realistic", "Open-Minded", "Adventuresome"],
    ["Daring", "Impulsive", "Fun"],
    ["Exciting", "Courageous", "Skillful"]
]

greenWords = [
    ["Versatile", "Inventive", "Competent"],
    ["Curious", "Conceptual", "Knowledgeable"],
    ["Theoretical", "Seeking", "Ingenious"],
    ["Determined", "Complex", "Composed"],
    ["Determined", "Principled", "Rational"]
]

goldWords = [
    ["Parental", "Traditional", "Responsible"],
    ["Practical", "Sensible", "Dependable"],
    ["Loyal", "Conservative", "Organized"],
    ["Concerned", "Procedural", "Cooperative"],
    ["Orderly", "Habitual", "Caring"]
]

blue = 0
orange = 0
green = 0
gold = 0


current = 0

while current < 5:
    print("1. " + str(blueWords[current]))
    print("2. " + str(orangeWords[current]))
    print("3. " + str(greenWords[current]))
    print("4. " + str(goldWords[current]))

    choice = raw_input("Which set of words best describes who you are? ")

    if choice == "1":
        blue = blue + 1
    if choice == "2":
        orange = orange + 1
    if choice == "3":
        green = green + 1
    if choice == "4":
        gold = gold + 1

    current += 1

if blue > orange:
    if blue > green:
        if blue > gold:
            print("Blue")
if orange > blue:
    if orange > green:
        if orange > gold:
            print("Orange")
if green > blue:
    if green > orange:
        if green > gold:
            print("Green")
if gold > blue:
    if gold > orange:
        if gold > green:
            print("Gold")
