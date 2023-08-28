from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_user_skill_model import CompanyUserSkillModel
from ...models.error_model import ErrorModel
from ...models.validation_model import ValidationModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    company_user_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v0.1/companies/{companyId}/users/{companyUserId}/skills".format(
            companyId=company_id,
            companyUserId=company_user_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorModel, List["CompanyUserSkillModel"], ValidationModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CompanyUserSkillModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, ErrorModel, List["CompanyUserSkillModel"], ValidationModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: int,
    company_user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ErrorModel, List["CompanyUserSkillModel"], ValidationModel]]:
    """Get skills list

    Args:
        company_id (int):
        company_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, List['CompanyUserSkillModel'], ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        company_user_id=company_user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: int,
    company_user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ErrorModel, List["CompanyUserSkillModel"], ValidationModel]]:
    """Get skills list

    Args:
        company_id (int):
        company_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, List['CompanyUserSkillModel'], ValidationModel]
    """

    return sync_detailed(
        company_id=company_id,
        company_user_id=company_user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    company_user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ErrorModel, List["CompanyUserSkillModel"], ValidationModel]]:
    """Get skills list

    Args:
        company_id (int):
        company_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, List['CompanyUserSkillModel'], ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        company_user_id=company_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    company_user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ErrorModel, List["CompanyUserSkillModel"], ValidationModel]]:
    """Get skills list

    Args:
        company_id (int):
        company_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, List['CompanyUserSkillModel'], ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            company_user_id=company_user_id,
            client=client,
        )
    ).parsed
