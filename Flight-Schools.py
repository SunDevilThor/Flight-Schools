# Flight Schools - Webscraping Project from Upwork

# Objective: Gather data on all of the Airplane Flight Schools in the USA from:
# https://www.flightschoollist.com/airplane-flight-schools/

# And to create a spreadsheet with the following data:

# 1. Business Name
# 2. Owner/Director/CEO First and Last Name
# 3. Owner/Director/CEO Email ("info@..." or "contact@company.com" not accepted)
# 4. Owner/Director/CEO Contact Phone Number
# 5. Business Website URL
# 6. Business Address
# 7. Business Phone Number

# How many flight schools are operating in the USA?

import requests
from bs4 import BeautifulSoup
import pandas as pd


MASTER_LIST = []

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'NewHampshire', 'NewJersey',
          'NewMexico', 'NewYork', 'NorthCarolona', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland', 'SouthCarolina',
          'SouthDakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgina', 'West Virginia', 'Wisconsin', 'Wyoming']


flight_school_states_urls = []
school_urls = []
contact_details_list = []
num_schools_per_state = []


def flight_state_urls():
    for state in states:
        flight_schools = f'https://www.flightschoollist.com/{state}-airplane-flight-schools/'
        r = requests.get(flight_schools)
        print('Getting URL for state:', state, r.status_code)
        flight_school_states_urls.append(flight_schools) 


def state_school_urls():
    for state in states: 
        print('Getting school links for', state)
        state_url = f'https://www.flightschoollist.com/{state}-airplane-flight-schools/'
        base_url = 'https://www.flightschoollist.com'

        r = requests.get(state_url)
        soup = BeautifulSoup(r.text, 'html.parser')

        pagination = soup.find_all('ul', class_ = 'pagination pagination-sm pull-right')

        for item in pagination:
            partial_link = item.find('li').find('a')['href']
            num_schools = int(partial_link.split('=')[2])

            num_schools_per_state.append(num_schools)

        data = soup.find_all('tbody')
        for item in data: 
            sections = item.find_all('tr')
            for td in sections: 
                listings = td.find_all('td')

                for item in listings[1]:
                    link = base_url + item['href']

                    school_urls.append(link)


def school_info():
    for url in school_urls:
        print('Gathering info from:', url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        contact_details = soup.find_all('ul', class_ = 'list list-icons list-icons-style-3 mt-xlg')

        for item in contact_details:
            information = item.text
            pieces = information.split('  ')

            try: 
                school_name = item.find('a').text
                address = pieces[1].split(':')[1].strip()
                airport = pieces[2].split(':')[1].strip()
                phone_number = pieces[3].split(':')[1].strip()
                email = pieces[4].split(':')[1].strip()
                school_url = item.find('a')['href']

            except Exception as error:
                print(error, school_name, school_url)
                pass
            
            print('Getting contact details for:', school_name)

            details = {
                'school_name': school_name, 
                'address': address, 
                'airport': airport, 
                'phone_number': phone_number, 
                'email': email, 
                'school_url': school_url,
            }

            contact_details_list.append(details)


def output():
    df = pd.DataFrame(contact_details_list)
    df.to_csv('Flight-Schools-Information.csv')
    print(df.head())
    print('Success. Items saved to CSV file.')




# DONE: flight_state_urls function working good
# DONE: state_school_urls function is working
# DONE: school_info function is working


if __name__ == '__main__':
    #pass
    flight_state_urls()
    #print(flight_school_states_urls)
    state_school_urls()
    #print(school_urls)
    school_info()
    #print(contact_details_list)
    print('Total amount of flight schools in the USA:', sum(num_schools_per_state))
    #output()


# Workflow: 

# TO-DO: 
# import Requests SESSION for faster scraping
# DONE: Got result of 'num_schools' (ex: CA has 91, AZ has 24)
# Pagination for state_school_urls and school_info functions 
# Change num_schools into page numbers

# Bugs: 
# "Index error: list out of range" for a few items in "details" dictionary in school_info function

# Total amount of flight schools in the USA: 867


# https://www.flightschoollist.com/alabama-airplane-flight-schools/?pageNum_rsSchoolLocation=0&totalRows_rsSchoolLocation=11
# https://www.flightschoollist.com/alabama-airplane-flight-schools/?pageNum_rsSchoolLocation=1&totalRows_rsSchoolLocation=11


