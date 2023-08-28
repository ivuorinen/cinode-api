import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.event_status_value import EventStatusValue
from ..models.event_type import EventType
from ..models.event_visibility import EventVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerEventMeetingAddEditModel")


@_attrs_define
class CustomerEventMeetingAddEditModel:
    """
    Attributes:
        title (str):
        customer_contact_id (Union[Unset, None, int]):
        start_date_time (Union[Unset, datetime.datetime]):
        end_date_time (Union[Unset, datetime.datetime]):
        timezone_id (Union[Unset, None, str]): The desired timezone to be used for StartDateTime and EndDateTime
            properties. Valid timezone ids can be found at https://nodatime.org/TimeZones
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
    customer_contact_id: Union[Unset, None, int] = UNSET
    start_date_time: Union[Unset, datetime.datetime] = UNSET
    end_date_time: Union[Unset, datetime.datetime] = UNSET
    timezone_id: Union[Unset, None, str] = UNSET
    assigned_to_company_user_id: Union[Unset, None, int] = UNSET
    status: Union[Unset, EventStatusValue] = UNSET
    type: Union[Unset, EventType] = UNSET
    description: Union[Unset, None, str] = UNSET
    visibility: Union[Unset, EventVisibility] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        customer_contact_id = self.customer_contact_id
        start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

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
        if customer_contact_id is not UNSET:
            field_dict["customerContactId"] = customer_contact_id
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
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

        customer_contact_id = d.pop("customerContactId", UNSET)

        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: Union[Unset, datetime.datetime]
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        _end_date_time = d.pop("endDateTime", UNSET)
        end_date_time: Union[Unset, datetime.datetime]
        if isinstance(_end_date_time, Unset):
            end_date_time = UNSET
        else:
            end_date_time = isoparse(_end_date_time)

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

        customer_event_meeting_add_edit_model = cls(
            title=title,
            customer_contact_id=customer_contact_id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            timezone_id=timezone_id,
            assigned_to_company_user_id=assigned_to_company_user_id,
            status=status,
            type=type,
            description=description,
            visibility=visibility,
        )

        return customer_event_meeting_add_edit_model
