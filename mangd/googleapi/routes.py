#google api imports
from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from flask import session, redirect, request, url_for, Blueprint
import os 

googleapi = Blueprint('googleapi', __name__)

#permition of what the user will allow tthe web app to use
CLIENT_SECRETS_FILE = 'mangd\googleapi\client_secret.json'
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
CALENDAR_SCOPES = ['openid', 'https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']


@googleapi.route('/authorize')
def authorize():
  flow = Flow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, scopes=CALENDAR_SCOPES)
  flow.redirect_uri = url_for('googleapi.oauth2callback', _external=True)
  authorization_url, state = flow.authorization_url(
      access_type='offline',
      include_granted_scopes='true')
  session['state'] = state
  return redirect(authorization_url)

@googleapi.route('/oauth2callback')
def oauth2callback():
  state = session['state']
  flow = Flow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, scopes=CALENDAR_SCOPES, state=state)
  flow.redirect_uri = url_for('googleapi.oauth2callback', _external=True)
  authorization_response = request.url
  flow.fetch_token(authorization_response=authorization_response)
  credentials = flow.credentials
  session['credentials'] = credentials_to_dict(credentials)
  return redirect(url_for("todos.todos"))


def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}
