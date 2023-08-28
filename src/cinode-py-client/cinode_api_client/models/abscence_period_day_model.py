from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calendar_day_model import CalendarDayModel


T = TypeVar("T", bound="AbscencePeriodDayModel")


@_attrs_define
class AbscencePeriodDayModel:
    """
    Attributes:
        calendar_day (Union[Unset, None, CalendarDayModel]):
    """

    calendar_day: Union[Unset, None, "CalendarDayModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        calendar_day: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.calendar_day, Unset):
            calendar_day = self.calendar_day.to_dict() if self.calendar_day else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if calendar_day is not UNSET:
            field_dict["calendarDay"] = calendar_day

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.calendar_day_model import CalendarDayModel

        d = src_dict.copy()
        _calendar_day = d.pop("calendarDay", UNSET)
        calendar_day: Union[Unset, None, CalendarDayModel]
        if _calendar_day is None:
            calendar_day = None
        elif isinstance(_calendar_day, Unset):
            calendar_day = UNSET
        else:
            calendar_day = CalendarDayModel.from_dict(_calendar_day)

        abscence_period_day_model = cls(
            calendar_day=calendar_day,
        )

        return abscence_period_day_model
