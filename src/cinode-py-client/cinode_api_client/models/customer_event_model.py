import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.event_type import EventType
from ..models.event_visibility import EventVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_comment_model import EventCommentModel
    from ..models.link import Link


T = TypeVar("T", bound="CustomerEventModel")


@_attrs_define
class CustomerEventModel:
    """
    Attributes:
        customer_id (Union[Unset, None, int]):
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
        event_date (Union[Unset, datetime.datetime]):
        links (Union[Unset, None, List['Link']]):
    """

    customer_id: Union[Unset, None, int] = UNSET
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
    event_date: Union[Unset, datetime.datetime] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
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
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
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
        customer_id = d.pop("customerId", UNSET)

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

        customer_event_model = cls(
            customer_id=customer_id,
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
            event_date=event_date,
            links=links,
        )

        return customer_event_model
