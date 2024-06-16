import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.protobuf import service
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import email


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def myEmails():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
        service = build('gmail', 'v1', credentials= creds)


        specificEmails = ['info@higround.co']

        for emails in specificEmails:
            query = f'from:{specificEmails}'
            result = service.users().messages().list(userId='me').execute()
            messages = result.get('messages')
            if not messages:
                print("No messages found")
            else:
                for msg in messages:
                    msgId = msg['id']

                    service.users().messages().modify(userId = 'me', id = msgId, body = {'removeLabelIds': ['INBOX']}).execute()

                print(f"Archived {len(messages)} messages from {specificEmails}.")




if __name__ == '__main__':
    myEmails()
