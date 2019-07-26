from google.appengine.api import users
from google.appengine.ext import ndb

class GoogleUser(ndb.Model):
    first_name = ndb.StringProperty(required = True)
    last_initial = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    hasTakenTest = ndb.BooleanProperty(required = True)
    color = ndb.StringProperty(required = False)
    education_and_careers = ndb.StringProperty(required = False)
    hobbies = ndb.StringProperty(required = False)
    living_and_travel = ndb.StringProperty(required = False)
    music = ndb.StringProperty(required = False)
    # interests = ndb.JsonProperty(requred = False)
