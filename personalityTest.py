from google.appengine.ext import ndb
import random
class answersStore(ndb.Model):
    color = ndb.StringProperty(required=True)
class userInterests(ndb.Model):
    hobbies = ndb.StringProperty(required=True)
    living_and_travel = ndb.StringProperty(required=True)
    education_and_careers = ndb.StringProperty(required=True)
    music = ndb.StringProperty(required=True)
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


personalityresults = {
    "blue_hobbies" : ["Social Events", "Camp Counselor", "Volunteering", "Activism"],
    "blue_education_and_careers": ["Consultant", "Human Resources Manager", "Therapist", "Journalist", "Social Worker", "Flight Attendant", "Tour Guide", "Teacher", "Environmentalist"],
    "blue_music" :["Love Songs", "Pop Genre"],
    "blue_living_and_travel": ["Living in the suburbs", "Yosemite National Park", "Yellowstone National Park", "New Zealand", "Grand Canyon", "Iceland", "Canada"],
    "orange_hobbies" : ["Football", "Basketball", "Hockey", "Skydiving", "Rollercoasters"],
    "orange_education_and_careers": ["Entrepreneur", "Marketing", "Advertising", "Actor", "Painter", "Comedian", "Dance Teacher"],
    "orange_music" :["Rap Genre", "Rock and Roll"],
    "orange_living_and_travel": ["Living in the city", "Hong Kong", "Dubai", "Tokyo", "Seoul", "New York", "Miami"],
    "green_hobbies" : ["Chess", "Golf", "Photography", "Reading", "Rocket Science"],
    "green_education_and_careers": ["Attorney", "Researcher", "Engineer", "Veterinarian", "Physician", "FBI Agent"],
    "green_music" :["Classical Genre", "Podcasts"],
    "green_living_and_travel": ["Living in the city", "Silicon Valley", "New York", "Austin", "Chicago", "Seattle", "Zurich", "London", "Beijing" ],
    "gold_hobbies" : ["Soccer", "Volunteering", "Personal Projects", "Organizing Events", "Minimalism"],
    "gold_education_and_careers": ["Accountant", "Financial Planner", "Manager", "Statistical Clerk", "Secretary", "Bank Officer", "Auditor"],
    "gold_music" :["Classical Genre", "Pop Genre"],
    "gold_living_and_travel": ["Living in mid-sized cities", "Boston", "Ann Arbor", "New England", "Toronto", "Rome", "Portland", "Syracuse"]

}



def choosing_interests(category):
    choose = random.randint(0, len(personalityresults[category])-1)
    interest = personalityresults[category]
    return interest[choose]

print(choosing_interests("gold_hobbies"))

#print(looping_through("question1", "Versatile <br> Inventive <br> Competent"))
