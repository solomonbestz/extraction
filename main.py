import requests
from bs4 import BeautifulSoup


url = 'https://9jabestz.com/movies'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
yearly_contribution = soup.find('body').find_all('h3')

for x in yearly_contribution:
    print(x.text.strip())