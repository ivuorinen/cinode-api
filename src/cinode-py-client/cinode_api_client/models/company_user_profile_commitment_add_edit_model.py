import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfileCommitmentAddEditModel")


@_attrs_define
class CompanyUserProfileCommitmentAddEditModel:
    """
    Attributes:
        title (str):
        description (Union[Unset, None, str]):
        is_current (Union[Unset, None, bool]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        url (Union[Unset, None, str]):
    """

    title: str
    description: Union[Unset, None, str] = UNSET
    is_current: Union[Unset, None, bool] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        description = self.description
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
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        d = src_dict.copy()
        title = d.pop("title")

        description = d.pop("description", UNSET)

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

        company_user_profile_commitment_add_edit_model = cls(
            title=title,
            description=description,
            is_current=is_current,
            start_date=start_date,
            end_date=end_date,
            url=url,
        )

        return company_user_profile_commitment_add_edit_model
