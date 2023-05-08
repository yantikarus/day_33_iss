import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.048615 # Your latitude
MY_LONG = -124.070847 # Your longitude

my_email = lallal@yahoo.com
my_pass = fadsfasdf
iss_nearby = False


def iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 6
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 18
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise :
        return True

while True:
    time.sleep(600)
    if iss_nearby() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=passw)
        connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject: ISS above Calgary\n\nlook up!")




