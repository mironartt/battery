# libattery

db : 
    'NAME': 'li_battery_db',
    'USER': 'li_battery_user',
    'PASSWORD': 'li_battery_password',
    
CREATE DATABASE li_battery_db;
CREATE USER li_battery_user WITH password 'li_battery_password';
GRANT ALL ON DATABASE li_battery_db TO search_space_user;


