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


def getImage(keyword):
    words = []
    for word in keyword.split(' '):
        words.append(word)

    if len(words) == 1:
        return "https://source.unsplash.com/random/?" + keyword

    connect = ""
    for i in range(0, len(words)):
        print(i)
        print(len(words) - 1)
        if i == len(words) - 1:
            connect += words[i]
        else:
            connect += words[i] + "%20"

    print(connect)

    return "https://source.unsplash.com/random/?" + connect
