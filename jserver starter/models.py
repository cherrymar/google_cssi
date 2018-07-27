from google.appengine.ext import ndb

class Person( ndb.Model ):
    nickname = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    user_id = ndb.StringProperty(required=True)
    page_view_count = ndb.IntegerProperty(required=True)

    def increment(self):
        self.page_view_count += 1
