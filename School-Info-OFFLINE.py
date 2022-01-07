# OFFLINE file for parsing school contact info HTML file

from bs4 import BeautifulSoup

with open('School-Info-Offline.html') as file: 
    soup = BeautifulSoup(file, 'html.parser')

contact_details_list = []

contact_details = soup.find_all('ul', class_ = 'list list-icons list-icons-style-3 mt-xlg')

for item in contact_details:
   information = item.text
   pieces = information.split('  ')

   school_name = item.find('a').text
   address = pieces[1].split(':')[1].strip()
   airport = pieces[2].split(':')[1].strip()
   phone_number = pieces[3].split(':')[1].strip()
   email = pieces[4].split(':')[1].strip()
   school_url = item.find('a')['href']

   details = {
      'school_name': school_name, 
      'address': address, 
      'airport': airport, 
      'phone_number': phone_number, 
      'email': email, 
      'school_url': school_url,
   }

   contact_details_list.append(details)

print(contact_details_list)

