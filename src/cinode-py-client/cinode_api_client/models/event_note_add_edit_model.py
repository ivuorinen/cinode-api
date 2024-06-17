import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.event_note_type import EventNoteType
from ..models.event_status_value import EventStatusValue
from ..models.event_type import EventType
from ..models.event_visibility import EventVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventNoteAddEditModel")


@_attrs_define
class EventNoteAddEditModel:
    """
    Attributes:
        title (str):
        note_type (Union[Unset, None, EventNoteType]):

            Ej angiven = 0

            Telefonsamtal = 1

            E-mail = 2
        note_date (Union[Unset, None, datetime.datetime]):
        timezone_id (Union[Unset, None, str]): The desired timezone to be used for NoteDate property. Valid timezone ids
            can be found at https://nodatime.org/TimeZones
            If empty, the timezone of the executing user (API account) will be used.
        assigned_to_company_user_id (Union[Unset, None, int]):
        status (Union[Unset, EventStatusValue]):

            Inte påbörjad = 0

            Påbörjad = 1

            Färdig = 2

            Uppskjuten = 3

            Väntar = 4
        type (Union[Unset, EventType]):

            Möte = 0

            Notering = 1

            Uppgift = 2

            Samtal = 3
        description (Union[Unset, None, str]):
        visibility (Union[Unset, EventVisibility]):

            Publik = 0

            Privat = 1
    """

    title: str
    note_type: Union[Unset, None, EventNoteType] = UNSET
    note_date: Union[Unset, None, datetime.datetime] = UNSET
    timezone_id: Union[Unset, None, str] = UNSET
    assigned_to_company_user_id: Union[Unset, None, int] = UNSET
    status: Union[Unset, EventStatusValue] = UNSET
    type: Union[Unset, EventType] = UNSET
    description: Union[Unset, None, str] = UNSET
    visibility: Union[Unset, EventVisibility] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        note_type: Union[Unset, None, int] = UNSET
        if not isinstance(self.note_type, Unset):
            note_type = self.note_type.value if self.note_type else None

        note_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.note_date, Unset):
            note_date = self.note_date.isoformat() if self.note_date else None

        timezone_id = self.timezone_id
        assigned_to_company_user_id = self.assigned_to_company_user_id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        description = self.description
        visibility: Union[Unset, int] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
            }
        )
        if note_type is not UNSET:
            field_dict["noteType"] = note_type
        if note_date is not UNSET:
            field_dict["noteDate"] = note_date
        if timezone_id is not UNSET:
            field_dict["timezoneId"] = timezone_id
        if assigned_to_company_user_id is not UNSET:
            field_dict["assignedToCompanyUserId"] = assigned_to_company_user_id
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        _note_type = d.pop("noteType", UNSET)
        note_type: Union[Unset, None, EventNoteType]
        if _note_type is None:
            note_type = None
        elif isinstance(_note_type, Unset):
            note_type = UNSET
        else:
            note_type = EventNoteType(_note_type)

        _note_date = d.pop("noteDate", UNSET)
        note_date: Union[Unset, None, datetime.datetime]
        if _note_date is None:
            note_date = None
        elif isinstance(_note_date, Unset):
            note_date = UNSET
        else:
            note_date = isoparse(_note_date)

        timezone_id = d.pop("timezoneId", UNSET)

        assigned_to_company_user_id = d.pop("assignedToCompanyUserId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, EventStatusValue]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EventStatusValue(_status)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EventType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EventType(_type)

        description = d.pop("description", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, EventVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = EventVisibility(_visibility)

        event_note_add_edit_model = cls(
            title=title,
            note_type=note_type,
            note_date=note_date,
            timezone_id=timezone_id,
            assigned_to_company_user_id=assigned_to_company_user_id,
            status=status,
            type=type,
            description=description,
            visibility=visibility,
        )

        return event_note_add_edit_model
