from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    id: int,
    attachment_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v0.1/companies/{companyId}/projects/{id}/attachments/{attachmentId}".format(
            companyId=company_id,
            id=id,
            attachmentId=attachment_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorModel, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorModel.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorModel, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: int,
    id: int,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ErrorModel, str]]:
    """Get Project file attachment by Id

     Requires access level: CompanyManager. Requires module: Assignments.

    Args:
        company_id (int):
        id (int):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, str]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        id=id,
        attachment_id=attachment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: int,
    id: int,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ErrorModel, str]]:
    """Get Project file attachment by Id

     Requires access level: CompanyManager. Requires module: Assignments.

    Args:
        company_id (int):
        id (int):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, str]
    """

    return sync_detailed(
        company_id=company_id,
        id=id,
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    id: int,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ErrorModel, str]]:
    """Get Project file attachment by Id

     Requires access level: CompanyManager. Requires module: Assignments.

    Args:
        company_id (int):
        id (int):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, str]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        id=id,
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    id: int,
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ErrorModel, str]]:
    """Get Project file attachment by Id

     Requires access level: CompanyManager. Requires module: Assignments.

    Args:
        company_id (int):
        id (int):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, str]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            id=id,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
