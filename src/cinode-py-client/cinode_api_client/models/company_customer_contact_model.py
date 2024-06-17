import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_tag_model import CompanyTagModel
    from ..models.company_user_base_model import CompanyUserBaseModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyCustomerContactModel")


@_attrs_define
class CompanyCustomerContactModel:
    """
    Attributes:
        title (Union[Unset, None, str]):
        phone1 (Union[Unset, None, str]):
        phone2 (Union[Unset, None, str]):
        comments (Union[Unset, None, str]):
        last_touched_date (Union[Unset, datetime.datetime]):
        created_date_time (Union[Unset, datetime.datetime]):
        updated_date_time (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, None, CompanyUserBaseModel]):
        tags (Union[Unset, None, List['CompanyTagModel']]):
        id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        customer_id (Union[Unset, int]):
        slug (Union[Unset, None, str]):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        pronouns (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    title: Union[Unset, None, str] = UNSET
    phone1: Union[Unset, None, str] = UNSET
    phone2: Union[Unset, None, str] = UNSET
    comments: Union[Unset, None, str] = UNSET
    last_touched_date: Union[Unset, datetime.datetime] = UNSET
    created_date_time: Union[Unset, datetime.datetime] = UNSET
    updated_date_time: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    tags: Union[Unset, None, List["CompanyTagModel"]] = UNSET
    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, int] = UNSET
    slug: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    pronouns: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        phone1 = self.phone1
        phone2 = self.phone2
        comments = self.comments
        last_touched_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_touched_date, Unset):
            last_touched_date = self.last_touched_date.isoformat()

        created_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat()

        updated_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.updated_date_time, Unset):
            updated_date_time = self.updated_date_time.isoformat()

        created_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict() if self.created_by else None

        tags: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = []
                for tags_item_data in self.tags:
                    tags_item = tags_item_data.to_dict()

                    tags.append(tags_item)

        id = self.id
        company_id = self.company_id
        customer_id = self.customer_id
        slug = self.slug
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        pronouns = self.pronouns
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
        if title is not UNSET:
            field_dict["title"] = title
        if phone1 is not UNSET:
            field_dict["phone1"] = phone1
        if phone2 is not UNSET:
            field_dict["phone2"] = phone2
        if comments is not UNSET:
            field_dict["comments"] = comments
        if last_touched_date is not UNSET:
            field_dict["lastTouchedDate"] = last_touched_date
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if updated_date_time is not UNSET:
            field_dict["updatedDateTime"] = updated_date_time
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if tags is not UNSET:
            field_dict["tags"] = tags
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if pronouns is not UNSET:
            field_dict["pronouns"] = pronouns
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_tag_model import CompanyTagModel
        from ..models.company_user_base_model import CompanyUserBaseModel
        from ..models.link import Link

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        phone1 = d.pop("phone1", UNSET)

        phone2 = d.pop("phone2", UNSET)

        comments = d.pop("comments", UNSET)

        _last_touched_date = d.pop("lastTouchedDate", UNSET)
        last_touched_date: Union[Unset, datetime.datetime]
        if isinstance(_last_touched_date, Unset):
            last_touched_date = UNSET
        else:
            last_touched_date = isoparse(_last_touched_date)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, datetime.datetime]
        if isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        _updated_date_time = d.pop("updatedDateTime", UNSET)
        updated_date_time: Union[Unset, datetime.datetime]
        if isinstance(_updated_date_time, Unset):
            updated_date_time = UNSET
        else:
            updated_date_time = isoparse(_updated_date_time)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, None, CompanyUserBaseModel]
        if _created_by is None:
            created_by = None
        elif isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = CompanyUserBaseModel.from_dict(_created_by)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = CompanyTagModel.from_dict(tags_item_data)

            tags.append(tags_item)

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        slug = d.pop("slug", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        pronouns = d.pop("pronouns", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_customer_contact_model = cls(
            title=title,
            phone1=phone1,
            phone2=phone2,
            comments=comments,
            last_touched_date=last_touched_date,
            created_date_time=created_date_time,
            updated_date_time=updated_date_time,
            created_by=created_by,
            tags=tags,
            id=id,
            company_id=company_id,
            customer_id=customer_id,
            slug=slug,
            first_name=first_name,
            last_name=last_name,
            email=email,
            pronouns=pronouns,
            links=links,
        )

        return company_customer_contact_model
