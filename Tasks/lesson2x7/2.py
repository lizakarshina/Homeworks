# Підключення до сервісного аккаунту гугл клауд та гугл таблиць
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# підключення до ?
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


# Підклбючення до сервісного аккаунту за допомогою ключа
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "endless-beach-447312-i9-52a137f071b7.json", scope
)


# Вхід в аккаунт
client = gspread.authorize(creds)

# Підключення до таблиці
data = client.open_by_key('1ifqh6r1qOJnytfNwJ2euU84fRbJ6ZKZFE7FI44gy-lo')

# Перемикання між аркушами
data1 = data.worksheet('Sheet2')