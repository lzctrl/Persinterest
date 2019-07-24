import webapp2  #connecting to the google app engine yaml file
import jinja2 #connets to the html files
import os #apple operating system
# from google.appengine.api import urlfetch
# import json
from personalityTest import answersStore


#jinja2.Environment is a constructor

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



class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_page = jinja_env.get_template('pages/about.html')
        self.response.write(about_page.render())
    def post(self):
        answer1 = self.request.get("template")
        answer2 = self.request.get("template2")
        answer3 = self.request.get("template3")
        answer4 = self.request.get("template4")
        answer5 = self.request.get("template5")
        answer_store = answersStore(a1 = answer1, a2 = answer2, a3 = answer3, a4 = answer4, a5 = answer5)
        answer_store.put()
        data = {
            "user_answer" : [answer1, answer2, answer3, answer4, answer5]
                # "user_answer1": answer1,
                # "user_answer2": answer2,
                # "user_answer3": answer3,
                # "user_answer4": answer4,
                # "user_answer5": answer5
        }
        about_template = jinja_env.get_template('pages/about.html')
        self.response.write(about_template.render(data))

class ConnectionsPage(webapp2.RequestHandler):
    def get(self):
        connections_page = jinja_env.get_template('pages/connections.html')
        self.response.write(connections_page.render())

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        results_page = jinja_env.get_template('pages/results.html')
        self.response.write(results_page.render())

# the app configuration section
app = webapp2.WSGIApplication(
    [('/', WelcomePage), ('/pages/personalitytest', PersonalityTestPage), ('/pages/about', AboutPage), ('/pages/connections', ConnectionsPage), ('/pages/results', ResultsPage)],
    debug = True
)
