import gspread

worksheet = gspread.service_account(filename='credentials/credentials.json').open('Cameras').get_worksheet(0)
