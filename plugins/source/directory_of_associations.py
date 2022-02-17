from bs4 import BeautifulSoup

from systems.plugins.index import BaseProvider

import requests


class Provider(BaseProvider('source', 'directory_of_associations')):

    state_codes = [
        'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
        'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
        'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
        'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
        'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'
    ]


    def item_columns(self):
        return ['name', 'type', 'url', 'city', 'state', 'zipcode', 'bio', 'member_count', 'staff_count', 'year_founded', 'budget']


    def load_items(self, context):
        for state_code in self.state_codes:
            page = 1
            while page > 0:
                base_url = 'https://directoryofassociations.com/browse.asp?dp='+str(page)+'&n=&s='+state_code+'&c=&z=&t1=&g=&m='
                page = requests.get(base_url)
                soup = BeautifulSoup(page.content, "html.parser")
                results = soup.find_all("tr", class_="")
                if results:
                    for result in results:
                        data = {}
                        org_href = result.find('a')['href']
                        org_name = result.find('a').find('strong').text
                        data['name'] = org_name

                        org_dir_url = 'https://directoryofassociations.com/' + org_href
                        org_dir_page = requests.get(org_dir_url)
                        org_dir_soup = BeautifulSoup(org_dir_page.content, "html.parser")

                        org_url = org_dir_soup.find('div', class_='jumbotron').find('h2').text
                        data['url'] = org_url

                        org_address = org_dir_soup.find('div', class_='jumbotron').find('p')

                        org_address_locality = org_address.find('span',itemprop='locality').text
                        data['city'] = org_address_locality

                        org_address_region = org_address.find('span',itemprop='region').text
                        data['state'] = state_code

                        org_address_zip = org_address.find('span',itemprop='postal-code').text
                        data['zipcode'] = org_address_zip

                        org_bio = org_dir_soup.find('div', class_='col-md-12').find('p').text
                        data['bio'] = org_bio

                        org_info_summary = org_dir_soup.find_all('div', class_='row')[1].find_all('span')
                        try:
                            data['member_count'] = org_info_summary[0].text
                        except:
                            data['member_count'] = ''

                        try:
                            data['staff_count'] = org_info_summary[2].text
                        except:
                            data['staff_count'] = ''

                        try:
                            data['year_founded'] = org_info_summary[1].text
                        except:
                            data['year_founded'] = ''

                        try:
                            data['budget'] = org_info_summary[3].text
                        except:
                            data['budget'] = ''

                        try:
                            data['type'] = org_info_summary[5].text
                        except:
                            data['type'] = ''

                        yield data

                    page += 1


    def load_item(self, association, context):
        return [
            association['name'],
            association['type'],
            association['url'],
            association['city'],
            association['state'],
            association['zipcode'],
            association['bio'],
            association['member_count'],
            association['staff_count'],
            association['year_founded'],
            association['budget']
        ]
