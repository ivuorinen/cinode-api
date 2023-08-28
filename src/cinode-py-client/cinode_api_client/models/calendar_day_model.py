import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarDayModel")


@_attrs_define
class CalendarDayModel:
    """
    Attributes:
        date (Union[Unset, datetime.datetime]):
        year (Union[Unset, int]):
        month (Union[Unset, int]):
        day (Union[Unset, int]):
        weekday (Union[Unset, int]):
        week (Union[Unset, int]):
        quarter (Union[Unset, int]):
        day_of_year (Union[Unset, int]):
    """

    date: Union[Unset, datetime.datetime] = UNSET
    year: Union[Unset, int] = UNSET
    month: Union[Unset, int] = UNSET
    day: Union[Unset, int] = UNSET
    weekday: Union[Unset, int] = UNSET
    week: Union[Unset, int] = UNSET
    quarter: Union[Unset, int] = UNSET
    day_of_year: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        year = self.year
        month = self.month
        day = self.day
        weekday = self.weekday
        week = self.week
        quarter = self.quarter
        day_of_year = self.day_of_year

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if day is not UNSET:
            field_dict["day"] = day
        if weekday is not UNSET:
            field_dict["weekday"] = weekday
        if week is not UNSET:
            field_dict["week"] = week
        if quarter is not UNSET:
            field_dict["quarter"] = quarter
        if day_of_year is not UNSET:
            field_dict["dayOfYear"] = day_of_year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        year = d.pop("year", UNSET)

        month = d.pop("month", UNSET)

        day = d.pop("day", UNSET)

        weekday = d.pop("weekday", UNSET)

        week = d.pop("week", UNSET)

        quarter = d.pop("quarter", UNSET)

        day_of_year = d.pop("dayOfYear", UNSET)

        calendar_day_model = cls(
            date=date,
            year=year,
            month=month,
            day=day,
            weekday=weekday,
            week=week,
            quarter=quarter,
            day_of_year=day_of_year,
        )

        return calendar_day_model
