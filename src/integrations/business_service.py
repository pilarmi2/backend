import json
import os
from typing import Union

import requests

from src.models.score import Score
from src.models.standard_response import StandardResponse


class BusinessService:
    def __init__(self):
        """
        Initialize StoreService class.
        """
        self.__url = os.environ["BUSINESS_SERVICE"]

    def get_score(self, municipality_id: str, period: str) -> Union[Score, StandardResponse]:
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/score?period={period}")

        if response.text != "null" and response.status_code == 200:
            return Score(**response.json())
        else:
            return None
