import os
import requests
from typing import Union

from src.models.score import Score
from src.models.standard_response import StandardResponse


class BusinessService:
    def __init__(self):
        """
        Initialize BusinessService class.
        """
        self.__url = os.environ["BUSINESS_SERVICE"]

    def get_score(self, municipality_id: str, period: str) -> Union[Score, StandardResponse]:
        """
        Get score data by municipality ID and period from the business service.

        Args:
            municipality_id (str): The ID of the municipality.
            period (str): The period for the score.

        Returns:
            Union[Score, StandardResponse] or None: Object representing the score data if successful,
            StandardResponse if the request fails, or None if no data found.
        """
        response = requests.get(f"{self.__url}/municipalities/{municipality_id}/score?period={period}")

        if response.text != "null" and response.status_code == 200:
            return Score(**response.json())
        else:
            return None
