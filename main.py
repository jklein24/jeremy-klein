# import the Bottle framework
from bottle import Bottle
from bottle import static_file

# Create the Bottle WSGI application.
bottle = Bottle()
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


# Define a handler for the root URL of our application.
@bottle.route('/')
def hello():
    return static_file('index.html', root='')



# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.'