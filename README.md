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


https://www.lithiumbatterypower.com/
https://relionbattery.com/products/lithium/rb100 - близко к нашей теме
https://www.solarpowerworldonline.com/2015/08/what-is-the-best-type-of-battery-for-solar-storage/ - информация по батареям
https://www.dnkpower.com/lifepo4-battery/ - еще информация
https://www.lithiumpowerinc.com/ph48-5-industrial-lithium-battery.html - информация
https://flexsolsolutions.com/soluxio/advantages-lithium-batteries/ - информация
https://lithiumbatterycompany.com/ - лендинг по теме
https://www.victronenergy.com/batteries - информация
http://www.ibt-power.com/About_IBT_Power.html - информация
http://www.rollsbattery.com/ - по теме ландинга
https://www.victronenergy.com/ - по теме лендинга и информация