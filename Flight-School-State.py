# Used to test 

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.flightschoollist.com/Alaska-airplane-flight-schools/')
soup = BeautifulSoup(r.text, 'html.parser')

base_url = 'https://www.flightschoollist.com'

#for page in range(10):
#    url = f'https://www.flightschoollist.com/california-airplane-flight-schools/?pageNum_rsSchoolLocation={page}&totalRows_rsSchoolLocation=91'

pagination = soup.find_all('ul', class_ = 'pagination pagination-sm pull-right')

for item in pagination:
    partial_link = item.find('li').find('a')['href']
    num_schools = partial_link.split('=')[2]
    print(num_schools)

data = soup.find_all('tbody')
for item in data: 
    sections = item.find_all('tr')
    for td in sections: 
        listings = td.find_all('td')

        for item in listings[1]:
            link = base_url + item['href']
  


# Still need: 
# Pagination
# 