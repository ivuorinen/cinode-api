from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyResumeTemplateBaseModel")


@_attrs_define
class CompanyResumeTemplateBaseModel:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        company_resume_template_base_model = cls(
            id=id,
            title=title,
        )

        return company_resume_template_base_model
