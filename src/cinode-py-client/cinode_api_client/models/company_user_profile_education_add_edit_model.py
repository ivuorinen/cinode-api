import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_model import LocationModel


T = TypeVar("T", bound="CompanyUserProfileEducationAddEditModel")


@_attrs_define
class CompanyUserProfileEducationAddEditModel:
    """
    Attributes:
        school_name (str):
        program_name (str):
        degree (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        location (Union[Unset, None, LocationModel]):
        is_current (Union[Unset, None, bool]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        url (Union[Unset, None, str]):
    """

    school_name: str
    program_name: str
    degree: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, "LocationModel"] = UNSET
    is_current: Union[Unset, None, bool] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        school_name = self.school_name
        program_name = self.program_name
        degree = self.degree
        description = self.description
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        is_current = self.is_current
        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "schoolName": school_name,
                "programName": program_name,
            }
        )
        if degree is not UNSET:
            field_dict["degree"] = degree
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_model import LocationModel

        d = src_dict.copy()
        school_name = d.pop("schoolName")

        program_name = d.pop("programName")

        degree = d.pop("degree", UNSET)

        description = d.pop("description", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, None, LocationModel]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationModel.from_dict(_location)

        is_current = d.pop("isCurrent", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, None, datetime.datetime]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        url = d.pop("url", UNSET)

        company_user_profile_education_add_edit_model = cls(
            school_name=school_name,
            program_name=program_name,
            degree=degree,
            description=description,
            location=location,
            is_current=is_current,
            start_date=start_date,
            end_date=end_date,
            url=url,
        )

        return company_user_profile_education_add_edit_model
