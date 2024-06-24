# send_email.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import kreds
import os 
import yaml

directory = 'ymalbk'

yaml_files = [f for f in os.listdir(directory) if f.endswith('.yaml') or f.endswith('.yml')]

yaml_files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
most_recent_yaml_file = os.path.join(directory, yaml_files[0])

with open(most_recent_yaml_file, 'r') as file:
    data = yaml.safe_load(file)

euro_data = data['bpi']['EUR']
euro_code = euro_data['code']
euro_rate = euro_data['rate']

directory = 'weatherdata'

yaml_files = [f for f in os.listdir(directory) if f.endswith('.yaml') or f.endswith('.yml')]

yaml_files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
most_recent_yaml_file = os.path.join(directory, yaml_files[0])

with open(most_recent_yaml_file, 'r') as file:
    data = yaml.safe_load(file)

weather_data19 = data['actual']['stationmeasurements'][19]
weather_report = data['forecast']['weatherreport']['summary']
weather_stationname = weather_data19['stationname']
temp = weather_data19['temperature']
leeuwarden = f"De temperatuur in {weather_stationname} is {temp} graden Celsius"

weather_data10 = data['actual']['stationmeasurements'][10]
weather_report = data['forecast']['weatherreport']['summary']
weather_stationname10 = weather_data10['stationname']
temp10 = weather_data10['temperature']
groningen = f"De temperatuur in {weather_stationname10} is {temp10} graden Celsius"
#print(leeuwarden)
#print(groningen)

## debug dingen
#print(euro_code)
#print("Current price:", euro_rate)
#print("De tempratuur in", weather_stationname, "is ", temp, "graden Celsius")
#print("De tempratuur in", weather_stationname10, "is ", temp10,"graden Celsius")

# Email opmaak
subject = "BTC price"
body = f"EUR Code: {euro_code}\nEUR prijs: € {euro_rate}\n\nWeather report\n{leeuwarden}\n{groningen}" 
#body = {
#    "euro_code": euro_code,
#    "euro_rate": euro_rate,
#    # Add other elements to the body as needed
#}
#
# pakt de variable van de kreds.py

sender_email = kreds.sender_email
receiver_email = kreds.receiver_email
passwd = kreds.password

# maakt een container en vult de verzend informatie in.
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = "Daily Finance with Xiam"
msg['To'] = ",".join(receiver_email)

msg.attach(MIMEText(body, 'plain'))

# Log in to the SMTP server and send the email
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, passwd)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
