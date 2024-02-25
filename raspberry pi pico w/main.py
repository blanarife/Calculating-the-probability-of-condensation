from machine import Pin
from time import sleep
from DHT22 import DHT22
from lcd1602 import LCD
import utime as time
import network
import urequests

lcd=LCD()

IFTTT_URL = '/trigger/temp/with/key/###'
server = 'maker.ifttt.com'

dht22=DHT22(Pin(15,Pin.IN,Pin.PULL_UP))#sensor connected GPIO 15 pin 
button = Pin(14, Pin.IN, Pin.PULL_UP)


ssid = '###'
password = '###'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
    lcd.clear()
    print('Connecting...')
    lcd.write(0, 0, "Connecting...")
    time.sleep(1)
ip = wlan.ifconfig()[0]
print('Connection successful')
lcd.write(0, 1, "Done")
print(f'Connected on {ip} \n')


def make_ifttt_request():
    print('Connecting to', server)
    json_data = '{"value1":"' + str(T) + '","value2":"' + str(H)  + '"}'
    headers = {'Content-Type': 'application/json'}
    response = urequests.post('https://' + server + IFTTT_URL, data=json_data, headers=headers)
    print('Response:', response.content.decode())
    response.close()
    print('Closing Connection')




while True:
    try:
        if button.value() == 0:
            T, H = dht22.read()
        
            print("Temperatura: ", str(T),"C")
            print("Umiditate: ", str(H),"%")
            lcd.clear()
            temps="Temp: "+ str(T) + "C"
            hum="Umiditate: "+ str(H) + "%"
            lcd.write(0, 0, temps)
            lcd.write(0, 1, hum)
            make_ifttt_request()
            time.sleep_ms(500)
    except OSError as e:
        #continue
        print('Connection closed')


