import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = './credentials.json'
CALENDAR_ID = 'primary'

def get_calendar_service():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_event(summary, start_time, end_time):
    service = get_calendar_service()
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Tbilisi',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Tbilisi',
        }
    }

    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return event.get('htmlLink')
