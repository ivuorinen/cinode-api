from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyUserProfileExtSkillAddEditModel")


@_attrs_define
class CompanyUserProfileExtSkillAddEditModel:
    """
    Attributes:
        title (str):
    """

    title: str

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        company_user_profile_ext_skill_add_edit_model = cls(
            title=title,
        )

        return company_user_profile_ext_skill_add_edit_model
