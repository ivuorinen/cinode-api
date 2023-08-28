import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailabilityFilterModel")


@_attrs_define
class AvailabilityFilterModel:
    """
    Attributes:
        start_date (datetime.datetime):
        end_date (datetime.datetime):
        company_user_id (Union[Unset, None, int]):
    """

    start_date: datetime.datetime
    end_date: datetime.datetime
    company_user_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        company_user_id = self.company_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        company_user_id = d.pop("companyUserId", UNSET)

        availability_filter_model = cls(
            start_date=start_date,
            end_date=end_date,
            company_user_id=company_user_id,
        )

        return availability_filter_model
