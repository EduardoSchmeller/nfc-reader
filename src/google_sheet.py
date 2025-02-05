import gspread
from google.oauth2.service_account import Credentials
import reader_nfc

SERVICE_ACCOUNT_FILE = ""
SPREADSHEET_ID = ""
SHEET_NAME = "Janeiro/nota-1"

def google_autenticator():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
    client = gspread.authorize(creds)
    return client


client = google_autenticator()
spreadsheet = client.open_by_key(SPREADSHEET_ID)


def checking_spreadsheet_existence(sheet_name):
    try:
        sheet = spreadsheet.worksheet(sheet_name)
        return sheet
    
    except gspread.exceptions.WorksheetNotFound:
        print("Spreadsheet not found")
        exit()


spreadsheet_exists = checking_spreadsheet_existence(SHEET_NAME)
data = spreadsheet_exists.get_all_values()


def save_data_to_spreadsheet(id):
    nfc_pure_data = reader_nfc.nfc_parse_items(id)
    sheet_data = reader_nfc.convert_date_to_sheet_format(nfc_pure_data)
    last_filled_row = len(spreadsheet_exists.get_all_values())
    next_row = last_filled_row + 1
    spreadsheet_exists.update(f"A{next_row}", [sheet_data[0] + sheet_data[1] + sheet_data[2] + sheet_data[3]])

    return spreadsheet_exists
