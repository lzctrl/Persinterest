import webapp2  #connecting to the google app engine yaml file
import jinja2 #connets to the html files
import os #apple operating system
# from google.appengine.api import urlfetch
# import json
from google.appengine.api import users
from google.appengine.ext import ndb

#jinja2.Environment is a constructor

class TestUser(ndb.Model):
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
        self.response.write(welcome_page.render())

class PersonalityTestPage(webapp2.RequestHandler):
    def get(self):
        personality_test_page = jinja_env.get_template('pages/personalitytest.html')
        # personality_dictionary = Questions.adjectives_dict

        personalitytest = {
            # index 0 = blueWords, 1 = orangeWords, 2 = greenWords, 3 = goldWords
        "question1": ["Authentic <br> Harmonious <br> Compassionate", "Active <br> Opportunistic <br> Spontaneous", "Versatile <br> Inventive <br> Competent", "Parental <br> Traditional <br> Responsible"],
        "question2": ["Unique <br> Empathetic <br> Communicative", "Competitive <br> Impetuous <br> Impactful","Curious <br> Conceptual <br> Knowledgeable","Practical <br> Sensible <br> Dependable"],
        "question3": ["Devoted <br> Warm <br> Personable", "Realistic <br> Open-Minded <br> Adventuresome", "Theoretical <br> Seeking <br> Ingenious", "Loyal <br> Conservative <br> Organized"],
        "question4": ["Loving <br> Inspirational<br> Dramatic", "Daring <br> Impulsive <br> Fun", "Determined <br> Complex <br> Composed","Concerned <br> Procedural <br> Cooperative"],
        "question5": ["Vivacious <br> Affectionate <br> Sympathetic", "Exciting <br> Courageous <br> Skillful", "Determined <br> Principled <br> Rational", "Orderly <br> Habitual <br> Caring"]
        }
        self.response.write(personality_test_page.render(personalitytest))


        # def post(self):
        #     answer1 =
        #     answer2 =
        #     answer3 =
        #     answer4 =

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
        user = users.get_current_user()
        print("WE ARE HERE 3")
        test_user = TestUser(
            first_name=self.request.get('first_name'),
            last_initial=self.request.get('last_initial'),
            email = user.nickname()
        )
        test_user.put()
        # results_page = jinja_env.get_template('pages/results.html')
        # self.response.write(results_page.render())

class NewUserPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            email_address = user.nickname()
            logout_url = users.create_logout_url('/pages/results')
            logout_button = '<a href="%s"> Log out</a>' % logout_url

            existing_user = TestUser.query().filter(TestUser.email == email_address).get()
            if existing_user:
                #takes them to the results page/connection page with others
                results_page = jinja_env.get_template('pages/results.html')
                self.response.write(results_page.render())
            else:
                #insert a "not registered yet?" prompt with a redirection to this please register page
                login_url = users.create_login_url('/pages/results')
                login_button = '<a href="%s"> Sign In</a>' % login_url
                # login_button = '<a href="' + login_url + '"> Sign In</a>'
                self.response.write("Please login: " + login_button + "<br>We are here");

        else:
            login_url = users.create_login_url('/pages/results')
            login_button = '<a href="%s"> Sign In</a>' % login_url
            # login_button = '<a href="' + login_url + '"> Sign In</a>'
            self.response.write(login_url)

    def post(self):
        user = users.get_current_user()
        print("WE ARE HERE 4")
        test_user = TestUser(
            first_name=self.request.get('first_name'),
            last_initial=self.request.get('last_initial'),
            email = user.nickname()
        )
        test_user.put()
        # results_page = jinja_env.get_template('pages/results.html')
        # self.response.write(results_page.render())

# the app configuration section
app = webapp2.WSGIApplication(
    [('/', WelcomePage), ('/pages/newUser', NewUserPage), ('/pages/personalitytest', PersonalityTestPage), ('/pages/about', AboutPage), ('/pages/connections', ConnectionsPage), ('/pages/results', ResultsPage)],
    debug = True
)
