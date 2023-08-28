import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_base_model import CompanyUserBaseModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyImageModel")


@_attrs_define
class CompanyImageModel:
    """
    Attributes:
        id (Union[Unset, int]):
        image_file_name (Union[Unset, str]):
        extension (Union[Unset, None, str]):
        company_id (Union[Unset, int]):
        created (Union[Unset, datetime.datetime]):
        assigned_to_company_user (Union[Unset, None, CompanyUserBaseModel]):
        uploaded_by_company_user (Union[Unset, None, CompanyUserBaseModel]):
        links (Union[Unset, None, List['Link']]):
    """

    id: Union[Unset, int] = UNSET
    image_file_name: Union[Unset, str] = UNSET
    extension: Union[Unset, None, str] = UNSET
    company_id: Union[Unset, int] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    assigned_to_company_user: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    uploaded_by_company_user: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        image_file_name = self.image_file_name
        extension = self.extension
        company_id = self.company_id
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        assigned_to_company_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_to_company_user, Unset):
            assigned_to_company_user = (
                self.assigned_to_company_user.to_dict() if self.assigned_to_company_user else None
            )

        uploaded_by_company_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.uploaded_by_company_user, Unset):
            uploaded_by_company_user = (
                self.uploaded_by_company_user.to_dict() if self.uploaded_by_company_user else None
            )

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
        if id is not UNSET:
            field_dict["id"] = id
        if image_file_name is not UNSET:
            field_dict["imageFileName"] = image_file_name
        if extension is not UNSET:
            field_dict["extension"] = extension
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created is not UNSET:
            field_dict["created"] = created
        if assigned_to_company_user is not UNSET:
            field_dict["assignedToCompanyUser"] = assigned_to_company_user
        if uploaded_by_company_user is not UNSET:
            field_dict["uploadedByCompanyUser"] = uploaded_by_company_user
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_base_model import CompanyUserBaseModel
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        image_file_name = d.pop("imageFileName", UNSET)

        extension = d.pop("extension", UNSET)

        company_id = d.pop("companyId", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _assigned_to_company_user = d.pop("assignedToCompanyUser", UNSET)
        assigned_to_company_user: Union[Unset, None, CompanyUserBaseModel]
        if _assigned_to_company_user is None:
            assigned_to_company_user = None
        elif isinstance(_assigned_to_company_user, Unset):
            assigned_to_company_user = UNSET
        else:
            assigned_to_company_user = CompanyUserBaseModel.from_dict(_assigned_to_company_user)

        _uploaded_by_company_user = d.pop("uploadedByCompanyUser", UNSET)
        uploaded_by_company_user: Union[Unset, None, CompanyUserBaseModel]
        if _uploaded_by_company_user is None:
            uploaded_by_company_user = None
        elif isinstance(_uploaded_by_company_user, Unset):
            uploaded_by_company_user = UNSET
        else:
            uploaded_by_company_user = CompanyUserBaseModel.from_dict(_uploaded_by_company_user)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_image_model = cls(
            id=id,
            image_file_name=image_file_name,
            extension=extension,
            company_id=company_id,
            created=created,
            assigned_to_company_user=assigned_to_company_user,
            uploaded_by_company_user=uploaded_by_company_user,
            links=links,
        )

        return company_image_model
