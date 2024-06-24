import yaml
import os

directory = 'ymalbk'

yaml_files = [f for f in os.listdir(directory) if f.endswith('.yaml') or f.endswith('.yml')]

yaml_files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
most_recent_yaml_file = os.path.join(directory, yaml_files[0])

with open(most_recent_yaml_file, 'r') as file:
    data = yaml.safe_load(file)

euro_data = data['bpi']['EUR']
euro_code = euro_data['code']
euro_rate = euro_data['rate']

print(euro_code)
print("Current price:", euro_rate)
