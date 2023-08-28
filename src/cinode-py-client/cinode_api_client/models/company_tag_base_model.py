from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyTagBaseModel")


@_attrs_define
class CompanyTagBaseModel:
    """
    Attributes:
        company_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        seo_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
    """

    company_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        id = self.id
        seo_id = self.seo_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
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
        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        id = d.pop("id", UNSET)

        seo_id = d.pop("seoId", UNSET)

        name = d.pop("name", UNSET)

        company_tag_base_model = cls(
            company_id=company_id,
            id=id,
            seo_id=seo_id,
            name=name,
        )

        return company_tag_base_model
