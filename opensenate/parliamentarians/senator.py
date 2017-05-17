import requests
from ..exceptions import ApiError
from urllib.parse import urljoin
from datetime import datetime
import xml.etree.ElementTree as ElementTree

SENATE_BASE_URL = "http://legis.senado.gov.br/dadosabertos/"


class SenatorClient(object):
    senators_relative_url = "senador/lista/atual"

    def __init__(self):
        pass

    def get(self):
        get_url = urljoin(SENATE_BASE_URL, self.senators_relative_url)
        response = requests.get(get_url)
        if response.status_code != 200:
            raise ApiError('GET {} {}'.format(self.senators_relative_url, response.status_code))
        root = ElementTree.fromstring(response.content)
        senators = []
        for senator_tree in root.find("Parlamentares"):
            senator_id = senator_tree.find("IdentificacaoParlamentar")
            senator_mandate = senator_tree.find("Mandato")

            senator = dict(senator_code=senator_id.find("CodigoParlamentar").text,
                           senator_name=senator_id.find("NomeCompletoParlamentar").text,
                           senator_gender=senator_id.find("SexoParlamentar").text,
                           senator_type=senator_id.find("FormaTratamento").text,
                           senator_exercise_code=senator_mandate.find("Exercicios").find("Exercicio").find(
                               "CodigoExercicio").text,
                           senator_exercise_start=senator_mandate.find("Exercicios").find("Exercicio").find(
                               "DataInicio").text,
                           senator_mandate_code=senator_mandate.find("CodigoMandato").text,
                           senator_mandate_uf=senator_mandate.find("UfParlamentar").text)
            if senator['senator_exercise_start']:
                senator['senator_exercise_start'] = datetime.strptime(
                    senator['senator_exercise_start'], '%Y-%m-%d').date()
            senators.append(senator)
        return senators
