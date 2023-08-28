from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCandidateUriAttachmentAddModel")


@_attrs_define
class CompanyCandidateUriAttachmentAddModel:
    """
    Attributes:
        uri (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
    """

    uri: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uri = self.uri
        title = self.title
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if uri is not UNSET:
            field_dict["uri"] = uri
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uri = d.pop("uri", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        company_candidate_uri_attachment_add_model = cls(
            uri=uri,
            title=title,
            description=description,
        )

        return company_candidate_uri_attachment_add_model
