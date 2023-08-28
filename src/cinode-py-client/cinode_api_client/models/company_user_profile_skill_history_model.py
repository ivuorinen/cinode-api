import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfileSkillHistoryModel")


@_attrs_define
class CompanyUserProfileSkillHistoryModel:
    """
    Attributes:
        id (Union[Unset, None, int]):
        change_date_time (Union[Unset, None, datetime.datetime]):
        level (Union[Unset, None, int]):
        profile_id (Union[Unset, None, int]):
        keyword_id (Union[Unset, None, int]):
        favourite (Union[Unset, bool]):
    """

    id: Union[Unset, None, int] = UNSET
    change_date_time: Union[Unset, None, datetime.datetime] = UNSET
    level: Union[Unset, None, int] = UNSET
    profile_id: Union[Unset, None, int] = UNSET
    keyword_id: Union[Unset, None, int] = UNSET
    favourite: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        change_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.change_date_time, Unset):
            change_date_time = self.change_date_time.isoformat() if self.change_date_time else None

        level = self.level
        profile_id = self.profile_id
        keyword_id = self.keyword_id
        favourite = self.favourite

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if change_date_time is not UNSET:
            field_dict["changeDateTime"] = change_date_time
        if level is not UNSET:
            field_dict["level"] = level
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if keyword_id is not UNSET:
            field_dict["keywordId"] = keyword_id
        if favourite is not UNSET:
            field_dict["favourite"] = favourite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _change_date_time = d.pop("changeDateTime", UNSET)
        change_date_time: Union[Unset, None, datetime.datetime]
        if _change_date_time is None:
            change_date_time = None
        elif isinstance(_change_date_time, Unset):
            change_date_time = UNSET
        else:
            change_date_time = isoparse(_change_date_time)

        level = d.pop("level", UNSET)

        profile_id = d.pop("profileId", UNSET)

        keyword_id = d.pop("keywordId", UNSET)

        favourite = d.pop("favourite", UNSET)

        company_user_profile_skill_history_model = cls(
            id=id,
            change_date_time=change_date_time,
            level=level,
            profile_id=profile_id,
            keyword_id=keyword_id,
            favourite=favourite,
        )

        return company_user_profile_skill_history_model
