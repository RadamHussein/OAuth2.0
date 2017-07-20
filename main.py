import webapp2
import json
import random
import string
import logging
import os
import urllib
import urllib2
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch

def getRandomState():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])

client_id = '1017761054905-ra5dv7ca5khohs1msg3l7cqft19gv1a9.apps.googleusercontent.com'
client_secret = 'PFmUQEQlgGzXUpugxihDSdnv'
response_type = 'response_type=code'
#redirect_uri = 'http://localhost:8080/OAuth'
redirect_uri = 'https://oauth-174216.appspot.com/OAuth'
scope = 'scope=email'
global state

# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        global state
        state = getRandomState()
        return self.redirect('https://accounts.google.com/o/oauth2/v2/auth' + '?' + response_type + '&client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&' + scope + '&state=' + state)

class OAuth(webapp2.RequestHandler):

    def get(self):
        response = self.request.GET
        code = response['code']

        post_body = {
            'code':code,
            'client_id':client_id,
            'client_secret':client_secret,
            #'redirect_uri':'http://localhost:8080/OAuth',
            'redirect_uri':'https://oauth-174216.appspot.com/OAuth',
            'grant_type':'authorization_code'
        }

        #send the request
        try:
            data = urllib.urlencode(post_body)
            headers = {'Content-Type':'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(
                url="https://www.googleapis.com/oauth2/v4/token",
                payload = data,
                method = urlfetch.POST,
                headers = headers
            )
            response = json.loads(result.content)
            access_token = response['access_token']
            access_str = json.dumps(access_token)
            bearer = 'Bearer '
            authorization = bearer + access_token
            final_auth = json.dumps(authorization)
            try:
                headers = {'Authorization':authorization}
                url = 'https://www.googleapis.com/plus/v1/people/me'
                result = urlfetch.fetch(url, headers=headers)
                if result.status_code == 200:
                    result_dict = json.loads(result.content)
                    name = result_dict['name']
                    first_name = name['givenName']
                    last_name = name['familyName']

                    #set up temptlate values
                    template_values = {
                        'url':result_dict['url'],
                        'first_name':first_name,
                        'last_name':last_name,
                        'state':state,
                    }

                    #render template
                    path = os.path.join(os.path.dirname(__file__), 'www/template.html')
                    self.response.out.write(template.render(path, template_values))
                else:
                    self.response.write(result.content)
            except urlfetch.Error:
                logging.exception('Caught exception fetching url')
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
# [END main_page]

# [START app]
app = webapp2.WSGIApplication([
    ('/OAuth/provider', MainPage),
    ('/OAuth', OAuth),
], debug=True)
# [END app]
