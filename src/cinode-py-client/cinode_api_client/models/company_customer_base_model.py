import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="CompanyCustomerBaseModel")


@_attrs_define
class CompanyCustomerBaseModel:
    """
    Attributes:
        id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        identification (Union[Unset, None, str]):
        seo_id (Union[Unset, None, str]):
        created_date_time (Union[Unset, None, datetime.datetime]):
        updated_date_time (Union[Unset, None, datetime.datetime]):
        last_touch_date_time (Union[Unset, None, datetime.datetime]):
        status (Union[Unset, Status]):

            Inaktiv = 0

            Aktiv = 1
        links (Union[Unset, None, List['Link']]):
    """

    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    identification: Union[Unset, None, str] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    created_date_time: Union[Unset, None, datetime.datetime] = UNSET
    updated_date_time: Union[Unset, None, datetime.datetime] = UNSET
    last_touch_date_time: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, Status] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        company_id = self.company_id
        name = self.name
        description = self.description
        identification = self.identification
        seo_id = self.seo_id
        created_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat() if self.created_date_time else None

        updated_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_date_time, Unset):
            updated_date_time = self.updated_date_time.isoformat() if self.updated_date_time else None

        last_touch_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_touch_date_time, Unset):
            last_touch_date_time = self.last_touch_date_time.isoformat() if self.last_touch_date_time else None

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if identification is not UNSET:
            field_dict["identification"] = identification
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if updated_date_time is not UNSET:
            field_dict["updatedDateTime"] = updated_date_time
        if last_touch_date_time is not UNSET:
            field_dict["lastTouchDateTime"] = last_touch_date_time
        if status is not UNSET:
            field_dict["status"] = status
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        identification = d.pop("identification", UNSET)

        seo_id = d.pop("seoId", UNSET)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, None, datetime.datetime]
        if _created_date_time is None:
            created_date_time = None
        elif isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        _updated_date_time = d.pop("updatedDateTime", UNSET)
        updated_date_time: Union[Unset, None, datetime.datetime]
        if _updated_date_time is None:
            updated_date_time = None
        elif isinstance(_updated_date_time, Unset):
            updated_date_time = UNSET
        else:
            updated_date_time = isoparse(_updated_date_time)

        _last_touch_date_time = d.pop("lastTouchDateTime", UNSET)
        last_touch_date_time: Union[Unset, None, datetime.datetime]
        if _last_touch_date_time is None:
            last_touch_date_time = None
        elif isinstance(_last_touch_date_time, Unset):
            last_touch_date_time = UNSET
        else:
            last_touch_date_time = isoparse(_last_touch_date_time)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status(_status)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_customer_base_model = cls(
            id=id,
            company_id=company_id,
            name=name,
            description=description,
            identification=identification,
            seo_id=seo_id,
            created_date_time=created_date_time,
            updated_date_time=updated_date_time,
            last_touch_date_time=last_touch_date_time,
            status=status,
            links=links,
        )

        return company_customer_base_model
