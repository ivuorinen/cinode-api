from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ITemplateStyleAssetViewModel")


@_attrs_define
class ITemplateStyleAssetViewModel:
    """
    Attributes:
        company_id (Union[Unset, int]):
        resume_template_id (Union[Unset, int]):
        id (Union[Unset, int]):
        order (Union[Unset, int]):
        file_name (Union[Unset, None, str]):
        version (Union[Unset, None, str]):
    """

    company_id: Union[Unset, int] = UNSET
    resume_template_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    order: Union[Unset, int] = UNSET
    file_name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        resume_template_id = self.resume_template_id
        id = self.id
        order = self.order
        file_name = self.file_name
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if resume_template_id is not UNSET:
            field_dict["resumeTemplateId"] = resume_template_id
        if id is not UNSET:
            field_dict["id"] = id
        if order is not UNSET:
            field_dict["order"] = order
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        resume_template_id = d.pop("resumeTemplateId", UNSET)

        id = d.pop("id", UNSET)

        order = d.pop("order", UNSET)

        file_name = d.pop("fileName", UNSET)

        version = d.pop("version", UNSET)

        i_template_style_asset_view_model = cls(
            company_id=company_id,
            resume_template_id=resume_template_id,
            id=id,
            order=order,
            file_name=file_name,
            version=version,
        )

        return i_template_style_asset_view_model
