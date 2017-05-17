import requests
from ..exceptions import ApiError
from urllib.parse import urljoin
from datetime import datetime

SENATE_BASE_URL = "http://legis.senado.gov.br/dadosabertos/"


class SenatorClient(object):
    senators_relative_url = "senador/lista/atual"
    headers = {
        "Accept": "application/json"
    }

    def __init__(self):
        pass

    def get(self):
        get_url = urljoin(SENATE_BASE_URL, self.senators_relative_url)
        response = requests.get(get_url, headers=self.headers)
        if response.status_code != 200:
            raise ApiError('GET {} {}'.format(self.senators_relative_url, response.status_code))
        senators = response.json()

        return senators["ListaParlamentarEmExercicio"]["Parlamentares"]["Parlamentar"]