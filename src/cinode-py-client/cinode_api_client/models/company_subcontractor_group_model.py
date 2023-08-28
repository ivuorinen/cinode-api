from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_base_model import CompanyUserBaseModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanySubcontractorGroupModel")


@_attrs_define
class CompanySubcontractorGroupModel:
    """
    Attributes:
        company_user_manager (Union[Unset, None, CompanyUserBaseModel]):
        members (Union[Unset, None, List['CompanyUserBaseModel']]):
        id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    company_user_manager: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    members: Union[Unset, None, List["CompanyUserBaseModel"]] = UNSET
    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_manager: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company_user_manager, Unset):
            company_user_manager = self.company_user_manager.to_dict() if self.company_user_manager else None

        members: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            if self.members is None:
                members = None
            else:
                members = []
                for members_item_data in self.members:
                    members_item = members_item_data.to_dict()

                    members.append(members_item)

        id = self.id
        company_id = self.company_id
        name = self.name
        description = self.description
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
        if company_user_manager is not UNSET:
            field_dict["companyUserManager"] = company_user_manager
        if members is not UNSET:
            field_dict["members"] = members
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_base_model import CompanyUserBaseModel
        from ..models.link import Link

        d = src_dict.copy()
        _company_user_manager = d.pop("companyUserManager", UNSET)
        company_user_manager: Union[Unset, None, CompanyUserBaseModel]
        if _company_user_manager is None:
            company_user_manager = None
        elif isinstance(_company_user_manager, Unset):
            company_user_manager = UNSET
        else:
            company_user_manager = CompanyUserBaseModel.from_dict(_company_user_manager)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = CompanyUserBaseModel.from_dict(members_item_data)

            members.append(members_item)

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_subcontractor_group_model = cls(
            company_user_manager=company_user_manager,
            members=members,
            id=id,
            company_id=company_id,
            name=name,
            description=description,
            links=links,
        )

        return company_subcontractor_group_model
