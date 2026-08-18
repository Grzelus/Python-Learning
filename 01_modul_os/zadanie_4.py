
import os

username = os.getenv('USERNAME') or os.getenv('USER')
print(username)

app_mode = os.getenv('APP_MODE', 'DEVELOPMENT')
print(app_mode)

os.environ['SECRET_KEY'] = 'tajny_klucz_123'
print(os.getenv('SECRET_KEY'))
