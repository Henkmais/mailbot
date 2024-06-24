import datetime
import os 
import requests

today = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
def download_yaml(url, folder, filename):
    response = requests.get(url)
    if response.status_code == 200:
        filepath = os.path.join(folder, f"{filename}_{today}.yml")
        with open(filepath, 'w') as file:
            file.write(response.text)
        print("YAML data downloaded and saved to", filepath)

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
#url = "https://data.buienradar.nl/2.0/feed/json"
folder = "ymalbk"  # Specify the folder path here
filename = "data"
download_yaml(url, folder, filename)

url2 = "https://data.buienradar.nl/2.0/feed/json"
folder = "weatherdata"  # Specify the folder path here
filename = "data"
download_yaml(url2, folder, filename)
