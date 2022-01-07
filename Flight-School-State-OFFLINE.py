# OFFLINE file used to parse HTML

from bs4 import BeautifulSoup

file = open('State-Offline.html')


states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'NewHampshire', 'NewJersey',
          'NewMexico', 'NewYork', 'NorthCarolona', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland', 'SouthCarolina',
          'SouthDakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgina', 'West Virginia', 'Wisconsin', 'Wyoming']


school_urls = []

def test(state):
    soup = BeautifulSoup(file, 'html.parser')

    base_url = 'https://www.flightschoollist.com'
    state_url = f'https://www.flightschoollist.com/{state}-airplane-flight-schools/'


    pagination = soup.find_all('ul', class_ = 'pagination pagination-sm pull-right')

    for item in pagination:
        partial_link = item.find('li').find('a')['href']
        num_schools = partial_link.split('=')[2]

    data = soup.find_all('tbody')
    for item in data: 
        sections = item.find_all('tr')
        for td in sections: 
            listings = td.find_all('td')

            for item in listings[1]:
                link = base_url + item['href']
            

                school_urls.append(link)


test('California')


# DONE: 
# School name
# Airport 
# Location
# School URL


# Still need: 
# Pagination
# 