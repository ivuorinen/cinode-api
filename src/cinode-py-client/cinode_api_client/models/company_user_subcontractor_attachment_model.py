from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.attachment_type import AttachmentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserSubcontractorAttachmentModel")


@_attrs_define
class CompanyUserSubcontractorAttachmentModel:
    """
    Attributes:
        company_user_id (Union[Unset, int]):
        attachment_type (Union[Unset, AttachmentType]):

            File = 0

            Uri = 1
        company_id (Union[Unset, None, int]):
        id (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    company_user_id: Union[Unset, int] = UNSET
    attachment_type: Union[Unset, AttachmentType] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_id = self.company_user_id
        attachment_type: Union[Unset, int] = UNSET
        if not isinstance(self.attachment_type, Unset):
            attachment_type = self.attachment_type.value

        company_id = self.company_id
        id = self.id
        title = self.title
        description = self.description
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if attachment_type is not UNSET:
            field_dict["attachmentType"] = attachment_type
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        company_user_id = d.pop("companyUserId", UNSET)

        _attachment_type = d.pop("attachmentType", UNSET)
        attachment_type: Union[Unset, AttachmentType]
        if isinstance(_attachment_type, Unset):
            attachment_type = UNSET
        else:
            attachment_type = AttachmentType(_attachment_type)

        company_id = d.pop("companyId", UNSET)

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_subcontractor_attachment_model = cls(
            company_user_id=company_user_id,
            attachment_type=attachment_type,
            company_id=company_id,
            id=id,
            title=title,
            description=description,
            links=links,
        )

        return company_user_subcontractor_attachment_model
