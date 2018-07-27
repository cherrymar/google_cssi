import webapp2

from google.appengine.ext import ndb


class Person( ndb.Model ):
    name = ndb.StringProperty(required=True)
    height = ndb.IntegerProperty(required=True)
    interests = ndb.StringProperty(repeated=True, required=False)



class DemoHandler( webapp2.RequestHandler):
    def get(self):
        my_query = Person.query()
        # print(my_query)
        persons = my_query.fetch()
        # print(persons)

        seemongs = my_query.filter(Person.name == "Seemong").fetch()
        print( seemongs )

        tall_people = my_query.filter(Person.height > 90).fetch()
        ordered_names = my_query.order(Person.name).fetch(1)
        results = str(ordered_names)

        # jordan = Person( name='Jordan', height=74 )
        # seemong = Person( name="Seemong", height=72)
        # # self.response.write(jordan)
        self.response.write(results)
        #
        # jordan.put()
        # seemong.put()

app = webapp2.WSGIApplication([
    ('/', DemoHandler),

], debug=True)
