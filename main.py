import webapp2  #connecting to the google app engine yaml file
import jinja2 #connets to the html files
import os #apple operating system
# from google.appengine.api import urlfetch
# import json
from personalityTest import looping_through
from personalityTest import answersStore
from personalityTest import userAnswers


personalitytest = {
    # index 0 = blueWords, 1 = orangeWords, 2 = greenWords, 3 = goldWords
"question1": ["Authentic <br> Harmonious <br> Compassionate", "Active <br> Opportunistic <br> Spontaneous", "Versatile <br> Inventive <br> Competent", "Parental <br> Traditional <br> Responsible"],
"question2": ["Unique <br> Empathetic <br> Communicative", "Competitive <br> Impetuous <br> Impactful","Curious <br> Conceptual <br> Knowledgeable","Practical <br> Sensible <br> Dependable"],
"question3": ["Devoted <br> Warm <br> Personable", "Realistic <br> Open-Minded <br> Adventuresome", "Theoretical <br> Seeking <br> Ingenious", "Loyal <br> Conservative <br> Organized"],
"question4": ["Loving <br> Inspirational<br> Dramatic", "Daring <br> Impulsive <br> Fun", "Determined <br> Complex <br> Composed","Concerned <br> Procedural <br> Cooperative"],
"question5": ["Vivacious <br> Affectionate <br> Sympathetic", "Exciting <br> Courageous <br> Skillful", "Determined <br> Principled <br> Rational", "Orderly <br> Habitual <br> Caring"]
}

from google.appengine.api import users
from google.appengine.ext import ndb

#jinja2.Environment is a constructor

class GoogleUser(ndb.Model):
    first_name = ndb.StringProperty(required = True)
    last_initial = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)

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
            signedIn = False
            logout_url = ""
            goToURL = ""
            hasTakenTest = False

            if existing_user:
                if hasTakenTest == True:
                    user_status = "Results"
                    goToURL = "/pages/newUser"
                else:
                    user_status = "Take Test"
                    goToURL = "/pages/personalitytest"

                signedIn = True
                logout_url = users.create_logout_url('/')
            else:
                user_status = "Add Info"


            mydict = {
                "status": user_status,
                "isSignedIn": signedIn,
                "url": logout_url,
                "goTo": goToURL
            }

            self.response.write(welcome_page.render(mydict))
        else:
            user_status = "Sign In"
            login_url = users.create_login_url('/pages/newUser')

            mydict = {
                "status": user_status,
                "isSignedIn": False,
                "goTo": login_url
            }

            self.response.write(welcome_page.render(mydict))

class PersonalityTestPage(webapp2.RequestHandler):
    def get(self):
        personality_test_page = jinja_env.get_template('pages/personalitytest.html')
        # personality_dictionary = Questions.adjectives_dict

        self.response.write(personality_test_page.render(personalitytest))


class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_page = jinja_env.get_template('pages/about.html')
        self.response.write(about_page.render())

class ConnectionsPage(webapp2.RequestHandler):
    def get(self):
        connections_page = jinja_env.get_template('pages/connections.html')
        self.response.write(connections_page.render())

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        results_page = jinja_env.get_template('pages/results.html')
        self.response.write(results_page.render())
        
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

        if(list_colors.index(max_value) == 0):
            color_store = answersStore(color = "Blue")
        elif(list_colors.index(max_value) == 1):
            color_store = answersStore(color = "Orange")
        elif(list_colors.index(max_value) == 2):
            color_store = answersStore(color = "Green")
        elif(list_colors.index(max_value) == 3):
            color_store = answersStore(color = "Gold")

        # user_array.put()
        color_store.put()
        data = {
            "user_color" : color_store.color
            # "user_all_answers" : user_answers
        }

        user = users.get_current_user()

        google_user = GoogleUser(
            first_name=self.request.get('first_name'),
            last_initial=self.request.get('last_initial'),
            email = user.nickname()
        )

        google_user.put()

        about_template = jinja_env.get_template('pages/about.html')
        self.response.write(about_template.render(data))

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
