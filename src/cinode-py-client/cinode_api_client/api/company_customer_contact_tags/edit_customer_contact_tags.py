from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_tag_model import CompanyTagModel
from ...models.error_model import ErrorModel
from ...models.validation_model import ValidationModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    customer_id: int,
    contact_id: int,
    *,
    json_body: List["CompanyTagModel"],
) -> Dict[str, Any]:
    pass

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "post",
        "url": "/v0.1/companies/{companyId}/customers/{customerId}/contacts/{contactId}/tags".format(
            companyId=company_id,
            customerId=customer_id,
            contactId=contact_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorModel, List["CompanyTagModel"], ValidationModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CompanyTagModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationModel.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
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
) -> Response[Union[Any, ErrorModel, List["CompanyTagModel"], ValidationModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: int,
    customer_id: int,
    contact_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List["CompanyTagModel"],
) -> Response[Union[Any, ErrorModel, List["CompanyTagModel"], ValidationModel]]:
    r"""Edit Tags for CustomerContact

     Note:

        Posted tags will replace any existing tags for the contact.
        A new tag will be created if the Id for a tag is not provided.

    Sample request:

        POST /v0.1/companies/1/customers/19870/contacts/5360/tags
        [
            {
                \"name\": \"tag-name\",
                \"id\": 2
            },
            {
                \"name\": \"tag-test\",
                \"id\": 1
            },
        ]

    Args:
        company_id (int):
        customer_id (int):
        contact_id (int):
        json_body (List['CompanyTagModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, List['CompanyTagModel'], ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        customer_id=customer_id,
        contact_id=contact_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: int,
    customer_id: int,
    contact_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List["CompanyTagModel"],
) -> Optional[Union[Any, ErrorModel, List["CompanyTagModel"], ValidationModel]]:
    r"""Edit Tags for CustomerContact

     Note:

        Posted tags will replace any existing tags for the contact.
        A new tag will be created if the Id for a tag is not provided.

    Sample request:

        POST /v0.1/companies/1/customers/19870/contacts/5360/tags
        [
            {
                \"name\": \"tag-name\",
                \"id\": 2
            },
            {
                \"name\": \"tag-test\",
                \"id\": 1
            },
        ]

    Args:
        company_id (int):
        customer_id (int):
        contact_id (int):
        json_body (List['CompanyTagModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, List['CompanyTagModel'], ValidationModel]
    """

    return sync_detailed(
        company_id=company_id,
        customer_id=customer_id,
        contact_id=contact_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    customer_id: int,
    contact_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List["CompanyTagModel"],
) -> Response[Union[Any, ErrorModel, List["CompanyTagModel"], ValidationModel]]:
    r"""Edit Tags for CustomerContact

     Note:

        Posted tags will replace any existing tags for the contact.
        A new tag will be created if the Id for a tag is not provided.

    Sample request:

        POST /v0.1/companies/1/customers/19870/contacts/5360/tags
        [
            {
                \"name\": \"tag-name\",
                \"id\": 2
            },
            {
                \"name\": \"tag-test\",
                \"id\": 1
            },
        ]

    Args:
        company_id (int):
        customer_id (int):
        contact_id (int):
        json_body (List['CompanyTagModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, List['CompanyTagModel'], ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        customer_id=customer_id,
        contact_id=contact_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    customer_id: int,
    contact_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: List["CompanyTagModel"],
) -> Optional[Union[Any, ErrorModel, List["CompanyTagModel"], ValidationModel]]:
    r"""Edit Tags for CustomerContact

     Note:

        Posted tags will replace any existing tags for the contact.
        A new tag will be created if the Id for a tag is not provided.

    Sample request:

        POST /v0.1/companies/1/customers/19870/contacts/5360/tags
        [
            {
                \"name\": \"tag-name\",
                \"id\": 2
            },
            {
                \"name\": \"tag-test\",
                \"id\": 1
            },
        ]

    Args:
        company_id (int):
        customer_id (int):
        contact_id (int):
        json_body (List['CompanyTagModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, List['CompanyTagModel'], ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            customer_id=customer_id,
            contact_id=contact_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
