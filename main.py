import webapp2  #connecting to the google app engine yaml file
import jinja2 #connets to the html files
import os #apple operating system
# from google.appengine.api import urlfetch
# import json


#jinja2.Environment is a constructor

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_page = jinja_env.get_template('index.html')
        self.response.write(welcome_page.render())

# the app configuration section
app = webapp2.WSGIApplication(
    [('/', WelcomePage)], debug = True
)
