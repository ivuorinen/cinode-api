from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_event_note_model import CustomerEventNoteModel
from ...models.error_model import ErrorModel
from ...models.validation_model import ValidationModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    customer_id: int,
    id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v0.1/companies/{companyId}/customers/{customerId}/events/notes/{id}".format(
            companyId=company_id,
            customerId=customer_id,
            id=id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CustomerEventNoteModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationModel.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorModel.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: int,
    customer_id: int,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]]:
    """Get customer event note by id

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        customer_id (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        customer_id=customer_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: int,
    customer_id: int,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]]:
    """Get customer event note by id

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        customer_id (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]
    """

    return sync_detailed(
        company_id=company_id,
        customer_id=customer_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    customer_id: int,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]]:
    """Get customer event note by id

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        customer_id (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        customer_id=customer_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    customer_id: int,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]]:
    """Get customer event note by id

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        customer_id (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CustomerEventNoteModel, ErrorModel, ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            customer_id=customer_id,
            id=id,
            client=client,
        )
    ).parsed
