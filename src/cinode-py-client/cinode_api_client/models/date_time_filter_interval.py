import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateTimeFilterInterval")


@_attrs_define
class DateTimeFilterInterval:
    """
    Attributes:
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
    """

    from_: Union[Unset, None, datetime.datetime] = UNSET
    to: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_: Union[Unset, None, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat() if self.from_ else None

        to: Union[Unset, None, str] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat() if self.to else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, None, datetime.datetime]
        if _from_ is None:
            from_ = None
        elif isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, None, datetime.datetime]
        if _to is None:
            to = None
        elif isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        date_time_filter_interval = cls(
            from_=from_,
            to=to,
        )

        return date_time_filter_interval
