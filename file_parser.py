import os
import requests
from bs4 import BeautifulSoup

# file type, ex. ".pdf"
file_type = ".pdf"

# site URL, ex. "https://history.md/personalitati_istorice"
base_url = 'https://history.md/personalitati_istorice'

output_dir = 'downloaded_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# get site HTML
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# find all files
file_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(file_type)]

# download all files_type
for link in file_links:
    file_url = base_url + link
    file_response = requests.get(file_url)
    
    # file name for save
    filename = os.path.join(output_dir, link.split('/')[-1])
    
    # save file
    with open(filename, 'wb') as f:
        f.write(file_response.content)
    
    print(f'Скачан файл: {filename}')

print('Все файлы загружены.')
