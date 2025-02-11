import requests
from bs4 import BeautifulSoup
import csv
import re
import json

# Define the URL
url = 'https://www.tennisabstract.com/cgi-bin/player-more.cgi?p=104925/Novak-Djokovic&table=mcp-return'

# Fetch the page content
response = requests.get(url)
content = response.text

# Parse the HTML
soup = BeautifulSoup(content, 'html.parser')

# Find all the <script> tags
scripts = soup.find_all('script')
print(scripts)
# Initialize player_frag variable
player_frag = None

# Extract the player_frag variable content
for script in scripts:
    if script.string:
        match = re.search(r'var player_frag', script.string, re.S)
        if match:
            player_frag = json.loads(match.group(1))
            break
print(player_frag)

# If player_frag is found, extract data
if player_frag and 'data' in player_frag:
    # Extract table headers and rows
    headers = player_frag['header']
    rows = player_frag['data']

    # Create CSV file and write headers
    with open('djokovic_return.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        # Write row data
        for row in rows:
            writer.writerow(row)

    print('Data has been written to player_data.csv')
else:
    print('player_frag variable not found or does not contain data')
