# libattery



db : 
    'NAME': 'li_battery_db',
    'USER': 'li_battery_user',
    'PASSWORD': 'li_battery_password',

1. Создать postgres bd
    CREATE DATABASE li_battery_db;
    CREATE USER li_battery_user WITH password 'li_battery_password';
    GRANT ALL ON DATABASE li_battery_db TO search_space_user;
    
2. Создать виртуалку
    в консоли:
    virtualenv -p python3 venv
    
3. Активировать виртуалку
   source venv/bin/activate
   
4.  Установить зависимости
    pip install -r requirements.txt

дальше тестить


