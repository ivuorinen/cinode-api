from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_customer_manager_model import CompanyCustomerManagerModel
    from ..models.company_tag_base_model import CompanyTagBaseModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyCustomerExtendedModel")


@_attrs_define
class CompanyCustomerExtendedModel:
    """
    Attributes:
        email (Union[Unset, None, str]):
        tags (Union[Unset, None, List['CompanyTagBaseModel']]):
        managers (Union[Unset, None, List['CompanyCustomerManagerModel']]):
        id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        identification (Union[Unset, None, str]):
        seo_id (Union[Unset, None, str]):
        status (Union[Unset, Status]):

            Inaktiv = 0

            Aktiv = 1
        links (Union[Unset, None, List['Link']]):
    """

    email: Union[Unset, None, str] = UNSET
    tags: Union[Unset, None, List["CompanyTagBaseModel"]] = UNSET
    managers: Union[Unset, None, List["CompanyCustomerManagerModel"]] = UNSET
    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    identification: Union[Unset, None, str] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    status: Union[Unset, Status] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        tags: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = []
                for tags_item_data in self.tags:
                    tags_item = tags_item_data.to_dict()

                    tags.append(tags_item)

        managers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.managers, Unset):
            if self.managers is None:
                managers = None
            else:
                managers = []
                for managers_item_data in self.managers:
                    managers_item = managers_item_data.to_dict()

                    managers.append(managers_item)

        id = self.id
        company_id = self.company_id
        name = self.name
        description = self.description
        identification = self.identification
        seo_id = self.seo_id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        if email is not UNSET:
            field_dict["email"] = email
        if tags is not UNSET:
            field_dict["tags"] = tags
        if managers is not UNSET:
            field_dict["managers"] = managers
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if identification is not UNSET:
            field_dict["identification"] = identification
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if status is not UNSET:
            field_dict["status"] = status
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_customer_manager_model import CompanyCustomerManagerModel
        from ..models.company_tag_base_model import CompanyTagBaseModel
        from ..models.link import Link

        d = src_dict.copy()
        email = d.pop("email", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = CompanyTagBaseModel.from_dict(tags_item_data)

            tags.append(tags_item)

        managers = []
        _managers = d.pop("managers", UNSET)
        for managers_item_data in _managers or []:
            managers_item = CompanyCustomerManagerModel.from_dict(managers_item_data)

            managers.append(managers_item)

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        identification = d.pop("identification", UNSET)

        seo_id = d.pop("seoId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status(_status)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_customer_extended_model = cls(
            email=email,
            tags=tags,
            managers=managers,
            id=id,
            company_id=company_id,
            name=name,
            description=description,
            identification=identification,
            seo_id=seo_id,
            status=status,
            links=links,
        )

        return company_customer_extended_model
