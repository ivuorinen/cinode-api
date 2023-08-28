import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="CompanyCandidateBaseModel")


@_attrs_define
class CompanyCandidateBaseModel:
    """
    Attributes:
        id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        seo_id (Union[Unset, None, str]):
        firstname (Union[Unset, None, str]):
        first_name (Union[Unset, None, str]):
        lastname (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        created_date_time (Union[Unset, datetime.datetime]):
        last_touch_date_time (Union[Unset, None, datetime.datetime]):
        updated_date_time (Union[Unset, None, datetime.datetime]):
        links (Union[Unset, None, List['Link']]):
    """

    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    firstname: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    lastname: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    created_date_time: Union[Unset, datetime.datetime] = UNSET
    last_touch_date_time: Union[Unset, None, datetime.datetime] = UNSET
    updated_date_time: Union[Unset, None, datetime.datetime] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        company_id = self.company_id
        seo_id = self.seo_id
        firstname = self.firstname
        first_name = self.first_name
        lastname = self.lastname
        last_name = self.last_name
        created_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat()

        last_touch_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_touch_date_time, Unset):
            last_touch_date_time = self.last_touch_date_time.isoformat() if self.last_touch_date_time else None

        updated_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_date_time, Unset):
            updated_date_time = self.updated_date_time.isoformat() if self.updated_date_time else None

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
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if last_touch_date_time is not UNSET:
            field_dict["lastTouchDateTime"] = last_touch_date_time
        if updated_date_time is not UNSET:
            field_dict["updatedDateTime"] = updated_date_time
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        seo_id = d.pop("seoId", UNSET)

        firstname = d.pop("firstname", UNSET)

        first_name = d.pop("firstName", UNSET)

        lastname = d.pop("lastname", UNSET)

        last_name = d.pop("lastName", UNSET)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, datetime.datetime]
        if isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        _last_touch_date_time = d.pop("lastTouchDateTime", UNSET)
        last_touch_date_time: Union[Unset, None, datetime.datetime]
        if _last_touch_date_time is None:
            last_touch_date_time = None
        elif isinstance(_last_touch_date_time, Unset):
            last_touch_date_time = UNSET
        else:
            last_touch_date_time = isoparse(_last_touch_date_time)

        _updated_date_time = d.pop("updatedDateTime", UNSET)
        updated_date_time: Union[Unset, None, datetime.datetime]
        if _updated_date_time is None:
            updated_date_time = None
        elif isinstance(_updated_date_time, Unset):
            updated_date_time = UNSET
        else:
            updated_date_time = isoparse(_updated_date_time)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_candidate_base_model = cls(
            id=id,
            company_id=company_id,
            seo_id=seo_id,
            firstname=firstname,
            first_name=first_name,
            lastname=lastname,
            last_name=last_name,
            created_date_time=created_date_time,
            last_touch_date_time=last_touch_date_time,
            updated_date_time=updated_date_time,
            links=links,
        )

        return company_candidate_base_model
