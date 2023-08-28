import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserImageModel")


@_attrs_define
class CompanyUserImageModel:
    """
    Attributes:
        image_id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        url (Union[Unset, None, str]):
        large_image_url (Union[Unset, None, str]):
        uploaded_when (Union[Unset, datetime.datetime]):
        links (Union[Unset, None, List['Link']]):
    """

    image_id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    url: Union[Unset, None, str] = UNSET
    large_image_url: Union[Unset, None, str] = UNSET
    uploaded_when: Union[Unset, datetime.datetime] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        image_id = self.image_id
        company_id = self.company_id
        url = self.url
        large_image_url = self.large_image_url
        uploaded_when: Union[Unset, str] = UNSET
        if not isinstance(self.uploaded_when, Unset):
            uploaded_when = self.uploaded_when.isoformat()

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
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if url is not UNSET:
            field_dict["url"] = url
        if large_image_url is not UNSET:
            field_dict["largeImageUrl"] = large_image_url
        if uploaded_when is not UNSET:
            field_dict["uploadedWhen"] = uploaded_when
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        image_id = d.pop("imageId", UNSET)

        company_id = d.pop("companyId", UNSET)

        url = d.pop("url", UNSET)

        large_image_url = d.pop("largeImageUrl", UNSET)

        _uploaded_when = d.pop("uploadedWhen", UNSET)
        uploaded_when: Union[Unset, datetime.datetime]
        if isinstance(_uploaded_when, Unset):
            uploaded_when = UNSET
        else:
            uploaded_when = isoparse(_uploaded_when)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_image_model = cls(
            image_id=image_id,
            company_id=company_id,
            url=url,
            large_image_url=large_image_url,
            uploaded_when=uploaded_when,
            links=links,
        )

        return company_user_image_model
