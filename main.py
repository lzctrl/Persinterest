import webapp2  #connecting to the google app engine yaml file
import jinja2 #connets to the html files
import os #apple operating system
import random
from personalityTest import looping_through, answersStore, userInterests, choosing_interests
from google.appengine.api import users
from google.appengine.ext import ndb
from models import GoogleUser, getImage

personalitytest = {
    "question1": ["Authentic <br> Harmonious <br> Compassionate", "Active <br> Opportunistic <br> Spontaneous", "Versatile <br> Inventive <br> Competent", "Parental <br> Traditional <br> Responsible"],
    "question2": ["Unique <br> Empathetic <br> Communicative", "Competitive <br> Impetuous <br> Impactful","Curious <br> Conceptual <br> Knowledgeable","Practical <br> Sensible <br> Dependable"],
    "question3": ["Devoted <br> Warm <br> Personable", "Realistic <br> Open-Minded <br> Adventuresome", "Theoretical <br> Seeking <br> Ingenious", "Loyal <br> Conservative <br> Organized"],
    "question4": ["Loving <br> Inspirational<br> Dramatic", "Daring <br> Impulsive <br> Fun", "Determined <br> Complex <br> Composed","Concerned <br> Procedural <br> Cooperative"],
    "question5": ["Vivacious <br> Affectionate <br> Sympathetic", "Exciting <br> Courageous <br> Skillful", "Determined <br> Principled <br> Rational", "Orderly <br> Habitual <br> Caring"]
}
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
    "gold_hobbies" : ["Soccer", "Volunteering", "Personal Projects", "Organizing Events"],
    "gold_education_and_careers": ["Accountant", "Financial Planner", "Manager", "Statistical Clerk", "Secretary", "Bank Officer", "Auditor"],
    "gold_music" :["Classical Genre", "Pop Genre"],
    "gold_living_and_travel": ["Living in mid-sized cities", "Boston", "Ann Arbor", "New England", "Toronto", "Rome", "Portland", "Syracuse"]

}

#jinja2.Environment is a constructor

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_page = jinja_env.get_template('index.html')

        user = users.get_current_user()
        if user:
            email_address = user.nickname()

            existing_user = GoogleUser.query().filter(GoogleUser.email == email_address).get()
            user_status = ""
            logout_url = ""
            goToURL = ""
            currentUser = GoogleUser.query().filter(GoogleUser.email == email_address).get()

            if existing_user:
                if currentUser.hasTakenTest == True:
                    user_status = "Results"
                    goToURL = "/pages/results"
                    button_text = "Results"
                    button_url = "/pages/results"
                else:
                    user_status = "Get Started"
                    goToURL = "/pages/personalitytest"
                    button_text = "Get Started"
                    button_url = "/pages/personalitytest"
            else:
                user_status = "Add Info"
                goToURL = "/pages/newUser"
                button_text = "Get Started"
                button_url = "/pages/personalitytest"

            logout_url = users.create_logout_url('/')
            signedIn = True

            mydict = {
                "status": user_status,
                "isSignedIn": signedIn,
                "url": logout_url,
                "goTo": goToURL,
                "main_button_text": button_text,
                "main_button_url": button_url
            }

            self.response.write(welcome_page.render(mydict))
        else:
            user_status = "Sign Up"
            login_url = users.create_login_url('/pages/newUser')


            mydict = {
                "status": user_status,
                "isSignedIn": False,
                "goTo": login_url,
                "main_button_text": user_status,
                "main_button_url": login_url
            }

            self.response.write(welcome_page.render(mydict))

    def post(self):
        welcome_page = jinja_env.get_template('index.html')

        user = users.get_current_user()

        google_user = GoogleUser(
            first_name=self.request.get('first_name'),
            last_initial=self.request.get('last_initial'),
            email = user.nickname(),
            hasTakenTest = False,
            color = ""
            # interests = {}
        )

        google_user.put()

        user = users.get_current_user()
        if user:
            email_address = user.nickname()

            existing_user = GoogleUser.query().filter(GoogleUser.email == email_address).get()
            user_status = ""
            logout_url = ""
            goToURL = ""
            currentUser = GoogleUser.query().filter(GoogleUser.email == email_address).get()
            if existing_user:
                if currentUser.hasTakenTest == True:
                    user_status = "Results"
                    goToURL = "/pages/results"
                    button_text = "Results"
                    button_url = "/pages/results"
                else:
                    user_status = "Take Test"
                    goToURL = "/pages/personalitytest"
                    button_text = "Get Started"
                    button_url = "/pages/personalitytest"
            else:
                user_status = "Add Info"
                goToURL = "/pages/newUser"
                button_text = "Get Started"
                button_url = "/pages/personalitytest"

            logout_url = users.create_logout_url('/')
            signedIn = True

            mydict = {
                "status": user_status,
                "isSignedIn": signedIn,
                "url": logout_url,
                "goTo": goToURL,
                "main_button_text": button_text,
                "main_button_url": button_url

            }

            self.response.write(welcome_page.render(mydict))

class PersonalityTestPage(webapp2.RequestHandler):
    def get(self):
        personality_test_page = jinja_env.get_template('pages/personalitytest.html')
        self.response.write(personality_test_page.render(personalitytest))


