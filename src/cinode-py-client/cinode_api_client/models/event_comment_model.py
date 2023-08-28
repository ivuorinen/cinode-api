import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventCommentModel")


@_attrs_define
class EventCommentModel:
    """
    Attributes:
        id (Union[Unset, None, int]):
        event_id (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        company_user_id (Union[Unset, int]):
        company_user_name (Union[Unset, None, str]):
        created (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, None, int] = UNSET
    event_id: Union[Unset, None, str] = UNSET
    text: Union[Unset, None, str] = UNSET
    company_user_id: Union[Unset, int] = UNSET
    company_user_name: Union[Unset, None, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        event_id = self.event_id
        text = self.text
        company_user_id = self.company_user_id
        company_user_name = self.company_user_name
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if text is not UNSET:
            field_dict["text"] = text
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if company_user_name is not UNSET:
            field_dict["companyUserName"] = company_user_name
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        event_id = d.pop("eventId", UNSET)

        text = d.pop("text", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        company_user_name = d.pop("companyUserName", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        event_comment_model = cls(
            id=id,
            event_id=event_id,
            text=text,
            company_user_id=company_user_id,
            company_user_name=company_user_name,
            created=created,
        )

        return event_comment_model
