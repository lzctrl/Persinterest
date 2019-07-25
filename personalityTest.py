from google.appengine.ext import ndb
class answersStore(ndb.Model):
    color = ndb.StringProperty(required=True)
class userAnswers(ndb.Model):
    a1 = ndb.StringProperty(required=True)
    a2 = ndb.StringProperty(required=True)
    a3 = ndb.StringProperty(required=True)
    a4 = ndb.StringProperty(required=True)
    a5 = ndb.StringProperty(required=True)
personalitytest = {
    # index 0 = blueWords, 1 = orangeWords, 2 = greenWords, 3 = goldWords
"question1": ["Authentic <br> Harmonious <br> Compassionate", "Active <br> Opportunistic <br> Spontaneous", "Versatile <br> Inventive <br> Competent", "Parental <br> Traditional <br> Responsible"],
"question2": ["Unique <br> Empathetic <br> Communicative", "Competitive <br> Impetuous <br> Impactful","Curious <br> Conceptual <br> Knowledgeable","Practical <br> Sensible <br> Dependable"],
"question3": ["Devoted <br> Warm <br> Personable", "Realistic <br> Open-Minded <br> Adventuresome", "Theoretical <br> Seeking <br> Ingenious", "Loyal <br> Conservative <br> Organized"],
"question4": ["Loving <br> Inspirational<br> Dramatic", "Daring <br> Impulsive <br> Fun", "Determined <br> Complex <br> Composed","Concerned <br> Procedural <br> Cooperative"],
"question5": ["Vivacious <br> Affectionate <br> Sympathetic", "Exciting <br> Courageous <br> Skillful", "Determined <br> Principled <br> Rational", "Orderly <br> Habitual <br> Caring"]
}


def looping_through(question_num, compare_to):
    for x in personalitytest[question_num]:
        if (x == compare_to):
            return personalitytest[question_num].index(x)


#print(looping_through("question1", "Versatile <br> Inventive <br> Competent"))


# blueWords = [
#     ["Authentic", "Harmonious", "Compassionate"],
#     ["Unique", "Empathetic", "Communicative"],
#     ["Devoted", "Warm", "Personable"],
#     ["Loving", "Inspirational", "Dramatic"],
#     ["Vivacious", "Affectionate", "Sympathetic"]
# ]
#
# orangeWords = [
#     ["Active", "Opportunistic", "Spontaneous"],
#     ["Competitive", "Impetuous", "Impactful"],
#     ["Realistic", "Open-Minded", "Adventuresome"],
#     ["Daring", "Impulsive", "Fun"],
#     ["Exciting", "Courageous", "Skillful"]
# ]
#
# greenWords = [
#     ["Versatile", "Inventive", "Competent"],
#     ["Curious", "Conceptual", "Knowledgeable"],
#     ["Theoretical", "Seeking", "Ingenious"],
#     ["Determined", "Complex", "Composed"],
#     ["Determined", "Principled", "Rational"]
# ]
#
# goldWords = [
#     ["Parental", "Traditional", "Responsible"],
#     ["Practical", "Sensible", "Dependable"],
#     ["Loyal", "Conservative", "Organized"],
#     ["Concerned", "Procedural", "Cooperative"],
#     ["Orderly", "Habitual", "Caring"]
# ]
#
# blue = 0
# orange = 0
# green = 0
# gold = 0
#
#
# current = 0
#
# while current < 5:
#     print("1. " + str(blueWords[current]))
#     print("2. " + str(orangeWords[current]))
#     print("3. " + str(greenWords[current]))
#     print("4. " + str(goldWords[current]))
#
#     choice = raw_input("Which set of words best describes who you are? ")
#
#     if choice == "1":
#         blue = blue + 1
#     if choice == "2":
#         orange = orange + 1
#     if choice == "3":
#         green = green + 1
#     if choice == "4":
#         gold = gold + 1
#
#     current += 1
#
# if blue > orange:
#     if blue > green:
#         if blue > gold:
#             print("Blue")
# if orange > blue:
#     if orange > green:
#         if orange > gold:
#             print("Orange")
# if green > blue:
#     if green > orange:
#         if green > gold:
#             print("Green")
# if gold > blue:
#     if gold > orange:
#         if gold > green:
#             print("Gold")


# class Questions:
#     adjectives_dict = { blueWords : [
#         ["Authentic", "Harmonious", "Compassionate"],
#         ["Unique", "Empathetic", "Communicative"],
#         ["Devoted", "Warm", "Personable"],
#         ["Loving", "Inspirational", "Dramatic"],
#         ["Vivacious", "Affectionate", "Sympathetic"]
#     ]
#
#     orangeWords : [
#         ["Active", "Opportunistic", "Spontaneous"],
#         ["Competitive", "Impetuous", "Impactful"],
#         ["Realistic", "Open-Minded", "Adventuresome"],
#         ["Daring", "Impulsive", "Fun"],
#         ["Exciting", "Courageous", "Skillful"]
#     ]
#
#     greenWords : [
#         ["Versatile", "Inventive", "Competent"],
#         ["Curious", "Conceptual", "Knowledgeable"],
#         ["Theoretical", "Seeking", "Ingenious"],
#         ["Determined", "Complex", "Composed"],
#         ["Determined", "Principled", "Rational"]
#     ]
#
#     goldWords : [
#         ["Parental", "Traditional", "Responsible"],
#         ["Practical", "Sensible", "Dependable"],
#         ["Loyal", "Conservative", "Organized"],
#         ["Concerned", "Procedural", "Cooperative"],
#         ["Orderly", "Habitual", "Caring"]
#     ]
#     }
