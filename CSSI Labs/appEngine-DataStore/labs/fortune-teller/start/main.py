#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import random
import jinja2


def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list=[
        'Money is on the way',
        'You will get a job at Google',
        'Someone will give you food',
        'An apple will fall from the sky and land at your feet',
        'Someone will ask you for food',
        'The person you are looking for will arrive',
        'E=mc^2',
        'You will face a danger and WIN',
        'You will face a danger and LOSE',
        'Ben will say "hi cher" in two seconds',
        'You will find a new job',
        'You will get a raise',
        'Google will hire you',
        'Amazon will hire you',
        'Facebook will hire you',
        'No one will hire you',
        'You will be the next billionaire',
        'You will NOT get freshman 15',
    ]
    #use the random library to return a random element from the array
    random_fortune = fortune_list[random.randint( 0, len(fortune_list) - 1 )]
    return(random_fortune)


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader( os.path.dirname(__file__) )
)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("templates/fortune-results.html")
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        self.response.write( results_template.render() )
        # self.response.write( get_fortune() )
    #add a post method
    def post(self):
        end_template = jinja_current_directory.get_template( "templates/fortune-end.html")
        user_astro_sign = self.request.get('user_astrological_sign')

        user_input = {
            "sign" : user_astro_sign,
            "fortune" : get_fortune(),
        }
        self.response.write(end_template.render(user_input))


class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Goodbye World. Goodbye to the root route of my app')

#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler),
    ('/farewell', GoodbyeHandler), #maps '/predict' to the FortuneHandler
], debug=True)
