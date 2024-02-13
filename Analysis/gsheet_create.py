import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json', scope)
client = gspread.authorize(credentials)

#this code was used to create the google sheet to store the data.
#sheet = client.create("GWU_data_sheet")
#sheet.share('yoerisamwel@gmail.com', perm_type='user',role='writer')

sheet = client.open('GWU_data_sheet').sheet1

df = pd.read_excel('Superstore.xlsx')

df = df.applymap(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(x) and isinstance(x, pd.Timestamp) else x)

sheet.update([df.columns.values.tolist()] + df.values.tolist())

