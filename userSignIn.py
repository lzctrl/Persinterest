import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

class TestUser(ndb.Model):
    first_name = ndb.StringProperty(required = True)
    last_initial = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)



class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email_address = user.nickname()
            logout_url = users.create_logout_url('/')
            logout_button = '<a href="%s"> Log out</a>' % logout_url

            existing_user = TestUser.query().filter(TestUser.email == email_address).get()
            if existing_user:
                #takes them to the results page/connection page with others
                self.response.write('Welcome Back! ' + existing_user.first_name + "<br>" +logout_button)
            else:
                #insert a "not registered yet?" prompt with a redirection to this please register page
                self.response.write('''Please register!
                    <form method='post' action='/'>
                        First Name: <input type='text' name='first_name'>
                        Last Initial: <input type='text' maxlength='1' name='last_initial'>
                        <input type='submit'>
                    </form>
                    <br>
                ''' )
                #     self.response.write("")

        else:
            login_url = users.create_login_url('/')
            login_button = '<a href="%s"> Sign In</a>' % login_url
            # login_button = '<a href="' + login_url + '"> Sign In</a>'
            self.response.write("Please log in!<br>" + login_button)
    def post(self):
        user = users.get_current_user()
        if user:
            test_user = TestUser(
                first_name=self.request.get('first_name'),
                last_initial=self.request.get('last_initial'),
                email = user.nickname()
            )
            test_user.put()
            self.response.write('Thank you for registering <a href="/">Results</a>')

#initialization code
app = webapp2.WSGIApplication(
    [('/', MainHandler)],
    debug = True
)
