import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.absence_type_dto import AbsenceTypeDto
    from ..models.link import Link


T = TypeVar("T", bound="AbsencePeriodDtoModel")


@_attrs_define
class AbsencePeriodDtoModel:
    """
    Attributes:
        id (Union[Unset, int]):
        absence_type (Union[Unset, None, AbsenceTypeDto]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        extent_percentage (Union[Unset, int]):
        company_user_id (Union[Unset, int]):
        company_user_seo_id (Union[Unset, None, str]):
        company_id (Union[Unset, int]):
        company_seo_id (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    id: Union[Unset, int] = UNSET
    absence_type: Union[Unset, None, "AbsenceTypeDto"] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    extent_percentage: Union[Unset, int] = UNSET
    company_user_id: Union[Unset, int] = UNSET
    company_user_seo_id: Union[Unset, None, str] = UNSET
    company_id: Union[Unset, int] = UNSET
    company_seo_id: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        absence_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.absence_type, Unset):
            absence_type = self.absence_type.to_dict() if self.absence_type else None

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        extent_percentage = self.extent_percentage
        company_user_id = self.company_user_id
        company_user_seo_id = self.company_user_seo_id
        company_id = self.company_id
        company_seo_id = self.company_seo_id
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
        if absence_type is not UNSET:
            field_dict["absenceType"] = absence_type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if extent_percentage is not UNSET:
            field_dict["extentPercentage"] = extent_percentage
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if company_user_seo_id is not UNSET:
            field_dict["companyUserSeoId"] = company_user_seo_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_seo_id is not UNSET:
            field_dict["companySeoId"] = company_seo_id
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.absence_type_dto import AbsenceTypeDto
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _absence_type = d.pop("absenceType", UNSET)
        absence_type: Union[Unset, None, AbsenceTypeDto]
        if _absence_type is None:
            absence_type = None
        elif isinstance(_absence_type, Unset):
            absence_type = UNSET
        else:
            absence_type = AbsenceTypeDto.from_dict(_absence_type)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        extent_percentage = d.pop("extentPercentage", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        company_user_seo_id = d.pop("companyUserSeoId", UNSET)

        company_id = d.pop("companyId", UNSET)

        company_seo_id = d.pop("companySeoId", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        absence_period_dto_model = cls(
            id=id,
            absence_type=absence_type,
            start_date=start_date,
            end_date=end_date,
            extent_percentage=extent_percentage,
            company_user_id=company_user_id,
            company_user_seo_id=company_user_seo_id,
            company_id=company_id,
            company_seo_id=company_seo_id,
            links=links,
        )

        return absence_period_dto_model
