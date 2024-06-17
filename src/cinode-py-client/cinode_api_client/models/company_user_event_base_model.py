import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.event_type import EventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserEventBaseModel")


@_attrs_define
class CompanyUserEventBaseModel:
    """
    Attributes:
        company_user_id (Union[Unset, None, int]):
        type (Union[Unset, EventType]):

            Möte = 0

            Notering = 1

            Uppgift = 2

            Samtal = 3
        id (Union[Unset, None, str]):
        company_id (Union[Unset, None, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        description_html (Union[Unset, None, str]):
        description_delta (Union[Unset, None, str]):
        event_date (Union[Unset, datetime.datetime]):
        links (Union[Unset, None, List['Link']]):
    """

    company_user_id: Union[Unset, None, int] = UNSET
    type: Union[Unset, EventType] = UNSET
    id: Union[Unset, None, str] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    description_html: Union[Unset, None, str] = UNSET
    description_delta: Union[Unset, None, str] = UNSET
    event_date: Union[Unset, datetime.datetime] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_id = self.company_user_id
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id
        company_id = self.company_id
        title = self.title
        description = self.description
        description_html = self.description_html
        description_delta = self.description_delta
        event_date: Union[Unset, str] = UNSET
        if not isinstance(self.event_date, Unset):
            event_date = self.event_date.isoformat()

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
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if description_html is not UNSET:
            field_dict["descriptionHtml"] = description_html
        if description_delta is not UNSET:
            field_dict["descriptionDelta"] = description_delta
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        company_user_id = d.pop("companyUserId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EventType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EventType(_type)

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        description_html = d.pop("descriptionHtml", UNSET)

        description_delta = d.pop("descriptionDelta", UNSET)

        _event_date = d.pop("eventDate", UNSET)
        event_date: Union[Unset, datetime.datetime]
        if isinstance(_event_date, Unset):
            event_date = UNSET
        else:
            event_date = isoparse(_event_date)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_event_base_model = cls(
            company_user_id=company_user_id,
            type=type,
            id=id,
            company_id=company_id,
            title=title,
            description=description,
            description_html=description_html,
            description_delta=description_delta,
            event_date=event_date,
            links=links,
        )

        return company_user_event_base_model
