from http import HTTPStatus
from typing import Annotated, List, Union

from fastapi import Body

from src.integrations.business_service import BusinessService
from src.models.score import router
from src.models.score import Score
from src.models.standard_response import StandardResponse

business_service: BusinessService = BusinessService()


@router.get('')
async def search_score(
        municipality_id: str,
        period: str
) -> Union[Score, StandardResponse]:
    score: Score = business_service.get_score(municipality_id, period)

    if score is not None:
        return score
    else:
        return StandardResponse(status=200, message="Non-existent municipality, try different municipality id")
