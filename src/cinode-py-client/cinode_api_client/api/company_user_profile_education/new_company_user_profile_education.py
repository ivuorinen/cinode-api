from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_user_profile_education_add_edit_model import CompanyUserProfileEducationAddEditModel
from ...models.company_user_profile_education_model import CompanyUserProfileEducationModel
from ...models.error_model import ErrorModel
from ...models.validation_model import ValidationModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    company_user_id: int,
    *,
    json_body: CompanyUserProfileEducationAddEditModel,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v0.1/companies/{companyId}/users/{companyUserId}/profile/educations".format(
            companyId=company_id,
            companyUserId=company_user_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CompanyUserProfileEducationModel.from_dict(response.json())

        return response_201
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
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]]:
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
    json_body: CompanyUserProfileEducationAddEditModel,
) -> Response[Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]]:
    """Create Profile Education

    Args:
        company_id (int):
        company_user_id (int):
        json_body (CompanyUserProfileEducationAddEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        company_user_id=company_user_id,
        json_body=json_body,
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
    json_body: CompanyUserProfileEducationAddEditModel,
) -> Optional[Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]]:
    """Create Profile Education

    Args:
        company_id (int):
        company_user_id (int):
        json_body (CompanyUserProfileEducationAddEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]
    """

    return sync_detailed(
        company_id=company_id,
        company_user_id=company_user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    company_user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CompanyUserProfileEducationAddEditModel,
) -> Response[Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]]:
    """Create Profile Education

    Args:
        company_id (int):
        company_user_id (int):
        json_body (CompanyUserProfileEducationAddEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        company_user_id=company_user_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    company_user_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: CompanyUserProfileEducationAddEditModel,
) -> Optional[Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]]:
    """Create Profile Education

    Args:
        company_id (int):
        company_user_id (int):
        json_body (CompanyUserProfileEducationAddEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CompanyUserProfileEducationModel, ErrorModel, ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            company_user_id=company_user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
