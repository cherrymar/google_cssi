import logging
import os
import jinja2
import webapp2
import json
import urllib2
from google.appengine.api import urlfetch
from google.appengine.api import users
from models import Person


jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates'))



class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            #user is logged in
            log_url = users.create_logout_url('/')
            log_message = 'Sign Out'

            my_query = Person.query().filter(Person.user_id == user.user_id() ).fetch()
            if len(my_query) == 0:
                human = Person( nickname=user.nickname(), email=user.email(), user_id=user.user_id(), page_view_count=1 )
                human.put()
                # count = 1
            else:
                human = my_query[0]
                human.increment()
                human.put()
                # count = human.page_view_count

        else:
            #user is not logged in
            log_url = users.create_login_url('/')
            log_message = 'Sign In'
            # count = 0;



        response = json.loads(urlfetch.fetch("http://jservice.io/api/random?count=2").content)

        answer = response[0]['answer']
        question = response[0]['question']
        category = response[0]['category']['title']

        template = jinja_environment.get_template('main.html')
        variables = {'answer': answer,
                     'question': question,
                     'category': category,
                     'user': user,
                     'log_url': log_url,
                     'log_message': log_message,
                     # 'count': count
                     }
        self.response.out.write(template.render(variables))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
