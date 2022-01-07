# Uses Requests-HTML to Render page

from requests_html import HTMLSession

def test(state):
    session = HTMLSession()
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
    state_url = f'https://www.flightschoollist.com/{state}-airplane-flight-schools/'
    r = session.get(state_url, headers=headers)
    r.html.render(sleep=1, keep_page=True)  # Running this will make the script freeze up

    num_schools_section = r.html.find('strong.alternative-font', first=True)
    print(num_schools_section)





test('Arizona')


# num_schools_section.text or num_schools_section.full_text will result in 0
