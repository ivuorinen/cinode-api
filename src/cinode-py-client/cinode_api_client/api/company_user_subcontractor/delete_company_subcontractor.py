from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.validation_model import ValidationModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: int,
    id: int,
    *,
    first_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["firstName"] = first_name

    params["lastName"] = last_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": "/v0.1/companies/{companyId}/subcontractors/{id}".format(
            companyId=company_id,
            id=id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorModel, ValidationModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
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
) -> Response[Union[Any, ErrorModel, ValidationModel]]:
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
    first_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorModel, ValidationModel]]:
    """Delete subcontractor from the system
    This action is irreversible, use with caution

     Requires access level: PartnerManager. Requires module: Partners.

    Args:
        company_id (int):
        id (int):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        id=id,
        first_name=first_name,
        last_name=last_name,
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
    first_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorModel, ValidationModel]]:
    """Delete subcontractor from the system
    This action is irreversible, use with caution

     Requires access level: PartnerManager. Requires module: Partners.

    Args:
        company_id (int):
        id (int):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, ValidationModel]
    """

    return sync_detailed(
        company_id=company_id,
        id=id,
        client=client,
        first_name=first_name,
        last_name=last_name,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    first_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorModel, ValidationModel]]:
    """Delete subcontractor from the system
    This action is irreversible, use with caution

     Requires access level: PartnerManager. Requires module: Partners.

    Args:
        company_id (int):
        id (int):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        id=id,
        first_name=first_name,
        last_name=last_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    first_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorModel, ValidationModel]]:
    """Delete subcontractor from the system
    This action is irreversible, use with caution

     Requires access level: PartnerManager. Requires module: Partners.

    Args:
        company_id (int):
        id (int):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            id=id,
            client=client,
            first_name=first_name,
            last_name=last_name,
        )
    ).parsed