class AboutPage(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()

        signedIn = False

        if user:
            signedIn = True

        mydict = {
            "isSignedIn": signedIn
        }

        about_page = jinja_env.get_template('pages/about.html')
        self.response.write(about_page.render(mydict))

class ConnectionsPage(webapp2.RequestHandler):
    def get(self):
        connections_page = jinja_env.get_template('pages/connections.html')
        self.response.write(connections_page.render())

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        email_address = user.nickname()
        currentUser = GoogleUser.query().filter(GoogleUser.email == email_address).get()
        userColorImg = ""
        data = {
            "user_color" : currentUser.color,
            "user_hobbies": currentUser.hobbies,
            "user_living_and_travel": currentUser.living_and_travel,
            "user_education_and_careers": currentUser.education_and_careers,
            "user_music": currentUser.music,
            "colorImage": getImage(currentUser.color),
            "hobbies_image": getImage(currentUser.hobbies),
            "living_and_travel_image": getImage(currentUser.living_and_travel),
            "education_and_careers_image": getImage(currentUser.education_and_careers),
            "music_image": getImage(currentUser.music),
            "connect_image": getImage("iphone")
        }
        results_page = jinja_env.get_template('pages/results.html')
        self.response.write(results_page.render(data))

    def post(self):

        answer1 = self.request.get("template")
        answer2 = self.request.get("template2")
        answer3 = self.request.get("template3")
        answer4 = self.request.get("template4")
        answer5 = self.request.get("template5")

        answers_index = [looping_through("question1", answer1),
        looping_through("question2", answer2),
        looping_through("question3", answer3),
        looping_through("question4", answer4),
        looping_through("question5", answer5)]
        list_colors = [0, 0, 0, 0]
        for index in answers_index:
            if (index == 0):
                list_colors[0] +=1
            elif(index == 1):
                list_colors[1] +=1
            elif(index==2):
                list_colors[2] +=1
            else:
                list_colors[3] +=1
        max_value = 0
        if(list_colors.count(2)==2):
            max_value = 2
        else:
            max_value = max(list_colors)

        user_color = ""

        if(list_colors.index(max_value) == 0):
            user_color = "Blue"
            color_interest = userInterests(hobbies = choosing_interests("blue_hobbies"),
                                             living_and_travel =choosing_interests("blue_living_and_travel"),
                                             education_and_careers=choosing_interests("blue_education_and_careers"),
                                             music=choosing_interests("blue_music"),)
        elif(list_colors.index(max_value) == 1):
            user_color = "Orange"
            color_interest = userInterests(hobbies = choosing_interests("orange_hobbies"),
                                             living_and_travel =choosing_interests("orange_living_and_travel"),
                                             education_and_careers=choosing_interests("orange_education_and_careers"),
                                             music=choosing_interests("orange_music"),)
        elif(list_colors.index(max_value) == 2):
            user_color = "Green"
            color_interest = userInterests(hobbies = choosing_interests("green_hobbies"),
                                             living_and_travel =choosing_interests("green_living_and_travel"),
                                             education_and_careers=choosing_interests("green_education_and_careers"),
                                             music=choosing_interests("green_music"),)
        elif(list_colors.index(max_value) == 3):
            user_color = "Gold"
            color_interest = userInterests(hobbies = choosing_interests("gold_hobbies"),
                                             living_and_travel =choosing_interests("gold_living_and_travel"),
                                             education_and_careers=choosing_interests("gold_education_and_careers"),
                                             music=choosing_interests("gold_music"),)

        user = users.get_current_user()
        email_address = user.nickname()
        color_interest.put()

        # user_array.put()
        currentUser = GoogleUser.query().filter(GoogleUser.email == email_address).get()
        currentUser.hasTakenTest = True
        currentUser.color = user_color
        currentUser.education_and_careers = color_interest.education_and_careers
        currentUser.hobbies = color_interest.hobbies
        currentUser.living_and_travel = color_interest.living_and_travel
        currentUser.music = color_interest.music

        currentUser.put()
        data = {
            "user_color" : user_color,
            "user_hobbies" : color_interest.hobbies,
            "user_living_and_travel": color_interest.living_and_travel,
            "user_education_and_careers": color_interest.education_and_careers,
            "user_music":color_interest.music,
            "colorImage": getImage(user_color),
            "hobbies_image": getImage(color_interest.hobbies),
            "living_and_travel_image": getImage(color_interest.living_and_travel),
            "education_and_careers_image": getImage(color_interest.education_and_careers),
            "music_image": getImage(color_interest.music),
            "connect_image": getImage("iphone")
            # "user_all_answers" : user_answers
        }

        results_template = jinja_env.get_template('pages/results.html')
        self.response.write(results_template.render(data))

class NewUserPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email_address = user.nickname()

            existing_user = GoogleUser.query().filter(GoogleUser.email == email_address).get()

            if existing_user:
                #takes them to the results page/connection page with others
                results_page = jinja_env.get_template('pages/results.html')
                self.response.write(results_page.render())
            else:
                #insert a "not registered yet?" prompt with a redirection to this please register page
                login_url = users.create_login_url('/pages/results')
                mydict = {
                    "url" : login_url,
                    "isUser": True
                }
                new_user_page = jinja_env.get_template('pages/newUser.html')
                self.response.write(new_user_page.render(mydict));
                pass
        else:
            login_url = users.create_login_url('/pages/newUser')
            self.redirect(login_url, True)
            # mydict = {
            #     "url" : login_url,
            #     "isUser": False
            # }
            # new_user_page = jinja_env.get_template('pages/newUser.html')
            # self.response.write(new_user_page.render(mydict));


class SettingsPage(webapp2.RequestHandler):
    def get(self):
        settings_page = jinja_env.get_template('pages/settings.html')
        self.response.write(settings_page.render())

# the app configuration section
app = webapp2.WSGIApplication(
    [('/', WelcomePage), ('/pages/newUser', NewUserPage),
    ('/pages/personalitytest', PersonalityTestPage), ('/pages/about', AboutPage),
    ('/pages/connections', ConnectionsPage), ('/pages/results', ResultsPage),
    ('/pages/settings', SettingsPage)],
    debug = True
)
