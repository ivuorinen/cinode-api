from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.candidate_attachment_multipart_data import CandidateAttachmentMultipartData
from ...models.company_candidate_file_attachment_list_model import CompanyCandidateFileAttachmentListModel
from ...models.error_model import ErrorModel
from ...models.validation_model import ValidationModel
from ...types import Response


def _get_kwargs(
    company_id: int,
    id: int,
    *,
    multipart_data: CandidateAttachmentMultipartData,
) -> Dict[str, Any]:
    pass

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/v0.1/companies/{companyId}/candidates/{id}/attachments".format(
            companyId=company_id,
            id=id,
        ),
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CompanyCandidateFileAttachmentListModel.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]]:
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
    multipart_data: CandidateAttachmentMultipartData,
) -> Response[Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]]:
    """Upload Candidate File Attachment

     Requires access level: CompanyRecruiter. Requires module: Recruitment.

    Args:
        company_id (int):
        id (int):
        multipart_data (CandidateAttachmentMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        id=id,
        multipart_data=multipart_data,
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
    multipart_data: CandidateAttachmentMultipartData,
) -> Optional[Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]]:
    """Upload Candidate File Attachment

     Requires access level: CompanyRecruiter. Requires module: Recruitment.

    Args:
        company_id (int):
        id (int):
        multipart_data (CandidateAttachmentMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]
    """

    return sync_detailed(
        company_id=company_id,
        id=id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    company_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: CandidateAttachmentMultipartData,
) -> Response[Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]]:
    """Upload Candidate File Attachment

     Requires access level: CompanyRecruiter. Requires module: Recruitment.

    Args:
        company_id (int):
        id (int):
        multipart_data (CandidateAttachmentMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        id=id,
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: int,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: CandidateAttachmentMultipartData,
) -> Optional[Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]]:
    """Upload Candidate File Attachment

     Requires access level: CompanyRecruiter. Requires module: Recruitment.

    Args:
        company_id (int):
        id (int):
        multipart_data (CandidateAttachmentMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CompanyCandidateFileAttachmentListModel, ErrorModel, ValidationModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            id=id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
