from unittest import TestCase
from ..parliamentarians import SenatorClient


class TestParliamentarians(TestCase):
    def test_get_senator(self):
        senator_client = SenatorClient()
        senators = senator_client.get()
        self.assertIsInstance(senators, list)
        if len(senators) <= 0:
            raise Exception("Empty list!")
