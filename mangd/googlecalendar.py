#google api imports
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

#permition of what the user will allow tthe web app to use
SCOPES = ['https://www.googleapis.com/auth/calendar']


# requests credetial from user if none are available
def google_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'mangd\client_secret.json', SCOPES)
            creds = flow.run_local_server(
                host='localhost',
                port=8080, 
                authorization_prompt_message='Please visit this URL: {url}', 
                success_message='The auth flow is complete; you may close this window.',
                open_browser=True)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service

#initialize google credentials using google_calendar_creds function
service = google_credentials()



