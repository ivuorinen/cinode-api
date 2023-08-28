import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatedModel")


@_attrs_define
class UpdatedModel:
    """
    Attributes:
        company_user_id (Union[Unset, None, int]):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        time (Union[Unset, None, datetime.datetime]):
    """

    company_user_id: Union[Unset, None, int] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    time: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_id = self.company_user_id
        first_name = self.first_name
        last_name = self.last_name
        time: Union[Unset, None, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat() if self.time else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_user_id = d.pop("companyUserId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, None, datetime.datetime]
        if _time is None:
            time = None
        elif isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        updated_model = cls(
            company_user_id=company_user_id,
            first_name=first_name,
            last_name=last_name,
            time=time,
        )

        return updated_model
