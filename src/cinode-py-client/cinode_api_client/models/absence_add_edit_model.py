import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbsenceAddEditModel")


@_attrs_define
class AbsenceAddEditModel:
    """
    Attributes:
        start (datetime.datetime):
        extent_percentage (float):
        absence_type_id (int):
        end (Union[Unset, None, datetime.datetime]):
    """

    start: datetime.datetime
    extent_percentage: float
    absence_type_id: int
    end: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.isoformat()

        extent_percentage = self.extent_percentage
        absence_type_id = self.absence_type_id
        end: Union[Unset, None, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat() if self.end else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "start": start,
                "extentPercentage": extent_percentage,
                "absenceTypeId": absence_type_id,
            }
        )
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = isoparse(d.pop("start"))

        extent_percentage = d.pop("extentPercentage")

        absence_type_id = d.pop("absenceTypeId")

        _end = d.pop("end", UNSET)
        end: Union[Unset, None, datetime.datetime]
        if _end is None:
            end = None
        elif isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        absence_add_edit_model = cls(
            start=start,
            extent_percentage=extent_percentage,
            absence_type_id=absence_type_id,
            end=end,
        )

        return absence_add_edit_model
