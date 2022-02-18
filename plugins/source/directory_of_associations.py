from bs4 import BeautifulSoup

from systems.plugins.index import BaseProvider

import requests


class Provider(BaseProvider('source', 'directory_of_associations')):

    base_url = 'https://directoryofassociations.com/browse.asp'

    state_codes = [
        'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
        'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
        'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
        'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
        'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'
    ]


    def item_columns(self):
        return [
            'name',
            'type',
            'url',
            'bio',
            'city',
            'state',
            'zipcode',
            'member_count',
            'staff_count',
            'year_founded',
            'budget'
        ]


    def load_items(self, context):
        request_options = [ 'n=', 'c=', 'z=', 't1=', 'g=', 'm=' ]

        for state_code in self.state_codes:
            page = self.command.get_state(self._get_page_state_name(state_code), 1)

            while True:
                self.command.notice("Retrieving Directory of Associations [ {} ] page {}".format(state_code, page))
                query_params = "&".join(request_options + [ "s={}".format(state_code), "dp={}".format(page) ])
                response = requests.get("{}?{}".format(self.base_url, query_params))

                soup = BeautifulSoup(response.content, 'html.parser')
                results = soup.find_all('tr', class_ = '')
                if not results:
                    break

                for result in results:
                    link = result.find('a')['href']
                    name = result.find('a').find('strong').text

                    info_response = requests.get("https://directoryofassociations.com/{}".format(link))
                    org_dir_soup = BeautifulSoup(info_response.content, 'html.parser')

                    address = org_dir_soup.find('div', class_='jumbotron').find('p')
                    summary = org_dir_soup.find_all('div', class_='row')[1].find_all('span')

                    yield {
                        'name': name,
                        'url': self._get_text(org_dir_soup.find('div', class_='jumbotron').find('h2')),
                        'bio': self._get_text(org_dir_soup.find('div', class_ = 'col-md-12').find('p')),
                        'state': state_code,
                        'city': self._get_text(address.find('span', itemprop = 'locality')),
                        'zipcode': self._get_text(address.find('span', itemprop = 'postal-code')),
                        'member_count': self._get_text(summary[0]),
                        'year_founded': self._get_text(summary[1]),
                        'staff_count': self._get_text(summary[2]),
                        'budget': self._get_text(summary[3]),
                        'type': self._get_text(summary[5])
                    }
                    self.command.sleep(0.5)

                page += 1
                self.command.set_state(self._get_page_state_name(state_code), page)
                self.command.sleep(2)

            self.command.delete_state(self._get_page_state_name(state_code))


    def load_item(self, association, context):
        values = []
        for field in self.item_columns():
            values.append(association[field])
        return values


    def _get_page_state_name(self, state_code):
        return "directory_of_associations_{}_page".format(state_code.lower())

    def _get_text(self, element):
        try:
            return element.text
        except Exception:
            return ''
