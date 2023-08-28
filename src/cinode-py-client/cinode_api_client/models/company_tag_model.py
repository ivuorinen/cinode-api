from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_tag_type_model import CompanyTagTypeModel


T = TypeVar("T", bound="CompanyTagModel")


@_attrs_define
class CompanyTagModel:
    """
    Attributes:
        tag_type (Union[Unset, None, CompanyTagTypeModel]):
        company_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        seo_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
    """

    tag_type: Union[Unset, None, "CompanyTagTypeModel"] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tag_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.tag_type, Unset):
            tag_type = self.tag_type.to_dict() if self.tag_type else None

        company_id = self.company_id
        id = self.id
        seo_id = self.seo_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tag_type is not UNSET:
            field_dict["tagType"] = tag_type
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if id is not UNSET:
            field_dict["id"] = id
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_tag_type_model import CompanyTagTypeModel

        d = src_dict.copy()
        _tag_type = d.pop("tagType", UNSET)
        tag_type: Union[Unset, None, CompanyTagTypeModel]
        if _tag_type is None:
            tag_type = None
        elif isinstance(_tag_type, Unset):
            tag_type = UNSET
        else:
            tag_type = CompanyTagTypeModel.from_dict(_tag_type)

        company_id = d.pop("companyId", UNSET)

        id = d.pop("id", UNSET)

        seo_id = d.pop("seoId", UNSET)

        name = d.pop("name", UNSET)

        company_tag_model = cls(
            tag_type=tag_type,
            company_id=company_id,
            id=id,
            seo_id=seo_id,
            name=name,
        )

        return company_tag_model
