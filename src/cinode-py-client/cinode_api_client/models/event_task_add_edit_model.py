import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.event_status_value import EventStatusValue
from ..models.event_task_type import EventTaskType
from ..models.event_type import EventType
from ..models.event_visibility import EventVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventTaskAddEditModel")


@_attrs_define
class EventTaskAddEditModel:
    """
    Attributes:
        title (str):
        task_type (Union[Unset, None, EventTaskType]):

            Ej angiven = 0

            Telefonsamtal = 1

            E-mail = 2
        has_time (Union[Unset, None, bool]):
        due_date_time (Union[Unset, None, datetime.datetime]):
        timezone_id (Union[Unset, None, str]): The desired timezone to be used for DueDateTime property. Valid timezone
            ids can be found at https://nodatime.org/TimeZones
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
    task_type: Union[Unset, None, EventTaskType] = UNSET
    has_time: Union[Unset, None, bool] = UNSET
    due_date_time: Union[Unset, None, datetime.datetime] = UNSET
    timezone_id: Union[Unset, None, str] = UNSET
    assigned_to_company_user_id: Union[Unset, None, int] = UNSET
    status: Union[Unset, EventStatusValue] = UNSET
    type: Union[Unset, EventType] = UNSET
    description: Union[Unset, None, str] = UNSET
    visibility: Union[Unset, EventVisibility] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        task_type: Union[Unset, None, int] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value if self.task_type else None

        has_time = self.has_time
        due_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date_time, Unset):
            due_date_time = self.due_date_time.isoformat() if self.due_date_time else None

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
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if has_time is not UNSET:
            field_dict["hasTime"] = has_time
        if due_date_time is not UNSET:
            field_dict["dueDateTime"] = due_date_time
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

        _task_type = d.pop("taskType", UNSET)
        task_type: Union[Unset, None, EventTaskType]
        if _task_type is None:
            task_type = None
        elif isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = EventTaskType(_task_type)

        has_time = d.pop("hasTime", UNSET)

        _due_date_time = d.pop("dueDateTime", UNSET)
        due_date_time: Union[Unset, None, datetime.datetime]
        if _due_date_time is None:
            due_date_time = None
        elif isinstance(_due_date_time, Unset):
            due_date_time = UNSET
        else:
            due_date_time = isoparse(_due_date_time)

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

        event_task_add_edit_model = cls(
            title=title,
            task_type=task_type,
            has_time=has_time,
            due_date_time=due_date_time,
            timezone_id=timezone_id,
            assigned_to_company_user_id=assigned_to_company_user_id,
            status=status,
            type=type,
            description=description,
            visibility=visibility,
        )

        return event_task_add_edit_model
