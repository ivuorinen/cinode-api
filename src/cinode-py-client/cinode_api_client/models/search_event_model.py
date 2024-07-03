import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.company_user_deletion_status import CompanyUserDeletionStatus
from ..models.event_entity_type import EventEntityType
from ..models.event_note_type import EventNoteType
from ..models.event_status_value import EventStatusValue
from ..models.event_type import EventType
from ..models.event_visibility import EventVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_comment_model import EventCommentModel
    from ..models.link import Link


T = TypeVar("T", bound="SearchEventModel")


@_attrs_define
class SearchEventModel:
    """
    Attributes:
        assigned_to_user_full_name (Union[Unset, None, str]):
        assigned_to_user_initials (Union[Unset, None, str]):
        assigned_to_user_show_as_deleted (Union[Unset, None, bool]):
        event_date_native_timezone (Union[Unset, datetime.datetime]):
        due_date_time_native_timezone (Union[Unset, None, datetime.datetime]):
        start_date_time_native_timezone (Union[Unset, None, datetime.datetime]):
        end_date_time_native_timezone (Union[Unset, None, datetime.datetime]):
        event_date_utc (Union[Unset, datetime.datetime]):
        due_date_time (Union[Unset, None, datetime.datetime]):
        due_date_time_utc (Union[Unset, None, datetime.datetime]):
        event_entity_type (Union[Unset, EventEntityType]):

            Kandidat = 0

            Kund = 1

            Uppdrag = 2

            Underkonsult = 3

            Medarbetare = 4

            Partner = 6

            Ej angiven = 7
        event_entity_id (Union[Unset, int]):
        event_entity_name (Union[Unset, None, str]):
        event_entity_seo_id (Union[Unset, None, str]):
        secondary_event_entity_type (Union[Unset, None, EventEntityType]):

            Kandidat = 0

            Kund = 1

            Uppdrag = 2

            Underkonsult = 3

            Medarbetare = 4

            Partner = 6

            Ej angiven = 7
        secondary_event_entity_id (Union[Unset, None, int]):
        secondary_event_entity_name (Union[Unset, None, str]):
        secondary_event_entity_seo_id (Union[Unset, None, str]):
        assigned_to_company_user_id (Union[Unset, None, int]):
        assigned_to_image_file_name (Union[Unset, None, str]):
        assigned_to_image_file_extension (Union[Unset, None, str]):
        assigned_to_seo_id (Union[Unset, None, str]):
        assigned_to_user_first_name (Union[Unset, None, str]):
        assigned_to_user_last_name (Union[Unset, None, str]):
        assigned_to_user_deletion_status (Union[Unset, None, CompanyUserDeletionStatus]):

            Aktiv = 0

            Marked for deletion = 1

            Borttagen = 2
        number_of_comments (Union[Unset, int]):
        status (Union[Unset, EventStatusValue]):

            Inte påbörjad = 0

            Påbörjad = 1

            Färdig = 2

            Uppskjuten = 3

            Väntar = 4
        start_date_time (Union[Unset, None, datetime.datetime]):
        start_date_time_utc (Union[Unset, None, datetime.datetime]):
        end_date_time (Union[Unset, None, datetime.datetime]):
        end_date_time_utc (Union[Unset, None, datetime.datetime]):
        event_type (Union[Unset, EventType]):

            Möte = 0

            Notering = 1

            Uppgift = 2

            Samtal = 3
        has_time (Union[Unset, None, bool]):
        timezone_id (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        external_sync_account_id (Union[Unset, None, str]):
        external_sync_account_company_user_id (Union[Unset, None, int]):
        external_sync_account_company_user_full_name (Union[Unset, None, str]):
        note_type (Union[Unset, None, EventNoteType]):

            Ej angiven = 0

            Telefonsamtal = 1

            E-mail = 2
        has_attendees (Union[Unset, None, bool]):
        is_overdue (Union[Unset, None, bool]):
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

    assigned_to_user_full_name: Union[Unset, None, str] = UNSET
    assigned_to_user_initials: Union[Unset, None, str] = UNSET
    assigned_to_user_show_as_deleted: Union[Unset, None, bool] = UNSET
    event_date_native_timezone: Union[Unset, datetime.datetime] = UNSET
    due_date_time_native_timezone: Union[Unset, None, datetime.datetime] = UNSET
    start_date_time_native_timezone: Union[Unset, None, datetime.datetime] = UNSET
    end_date_time_native_timezone: Union[Unset, None, datetime.datetime] = UNSET
    event_date_utc: Union[Unset, datetime.datetime] = UNSET
    due_date_time: Union[Unset, None, datetime.datetime] = UNSET
    due_date_time_utc: Union[Unset, None, datetime.datetime] = UNSET
    event_entity_type: Union[Unset, EventEntityType] = UNSET
    event_entity_id: Union[Unset, int] = UNSET
    event_entity_name: Union[Unset, None, str] = UNSET
    event_entity_seo_id: Union[Unset, None, str] = UNSET
    secondary_event_entity_type: Union[Unset, None, EventEntityType] = UNSET
    secondary_event_entity_id: Union[Unset, None, int] = UNSET
    secondary_event_entity_name: Union[Unset, None, str] = UNSET
    secondary_event_entity_seo_id: Union[Unset, None, str] = UNSET
    assigned_to_company_user_id: Union[Unset, None, int] = UNSET
    assigned_to_image_file_name: Union[Unset, None, str] = UNSET
    assigned_to_image_file_extension: Union[Unset, None, str] = UNSET
    assigned_to_seo_id: Union[Unset, None, str] = UNSET
    assigned_to_user_first_name: Union[Unset, None, str] = UNSET
    assigned_to_user_last_name: Union[Unset, None, str] = UNSET
    assigned_to_user_deletion_status: Union[Unset, None, CompanyUserDeletionStatus] = UNSET
    number_of_comments: Union[Unset, int] = UNSET
    status: Union[Unset, EventStatusValue] = UNSET
    start_date_time: Union[Unset, None, datetime.datetime] = UNSET
    start_date_time_utc: Union[Unset, None, datetime.datetime] = UNSET
    end_date_time: Union[Unset, None, datetime.datetime] = UNSET
    end_date_time_utc: Union[Unset, None, datetime.datetime] = UNSET
    event_type: Union[Unset, EventType] = UNSET
    has_time: Union[Unset, None, bool] = UNSET
    timezone_id: Union[Unset, None, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    external_sync_account_id: Union[Unset, None, str] = UNSET
    external_sync_account_company_user_id: Union[Unset, None, int] = UNSET
    external_sync_account_company_user_full_name: Union[Unset, None, str] = UNSET
    note_type: Union[Unset, None, EventNoteType] = UNSET
    has_attendees: Union[Unset, None, bool] = UNSET
    is_overdue: Union[Unset, None, bool] = UNSET
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
        assigned_to_user_full_name = self.assigned_to_user_full_name
        assigned_to_user_initials = self.assigned_to_user_initials
        assigned_to_user_show_as_deleted = self.assigned_to_user_show_as_deleted
        event_date_native_timezone: Union[Unset, str] = UNSET
        if not isinstance(self.event_date_native_timezone, Unset):
            event_date_native_timezone = self.event_date_native_timezone.isoformat()

        due_date_time_native_timezone: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date_time_native_timezone, Unset):
            due_date_time_native_timezone = (
                self.due_date_time_native_timezone.isoformat() if self.due_date_time_native_timezone else None
            )

        start_date_time_native_timezone: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date_time_native_timezone, Unset):
            start_date_time_native_timezone = (
                self.start_date_time_native_timezone.isoformat() if self.start_date_time_native_timezone else None
            )

        end_date_time_native_timezone: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date_time_native_timezone, Unset):
            end_date_time_native_timezone = (
                self.end_date_time_native_timezone.isoformat() if self.end_date_time_native_timezone else None
            )

        event_date_utc: Union[Unset, str] = UNSET
        if not isinstance(self.event_date_utc, Unset):
            event_date_utc = self.event_date_utc.isoformat()

        due_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date_time, Unset):
            due_date_time = self.due_date_time.isoformat() if self.due_date_time else None

        due_date_time_utc: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date_time_utc, Unset):
            due_date_time_utc = self.due_date_time_utc.isoformat() if self.due_date_time_utc else None

        event_entity_type: Union[Unset, int] = UNSET
        if not isinstance(self.event_entity_type, Unset):
            event_entity_type = self.event_entity_type.value

        event_entity_id = self.event_entity_id
        event_entity_name = self.event_entity_name
        event_entity_seo_id = self.event_entity_seo_id
        secondary_event_entity_type: Union[Unset, None, int] = UNSET
        if not isinstance(self.secondary_event_entity_type, Unset):
            secondary_event_entity_type = (
                self.secondary_event_entity_type.value if self.secondary_event_entity_type else None
            )

        secondary_event_entity_id = self.secondary_event_entity_id
        secondary_event_entity_name = self.secondary_event_entity_name
        secondary_event_entity_seo_id = self.secondary_event_entity_seo_id
        assigned_to_company_user_id = self.assigned_to_company_user_id
        assigned_to_image_file_name = self.assigned_to_image_file_name
        assigned_to_image_file_extension = self.assigned_to_image_file_extension
        assigned_to_seo_id = self.assigned_to_seo_id
        assigned_to_user_first_name = self.assigned_to_user_first_name
        assigned_to_user_last_name = self.assigned_to_user_last_name
        assigned_to_user_deletion_status: Union[Unset, None, int] = UNSET
        if not isinstance(self.assigned_to_user_deletion_status, Unset):
            assigned_to_user_deletion_status = (
                self.assigned_to_user_deletion_status.value if self.assigned_to_user_deletion_status else None
            )

        number_of_comments = self.number_of_comments
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        start_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat() if self.start_date_time else None

        start_date_time_utc: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date_time_utc, Unset):
            start_date_time_utc = self.start_date_time_utc.isoformat() if self.start_date_time_utc else None

        end_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat() if self.end_date_time else None

        end_date_time_utc: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date_time_utc, Unset):
            end_date_time_utc = self.end_date_time_utc.isoformat() if self.end_date_time_utc else None

        event_type: Union[Unset, int] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        has_time = self.has_time
        timezone_id = self.timezone_id
        external_id = self.external_id
        external_sync_account_id = self.external_sync_account_id
        external_sync_account_company_user_id = self.external_sync_account_company_user_id
        external_sync_account_company_user_full_name = self.external_sync_account_company_user_full_name
        note_type: Union[Unset, None, int] = UNSET
        if not isinstance(self.note_type, Unset):
            note_type = self.note_type.value if self.note_type else None

        has_attendees = self.has_attendees
        is_overdue = self.is_overdue
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
        if assigned_to_user_full_name is not UNSET:
            field_dict["assignedToUserFullName"] = assigned_to_user_full_name
        if assigned_to_user_initials is not UNSET:
            field_dict["assignedToUserInitials"] = assigned_to_user_initials
        if assigned_to_user_show_as_deleted is not UNSET:
            field_dict["assignedToUserShowAsDeleted"] = assigned_to_user_show_as_deleted
        if event_date_native_timezone is not UNSET:
            field_dict["eventDateNativeTimezone"] = event_date_native_timezone
        if due_date_time_native_timezone is not UNSET:
            field_dict["dueDateTimeNativeTimezone"] = due_date_time_native_timezone
        if start_date_time_native_timezone is not UNSET:
            field_dict["startDateTimeNativeTimezone"] = start_date_time_native_timezone
        if end_date_time_native_timezone is not UNSET:
            field_dict["endDateTimeNativeTimezone"] = end_date_time_native_timezone
        if event_date_utc is not UNSET:
            field_dict["eventDateUtc"] = event_date_utc
        if due_date_time is not UNSET:
            field_dict["dueDateTime"] = due_date_time
        if due_date_time_utc is not UNSET:
            field_dict["dueDateTimeUtc"] = due_date_time_utc
        if event_entity_type is not UNSET:
            field_dict["eventEntityType"] = event_entity_type
        if event_entity_id is not UNSET:
            field_dict["eventEntityId"] = event_entity_id
        if event_entity_name is not UNSET:
            field_dict["eventEntityName"] = event_entity_name
        if event_entity_seo_id is not UNSET:
            field_dict["eventEntitySeoId"] = event_entity_seo_id
        if secondary_event_entity_type is not UNSET:
            field_dict["secondaryEventEntityType"] = secondary_event_entity_type
        if secondary_event_entity_id is not UNSET:
            field_dict["secondaryEventEntityId"] = secondary_event_entity_id
        if secondary_event_entity_name is not UNSET:
            field_dict["secondaryEventEntityName"] = secondary_event_entity_name
        if secondary_event_entity_seo_id is not UNSET:
            field_dict["secondaryEventEntitySeoId"] = secondary_event_entity_seo_id
        if assigned_to_company_user_id is not UNSET:
            field_dict["assignedToCompanyUserId"] = assigned_to_company_user_id
        if assigned_to_image_file_name is not UNSET:
            field_dict["assignedToImageFileName"] = assigned_to_image_file_name
        if assigned_to_image_file_extension is not UNSET:
            field_dict["assignedToImageFileExtension"] = assigned_to_image_file_extension
        if assigned_to_seo_id is not UNSET:
            field_dict["assignedToSeoId"] = assigned_to_seo_id
        if assigned_to_user_first_name is not UNSET:
            field_dict["assignedToUserFirstName"] = assigned_to_user_first_name
        if assigned_to_user_last_name is not UNSET:
            field_dict["assignedToUserLastName"] = assigned_to_user_last_name
        if assigned_to_user_deletion_status is not UNSET:
            field_dict["assignedToUserDeletionStatus"] = assigned_to_user_deletion_status
        if number_of_comments is not UNSET:
            field_dict["numberOfComments"] = number_of_comments
        if status is not UNSET:
            field_dict["status"] = status
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if start_date_time_utc is not UNSET:
            field_dict["startDateTimeUtc"] = start_date_time_utc
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if end_date_time_utc is not UNSET:
            field_dict["endDateTimeUtc"] = end_date_time_utc
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if has_time is not UNSET:
            field_dict["hasTime"] = has_time
        if timezone_id is not UNSET:
            field_dict["timezoneId"] = timezone_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if external_sync_account_id is not UNSET:
            field_dict["externalSyncAccountId"] = external_sync_account_id
        if external_sync_account_company_user_id is not UNSET:
            field_dict["externalSyncAccountCompanyUserId"] = external_sync_account_company_user_id
        if external_sync_account_company_user_full_name is not UNSET:
            field_dict["externalSyncAccountCompanyUserFullName"] = external_sync_account_company_user_full_name
        if note_type is not UNSET:
            field_dict["noteType"] = note_type
        if has_attendees is not UNSET:
            field_dict["hasAttendees"] = has_attendees
        if is_overdue is not UNSET:
            field_dict["isOverdue"] = is_overdue
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
        assigned_to_user_full_name = d.pop("assignedToUserFullName", UNSET)

        assigned_to_user_initials = d.pop("assignedToUserInitials", UNSET)

        assigned_to_user_show_as_deleted = d.pop("assignedToUserShowAsDeleted", UNSET)

        _event_date_native_timezone = d.pop("eventDateNativeTimezone", UNSET)
        event_date_native_timezone: Union[Unset, datetime.datetime]
        if isinstance(_event_date_native_timezone, Unset):
            event_date_native_timezone = UNSET
        else:
            event_date_native_timezone = isoparse(_event_date_native_timezone)

        _due_date_time_native_timezone = d.pop("dueDateTimeNativeTimezone", UNSET)
        due_date_time_native_timezone: Union[Unset, None, datetime.datetime]
        if _due_date_time_native_timezone is None:
            due_date_time_native_timezone = None
        elif isinstance(_due_date_time_native_timezone, Unset):
            due_date_time_native_timezone = UNSET
        else:
            due_date_time_native_timezone = isoparse(_due_date_time_native_timezone)

        _start_date_time_native_timezone = d.pop("startDateTimeNativeTimezone", UNSET)
        start_date_time_native_timezone: Union[Unset, None, datetime.datetime]
        if _start_date_time_native_timezone is None:
            start_date_time_native_timezone = None
        elif isinstance(_start_date_time_native_timezone, Unset):
            start_date_time_native_timezone = UNSET
        else:
            start_date_time_native_timezone = isoparse(_start_date_time_native_timezone)

        _end_date_time_native_timezone = d.pop("endDateTimeNativeTimezone", UNSET)
        end_date_time_native_timezone: Union[Unset, None, datetime.datetime]
        if _end_date_time_native_timezone is None:
            end_date_time_native_timezone = None
        elif isinstance(_end_date_time_native_timezone, Unset):
            end_date_time_native_timezone = UNSET
        else:
            end_date_time_native_timezone = isoparse(_end_date_time_native_timezone)

        _event_date_utc = d.pop("eventDateUtc", UNSET)
        event_date_utc: Union[Unset, datetime.datetime]
        if isinstance(_event_date_utc, Unset):
            event_date_utc = UNSET
        else:
            event_date_utc = isoparse(_event_date_utc)

        _due_date_time = d.pop("dueDateTime", UNSET)
        due_date_time: Union[Unset, None, datetime.datetime]
        if _due_date_time is None:
            due_date_time = None
        elif isinstance(_due_date_time, Unset):
            due_date_time = UNSET
        else:
            due_date_time = isoparse(_due_date_time)

        _due_date_time_utc = d.pop("dueDateTimeUtc", UNSET)
        due_date_time_utc: Union[Unset, None, datetime.datetime]
        if _due_date_time_utc is None:
            due_date_time_utc = None
        elif isinstance(_due_date_time_utc, Unset):
            due_date_time_utc = UNSET
        else:
            due_date_time_utc = isoparse(_due_date_time_utc)

        _event_entity_type = d.pop("eventEntityType", UNSET)
        event_entity_type: Union[Unset, EventEntityType]
        if isinstance(_event_entity_type, Unset):
            event_entity_type = UNSET
        else:
            event_entity_type = EventEntityType(_event_entity_type)

        event_entity_id = d.pop("eventEntityId", UNSET)

        event_entity_name = d.pop("eventEntityName", UNSET)

        event_entity_seo_id = d.pop("eventEntitySeoId", UNSET)

        _secondary_event_entity_type = d.pop("secondaryEventEntityType", UNSET)
        secondary_event_entity_type: Union[Unset, None, EventEntityType]
        if _secondary_event_entity_type is None:
            secondary_event_entity_type = None
        elif isinstance(_secondary_event_entity_type, Unset):
            secondary_event_entity_type = UNSET
        else:
            secondary_event_entity_type = EventEntityType(_secondary_event_entity_type)

        secondary_event_entity_id = d.pop("secondaryEventEntityId", UNSET)

        secondary_event_entity_name = d.pop("secondaryEventEntityName", UNSET)

        secondary_event_entity_seo_id = d.pop("secondaryEventEntitySeoId", UNSET)

        assigned_to_company_user_id = d.pop("assignedToCompanyUserId", UNSET)

        assigned_to_image_file_name = d.pop("assignedToImageFileName", UNSET)

        assigned_to_image_file_extension = d.pop("assignedToImageFileExtension", UNSET)

        assigned_to_seo_id = d.pop("assignedToSeoId", UNSET)

        assigned_to_user_first_name = d.pop("assignedToUserFirstName", UNSET)

        assigned_to_user_last_name = d.pop("assignedToUserLastName", UNSET)

        _assigned_to_user_deletion_status = d.pop("assignedToUserDeletionStatus", UNSET)
        assigned_to_user_deletion_status: Union[Unset, None, CompanyUserDeletionStatus]
        if _assigned_to_user_deletion_status is None:
            assigned_to_user_deletion_status = None
        elif isinstance(_assigned_to_user_deletion_status, Unset):
            assigned_to_user_deletion_status = UNSET
        else:
            assigned_to_user_deletion_status = CompanyUserDeletionStatus(_assigned_to_user_deletion_status)

        number_of_comments = d.pop("numberOfComments", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, EventStatusValue]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EventStatusValue(_status)

        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: Union[Unset, None, datetime.datetime]
        if _start_date_time is None:
            start_date_time = None
        elif isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        _start_date_time_utc = d.pop("startDateTimeUtc", UNSET)
        start_date_time_utc: Union[Unset, None, datetime.datetime]
        if _start_date_time_utc is None:
            start_date_time_utc = None
        elif isinstance(_start_date_time_utc, Unset):
            start_date_time_utc = UNSET
        else:
            start_date_time_utc = isoparse(_start_date_time_utc)

        _end_date_time = d.pop("endDateTime", UNSET)
        end_date_time: Union[Unset, None, datetime.datetime]
        if _end_date_time is None:
            end_date_time = None
        elif isinstance(_end_date_time, Unset):
            end_date_time = UNSET
        else:
            end_date_time = isoparse(_end_date_time)

        _end_date_time_utc = d.pop("endDateTimeUtc", UNSET)
        end_date_time_utc: Union[Unset, None, datetime.datetime]
        if _end_date_time_utc is None:
            end_date_time_utc = None
        elif isinstance(_end_date_time_utc, Unset):
            end_date_time_utc = UNSET
        else:
            end_date_time_utc = isoparse(_end_date_time_utc)

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, EventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = EventType(_event_type)

        has_time = d.pop("hasTime", UNSET)

        timezone_id = d.pop("timezoneId", UNSET)

        external_id = d.pop("externalId", UNSET)

        external_sync_account_id = d.pop("externalSyncAccountId", UNSET)

        external_sync_account_company_user_id = d.pop("externalSyncAccountCompanyUserId", UNSET)

        external_sync_account_company_user_full_name = d.pop("externalSyncAccountCompanyUserFullName", UNSET)

        _note_type = d.pop("noteType", UNSET)
        note_type: Union[Unset, None, EventNoteType]
        if _note_type is None:
            note_type = None
        elif isinstance(_note_type, Unset):
            note_type = UNSET
        else:
            note_type = EventNoteType(_note_type)

        has_attendees = d.pop("hasAttendees", UNSET)

        is_overdue = d.pop("isOverdue", UNSET)

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

        search_event_model = cls(
            assigned_to_user_full_name=assigned_to_user_full_name,
            assigned_to_user_initials=assigned_to_user_initials,
            assigned_to_user_show_as_deleted=assigned_to_user_show_as_deleted,
            event_date_native_timezone=event_date_native_timezone,
            due_date_time_native_timezone=due_date_time_native_timezone,
            start_date_time_native_timezone=start_date_time_native_timezone,
            end_date_time_native_timezone=end_date_time_native_timezone,
            event_date_utc=event_date_utc,
            due_date_time=due_date_time,
            due_date_time_utc=due_date_time_utc,
            event_entity_type=event_entity_type,
            event_entity_id=event_entity_id,
            event_entity_name=event_entity_name,
            event_entity_seo_id=event_entity_seo_id,
            secondary_event_entity_type=secondary_event_entity_type,
            secondary_event_entity_id=secondary_event_entity_id,
            secondary_event_entity_name=secondary_event_entity_name,
            secondary_event_entity_seo_id=secondary_event_entity_seo_id,
            assigned_to_company_user_id=assigned_to_company_user_id,
            assigned_to_image_file_name=assigned_to_image_file_name,
            assigned_to_image_file_extension=assigned_to_image_file_extension,
            assigned_to_seo_id=assigned_to_seo_id,
            assigned_to_user_first_name=assigned_to_user_first_name,
            assigned_to_user_last_name=assigned_to_user_last_name,
            assigned_to_user_deletion_status=assigned_to_user_deletion_status,
            number_of_comments=number_of_comments,
            status=status,
            start_date_time=start_date_time,
            start_date_time_utc=start_date_time_utc,
            end_date_time=end_date_time,
            end_date_time_utc=end_date_time_utc,
            event_type=event_type,
            has_time=has_time,
            timezone_id=timezone_id,
            external_id=external_id,
            external_sync_account_id=external_sync_account_id,
            external_sync_account_company_user_id=external_sync_account_company_user_id,
            external_sync_account_company_user_full_name=external_sync_account_company_user_full_name,
            note_type=note_type,
            has_attendees=has_attendees,
            is_overdue=is_overdue,
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

        return search_event_model
