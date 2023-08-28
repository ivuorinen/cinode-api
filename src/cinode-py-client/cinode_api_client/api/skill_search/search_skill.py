from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.search_skill_query_model import SearchSkillQueryModel
from ...models.search_skill_result_model import SearchSkillResultModel
from ...models.validation_model import ValidationModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    *,
    json_body: SearchSkillQueryModel,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v0.1/companies/{companyId}/skills/search".format(
            companyId=company_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchSkillResultModel.from_dict(response.json())

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
) -> Response[Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]]:
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
    json_body: SearchSkillQueryModel,
) -> Response[Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]]:
    """Search users by skill keyword id

    Args:
        company_id (int):
        json_body (SearchSkillQueryModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]]
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
    json_body: SearchSkillQueryModel,
) -> Optional[Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]]:
    """Search users by skill keyword id

    Args:
        company_id (int):
        json_body (SearchSkillQueryModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]
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
    json_body: SearchSkillQueryModel,
) -> Response[Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]]:
    """Search users by skill keyword id

    Args:
        company_id (int):
        json_body (SearchSkillQueryModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]]
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
    json_body: SearchSkillQueryModel,
) -> Optional[Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]]:
    """Search users by skill keyword id

    Args:
        company_id (int):
        json_body (SearchSkillQueryModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel, SearchSkillResultModel, ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
