from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="ProjectBaseModel")


@_attrs_define
class ProjectBaseModel:
    """
    Attributes:
        company_id (Union[Unset, int]):
        customer_id (Union[Unset, int]):
        id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        customer_identifier (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    company_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    identifier: Union[Unset, None, str] = UNSET
    customer_identifier: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        customer_id = self.customer_id
        id = self.id
        title = self.title
        description = self.description
        identifier = self.identifier
        customer_identifier = self.customer_identifier
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
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if customer_identifier is not UNSET:
            field_dict["customerIdentifier"] = customer_identifier
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        customer_identifier = d.pop("customerIdentifier", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        project_base_model = cls(
            company_id=company_id,
            customer_id=customer_id,
            id=id,
            title=title,
            description=description,
            identifier=identifier,
            customer_identifier=customer_identifier,
            links=links,
        )

        return project_base_model
