import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.event_status_value import EventStatusValue
from ..models.event_type import EventType
from ..models.event_visibility import EventVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_comment_model import EventCommentModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserEventMeetingModel")


@_attrs_define
class CompanyUserEventMeetingModel:
    """
    Attributes:
        company_user_id (Union[Unset, None, int]):
        start_date_time (Union[Unset, datetime.datetime]):
        end_date_time (Union[Unset, datetime.datetime]):
        location (Union[Unset, None, str]):
        assigned_to_company_user_id (Union[Unset, None, int]):
        status (Union[Unset, EventStatusValue]):

            Inte påbörjad = 0

            Påbörjad = 1

            Färdig = 2

            Uppskjuten = 3

            Väntar = 4
        created_by_company_user_id (Union[Unset, int]):
        updated_by_company_user_id (Union[Unset, None, int]):
        created (Union[Unset, datetime.datetime]):
        updated (Union[Unset, None, datetime.datetime]):
        visibility (Union[Unset, EventVisibility]):

            Publik = 0

            Privat = 1
        comments (Union[Unset, None, List['EventCommentModel']]):
        type (Union[Unset, EventType]):

            Möte = 0

            Notering = 1

            Uppgift = 2

            Samtal = 3
        id (Union[Unset, None, str]):
        company_id (Union[Unset, None, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        description_html (Union[Unset, None, str]):
        description_delta (Union[Unset, None, str]):
        event_date (Union[Unset, datetime.datetime]):
        links (Union[Unset, None, List['Link']]):
    """

    company_user_id: Union[Unset, None, int] = UNSET
    start_date_time: Union[Unset, datetime.datetime] = UNSET
    end_date_time: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, None, str] = UNSET
    assigned_to_company_user_id: Union[Unset, None, int] = UNSET
    status: Union[Unset, EventStatusValue] = UNSET
    created_by_company_user_id: Union[Unset, int] = UNSET
    updated_by_company_user_id: Union[Unset, None, int] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    visibility: Union[Unset, EventVisibility] = UNSET
    comments: Union[Unset, None, List["EventCommentModel"]] = UNSET
    type: Union[Unset, EventType] = UNSET
    id: Union[Unset, None, str] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    description_html: Union[Unset, None, str] = UNSET
    description_delta: Union[Unset, None, str] = UNSET
    event_date: Union[Unset, datetime.datetime] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_id = self.company_user_id
        start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

        location = self.location
        assigned_to_company_user_id = self.assigned_to_company_user_id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        created_by_company_user_id = self.created_by_company_user_id
        updated_by_company_user_id = self.updated_by_company_user_id
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat() if self.updated else None

        visibility: Union[Unset, int] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        comments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            if self.comments is None:
                comments = None
            else:
                comments = []
                for comments_item_data in self.comments:
                    comments_item = comments_item_data.to_dict()

                    comments.append(comments_item)

        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id
        company_id = self.company_id
        title = self.title
        description = self.description
        description_html = self.description_html
        description_delta = self.description_delta
        event_date: Union[Unset, str] = UNSET
        if not isinstance(self.event_date, Unset):
            event_date = self.event_date.isoformat()

        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if location is not UNSET:
            field_dict["location"] = location
        if assigned_to_company_user_id is not UNSET:
            field_dict["assignedToCompanyUserId"] = assigned_to_company_user_id
        if status is not UNSET:
            field_dict["status"] = status
        if created_by_company_user_id is not UNSET:
            field_dict["createdByCompanyUserId"] = created_by_company_user_id
        if updated_by_company_user_id is not UNSET:
            field_dict["updatedByCompanyUserId"] = updated_by_company_user_id
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if comments is not UNSET:
            field_dict["comments"] = comments
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if description_html is not UNSET:
            field_dict["descriptionHtml"] = description_html
        if description_delta is not UNSET:
            field_dict["descriptionDelta"] = description_delta
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_comment_model import EventCommentModel
        from ..models.link import Link

        d = src_dict.copy()
        company_user_id = d.pop("companyUserId", UNSET)

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

        location = d.pop("location", UNSET)

        assigned_to_company_user_id = d.pop("assignedToCompanyUserId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, EventStatusValue]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EventStatusValue(_status)

        created_by_company_user_id = d.pop("createdByCompanyUserId", UNSET)

        updated_by_company_user_id = d.pop("updatedByCompanyUserId", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, None, datetime.datetime]
        if _updated is None:
            updated = None
        elif isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, EventVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = EventVisibility(_visibility)

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = EventCommentModel.from_dict(comments_item_data)

            comments.append(comments_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EventType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EventType(_type)

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        description_html = d.pop("descriptionHtml", UNSET)

        description_delta = d.pop("descriptionDelta", UNSET)

        _event_date = d.pop("eventDate", UNSET)
        event_date: Union[Unset, datetime.datetime]
        if isinstance(_event_date, Unset):
            event_date = UNSET
        else:
            event_date = isoparse(_event_date)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_event_meeting_model = cls(
            company_user_id=company_user_id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            location=location,
            assigned_to_company_user_id=assigned_to_company_user_id,
            status=status,
            created_by_company_user_id=created_by_company_user_id,
            updated_by_company_user_id=updated_by_company_user_id,
            created=created,
            updated=updated,
            visibility=visibility,
            comments=comments,
            type=type,
            id=id,
            company_id=company_id,
            title=title,
            description=description,
            description_html=description_html,
            description_delta=description_delta,
            event_date=event_date,
            links=links,
        )

        return company_user_event_meeting_model
