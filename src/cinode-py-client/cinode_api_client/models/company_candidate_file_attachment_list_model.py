from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_candidate_file_attachment_model import CompanyCandidateFileAttachmentModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyCandidateFileAttachmentListModel")


@_attrs_define
class CompanyCandidateFileAttachmentListModel:
    """
    Attributes:
        company_candidate_id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        attachments (Union[Unset, None, List['CompanyCandidateFileAttachmentModel']]):
        links (Union[Unset, None, List['Link']]):
    """

    company_candidate_id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    attachments: Union[Unset, None, List["CompanyCandidateFileAttachmentModel"]] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_candidate_id = self.company_candidate_id
        company_id = self.company_id
        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

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
        if company_candidate_id is not UNSET:
            field_dict["companyCandidateId"] = company_candidate_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_candidate_file_attachment_model import CompanyCandidateFileAttachmentModel
        from ..models.link import Link

        d = src_dict.copy()
        company_candidate_id = d.pop("companyCandidateId", UNSET)

        company_id = d.pop("companyId", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = CompanyCandidateFileAttachmentModel.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_candidate_file_attachment_list_model = cls(
            company_candidate_id=company_candidate_id,
            company_id=company_id,
            attachments=attachments,
            links=links,
        )

        return company_candidate_file_attachment_list_model
