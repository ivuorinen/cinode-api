from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.search_company_customer_contact_query_model import SearchCompanyCustomerContactQueryModel
from ...models.search_company_customer_contact_result_model import SearchCompanyCustomerContactResultModel
from ...models.validation_model import ValidationModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    *,
    json_body: SearchCompanyCustomerContactQueryModel,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v0.1/companies/{companyId}/customers/contacts/search".format(
            companyId=company_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchCompanyCustomerContactResultModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationModel.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorModel.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SearchCompanyCustomerContactQueryModel,
) -> Response[Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]]:
    """Get company customer contacts list from search criteria

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        json_body (SearchCompanyCustomerContactQueryModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SearchCompanyCustomerContactQueryModel,
) -> Optional[Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]]:
    """Get company customer contacts list from search criteria

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        json_body (SearchCompanyCustomerContactQueryModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SearchCompanyCustomerContactQueryModel,
) -> Response[Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]]:
    """Get company customer contacts list from search criteria

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        json_body (SearchCompanyCustomerContactQueryModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SearchCompanyCustomerContactQueryModel,
) -> Optional[Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]]:
    """Get company customer contacts list from search criteria

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        json_body (SearchCompanyCustomerContactQueryModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, SearchCompanyCustomerContactResultModel, ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
