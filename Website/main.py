import webapp2
import jinja2
import os

# START MAGIC CODE
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader( os.path.dirname(__file__) )
)
# END MAGIC CODE


class MainPage( webapp2.RequestHandler ):
    def get( self ):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write( 'Hello World \n' )
        self.response.write( 'WOWZA THIS IS MY FIRST LEGIT-ISH WEBPAGE' )

class HelloPage( webapp2.RequestHandler ):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        page = ( '<!DOCTYPE html>' +
            '<html>' +
            '<head>' +
            '</head>' +
            '<body>' +
            '<h1>Hello!</h1>' +
            '</body>' +
            '</html>' )
        self.response.write( page )

class InfoPage( webapp2.RequestHandler ):
    def get( self ):
        info_template = jinja_env.get_template("templates/info-input.html")
        # name = "Artemis"
        # input = {
        #     'name' : name,
        #     'sport' : 'soccer',
        #     'dance' : 'hip hop',
        #     'info_messages' : [
        #         'At bicycle camp today',
        #         'Played Dragon Quest Builders'
        #         ],
        #     'is_happy' : False,
        #     'flowers' : [
        #         'Daffodils', 'Horsetails', 'Lilies'
        #     ],
        # }
        self.response.write( info_template.render() )

    def post( self ):
        info_details = jinja_env.get_template( "templates/info.html")
        user_name = self.request.get('fullname')
        user_address = self.request.get('address')
        user_color = self.request.get('color')

        user_input = {
            "name" : user_name,
            "address" : user_address,
            "color" : user_color,
        }
        self.response.write( info_details.render(user_input) )

app = webapp2.WSGIApplication([ #constructor
    ('/', MainPage),
    ('/hello', HelloPage),
    ( '/info', InfoPage ),
], debug=True)
