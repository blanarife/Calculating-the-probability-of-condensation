import gspread
from oauth2client.service_account import ServiceAccountCredentials

def getdata():
    # Credentials ---Fisierul "creds.json", cu datele pentru conectare la Google Sheets nu este inclus in arhiva
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    client = gspread.authorize(creds)

    # Google Sheet ID
    sheet = client.open_by_key('1-DpiZRrBoznNpKmgqGpV4uiSZ_qjLg7MP8stOMHQRw0')

    # Worksheet
    worksheet = sheet.get_worksheet(0)

    # Valorile coloanelor
    column_values1 = worksheet.col_values(3)
    column_values2 = worksheet.col_values(4)

    # Este ignorata prima linie din Sheet
    column_values1 = column_values1[1:]
    column_values2 = column_values2[1:]


    float_values1 = [float(value) for value in column_values1 if value]
    float_values2 = [float(value) for value in column_values2 if value]

    #Calcularea mediilor pe coloane
    avg1 = sum(float_values1)/len(float_values1)
    avg2 = sum(float_values2)/len(float_values2)



    print(f"Average temp: {avg1}\n")
    print(f"Average humidity: {avg2}\n")
    return avg1, avg2

#getdata()