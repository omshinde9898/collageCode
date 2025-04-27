import requests

# URL of the raw file (not the GitHub page, but the raw file link)
url = 'https://raw.githubusercontent.com/omshinde9898/collageCode/main/DC_1/client.py'

# Local filename to save the file
filename = 'downloaded_file.py'

# Download the file
response = requests.get(url)
if response.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded successfully: {filename}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
