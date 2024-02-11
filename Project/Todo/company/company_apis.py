from fastapi import APIRouter, Depends
from company import dependencies

router = APIRouter(
    prefix= '/company_api',
    tags= ['company_api'],
    dependencies=[Depends(dependencies.get_token_header)],
    responses= {418 : {'description': 'Internal Use Only'}}
)


@router.get('/')
async def get_company_name():
    return {'company_name': 'Example Company, LLC'}


@router.get('/employees')
async def number_of_employees():
    return 162