from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_customer_model import CompanyCustomerModel
from ...models.error_model import ErrorModel
from ...models.operation import Operation
from ...models.validation_model import ValidationModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    id: int,
    *,
    json_body: List["Operation"],
) -> Dict[str, Any]:
    pass

    json_json_body = []
    for componentsschemas_json_patch_document_item_data in json_body:
        componentsschemas_json_patch_document_item = componentsschemas_json_patch_document_item_data.to_dict()

        json_json_body.append(componentsschemas_json_patch_document_item)

    return {
        "method": "patch",
        "url": "/v0.1/companies/{companyId}/customers/{id}".format(
            companyId=company_id,
            id=id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CompanyCustomerModel.from_dict(response.json())

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
) -> Response[Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List["Operation"],
) -> Response[Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]]:
    """Patch company customer

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        id (int):
        json_body (List['Operation']): Array of patch operations to perform

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        id=id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List["Operation"],
) -> Optional[Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]]:
    """Patch company customer

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        id (int):
        json_body (List['Operation']): Array of patch operations to perform

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]
    """

    return sync_detailed(
        company_id=company_id,
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List["Operation"],
) -> Response[Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]]:
    """Patch company customer

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        id (int):
        json_body (List['Operation']): Array of patch operations to perform

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        id=id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List["Operation"],
) -> Optional[Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]]:
    """Patch company customer

     Requires access level: CompanyManager. Requires module: Customers.

    Args:
        company_id (int):
        id (int):
        json_body (List['Operation']): Array of patch operations to perform

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CompanyCustomerModel, ErrorModel, ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
