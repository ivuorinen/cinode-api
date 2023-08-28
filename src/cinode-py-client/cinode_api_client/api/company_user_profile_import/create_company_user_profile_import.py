from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_company_user_profile_import_multipart_data import CreateCompanyUserProfileImportMultipartData
from ...models.error_model import ErrorModel
from ...models.validation_model import ValidationModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    company_user_id: int,
    *,
    multipart_data: CreateCompanyUserProfileImportMultipartData,
) -> Dict[str, Any]:
    pass

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/v0.1/companies/{companyId}/users/{companyUserId}/profile/import".format(
            companyId=company_id,
            companyUserId=company_user_id,
        ),
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorModel, ValidationModel]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = cast(Any, None)
        return response_202
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
) -> Response[Union[Any, ErrorModel, ValidationModel]]:
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
    multipart_data: CreateCompanyUserProfileImportMultipartData,
) -> Response[Union[Any, ErrorModel, ValidationModel]]:
    """Create new profile import for a user.

     This will start an async operation.
    - If the operation is started successfully, the response will be `202 Accepted` and the `Location`
    header will contain the URL to get the status of the operation.
    - If the operation is not started successfully, the response will be `400 Bad Request`

    Args:
        company_id (int):
        company_user_id (int):
        multipart_data (CreateCompanyUserProfileImportMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        company_user_id=company_user_id,
        multipart_data=multipart_data,
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
    multipart_data: CreateCompanyUserProfileImportMultipartData,
) -> Optional[Union[Any, ErrorModel, ValidationModel]]:
    """Create new profile import for a user.

     This will start an async operation.
    - If the operation is started successfully, the response will be `202 Accepted` and the `Location`
    header will contain the URL to get the status of the operation.
    - If the operation is not started successfully, the response will be `400 Bad Request`

    Args:
        company_id (int):
        company_user_id (int):
        multipart_data (CreateCompanyUserProfileImportMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, ValidationModel]
    """

    return sync_detailed(
        company_id=company_id,
        company_user_id=company_user_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    company_user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: CreateCompanyUserProfileImportMultipartData,
) -> Response[Union[Any, ErrorModel, ValidationModel]]:
    """Create new profile import for a user.

     This will start an async operation.
    - If the operation is started successfully, the response will be `202 Accepted` and the `Location`
    header will contain the URL to get the status of the operation.
    - If the operation is not started successfully, the response will be `400 Bad Request`

    Args:
        company_id (int):
        company_user_id (int):
        multipart_data (CreateCompanyUserProfileImportMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        company_user_id=company_user_id,
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    company_user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: CreateCompanyUserProfileImportMultipartData,
) -> Optional[Union[Any, ErrorModel, ValidationModel]]:
    """Create new profile import for a user.

     This will start an async operation.
    - If the operation is started successfully, the response will be `202 Accepted` and the `Location`
    header will contain the URL to get the status of the operation.
    - If the operation is not started successfully, the response will be `400 Bad Request`

    Args:
        company_id (int):
        company_user_id (int):
        multipart_data (CreateCompanyUserProfileImportMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            company_user_id=company_user_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
